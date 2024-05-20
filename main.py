import streamlit as st
from var10 import do_var10
st.image('titanic.jpg')
choice = st.selectbox('Вариант номер:',  ['вариант 10','вариант 12','вариант 13'])

if choice == 'Вариант 10':
    do_var10()
elif choice == 'Вариант 12':
    pass

