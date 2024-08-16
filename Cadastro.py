import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(nome, data_nasc, tipo):
    if nome and data_nasc <= date.today():
        with open("clientes.csv", "a", encoding="UTF-8") as file:
            file.write(f"{nome},{data_nasc},{tipo}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False
st.set_page_config(
    page_title="Cadastro de clientes",
    page_icon="📒"
)

st.title("Cadastro de Clientes")
st.divider()

nome = st.text_input("Digite o nome do cliente",
                     key="nome_cliente")

dt_nasc = st.date_input("Data de nascimento", min_value=date.min, max_value=date.today(), format="DD/MM/YYYY")

tipo = st.selectbox("Tipo de cliente",
                    ["Pessoa Física", "Pessoa Jurídica"])

btn_cadastrar = st.button("Cadastrar",
                          on_click=gravar_dados,
                          args=[nome, dt_nasc, tipo])
if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cilente cadastrado com sucesso!",
                   icon="👌")
    else:
        st.error("Cliente não cadastrado!",
                 icon="👎")