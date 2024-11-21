#Needed imports
import streamlit as st
import pytransit as pytr
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
import streamlit as st
import time

st.write("Hello")

#Example use of sliders
start_val, end_val = st.select_slider("Select the values 3 and 6 (in that order): ", 
                          options=np.arange(0,11,1),
                          value= (0, 10))

if start_val == 3 and end_val == 6:
    st.write("Good job!")

#Example use of single selection question

math_test_answer = st.radio("What's 3x2?:", 
                            options = 
                            [3, 6, 9, 12], 
                            captions = 
                            ["really?", "hmmm...", "not quite", "miles off"],
                            index = None)       #So no value starts selected

if math_test_answer == None:
    st.write("Please answer the question >:(")
elif math_test_answer == 6:
    st.write("You passed the math test!")
else: 
    st.write("You failed the math test!")