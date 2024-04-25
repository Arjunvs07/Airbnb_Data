import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image

df = pd.read_csv('C:\\Users\\ADMIN\\New folder\\Airbnb.csv')
# data preprocessing
df['name'].fillna("Unknown",inplace= True)
df['host_location'].fillna("Unknown",inplace= True)

def neighbourhood(df1,neigh):
    new_df = df1[df1['host_neighbourhood']==neigh]
    new1 = new_df.groupby('room_type').sum('price')
    new1.reset_index(inplace=True)
    col1,col2 = st.columns(2)
    with col1:

        fig_1 =px.bar(new1,x = 'room_type',y = 'price',title = "Room type and Price",
                    color_discrete_sequence=px.colors.sequential.Rainbow_r,height = 650, width = 600)
        st.plotly_chart(fig_1)

    new2 = new_df.groupby('property_type').sum('accommodates')
    new2.reset_index(inplace=True)
    with col2:
        fig_2 = px.bar(new2,x = 'property_type',y = 'accommodates',title = "Property type and accommodates",
                            color_discrete_sequence=px.colors.sequential.Cividis_r,height = 650, width = 600 )
        st.plotly_chart(fig_2)

def availability(df2,val):
    if val == 30:
        figure_1 = px.pie(df2,values = 'availability_30',names= 'country',title = "COUNTRY AND AVAILABILITY FOR 30 DAYS")
        st.plotly_chart(figure_1)
    elif val==60:
        figure_2 = px.pie(df2,values='availability_60', names = 'country',title = "COUNTRY AND AVAILABILITY FOR 60 DAYS")
        st.plotly_chart(figure_2)
    elif val == 90:
        figure_3 = px.pie(df2,values='availability_90', names = 'country',title = "COUNTRY AND AVAILABILITY FOR 90 DAYS")
        st.plotly_chart(figure_3)
    elif val == 365:
        figure_4 = px.pie(df2,values='availability_365', names = 'country',title = "COUNTRY AND AVAILABILITY FOR 365 DAYS")
        st.plotly_chart(figure_4)

def review_details(df3,sub):
    new_df = df3[df3['suburb']==sub]
    fig = px.scatter(new_df, x= 'number_of_reviews',y ='review_scores',color ='room_type',title = "Review Details" )
    fig.update_layout(width = 1000,height = 800)
    st.plotly_chart(fig)

def host_neighbourhood(df4,coun):
    cdf = df4[df4['country']== coun]
    fig = px.scatter(cdf,x = 'host_neighbourhood',y = 'street',color = 'room_type')
    fig.update_layout(width = 1500,height = 1000)
    st.plotly_chart(fig)

def mapping_countries(df,co):
    mmdf = df[df['country']==co]
    selected_columns = ['latitude','longitude','street','review_scores','room_type']
    mdf = mmdf[selected_columns]
    fig = px.scatter_mapbox(mdf,lat= 'latitude',lon='longitude',color = 'room_type',
                            size = 'review_scores',size_max=30,zoom = 5, mapbox_style="carto-positron",
                            hover_name = 'street' )
    fig.update_layout(width =1600 , height = 700)
    st.plotly_chart(fig)


#Streamlit part
st.set_page_config(layout = "wide")
st.markdown("<h1 style='text-align: center; color: blue;'>AirBnb Analysis</h1>", unsafe_allow_html=True)
with st.sidebar:
    select = option_menu("Main Menu",["HOME","DATA EXPLORATION","CONTACTS"])
if select == "HOME":
    col1,col2 = st.columns(2)
    with col1:
        st.image(r"C:\Users\ADMIN\New folder\image-airbnb.jpg")
    with col2:
        st.write("***Airbnb is an American San Francisco-based company operating an online marketplace for short and long-term homestays and experiences. The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia. Airbnb is a shortened version of its original name, AirBedandBreakfast.com. The company is credited with revolutionizing the tourism industry, while also having been the subject of intense criticism by residents of tourism hotspot cities like Barcelona and Venice for enabling an unaffordable increase in home rents, and for a lack of regulation.*** ")
        st.write("")
        st.write("")
        st.write("***Skills take away From This Project:***")
        st.write("")
        st.write("")
        st.write("***Python Scripting, Data Preprocessing, Visualization, EDA, Streamlit,MongoDb, PowerBi or Tableau***")
        st.write("")
        st.write("")
        st.write("***Domain***")
        st.write("")
        st.write("")
        st.write("***Travel Industry, Property Management and Tourism***")


elif select == "DATA EXPLORATION":
    st.subheader("NEIGHBOURHOOD DATA VISUALIZATION")
    neighbour = st.selectbox("Select The Neighbourhood",df["host_neighbourhood"].unique())
    neighbourhood(df,neighbour)

    st.subheader("COUNTRY AND AVAILABILITY")
    value = [30,60,90,365]
    avail = st.selectbox("Select the Availability for ",value)
    availability(df,avail)

    st.subheader("SCATTER PLOT OF REVIEWS")
    suburb = st.selectbox("Select the Suburb :",df['suburb'].unique())
    review_details(df,suburb)

    st.subheader("SCATTER PLOT OF NEIGHBOURHOOD AND STREET")
    cou = st.selectbox("Select the Country :",df["country"].unique())
    host_neighbourhood(df,cou)

    st.subheader("MAP OF HOTSPOTS IN THE COUNTRY")
    co = st.selectbox("Select the Country 1:",df["country"].unique())
    mapping_countries(df,co)

elif select == "CONTACTS":
    col1,col2 = st.columns(2)
    with col1:
        st.image(r"D:\New folder\arju.jpg")
    
    with col2:
        st.write("")
        st.write("## This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, andlocation-based trends.")
        st.write("")
        st.write("")
        st.write("## Name : ARJUN V S")
        st.write("## Email : arjun07.cr@gmail.com")