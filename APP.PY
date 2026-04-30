import streamlit as st

st.title("Calculadora")

num1 = st.number_input("Primer número")
num2 = st.number_input("Segundo número")

operacion = st.selectbox(
    "Selecciona una operación",
    ["+", "-", "*", "/"]
)

if st.button("Calcular"):

    if operacion == "+":
        resultado = num1 + num2

    elif operacion == "-":
        resultado = num1 - num2

    elif operacion == "*":
        resultado = num1 * num2

    elif operacion == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "No se puede dividir entre 0"

    st.write("Resultado:", resultado)
