import pandas as pd
import numpy as np
import streamlit as st
import hdbcli
import plotly.express as px
import plotly.graph_objects as go
import os
import json
from hdbcli import dbapi

st.set_page_config(page_title="Table Selection", page_icon="📑", layout="wide")



def get_tabele_list(tables):
        table = ['Select Table']
        for i in tables:
            table.append(i[0])
        return table

def get_table_from_cursor(cursor):
        data = pd.DataFrame(cursor.fetchall())
        header = [i[0] for i in cursor.description]
        data = data.rename(columns=dict(zip(data.columns, header)))
        data = data.convert_dtypes()
        st.session_state.DF = data

if st.session_state.connection is None:
        st.warning('No connection found. Please upload the connection key first.', icon="⚠️")
else:
        cursor = st.session_state.connection.cursor()
        cursor.execute(f"SELECT TABLE_NAME FROM TABLES WHERE SCHEMA_NAME = '{'DBADMIN'}'")
        tables = cursor.fetchall()
        st.session_state.Table = st.selectbox('Select Table', get_tabele_list(tables))

        if st.session_state.Table != 'Select Table':
                cursor.execute(f"SELECT * FROM DBADMIN." + st.session_state.Table + " LIMIT 10000")
                get_table_from_cursor(cursor)

                st.write('Selected Table is: ' + st.session_state.Table)
                st.dataframe(st.session_state.DF.head(100), use_container_width=True)
                
                st.write('Table Discription')
                st.dataframe(st.session_state.DF.describe(), use_container_width=True)
                
                st.write("Table Column's Data Types")
                st.dataframe(st.session_state.DF.dtypes, use_container_width=True)