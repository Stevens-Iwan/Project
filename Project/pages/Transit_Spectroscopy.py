#Imports
import streamlit as st
import pytransit as pytr
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
import streamlit as st
import time
import pandas as pd

#Header
st.title("Transit Spectroscopy")
st.subheader("Spotting Signs of Life")
st.divider()

#Brief introduction
st.write("""Finding an exoplanet is just the first step. To truly understand an exoplanet (and if it holds life!), we need to investigate it's atmosphere. This is where
         Transit Spectroscopy comes in.""")

st.write("""When an exoplanet passes in front of it's host star, some of the starlight filters through the atmosphere of the planet. By studying the changes in the star's light,
         researchers can identify the makeup of an exoplanet's atmosphere, and start to make claims about the potential of extra terrestrial life!""")

st.divider()

#Quick question
st.write("1. What information do we gain from performing transit spectroscopy?")
options1 = st.radio("Choose one:", 
                    ["The exoplanet's size",
                    "The exoplanet's orbital period",
                    "The exoplanet's atmospheric composition"], index = None, key = "q1")

if options1 == "The exoplanet's atmospheric composition":
    st.success("Correct! From this method we can learn about the makeup of an exoplanet's atmosphere.")
elif options1 == "The exoplanet's orbital period":
    st.error("Not quite! From this method we can learn about the makeup of an exoplanet's atmosphere.")
elif options1 == "The exoplanet's size":
    st.error("Not quite! From this method we can learn about the makeup of an exoplanet's atmosphere.")

st.divider()

#Introduction to absorption lines
#Using "particle A 100% absorbs green" simpilification
st.subheader("Absorption Lines")
st.write("""When white light from a star passes through the atmosphere of a planet, some colours (or wavelengths) get absorbed by gases within the atmosphere.
         Each type of atom of molecule absorbs light at different specific wavelengths, leaving dark lines in the spectrum of the star. These are called
         absorption lines.""")
st.write("By studying where these lines appear, astronomers can deduce the makeup of an exoplanet's atmosphere.")

st.image("absorptionlines.png", caption = "Example absorption lines. Each dark line represents a specific atom or molecule's absorption.")

st.divider()

#Mid-easy questions on absorptionlines
st.write("2. What do absorption lines tell us about an exoplanet?")

options2 = st.radio("Choose one:",
                    ["Exoplanet's distance from it's star",
                    "Which atoms/molecules are present in the atmosphere",
                    "How long the exoplanet takes to orbit it's star"], None, key = "q2"
                    )

if options2 == "Exoplanet's distance from it's star":
    st.error("Not quite! From observing absorption lines we can understand what atoms or molecules are present in an atmosphere.")

elif options2 == "Which atoms/molecules are present in the atmosphere":
    st.success("Correct! From observing absorption lines we can understand what atoms or molecules are present in an atmosphere.")

elif options2 == "How long the exoplanet takes to orbit it's star":
    st.error("Not quite! From observing absorption lines we can understand what atoms or molecules are present in an atmosphere.")


st.write("3. Why do you think different gases absorb different wavelengths of light?")

options3 = st.radio("Choose one:",
                    ["Because of the colour of the host star",
                     "Because of the planet's surface temperature",
                     "Because each gas has it's own molecular structure and energy levels"], None, key = "q3"
                     )

if options3 == "Because of the colour of the host star":
    st.error("Not quite! Different gases absorb different wavelengths due to their unique molecular structure and energy levels.")

elif options3 == "Because of the planet's surface temperature":
    st.error("Not quite! Different gases absorb different wavelengths due to their unique molecular structure and energy levels.")

elif options3 == "Because each gas has it's own molecular structure and energy levels":
    st.success("Correct! Different gases absorb different wavelengths due to their unique molecular structure and energy levels.")

st.divider()

#Interactive atmospheric mixing
st.subheader("Interactive Atmospheric Mixing")

#Sliders 
h2o = st.slider("Water Vapour (H2O) %", 0, 100, 30, 5, key = "h2o_slider")
ch4 = st.slider("Methane (CH4) %", 0, 100, 20, 5, key= "ch4_slider")
co2 = st.slider("Carbon Dioxide (CO2) %", 0, 100, 25, 5, key= "co2_slider")

#Define wavelength range in microns
wavelengths = np.linspace(1.0, 5.0, 500)

#Base flux (ones - normalised)
flux = np.ones_like(wavelengths)

#Apply absorption dips: gaussian dips for simplification
def absorption_dip(wave, center, strength, width=0.05):
    return strength * np.exp(-0.5 * ((wave - center)/width)**2)

#Add in the features
flux -= absorption_dip(wavelengths, 1.4, h2o/200)
flux -= absorption_dip(wavelengths, 2.3, ch4/200)
flux -= absorption_dip(wavelengths, 4.3, co2/200)

#Plot the graph
fig, ax = plt.subplots(figsize=(7,4))
ax.plot(wavelengths, flux, color='purple')
ax.set_xlabel("Wavelength (um)")
ax.set_ylabel("Relative Flux")
ax.set_title("Simulated Absorption Spectrum")
ax.set_ylim(0.7, 1.05)
ax.grid(True)
st.pyplot(fig)

st.divider()

#Questions about interactive element
st.write("4. What happens to the absorption dip at 4.3um if you increase the CO2 percentage?")

options4 = st.radio("Choose one:",
                    ["The dip gets deeper",
                     "The dip disappears",
                     "The dip moves to a different wavelength"], None, key="q4" 
                     )

if options4 == "The dip gets deeper":
    st.success("Correct! A deeper dip at 4.3um indicates more CO2.")

elif options4 == "The dip disappears":
    st.error("Not quite! A deeper dip at 4.3um indicates more CO2.")

elif options4 == ("The dip moves to a different wavelength"):
    st.error("Not quite! A deeper dip at 4.3um indicates more CO2.")

st.write("5. If the atmosphere contained no H2O, what would happen to the absorption feature at 1.4um?")

options5 = st.radio("Choose one:",
                    ["It would disappear",
                     "It would get deeper",
                     "It would move to a different wavelength"], None, key="q5"
                     )

if options5 == "It would disappear":
    st.success("Correct! Without any H2O to absorb, there would be no feature at this wavelength.")

elif options5 == "It would get deeper":
    st.error("Not quite! Without any H2O to absorb, there would be no feature at this wavelength.")

elif options5 == "It would move to a different wavelength":
    st.error("Not quite! Without any H2O to absorb, there would be no feature at this wavelength.")

st.write("6. If an exoplanet's atmosphere was rich in CH4 but contained no H2O or CO2, what would its absorption spectrum most likely look like?")

options6 = st.radio("Choose one:",
                    ["There would be a strong absorption dip only at 2.3 um",
                      "There would be strong dips at 1.4 µm, 2.3 µm, and 4.3 um",
                      "There would be no absorption features at all"], None, key = "q6"
                      )

if options6 == "There would be a strong absorption dip only at 2.3 um":
    st.success("Correct! Only methane would be present to absorb, at it's characteristic 2.3um.")

elif options6 == "There would be strong dips at 1.4 µm, 2.3 µm, and 4.3 um":
    st.error("Not quite! Only methane would be present to absorb, at it's characteristic 2.3um.")

elif options6 == "There would be no absorption features at all":
    st.error("Not quite! Only methane would be present to absorb, at it's characteristic 2.3um.")

st.divider()

#Biosignatures
st.subheader("Searching For life: Biosignatures")

st.write("""Now that you know how we can detect and study exoplanet atmospheres, the next question is: can we tell if something is alive out there?
        Scientists look for biosignatures, chemicals in an atmosphere that are typically produced by living organisms.
        If we detect these gases in the right combinations, it could suggest the presence of biological activity on an exoplanet.""")

st.write("Some key biosignatures include:")

st.markdown("""
- Oxygen (O2) - on Earth, 21% of our atmosphere is oxygen, almost entirely produced by life.
- Ozone (O3) - formed from oxygen, often linked to biological oxygen production.
- Methane (CH4) - produced by microbes and other organisms, on Earth it’s quickly destroyed unless continually replenished.
- Nitrous Oxide (N2O) - another gas made by microbes.
- Water Vapour (H2O) - essential for life as we know it.""")

#Quick question
st.write("7. Why would finding both oxygen and methane together in an exoplanet's atmosphere be potentially exciting for researchers?")

options7 = st.radio("Choose one:",
                     ["Because they occur naturally on all planets",
                      "Because their presence together suggests they could be produced by life",
                      "Because they make the planet hotter"], None, key="q7")

if options7 == "Because they occur naturally on all planets":
    st.error("Not quite! These gases would react together and wouldn't stay in an atmosphere for long. This suggests they're being actively produced by something - life?")

elif options7 == "Because their presence together suggests they could be produced by life":
    st.success("Correct! These gases would react together and wouldn't stay in an atmosphere for long. This suggests they're being actively produced by something - life?")

elif options7 == "Because they make the planet hotter":
    st.error("Not quite! These gases would react together and wouldn't stay in an atmosphere for long. This suggests they're being actively produced by something - life?")

st.divider()

#Conclusion
st.subheader("Conclusion")

st.write("""
By studying how starlight changes as it passes through an exoplanet’s atmosphere, we can uncover the gases present, identify key molecules like water vapour, methane, and oxygen, and even search for potential signs of life.
           
Transit Spectroscopy is one of the most exciting frontiers in astrophysics, not just for finding distant worlds, but for understanding what those worlds might be like.
         
As we continue refining our understanding and advancing observational technology, we move ever closer to answering one of humanity’s longest standing and most troubling questions:""")

st.subheader("Is There Anyone Else Out There?")

