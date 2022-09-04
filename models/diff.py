import torch
from diffusers import StableDiffusionInpaintPipeline

def remove_people(image, image_mask, device="cpu"):
  """Remove people from an image

  Args:
      image (PIL.Image): Image with people
      image_mask (PIL.Image): Mask that describes where the people are
      device (str, optional): Device to run the model on. Defaults to "cpu".

  Returns:
      PIL.Image: Image with people removed
  """
  image = image.resize((512, 512))
  image_mask = image_mask.resize((512, 512))

  model_id_or_path = "/home/jxli/stable-diffusion-v1-4"
  pipe = StableDiffusionInpaintPipeline.from_pretrained(model_id_or_path)
  pipe = pipe.to(device)

  prompt = "realistic photograph of scenery"
  with torch.no_grad():
    res = pipe(prompt=prompt, init_image=image, mask_image=image_mask, strength=0.7, num_inference_steps=50)
    images = res["sample"]

  return images[0]
