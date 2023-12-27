import pandas as pd
import numpy as np
import streamlit as st
import hdbcli
import plotly.express as px
import plotly.graph_objects as go
import os
import json
from hdbcli import dbapi
from pandasai import SmartDataframe
from pandasai.llm import GooglePalm

st.set_page_config(
    page_title="BOT Insights",
    page_icon="🤖",
    layout="wide",
)

if 'prompt' not in st.session_state:
    st.session_state.prompt = None

key_mode = st.sidebar.selectbox('Google GenAI API KEY input Mode: ',('Upload Own Key', 'Use Default Key'), key = 'key_sidebar')


if key_mode == 'Upload Own Key':
    api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password" )
else:
    api_key = st.secrets["API_KEY"]


if st.session_state.connection is None:
    st.warning('No connection found. Please upload the connection key first.', icon="⚠️")

elif st.session_state.DF is None:
    st.warning('No table selected. Please select the table first.', icon="⚠️")
    
elif len(api_key) <1:
    st.warning('Please enter your OpenAI API key.', icon="⚠️")
else:
    llm = GooglePalm(api_key=api_key)
    df = SmartDataframe(st.session_state.DF, config={"llm": llm})
    prompt_list = ['Hi']
    answer_list = ['Hello, I am a Maven-Bot. How can I help you?']
    st.session_state.prompt = 'Which Order Id repeate more times?'
    # '''with st.container(border=True):
    #     for i in range(0,len(prompt_list)):
    #         st.markdown(f'<h6 style="text-align: Right;">{prompt_list[i]}</h6>', unsafe_allow_html=True)
    #         st.markdown(f'<h6 style="text-align: Left;">{answer_list[i]}</h6>', unsafe_allow_html=True)'''

    prompt = st.text_input("Enter prompt:", st.session_state.prompt)
    response = df.chat(prompt)
    st.write(response)

    prompt_list.append(prompt)
    answer_list.append(response)

    st.session_state.prompt = ''


