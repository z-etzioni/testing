import streamlit as st
import math
from supabase import create_client, Client

st.set_page_config(page_title="Econ Salary", page_icon="📈", layout="centered")

SUPABASE_URL = "https://auqqsiljywsnqghtechh.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF1cXFzaWxqeXdzbnFnaHRlY2hoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQ3MjEwMzAsImV4cCI6MjA2MDI5NzAzMH0.jaDhkMMokUoBIOep1x2gUvdo5kVNzLcd6P_LZbQm8f4"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

if "already_logged" not in st.session_state:
    try:
        supabase.table("visits").insert({}).execute()
    except Exception as e:
        st.warning("Visitor logging failed.")
    st.session_state["already_logged"] = True

res = supabase.table("visits").select("id", count="exact").execute()
visits = res.count

st.title("Predicting Salaries of Economics Professors in the United States")
st.markdown(f"#### 👥 Total Visitors: {visits}")

def compute_y(Theory, Econometrics, TPhD, THired, N_pub, N_top5, Tenure, Full, USNews):
    log_y = 11.8583 - 0.0026605 * Theory + 0.030356 * Econometrics \
    + 0.023127 * TPhD - 0.0002489 * TPhD**2 - 0.02081 * THired + 0.00027308 * THired**2 \
    + 0.0014252 * (N_pub - N_top5) + 0.042406 * N_top5 - 0.00064717 * TPhD * N_top5\
    + 0.10419 * Tenure + 0.14185 * Full + 0.090521 * max(USNews-2,0) + 0.15594 * max(USNews - 4,0)
    return int(round(1.029*math.exp(log_y)/1000)*1000)


st.markdown("""
    <style>
    @media (prefers-color-scheme: dark) {
        .highlight-text {
            font-size: 20px;
            font-weight: bold;
            color: #FFFFFF !important;  /* White text in dark mode */
            padding: 5px;
        }
        .list-text {
            font-size: 18px;
            color: #DDDDDD !important;  /* Light gray for readability */
            padding-left: 15px;
        }
    }

    @media (prefers-color-scheme: light) {
        .highlight-text {
            font-size: 20px;
            font-weight: bold;
            color: #000000 !important;  /* Black text in light mode */
            padding: 5px;
        }
        .list-text {
            font-size: 18px;
            color: #333333 !important;  /* Dark gray for readability */
            padding-left: 15px;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="highlight-text">Developed by:</p>', unsafe_allow_html=True)
st.markdown('<p class="list-text">- <a href="https://alexisakira.github.io/">Alexis Akira Toda</a>, Professor, Emory University (data analysis)</p>', unsafe_allow_html=True)
st.markdown('<p class="list-text">- <a href="https://www.linkedin.com/in/zachary-etzioni-5904aa296/">Zachary Etzioni</a>, Class of 2027, Emory University (web tool)</p>', unsafe_allow_html=True)

st.markdown('<p class="highlight-text">The prediction is based on the following parameters (R-squared 80%):</p>', unsafe_allow_html=True)
st.markdown('<p class="list-text">- Education</p>', unsafe_allow_html=True)
st.markdown('<p class="list-text">- Employment</p>', unsafe_allow_html=True)
st.markdown('<p class="list-text">- Field</p>', unsafe_allow_html=True)
st.markdown('<p class="list-text">- Publications</p>', unsafe_allow_html=True)

st.markdown('<p class="highlight-text">The predictive model is an extension of <a href="https://econjwatch.org/articles/publications-citations-position-and-compensation-of-economics-professors">Lyu and Toda (2019)</a></p>', unsafe_allow_html=True)
st.markdown('<p class="list-text">Disclaimer: the model is still experimental</p>', unsafe_allow_html=True)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    /* Auto-detects dark or light mode */
    @media (prefers-color-scheme: dark) {
        html, body, .stApp {
            background-color: #121212;
            color: white;
        }
        .main-title { color: #FFD700; }  /* Gold Title in Dark Mode */
        .sub-text { color: #DDDDDD; }  /* Lighter Gray for Readability */
        .stNumberInput label, .stRadio label {
            color: white !important;
            font-weight: 600;
        }
        .stRadio div[role="radiogroup"] label {
            color: white !important;
            font-size: 16px;
            font-weight: bold;
        }
        .stNumberInput, .stRadio {
            background: #1E1E1E;
            color: white;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(255,255,255,0.1);
        }
        .stButton button {
            background-color: #1DB954;
            color: black;
        }
    }

    @media (prefers-color-scheme: light) {
        html, body, .stApp {
            background-color: white;
            color: black;
        }
        .main-title { color: #1E1E1E; }  /* Dark Title in Light Mode */
        .sub-text { color: #333333; }
        .stNumberInput label, .stRadio label {
            color: black !important;
            font-weight: 600;
        }
        .stRadio div[role="radiogroup"] label {
            color: black !important;
            font-size: 16px;
            font-weight: bold;
        }
        .stNumberInput, .stRadio {
            background: #F0F0F0;
            color: black;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        .stButton button {
            background-color: #007BFF;
            color: white;
        }
    }

    .main-title {
        font-size: 36px;
        text-align: center;
        font-weight: 600;
        margin-bottom: 10px;
    }
    .sub-text {
        font-size: 18px;
        text-align: center;
        font-weight: 300;
        margin-bottom: 20px;
    }
    .stButton button {
        font-size: 18px;
        padding: 12px 24px;
        border-radius: 8px;
        border: none;
        transition: 0.3s;
    }
    .stButton button:hover {
        filter: brightness(1.1);
    }
    </style>
""", unsafe_allow_html=True)


st.markdown('<p class="main-title">Enter your values below and click Compute Salary.</p>', unsafe_allow_html=True)

with st.container():
    TPhD = st.number_input("How many years ago did you finish PhD?", min_value=0, step=1, max_value = 50, format="%d")
    THired = st.number_input("How many years have you been working at your current institution?", min_value=0, step=1, max_value = 50, format="%d")
    Theory = st.radio("Is your research mainly about theoretical analysis of economic models? Choose Yes (1) or No (0).", [0, 1])
    Econometrics = st.radio("Is your research mainly about econometrics or statistics? Choose Yes (1) or No (0).", [0, 1])
    N_pub = st.number_input("How many papers have you published? Please include only peer-reviewed research or review articles that you are comfortable listing in your CV under 'research'. Exclude books, book chapters, comments, conference proceedings (no AEA P&P, please!), corrigenda, handbook chapters, etc.", min_value=0, step=1, format="%d")
    N_top5 = st.number_input("How many papers have you published in so-called 'Top 5' economics journals?", min_value=0, step=1, format="%d")
    Tenure = st.radio("Do you have tenure? Choose Yes (1) or No (0).", [0, 1])
    Full = st.radio("Are you a full professor? Choose Yes (1) or No (0).", [0, 1])
    USNews = st.number_input("What is the [US News Peer Assessment Score](https://www.usnews.com/best-graduate-schools/top-humanities-schools/economics-rankings) of your department? Enter 1.0 if your school is not listed.", min_value = 1.0, max_value = 5.0, value = "min", step = 0.1, format="%0.1f")

if st.button("🔍 Compute Salary"):
    salary = compute_y(Theory, Econometrics, TPhD, THired, N_pub, N_top5, Tenure, Full, USNews)
    st.success(f"💰 Your expected salary in 2024 is **${salary:,}**")
