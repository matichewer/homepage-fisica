import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import requests
from streamlit_option_menu import option_menu
import intro,cinematica,dinamica,energia,choque,sonido,anexo

# Correr aplicacion en terminal: python -m streamlit run ..../home.py


with st.sidebar:
    app = option_menu(
        menu_title='Proyecto',
        options=['Intro', 'Cinematica', 'Dinamica','Energia','Choque','Audio','Anexo'],
        icons=['house', 'c-circle-fill', 'graph-up','lightning','transparency','volume-up-fill','stickies'],
        menu_icon='chat-square-text',
        default_index=0,
        styles={
            "container": {"padding": "3!important", "background-color": "black"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px"},
            "nav-link-selected": {"background-color": "#FF532E"},
        }
    )


if app == "Intro":
    intro.app()
elif app == "Cinematica":
    cinematica.app()
elif app == "Dinamica":
    dinamica.app()
elif app == "Energia":
    energia.app()
elif app == "Choque":
    choque.app()
elif app == "Audio":
    sonido.app()
elif app == 'Anexo':
    anexo.app()

