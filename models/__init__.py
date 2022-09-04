from .diff import remove_people
from .seg import get_human_mask

def do_it(img):
    mask = get_human_mask(img)
    return remove_people(img, mask)
