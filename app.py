import streamlit as st
import os
import random

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Horn Sound Generator",
    page_icon="🔊",
    layout="centered",
    initial_sidebar_state="expanded"
)

# -------------------------------
# SIDEBAR: DARK MODE & VOLUME
# -------------------------------
st.sidebar.title("Settings")
dark_mode = st.sidebar.checkbox("Dark Mode")
volume = st.sidebar.slider("Volume", min_value=0.0, max_value=1.0, value=0.8, step=0.05)

if dark_mode:
    st.markdown(
        """
        <style>
        .main { background-color: #1e1e1e; color: #ffffff; }
        .stButton>button { background-color: #333333; color: #ffffff; }
        </style>
        """, unsafe_allow_html=True
    )

# -------------------------------
# TITLE & INSTRUCTIONS
# -------------------------------
st.title("🔊 Horn Sound Generator")
st.subheader("Click a horn to play or use Random Horn")
st.markdown("Use the search box to filter horns. Works great on mobile!")

# -------------------------------
# SOUND CONFIGURATION
# -------------------------------
SOUND_FOLDER = "sounds"
os.makedirs(SOUND_FOLDER, exist_ok=True)

horn_names = [
    "Car Horn", "Truck Horn", "Train Horn", "Police Siren", "Ambulance Siren",
    "Ship Horn", "Motorbike Horn", "Bicycle Horn", "Air Horn", "Bus Horn",
    "Emergency Vehicle Horn", "Fire Truck Horn", "Boat Horn", "Express Train Horn",
    "School Bus Horn", "Taxi Horn", "Rickshaw Horn", "Jeep Horn", "Truck Beep",
    "Car Beep", "Truck Air Horn", "Train Warning Horn", "Ship Warning Horn",
    "Police Car Siren", "Ambulance Siren 2", "Foghorn", "Motorcycle Beep", "Bus Beep",
    "Car Alarm", "Truck Alarm", "Horn Short", "Horn Long", "Horn Medium",
    "Train Pass", "Ship Pass", "Airplane Warning Horn", "Police Long Siren",
    "Ambulance Long Siren", "Fire Alarm", "Motorbike Beep", "Car Honk", "Truck Honk",
    "Express Bus Horn", "City Bus Horn", "Van Horn", "School Horn", "Factory Horn",
    "Truck Stop Horn", "Ship Dock Horn", "Train Station Horn", "Emergency Alert"
]

# -------------------------------
# SEARCH FILTER
# -------------------------------
search_term = st.text_input("Search Horns:")
filtered_horns = [horn for horn in horn_names if search_term.lower() in horn.lower()]

# -------------------------------
# RANDOM HORN BUTTON
# -------------------------------
if st.button("🎲 Play Random Horn"):
    horn_to_play = random.choice(filtered_horns) if filtered_horns else random.choice(horn_names)
    sound_file = os.path.join(SOUND_FOLDER, horn_to_play.replace(" ", "_") + ".mp3")
    if os.path.exists(sound_file):
        audio_bytes = open(sound_file, 'rb').read()
        st.audio(audio_bytes, format="audio/mp3", start_time=0)
    else:
        st.warning(f"Sound file {sound_file} not found!")

# -------------------------------
# DISPLAY HORNS IN GRID
# -------------------------------
cols = st.columns(3)
for idx, horn in enumerate(filtered_horns):
    col = cols[idx % 3]
    if col.button(horn):
        sound_file = os.path.join(SOUND_FOLDER, horn.replace(" ", "_") + ".mp3")
        if os.path.exists(sound_file):
            audio_bytes = open(sound_file, 'rb').read()
            st.audio(audio_bytes, format="audio/mp3", start_time=0)
        else:
            st.warning(f"Sound file {sound_file} not found!")

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit | Replace placeholder MP3s with real horn sounds in the `sounds/` folder")
