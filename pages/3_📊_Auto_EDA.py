import pandas as pd
import numpy as np
import streamlit as st
import pandas_profiling
import plotly.express as px
import plotly.graph_objects as go
from streamlit_pandas_profiling import st_profile_report


st.set_page_config(page_title="Auto EDA", page_icon="📊", layout="wide")

st.header('HANA - DB ANALYSIS')


if st.session_state.Table == 'Select Table':
    st.warning('No table selected. Please select the table first.', icon="⚠️")

else:
    st.info('Selected table : ' + st.session_state.Table,  icon='ℹ️')

    pr = st.session_state.DF.profile_report()
    st_profile_report(pr)