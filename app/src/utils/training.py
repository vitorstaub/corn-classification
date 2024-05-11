import os
import PIL.Image

def list_images(folder_path):
    images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".png") or f.endswith(".jpg")]
    return sorted(images)
  
def imgs():
  path = './utils/content'
  variables = []
  images = list_images(path)
  for idx, image_path in enumerate(images):
    img_name = f"img{idx}"
    img = PIL.Image.open(image_path)
    print(image_path)
    exec(f"{img_name} = img")
    variables.append(img_name)
    return images
  print(variables)