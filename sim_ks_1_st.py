import streamlit as st
import numpy as np

st.write('toto')


inf_att_p1 = st.number_input('Infantry attack (in %)', min_value=0.0, value=200.0, step=None, format="%0.2f", key=None, help=None, on_change=None, args=None, kwargs=None)
def fc_titi():
    st.write(inf_att_p1)


st.button('titi', on_click=fc_titi)

