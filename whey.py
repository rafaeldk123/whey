import streamlit as st
from PIL import Image

favicon=Image.open('logo.jfif')
st.set_page_config(page_title='Calculadora de Whey',page_icon=favicon,layout="wide", initial_sidebar_state="collapsed")

st.title('Calculadora de Whey')

peso = st.number_input('Peso total do produto (g):',min_value=1,max_value=9999999999999,value=900)
qtd = st.number_input('Quantidade por porção (g):',min_value=1,max_value=9999999999999,value=30)
qtd_prot = st.number_input('Quantidade de proteína por porção (g):',min_value=1,max_value=9999999999999,value=24)
valor = st.number_input('Valor do produto:',min_value=1,max_value=9999999999999,value=99)

peso=int(peso)
qtd=int(qtd)
qtd_prot=int(qtd_prot)
valor=int(valor)

percprot=int(round((qtd_prot*100/qtd)))
valor100gprot=round(100*(valor/(peso*(qtd_prot/qtd))),2)
st.write(f'**Percentual de proteína:** {percprot}%')
if percprot>100:
    st.warning('Por favor, ajuste os valores.', icon=None)
st.write(f'**Valor de 100g de proteína:** R${valor100gprot}')



