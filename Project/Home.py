#Imports
import streamlit as st
import pytransit as pytr
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
import streamlit as st
import time
import pandas as pd
import random

#Session state
if "q1_submitted" not in st.session_state:
    st.session_state.q1_submitted = False
if "q2_submitted" not in st.session_state:
    st.session_state.q2_submitted = False
if "q3_submitted" not in st.session_state:
    st.session_state.q3_submitted = False


#Definitions for questions
total_det = 5785
radial_det = 1094
transit_det = 4307

#Define exoplanet methods
detection_methods = pd.DataFrame(
        {
            "Method Name": ["Astrometry", "Imaging", "Radial Velocity", "Transit", "Transit Timing Variations"
                     ,"Eclipse Timing Variations", "Microlensing", "Pulsar Timing Variations", "Pulsation Timing Variations",
                     "Orbital Brightness Modulations","Disk Kinematics"],
            "Detections to Date": [3, 82, 1094, 4307, 32, 17, 230, 8, 2, 9, 1]
        }
)


#Title and header
st.title("Is There Anyone Else Out There?")
st.subheader("An Exploration of Exoplanets Through the Transit Method")
st.divider()

#Intro paragraph
st.write("""How do astrophysicists discover planets outside of our solar system, and what can be learned about them? 
         This interactive workshop will guide you through the captivating world of exoplanet detection and characterisation.""")

#Exoplanet k218b image
st.image("k218b.jpg", caption = "Exoplanet Kepler 218b")

#exoplanets introduction
st.write("""Exoplanets are planets that orbit a star outside of our Solar System. They vary massively, from smoulderingingly
         hot gas giants even larger than our Jupiter, to terrestrial Earth-likes that could hold alien life. The first exoplanet
         was discovered in 1992, and since then we have discovered many, many more.""")

st.write("""For centuries, humans have wondered whether we are alone in the universe. Investigation into these exoplanets could bring us far closer
         to finally answering this question. Further, by investigating exoplanets and the systems they reside in, we learn new information about
         the universe around us. As technology and understanding steadily improves, we may one day find evidence of life beyond Earth!""")

#Easy question to start, how many exoplanets to nearest 1000 using st.form
#Question 1
if not st.session_state.q1_submitted:
    with st.form("q1_form"):
        st.write("Question 1: How many exoplanets do you think we have discovered, to the nearest thousand?")
        q1_answer = st.text_input("Your answer:")
        q1_submit = st.form_submit_button("Submit Q1")

        if q1_submit:
            try:
                int(q1_answer)
                st.session_state.q1_answer = q1_answer
                st.session_state.q1_submitted = True
            except ValueError:
                st.error("Please enter a valid number.")

#Show answer after submitted
if st.session_state.q1_submitted:
    st.write(f"Your answer: {st.session_state.q1_answer}")
    q1_int_answer = int(st.session_state.q1_answer)
    if q1_int_answer == 6000:
        st.success("Correct! We have discovered 5785 exoplanets thus far!")
    elif q1_int_answer in [5000, 7000]:
        st.info("Close! We have discovered 5785 exoplanets thus far!")
    else:
        st.error("Not quite! We have discovered 5785 exoplanets thus far!")

st.divider()

#introduce the methods
st.subheader("How do we Detect These Exoplanets?")
st.write("""
         There are many methods used to detect exoplanets, each with it's own strengths and 
         weaknesses. The table below provides you with a quick overview of the methods
         and their detections so far!
         """)

#Display the dataframe
st.dataframe(
    detection_methods,
    width = 1000,
    height = 425,
)

st.write("""As you can see, two methods dominate exoplanet detection thus far. We will be 
         focusing on these two methods, the Radial Velocity Method, and the Transit 
         Method.""")

#percent of discoveries from transit

st.divider()

#Question 2
if not st.session_state.q2_submitted:
    with st.form("q2_form"):
        st.write("Question 2: To the nearest whole number, what percent of exoplanets discovered have come from the transit method and radial velocity methods combined?")
        q2_answer = st.text_input("Enter your answer here:")
        q2_submit = st.form_submit_button("Submit Q2")

        if q2_submit:
            try:
                int(q2_answer)
                st.session_state.q2_answer = q2_answer
                st.session_state.q2_submitted = True
            except ValueError:
                st.error("Please enter a valid number.")

#Show Q2 answer after submit
if st.session_state.q2_submitted:
    st.write(f"Your answer: {st.session_state.q2_answer}")
    q2_int_answer = int(st.session_state.q2_answer)
    if q2_int_answer == 93:
        st.success("Correct! 93.36% of all exoplanets currently discovered come from these two methods. Safe to say these methods dominate current exoplanet detection.")
    elif q2_int_answer in [90,91,92,94,95,96]:
        st.info("Close! 93.36% of all exoplanets currently discovered come from these two methods. Safe to say these methods dominate current exoplanet detection.")
    else:
        st.error("Not quite! 93.36% of all exoplanets currently discovered come from these two methods. Safe to say these methods dominate current exoplanet detection.")


#Question 3
if not st.session_state.q3_submitted:
    with st.form("q3_form", border=False):
        st.write("Question 3: To the nearest whole number, what percent of exoplanets discovered have come from the transit method alone?")
        q3_answer = st.text_input("Enter your answer here:")
        q3_submit = st.form_submit_button("Submit Q3")

        if q3_submit:
            try:
                int(q3_answer)
                st.session_state.q3_answer = q3_answer
                st.session_state.q3_submitted = True
            except ValueError:
                st.error("Please enter a valid number.")

#Show Q3 answer after submit
if st.session_state.q3_submitted:
    st.write(f"Your answer: {st.session_state.q3_answer}")
    q3_int_answer = int(st.session_state.q3_answer)
    if q3_int_answer == 74:
        st.success("Correct! 74.45% of all exoplanets currently discovered come from this method. This is the most popular method by far.")
    elif q3_int_answer in [71,72,73,75,76,77]:
        st.info("Close! 74.45% of all exoplanets currently discovered come from this method. This is the most popular method by far.")
    else:
        st.error("Not quite! 74.45% of all exoplanets currently discovered come from this method. This is the most popular method by far.")

st.divider()

#Fun fact randomiser

fun_facts = [
    "The first exoplanets were discovered orbiting a pulsar in 1992!",
    "The exoplanet Kepler 16b orbits a binary system, orbitting two stars!",
    "The closest exoplanet to us that has been discovered is Proxima Centauri b, only 4.25 light-years away!",
    "The smallest exoplanet discovered is called PSR J0337+1715(ABC) b (catchy...), and is 0.41% the size of Earth!",
    "The youngest exoplanet discovered is DH Tauri b, it's only 700,000 years old!",
    "The exoplanet with the shortest orbital period is GALEX 0718+3731 b, and takes 11.2 minutes to orbit its host star!",
    "The exoplanet with the longest orbital period is Gliese 900 b, and takes 1.27million years to orbit its host star!",
            ]

if st.button("Show a random fact"):
    st.success(random.choice(fun_facts))

st.divider()

st.write("""In this workshop, we'll be focusing on the transit method, and transit spectroscopy. These two methods have led to some of the most 
         exciting discoveries in exoplanet science, including the detection of atmospheres containing water vapour and hints of potentially 
         habitable conditions on distant worlds.""")

st.write("""In the next sections, we will explore how these techniques work in detail — starting with the transit method. Use the navigation menu
         on the left to begin your investigation.""")


#End of page


