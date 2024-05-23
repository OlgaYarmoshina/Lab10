import streamlit as st

st.header('Практическое занятие №11')
st.image('titanic.jpg')
st.header('Работа группы 2023-ФГиИБ-ПИ-2см: Подгруппа №2 ')

choice = st.selectbox('Вариант номер:',  ['вариант 10','вариант 8'])

#from var10 import do_var1
#from var10 import do_var5
from var8 import do_var8
from var10 import do_var10
#from var10 import do_var15
#from var10 import do_var18

if choice == 'вариант 10':
    do_var10()
#elif choice == 'вариант 5':
    #do_var5()
elif choice == 'вариант 8':
    do_var8()
#elif choice == 'вариант 1':
    #do_var1()
#elif choice == 'вариант 15':
   # do_var15()
#elif choice == 'вариант 18':
    #do_var18()

