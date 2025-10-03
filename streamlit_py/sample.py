import streamlit as st

st.title("Ani Shop")
st.header("Welcome to this Ani shop !")
st.write("This is the best anime website you buy what ever you want ")

fav_name=st.text_input("Enter your Anime ? :")
if fav_name:
    st.success(f"Your FAVOURITE aNIME IS : {fav_name}")

gener=st.selectbox ("your Favourite Anime Gener ? :" ,["Fantasy","Thriller","Action"])
st.write("your Favourite genere is :",gener)