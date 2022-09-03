import streamlit as st 
from PIL import Image


st.write("""
# Fella Remova 
Get rid of all those pesky fellas!
""")

pic = st.file_uploader("Picture to remove dem fellas", 
                type=["png", "jpg"], accept_multiple_files=False, 
                key=None, help=None, on_change=None, 
                args=None, kwargs=None, disabled=False)

if pic: 
    image = Image.open(pic)
    ## hook backend here 

    st.image(image, caption='Uploaded Image.', use_column_width=True)

    if st.button("Remove da fella's in this image?"):
        st.write("ok..")


else:
    st.write("Please upload an image in a jpeg or png format!") 


if st.button("Reset?"):
    pic = None 