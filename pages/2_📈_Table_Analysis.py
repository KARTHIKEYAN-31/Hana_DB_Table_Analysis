import pandas as pd
import numpy as np
import streamlit as st
import hdbcli
import plotly.express as px
import plotly.graph_objects as go
import os
import json
from hdbcli import dbapi

st.set_page_config(page_title="Analysis", page_icon="📈", layout="wide")

st.header('HANA - DB ANALYSIS')

if st.session_state.Table == 'Select Table':
    st.warning('No table selected. Please select the table first.', icon="⚠️")

else:

    st.info('Selected table : ' + st.session_state.Table,  icon='ℹ️')

    tab1, tab2 = st.tabs(["Uni-Variable Analysis", "Bi-Variable Analysis"])

    columns = st.session_state.DF.columns

    with tab1:
        column = st.selectbox('Select Column for Analysis', columns, key='column')

        chart_type = st.radio(
            "Which type of Chart do you want?",
            ["Box Plot", "Scatter Plot", "Histogram"],horizontal=True)

        if chart_type == "Histogram":
            fig = px.histogram(st.session_state.DF, x = column, nbins=10)
        elif chart_type == "Scatter Plot":
            fig = px.scatter(st.session_state.DF, y = column, x = st.session_state.DF.index)
        else:
            fig = px.box(st.session_state.DF, x = column)

        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        c1, c2 = st.columns(2)

        with c1:
            column1 = st.selectbox('Select Column for Analysis', columns, key='column1')

        with c2:
            column2 = st.selectbox('Select Column for Analysis', columns, key='column2')
        
        chart_type = st.radio(
            "Which type of Chart do you want?",
            ["Scatter Plot", "Histogram"],horizontal=True, key='chart_type')
        
        if chart_type == "Histogram":
            fig = px.histogram(st.session_state.DF, x = column1, y = column2, nbins=10)
        elif chart_type == "Scatter Plot":
            fig = px.scatter(st.session_state.DF, y = column1, x = column2)


        st.plotly_chart(fig, use_container_width=True)
            