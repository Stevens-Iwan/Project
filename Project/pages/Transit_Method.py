#Imports
import streamlit as st
from pytransit import RoadRunnerModel
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
import streamlit as st
import time
import pandas as pd
import random

##Brief outline
st.title("Transit Method")
st.subheader("Catching a Star Blinking")
st.divider()

st.write("""When an exoplanet passes in front of its star (from our point of view), it blocks a small fraction of the star’s light.
         This causes a small, temporary dip in brightness. This dip can be recorded on a graph called a light curve, helping astronomers
         to detect the presence of the planet. On this page, you'll learn how it works and even try creating your own light curves!""")

st.divider()

#Show an image of a simplified light curve
st.image("JWST_light_curve.png", caption="This light curve was captured by the James Webb Space Telescope. We can clearly see that the " \
"star's light dips as the planet passes in front.")

st.divider()

#Thorough intro
st.write("""The transit method is one of the most effective techniques astronomers use to detect exoplanets. 
         It works by measuring the tiny, regular dip in a star’s brightness when a planet passes directly in front of it from our point of view. This event is known as a transit.""")

st.write("""When a planet transits its star, it blocks a small fraction of the starlight, causing a temporary and predictable dimming.
          By monitoring the brightness of a star over a long period, astronomers can identify these dimming patterns and infer the presence of an orbiting planet.""")

st.write("""The data is recorded in a graph called a light curve (as seen above), which plots a star’s brightness over time. A transit produces a distinctive, symmetrical dip in the light curve.
         The depth of this dip tells us how large the planet is relative to its star: a larger planet blocks more light, creating a deeper dip.""")

#Quick Questions to break up text
st.write("Tick the correct statements to test your knowledge.")

with st.form("checkbox_quiz"):
    q1 = st.checkbox("The transit method detects change in a star's temperature.")
    q2 = st.checkbox("An exoplanet transit causes a slight dip in measured brightness from the star.")
    q3 = st.checkbox("The depth of the dip depends primarily upon the temperature of the star.")

    submitted = st.form_submit_button("Check answers")

if q1:
    st.error("Not quite! The transit method detects changes in the star's brightness.")

if q2: 
    st.success("Correct! The transit causes a small dip in measured brightness.")

if q3:
    st.error("Not quite! The depth depends primarily upon the ratio of planet radius to star radius.")

st.divider()

#Rest of introduction
st.write("""Importantly, not all exoplanets can be detected using this method. For a transit to be visible, the planet’s orbit must be aligned with our line of sight from Earth. 
         The exoplanet must at least partially eclipse the star. This introduces a natural bias, we can only detect a small fraction of existing exoplanets this way.""")

st.write("""Despite this limitation, the transit method has been responsible for the discovery of thousands of confirmed exoplanets.
          Even more excitingly, it enables us to calculate a planet’s radius and estimate its orbital period. When combined with other techniques this 
         method can even help deduce the compositions of atmospheres!""")

#More quick questions
with st.form("checkbox_quiz2"):
    q4 = st.checkbox("All exoplanets can be detected from Earth using the transit method.")
    q5 = st.checkbox("Through analysing the composition of an exoplanet's atmosphere, researchers could predict if life exists on that exoplanet.")

    submitted = st.form_submit_button("Check answers")

if q4:
    st.error("Not quite! Not all exoplanets can be detected this way. This method requires that the exoplanet transits in front of its host star from Earth's perspective.")

if q5: 
    st.success("Correct! Researchers can make assertions on the existence of life on an exoplanet using atmospheric makeup. More on this later!")

st.divider()

#Interactive light curve using pytransit, with diagram of system
st.subheader("Interactive Transit Light Curve")
st.write("Adjust the planet's size and orbit to see how the light curve and orbital system change!")

#Parameter sliders
rp_rs = st.slider("Planet-to-star radius ratio (Rp/Rs)", 0.01, 0.2, 0.1, 0.01)
a_rs = st.slider("Semi-major axis / star radius (a/Rs)", 2.0, 20.0, 10.0, 0.5)

#Set time array
times = np.linspace(-0.05, 0.05, 300)

#Initialize model
tm = RoadRunnerModel('quadratic')
tm.set_data(times)

#Evaluate using simplifications and slider inputs
flux = tm.evaluate(k=rp_rs, ldc=[0.3, 0.2], t0=0.0, p=1.0, a=a_rs, i=(np.pi/2))

#Create two columns to display side by side
col1, col2 = st.columns(2)

with col1:
    st.subheader("Transit Light Curve")
    fig1, ax1 = plt.subplots(figsize=(5, 3))
    ax1.plot(times, flux, color='blue')
    ax1.set_xlabel("Time from Mid-Transit (days)")
    ax1.set_ylabel("Relative Brightness")
    ax1.set_title("Simulated Light Curve")
    ax1.grid(True)
    st.pyplot(fig1)

with col2:
    st.subheader("System Diagram")
    fig2, ax2 = plt.subplots(figsize=(4, 4))  # Adjusted size for compactness

    #Star
    star = plt.Circle((0, 0), 1, color='gold', label='Star')
    ax2.add_artist(star)

    #Orbit
    orbit = plt.Circle((0, 0), a_rs, color='gray', fill=False, linestyle='--')
    ax2.add_artist(orbit)

    #Planet
    planet = plt.Circle((0, a_rs), rp_rs, color='blue', label='Planet')
    ax2.add_artist(planet)

    # Plot formatting
    ax2.set_xlim(-a_rs - 1, a_rs + 1)
    ax2.set_ylim(-a_rs - 1, a_rs + 1)
    ax2.set_aspect('equal')
    plt.title("System View")
    plt.axis('off')
    ax2.legend()
    st.pyplot(fig2)

st.divider()

#Introduce simplified equation
st.subheader("Transit Depth Equation")
st.latex(r"\Delta F = \left(\frac{R_p}{R_s}\right)^2")

st.write("""The transit depth is the fractional drop in brightness we see when an exoplanet passes in front of its star.
        It depends primarily on the ratio of the planet's radius to the star's radius.
        This makes the transit method especially good at measuring a planet’s size relative to its star.""")

#Show simplified transit depth equation, some easy numerical questions 
st.write("Finally, here are some questions to test your understanding of the transit depth equation.")

#Asking the questions in one form
with st.form("numerical_questions"):
    st.write("1. What is the transit depth if Rp/Rs = 0.1?")
    ans6 = st.number_input("Answer for 1. (as a decimal, e.g. 0.01)", min_value=0.0, max_value=1.0, step=0.0001, key="q6")

    st.write("2. If a planet causes a 0.0025 (0.25%) drop in brightness, what is Rp/Rs?")
    ans7 = st.number_input("Answer for Q2 (as a decimal, e.g. 0.05)", min_value=0.0, max_value=1.0, step=0.0001, key="q7")

    st.write("3. Calculate the transit depth for your chosen slider values above:")
    ans8 = st.number_input("Answer for Q3 (as a decimal)", min_value=0.0, max_value=1.0, step=0.0001, key="q8")

    #Submit button
    submitted = st.form_submit_button("Submit answers")

if submitted:
    if np.isclose(ans6, 0.01, atol=0.0005):
        st.success("1.: Correct! A planet with Rp/Rs = 0.1 would cause a 1% dip in brightness.")
    else:
        st.error("1.: Not quite! Remember ΔF = (Rp/Rs)².")

    # Check Q2
    if np.isclose(ans7, 0.05, atol=0.0005):
        st.success("2.: Correct! Rp/Rs = √0.0025 = 0.05.")
    else:
        st.error("2.: Not quite! Remember Rp/Rs = √(transit depth).")

    # Check Q3
    expected_depth = rp_rs**2
    if np.isclose(ans8, expected_depth, atol=0.0005):
        st.success(f"3.: Correct! The calculated transit depth is {expected_depth:.4f}.")
    else:
        st.error("3.: Not quite! Try using your Rp/Rs value from the slider: ({rp_rs:.2f})².")

st.divider()

#Conclude page
st.subheader("Conclusion")
st.write("""The transit method is one of the most powerful tools in modern exoplanet discovery.
         By carefully measuring the dip in a star’s brightness when a planet passes in front of it, astronomers can determine the planet’s radius relative to its star, 
         estimate its orbital distance, and even identify multiple planets in the same system.""")
         
st.write("""However, while the transit method reveals a planet’s size, it doesn’t tell us anything about what the planet is made of, whether it has an atmosphere, or what conditions might exist there.
To uncover those mysteries, scientists turn to a technique known as transit spectroscopy - studying the starlight that passes through a planet’s atmosphere during a transit.""")

st.write("""In the next section, you’ll explore how this method allows astronomers to detect the gases surrounding distant worlds, and search for signs that might one day hint at life beyond our Solar System.""")


