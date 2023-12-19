import pandas as pd
import numpy as np
import streamlit as st
import hdbcli
import plotly.express as px
import plotly.graph_objects as go
import os
import json
from hdbcli import dbapi


st.set_page_config(
    page_title="HANA - DB ANALYSIS",
    page_icon=":key:",
    layout="wide",
)


st.title("HANA - DB ANALYSIS")

if 'connection' not in st.session_state:
    st.session_state.connection = None
if 'DF' not in st.session_state:
       st.session_state.DF = None
if 'Table' not in st.session_state:
    st.session_state.Table = None
if 'key_file' not in st.session_state:
    st.session_state.key_file = None

@st.cache_resource
def create_connections():
    try:
        key = pd.read_json(st.session_state.key_file)
        db_url = key.iloc(1)[0][0]
        db_port = key.iloc(1)[1][0]
        db_user = key.iloc(1)[2][0]
        db_pwd = key.iloc(1)[3][0]
        st.session_state.connection = dbapi.connect(db_url, db_port, db_user, db_pwd)
    except Exception as e:
        st.error(e)


def get_key_file():
    key_file = st.file_uploader("", type=["json"])
    return key_file

st.session_state.key_file = get_key_file()
st.info('The json file should contain the connection details in the order of `host`, `port`, `user`, `password`, `database`', icon='ℹ️')


if st.session_state.key_file is not None:
    create_connections()

if st.session_state.connection is not None:
    st.success('Connection Created successfully!!')



