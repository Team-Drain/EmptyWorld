import streamlit as st
import urllib, io
from PIL import Image
from google.oauth2 import service_account
from google.cloud import storage


BUCKET_NAME = "fella-remova-photos"
#  = "maxresdefault.jpg"

st.write("""
# What's out there? See what a 0 person world looks like
""")

print(st.secrets["gcp_service_account"],"\n\n\n\n\n\n")
# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)

client = storage.Client(credentials=credentials)

# Retrieve file contents.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
#@st.experimental_memo(ttl=600)
def read_file(bucket_name, file_path):
    bucket = client.bucket(bucket_name)
    content = bucket.blob(file_path).download_as_string()
    return content


# get all blobs 
bucket = client.get_bucket(BUCKET_NAME)
blobs = bucket.list_blobs()

for blob in blobs:
    
    # URL='https://storage.googleapis.com/{}/{}'.format(bucket_name,picture_name)
    picture_name = blob.name 
    # x = read_file(BUCKET_NAME, picture_name)

    # b = io.BytesIO(x)

    # blob = bucket.blob(destination_blob_filename)
    downloaded_im_data = blob.download_as_bytes()
    downloaded_im = Image.open(io.BytesIO(downloaded_im_data))
    # im = Image.open(b)

    st.image(downloaded_im)


