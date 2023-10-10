
import numpy as np
import plotly.express as px
import pandas as pd
import streamlit as st
st.set_page_config(layout='wide')
desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',15)
df=pd.read_csv('india.csv')
list_of_states=list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title("India's Insides-Let's Explore")
selected_state=st.sidebar.selectbox('Select a state',list_of_states)
primary=st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary=st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))

plot=st.sidebar.button('Plot Graph')
if plot:
    st.text('Size represents primary parameter')
    st.text('Color represents secondary parameter')
    if selected_state=='Overall India':
        #plot for India
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",size=primary,color=secondary,zoom=3,size_max=35,
                                mapbox_style="carto-positron",color_continuous_scale='Viridis',
                                width=1200,height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:

        state_df=df[df['State']==selected_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude",size=primary, color=secondary, zoom=6,
                                size_max=35,
                                mapbox_style="carto-positron",color_continuous_scale='Viridis', width=1200, height=700, hover_name='District')
        st.plotly_chart(fig, use_container_width=True)