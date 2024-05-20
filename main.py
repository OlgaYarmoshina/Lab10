import matplotlib.pyplot as plt
import streamlit as st

st.image('titanic.jpg')
st.header('Данные пассажиров Титаника')
st.write("Для просмотра данных о стоимости билетов , выберите пункт из списка ")
selected = st.selectbox('Выберите тип стоимости', ['Средняя цена', 'Максимальная цена', 'Минимальная цена'])

