#Imports
import streamlit as st
import pytransit as pytr
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
import streamlit as st
import time
import pandas as pd

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

st.write("[put something here?]")

st.divider()

#introduce the methods
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
    hide_index = True
)

st.write("""As you can see, two methods dominate exoplanet detection thus far. We will be 
         focusing on these two methods, the Radial Velocity Method, and the Transit 
         Method.""")

st.write("[Work some softball questions in here: percent of just transit, then transit + rad. vel. (total = 5785)]")


#End of page
st.write("[Some variant of use the navigation bar to continue!]")

