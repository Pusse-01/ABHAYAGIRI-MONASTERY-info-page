import streamlit as st
from utils.read import read_file

st.set_page_config(page_title="ABHAYAGIRI MONASTERY")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title ("ABHAYAGIRI MONASTERY")

intro1 = read_file("./data/intro1.txt")
st.write(intro1)

images = ['./images/1.jpg', './images/2.jpg']
# st.image(images, use_column_width=True, width=80)

col1, col2 = st.columns(2)

with col1:
    st.image(images[0],caption="අභයගිරි දාගැබ")

with col2:
    st.image(images[1], caption="ස්තුපයේ ආයක")

intro2 = read_file("./data/intro2.txt")
st.write(intro2)

st.write("")

st.header("Lavatories in Abhayagiri monastery")
para2 = read_file("./data/para2.txt")
st.write(para2)
st.image("./images/5.png", caption="Map of Abhayagiriya Monastery")

st.write("")

st.subheader("Evidences for lavatiroes")
para3 = read_file("./data/evi1.txt")
st.write(para3)

st.image("./images/3.png")

st.warning("Read more [  from here](https://yukthiyawenuwen.blogspot.com/2014/11/blog-post_65.html)")

