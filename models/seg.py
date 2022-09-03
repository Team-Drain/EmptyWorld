import io
from PIL import Image
import torch
import numpy
import itertools

from transformers import DetrFeatureExtractor, DetrForSegmentation
from transformers.models.detr.feature_extraction_detr import rgb_to_id

feature_extractor = DetrFeatureExtractor.from_pretrained("facebook/detr-resnet-50-panoptic")
model = DetrForSegmentation.from_pretrained("facebook/detr-resnet-50-panoptic")

def get_human_mask(image):
  """Get a mask that colors the people in white and everything else in black.

  Args:
      image (PIL.Image): Input image

  Returns:
      PIL.Image: Image mask
  """

  # prepare image for the model
  inputs = feature_extractor(images=image, return_tensors="pt")

  # forward pass
  outputs = model(**inputs)

  # use the `post_process_panoptic` method of `DetrFeatureExtractor` to convert to COCO format
  processed_sizes = torch.as_tensor(inputs["pixel_values"].shape[-2:]).unsqueeze(0)
  result = feature_extractor.post_process_panoptic(outputs, processed_sizes)[0]

  # the segmentation is stored in a special-format png
  panoptic_seg = Image.open(io.BytesIO(result["png_string"]))
  panoptic_seg = numpy.array(panoptic_seg, dtype=numpy.uint8)
  # retrieve the ids corresponding to each mask
  panoptic_seg_id = rgb_to_id(panoptic_seg)

  # category_id of a person is 1. Filter this out.

  person_ids = set()
  for obj in result['segments_info']:
    if obj['category_id'] == 1:
      person_ids.add(obj['id'])

  mask = numpy.zeros(panoptic_seg_id.shape, dtype=numpy.uint8)

  rows, cols = panoptic_seg_id.shape
  for r, c in itertools.product(range(rows), range(cols)):
    if panoptic_seg_id[r, c] in person_ids:
      mask[r, c] = 1

  # Make areas to edit white 
  mask *= 255
  # Make mask a RGB thing with three color channels
  mask = numpy.stack([mask, mask, mask], axis=2)

  return Image.fromarray(mask, "RGB")