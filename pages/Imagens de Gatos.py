from apis import cat_images
import streamlit as st

st.markdown(" 🐱 Gatitos Aleatórios 🐈 ")
st.sidebar.markdown("https://api.thecatapi.com/v1/images/search")

cat_image_url = cat_images.gatinho()

if cat_image_url:
    st.write("Um gatito:")
    st.image(cat_image_url, caption='Minheu')