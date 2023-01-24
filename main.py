import streamlit as st
from PIL import Image
import pandas as pd
import pickle

def load_model():
    with open("model.pickle", "rb") as f:
        reg = pickle.load(f)
    return reg

PROPERTY_TYPE = (
    "apartment",
    "house"
)
DISTRICTS = [i for i in range(69001, 69010)]
EXTRAS = ("none", "ground", "pleasure grounds", "gardens", "deciduous forests", "orchards", "simple copses")
EXTRAS_SPECIAL = ("no special", "park", "vegetable garden", "building complex")
STATS = {
    "global": pd.read_csv("./data/stats-global.csv"),
    "houses": pd.read_csv("./data/stats-houses.csv"),
    "apartments": pd.read_csv("./data/stats-apartments.csv")
}
MODEL = load_model()

def get_n_lots(lots):
    return sum(1 for i in lots if i != 0)

def format_data() -> pd.DataFrame:
    df = pd.DataFrame(
        data=[[
            lots_surface[0], lots_surface[1], lots_surface[2], lots_surface[3], 
            lots_surface[3], get_n_lots(lots_surface), surface, rooms, land_surface, 0,
            0, 0, 0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0,
            0, 0, 0, 0
        ]], 
        columns=[
            "lot1_surface", "lot2_surface", "lot3_surface", "lot4_surface",
            "lot5_surface", "lots", "surface", "rooms", "land_surface", "apartment",
            "house", "deciduous_forests", "gardens", "ground", "none", "orchards",
            "pleasure_grounds", "simple_copses", "district_69001", "district_69002",
            "district_69003", "district_69004", "district_69005", "district_69006",
            "district_69007", "district_69008", "district_69009",
            "building_complex", "no_special", "park", "vegetable_garden"
        ]
    )
    df[[type, f"district_{district_id}", extra.replace(" ", "_"), extra_special.replace(" ", "_")]] = 1
    return df


st.set_page_config(
    page_title="House pricing prediction",
    layout="centered"
)
st.session_state.use_container_width = True
st.title("House pricing prediction in Lyon")
st.image(Image.open("./images/lyon.jpg"), caption="Lyon, FRANCE")

cols_property = st.columns(4)

type = cols_property[0].selectbox(
    "Type of property",
    PROPERTY_TYPE
)

surface = cols_property[1].number_input(
        "Surface (m²)",
        min_value=9.00,
        max_value=1000.00,
        step=0.01
)

rooms = cols_property[2].number_input(
        "Number of rooms",
        min_value=1,
        max_value=50,
        step=1
)

district_id = cols_property[3].selectbox(
    "District",
    DISTRICTS
)

lots_surface = []
cols_lots_surface_top = st.columns(2)
for i in range(2):
    lots_surface.append(cols_lots_surface_top[i].number_input(
        f"Lot {i+1} (m²)",
        min_value=0.00,
        max_value=1000.00,
        step=0.01
    ))

cols_lots_surface_bottom = st.columns(3)
for i in range(3):
    lots_surface.append(cols_lots_surface_bottom[i].number_input(
        f"Lot {i+3} (m²)",
        min_value=0.00,
        max_value=1000.00,
        step=0.01
    ))

cols_extras = st.columns(3)
extra = cols_extras[0].selectbox(
    "Extra",
    EXTRAS
)

extra_special = cols_extras[1].selectbox(
    "Special extra",
    EXTRAS_SPECIAL
)

land_surface = cols_extras[2].number_input(
    "Land surface (m²)",
    min_value=0.00,
    max_value=1000.00,
    step=0.01
)

if st.button("Predict"):
    st.dataframe(format_data())
    st.caption("your apartment")
    st.success(f"The estimated price of your {type} is {round(MODEL.predict(format_data())[0])}€.")
    st.caption("Note that this is just a prediction, the real price might be different from the predicted one.")

st.subheader("Some statistics to help you")

for name, stats in STATS.items():
    st.dataframe(
        stats.style.format({
            "average": "{:,.2f}€", 
            "25%": "{:,.2f}€", 
            "median": "{:,.2f}€", 
            "75%": "{:,.2f}€"
        }), use_container_width=st.session_state.use_container_width)
    st.caption(f"{name.capitalize()} statistics")