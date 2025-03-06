#Needed imports
import streamlit as st
import pytransit as pytr
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
import streamlit as st
import time

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

#Sample some questions
sample_slider1 = "What's 1+1?"
sample_slider2 = "What's 1+2?"
sample_slider_answ1 = 2
sample_slider_answ2 = 3
sample_slider_options = np.arange(0,11,1)
sample_value = 5

q1ans=slider_question(sample_slider1, sample_slider_answ1, sample_slider_options, sample_value,key="q1")
q2ans=slider_question(sample_slider2, sample_slider_answ2, sample_slider_options, sample_value,key="q2")

# insert button
def slider_answers():
  st.write("Here are the answers:")
  # st.write(q1ans.given_answer)
  q1ans.printanswer()
  q2ans.printanswer()

if st.button("Submit", key=1):
   slider_answers()

#Start generalising multiple choice
class multiple_choice(object):
   def __init__(self,question,answer, options,correct_reply="Correct!", wrong_reply="Try again!",key="q"): 
      self.key=key
      self.answer=answer
      self.wrong_reply=wrong_reply
      self.correct_reply=correct_reply
      self.given_answer = st.selectbox(question,options,key=key)
      return
   def printanswer(self):
        if self.given_answer == self.answer:
          st.write(self.key,self.given_answer,self.correct_reply)
          # pass
        else:
            st.write(self.key,self.given_answer,self.wrong_reply)
            # pass
        return (st.write("given answer:",self.key,self.given_answer))
 

sample_box1 = "What's 3x2?"
sample_box_ans = 6
sample_box_options = [5, 6, 9]

q3ans=multiple_choice(sample_box1, sample_box_ans, sample_box_options,key="q3")

#Insert a button
def select_answer():
  st.write("Here are the answers:")
  # st.write(q1ans.given_answer)
  q3ans.printanswer()

if st.button("Submit", key=2):
   select_answer()


#Start generalising number input questions
class numerical(object):
   def __init__(self,question,answer,correct_reply="Correct!", wrong_reply="Try again!",key="q"): 
      self.key=key
      self.answer=answer
      self.wrong_reply=wrong_reply
      self.correct_reply=correct_reply
      self.given_answer = st.number_input(question,key=key)
      return
   def printanswer(self):
        if self.given_answer == self.answer:
          st.write(self.key,self.given_answer,self.correct_reply)
          # pass
        else:
            st.write(self.key,self.given_answer,self.wrong_reply)
            # pass
        return (st.write("given answer:",self.key,self.given_answer))

sample_numerical1 = "What's 3x3?"
sample_numerical_ans = 9

q4ans= numerical(sample_numerical1, sample_numerical_ans, key = "q4")

#Insert a button
def numerical_answer():
  st.write("Here are the answers:")
  # st.write(q1ans.given_answer)
  q4ans.printanswer()

if st.button("Submit", key=4):
   numerical_answer()


#Dictionary example
question_dict = {
   "question1" : {
      "question" : "questiontext1",
      "answer" : "sampleanswer1",
      "options" : "sample options1",
      "value" : "sample value1",
      "correct reply" : "Correct!",
      "wrong reply" : "Try again!",
      "key" : "q1"
   },
   "question2" : {
      "question" : "questiontext2",
      "answer" : "sampleanswer2",
      "options" : "sample options2",
      "value" : "sample value2",
      "correct reply" : "Correct!",
      "wrong reply" : "Try again!",
      "key" : "q2"
   }
   
   }

st.write("Dictionary testing: ")
st.write(question_dict["question1"]["options"])
st.write(question_dict["question2"]["value"])
