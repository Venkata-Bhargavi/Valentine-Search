import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests

st.set_page_config(  # Alternate names: setup_page, page, layout
    layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
    initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
    page_title='Venkata_Bhargavi_Sikhakolli',  # String or None. Strings get appended with "• Streamlit".
    page_icon= None,  # String, anything supported by st.image, or None.
)
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
title_1,title_2 = st.columns([2,1])
with title_1:
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("<h1 style='font-size: 60px; text-align: center'>Find your Valentine</h1>", unsafe_allow_html=True)
with title_2:
    lottie_hello = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_ya6bnm3a.json")
    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        height="450px",
        width=None,
        key=None,
    )

st.markdown("-----------------------------------------------------------------------------------------------------------")
#Data as list to populate selectbox
Gender = ["Select","Female","Male","Prefer not to reveal"]
fun_list = ["Select","Outdoor activities (e.g. hiking, camping, etc.)","Indoor activities (e.g. reading, watching movies, etc.)","Adventure sports (e.g. skydiving, surfing, etc.)","Cultural activities (e.g. visiting museums, attending concerts, etc.)","Relaxation (e.g. yoga, spa days, etc.)"]
hobbie_list = ["Select","Art and craft","Cooking and baking""Music and instruments""Sports and fitness""Photography and videography""Traveling and exploring new places"]
work_list=["Select","Business/Entrepreneurship","Healthcare and medicine","Technology and software development","Education and teaching","Sales and marketing","Creative fields (e.g. writing, graphic design, etc.)","I'm currently looking for work"]
family_list=["Select","Close-knit and supportive","Large and spread out","Extroverted and social","Introverted and reserved"]
date_list = ["Select","Dinner and a show","Adventure and exploration","Relaxation and pampering","Cultural and educational","Something unique and unexpected"]
adventure_list = ["Select","Skydiving","Bungee jumping","Whitewater rafting","Rock climbing","Traveling solo to a foreign country","Trying a new and exotic cuisine"]
challenge_list = ["Select","Health and wellness","Relationships and communication","Career and work-life balance","Personal growth and self-discovery","Financial stability"]
goals_list = ["Select","Career success","Travel and exploration","Building a family and home","Personal growth and development","Financial stability and security"]
passion_list = ["Select","Environmental activism and conservation","Animal rights and welfare","Human rights and social justice","The arts and culture","Health and wellness","Education and mentorship"]
cuisine_list = ["Select","Italian","Mexican","Chinese","Indian","Mediterranean","Sushi"]
tradition_list = ["Select","Holidays and festivals","Family gatherings and celebrations","Religious and spiritual practices","Folklore and mythology","Cuisine and food","Art and craft"]
try_list = ["Select","Learning a new language","Trying a new sport or activity","Traveling to a new and exotic location","Taking up a new hobby or skill","Trying a new cuisine or restaurant","Participating in an extreme sport or adventure"]
#Columns
gen,temp = st.columns([1,1])
q1_1,q1_2 = st.columns([1,1])
q2_1,q2_2 = st.columns([1,1])
q3_1,q3_2 = st.columns([1,1])
q4_1,q4_2 = st.columns([1,1])
q5_1,q5_2 = st.columns([1,1])
q6_1,q6_2 = st.columns([1,1])
q7_1,q7_2 = st.columns([1,1])





#Actions in columns
with gen:
    st.selectbox("Gender",Gender)
with q1_1:
    st.selectbox("What do you like to do for fun?",fun_list)
with q1_2:
    st.selectbox("What are your favorite hobbies and interests?",hobbie_list)
with q2_1:
    st.selectbox("What do you do for work and what do you enjoy about it?",work_list)
with q2_2:
    st.selectbox("What are your family and friends like?",family_list)
with q3_1:
    st.selectbox("What is your idea of a perfect date?",date_list)
with q3_2:
    st.selectbox("What is the most adventurous thing you've ever done?",adventure_list)
with q4_1:
    st.selectbox("What is a personal challenge you've faced?",challenge_list)
with q4_2:
    st.selectbox("What are your goals and aspirations for the future?",goals_list)
with q5_1:
    st.selectbox("What is something you're passionate about?",passion_list)
with q5_2:
    st.selectbox("What is your favorite type of cuisine?",cuisine_list)
with q6_1:
    st.selectbox("What is a unique tradition or custom from your culture?",tradition_list)
with q6_2:
    st.selectbox("What is something you've always wanted to try but haven't yet?",try_list)
