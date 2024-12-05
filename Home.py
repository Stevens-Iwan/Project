#Needed imports
import streamlit as st
import pytransit as pytr
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
import streamlit as st
import time


"""
# My first app
Here's an example of filling in a table using pandas 
"""

import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

# #Testing a title and writing
# st.title("Title!")
# st.write("Hello World")

# #Put a dividing line in
# # st.divider()

# #Some simple latex for equations
# st.write("Simple quadratic:")
# st.latex(r"""
#          x^2 + 3x + 2 = 0
#          """)

# ###Simple plotting
# #Assigning sample data
# x_data = [1,2,3,4]
# y_data = [10,15,30,50]

# #Before the plt stuff
# fig, ax = plt.subplots()

# #Regular plt plotting
# plt.title("Title")
# plt.plot(x_data, y_data)

# #To actually show plot
# st.pyplot(fig)

#Start working on generalising slider questions
class slider_question(object):
    def __init__(self,question, answer, options, value, correct_reply="Correct!", wrong_reply="Try again!",key="q"):
      self.key=key
      self.answer=answer
      self.wrong_reply=wrong_reply
      self.correct_reply=correct_reply
      self.given_answer = st.select_slider(question, options, value,key=key)
      return
    
    def printanswer(self):
        if self.given_answer == self.answer:
          st.write(self.key,self.given_answer,self.correct_reply)
          # pass
        else:
            st.write(self.key,self.given_answer,self.wrong_reply)
            # pass
        return (st.write("given answer:",self.key,self.given_answer))

#Sample a question, whats 1+1 (bad example for slider, but nevertheless)
sample_question = "What's 1+1?"
sample_question2 = "What's 1+2?"
sample_answer = 2
sample_options = np.arange(0,11,1)
sample_value = 5

q1ans=slider_question(sample_question, sample_answer, sample_options, sample_value,key="q1")
q2ans=slider_question(sample_question, sample_answer, sample_options, sample_value,key="q2")

# insert button
def answers():
  st.write("HEre are the answres:")
  # st.write(q1ans.given_answer)
  q1ans.printanswer()

if st.button("Submit"):
   answers()
