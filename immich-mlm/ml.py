import io
from PIL import Image
from transformers import pipeline



def hugging_face_ic(img_data, model):
    img = Image.open(io.BytesIO(img_data))
    classifier = pipeline("image-classification", model=model)
    r = classifier(img)
    return r

"""
Models:

Falconsai/nsfw_image_detection
    Label: Normal
    Label: NSFW
microsoft/dit-large-finetuned-rvlcdip
    Label: *
"""
