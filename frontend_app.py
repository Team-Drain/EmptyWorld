import streamlit as st 
from PIL import Image
from io import BytesIO
from google.oauth2 import service_account
from google.cloud import storage
import base64
import uuid
from models import do_it

GLOBAL_BUCKET = "team-drain-photos"

st.write("""
# See what the world looks like without people in the way
""")

pic = st.file_uploader("Please upload a picture in png or jpg format", 
                type=["png", "jpg"], accept_multiple_files=False, 
                key=None, help=None, on_change=None, 
                args=None, kwargs=None, disabled=False)


convertedImage = None 

if pic: 
    image = Image.open(pic)
    ## hook backend here 
  
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    if st.button("Remove People in this image?"):
        # implement back end here
        # once image is done ask to contribute to the database
        convertedImage = do_it(image)
        print("backend here")
else:
    st.write("Please upload an image in a jpeg or png format!") 

if convertedImage != None and st.button("Contribute to the map?"):
    pic = None 
    st.write("#Empty worlds!")

    credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
    )

    client = storage.Client(credentials=credentials)

    bucket = client.get_bucket(GLOBAL_BUCKET)
    
    imageName =f"{uuid.uuid1()}.jpeg"
    path = f"{imageName}"

    blob = bucket.blob(f"{imageName}")

    bs = BytesIO()
    convertedImage.save(bs, "jpeg")
    blob.upload_from_string(bs.getvalue(), content_type="image/jpeg")

    st.image(convertedImage, caption='Empty World.', use_column_width=True)   


if st.button("Reset?"):
    pic = None 
    convertedImage = None 
