# EmptyWorld
## Team Drain PennApps Project

#### Application to remove people from images using modern deep learning techniques.

#### Webapp usage
Visit `emptyworld.tech` and follow the instructions.

#### Streamlit App Usage
```
mkdir ${YOUR_PROJECT_NAME}
cd ${YOUR_PROJECT_NAME}
git clone https://github.com/Team-Drain/EmptyWorld
pip install streamlit -U git+https://github.com/huggingface/diffusers -r requirements.txt
streamlit run run.py
```

#### Steps:
1. You upload an image onto our application (through the website or 
2. Application segments the image using a convolutional network to identify all humans and generate a mask
3. Uses stable-diffusion, an image generation paradigm, to fill in the areas in the mask to form a natural picture without any of the humans identified by the mask
4. You receive a copy of your image without any of the people identified by the segmentation present


#### Features:
* App running on Google Cloud
* Distributed application to service multiple clients at once

#### Future work:
* Allow user to select which identified people to remove from image
