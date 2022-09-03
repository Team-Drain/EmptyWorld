from models import remove_people, get_human_mask
from PIL import Image
img = Image.open("IMG_1640.jpeg")
mask = get_human_mask(img)
result = remove_people(img, mask)
result.save("result.png")