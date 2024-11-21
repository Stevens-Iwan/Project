#Needed imports
import streamlit as st
import pytransit as pytr
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
import streamlit as st
import time

#Start working on generalising slider questions
def slider_question(question, answer, options, value, correct_reply="Correct!", wrong_reply="Try again!"):
    given_answer = st.select_slider(question, options, value)
    if given_answer == answer:
        st.write(correct_reply)
    else:
        st.write(wrong_reply)

#Sample a question, whats 1+1 (bad example for slider, but nevertheless)
sample_question = "What's 1+1?"
sample_answer = 2
sample_options = np.arange[0,11,1]
sample_value = 5

slider_question(sample_question, sample_answer, sample_options, sample_value)

