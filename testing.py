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

#Testing a title and writing
st.title("Title!")
st.write("Hello World")


#Testing streaming text
streamed_text = """
  This text is coming out in a stream!
  It is currently coming out at a rate of 5 words/second, but this rate can be freely changed. 
  """

#Function to run through the text (could be made more general but not needed now)
def stream_data():
    for word in streamed_text.split(" "):
        yield word + " "
        time.sleep(0.2)

#Use the st.write_stream tool and call the function
if st.button("Stream the text?"):
    st.write_stream(stream_data)

#Put a dividing line in
st.divider()

#Some simple latex for equations
st.write("Simple quadratic:")
st.latex(r"""
         x^2 + 3x + 2 = 0
         """)

###Simple plotting
#Assigning sample data
x_data = [1,2,3,4]
y_data = [10,15,30,50]

#Before the plt stuff
fig, ax = plt.subplots()

#Regular plt plotting
plt.title("Title")
plt.plot(x_data, y_data)

#To actually show plot
st.pyplot(fig)