import streamlit as st 
from PIL import Image
from io import BytesIO
import pandas as pd
from google.oauth2 import service_account
from google.cloud import storage
import base64

import uuid

GLOBAL_BUCKET = "fella-remova-photos"


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
        if contributed:
            st.write("Nature is reclaimed!")

            credentials = service_account.Credentials.from_service_account_info(
            st.secrets["gcp_service_account"]
            )

            client = storage.Client(credentials=credentials)

            bucket = client.get_bucket(GLOBAL_BUCKET)

            imageName =f"{uuid.uuid1()}"
            path = f"{imageName}"

            blob = bucket.blob(f"{GLOBAL_BUCKET}/{imageName}.jpg")

            blob.content_type = "image/jpeg"
            st.write(f"writing")
            # with open(path, 'rb') as f:
            converted_string = base64.b64encode(image.read())
            blob.upload_from_string(converted_string)
            st.write(f"here {blob.public_url}")   
else:
    st.write("Please upload an image in a jpeg or png format!") 




if st.button("Reset?"):
    pic = None 