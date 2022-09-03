import streamlit as st 
from PIL import Image


st.write("""
# Peopla Remova 
Reclaim nature! 
""")

pic = st.file_uploader("Picture to remove all the people", 
                type=["png", "jpg"], accept_multiple_files=False, 
                key=None, help=None, on_change=None, 
                args=None, kwargs=None, disabled=False)

if pic: 
    image = Image.open(pic)
    ## hook backend here 
  
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    if st.button("Remove People in this image?"):
        # implement back end here
        # once image is done ask to contribute to the database
        contributed = False 
        if st.button("Contribute to the map?", disabled = contributed):
            contributed = True
            st.write("Nature is reclaimed!")
            # add the image to our database


else:
    st.write("Please upload an image in a jpeg or png format!") 


if st.button("Reset?"):
    pic = None 