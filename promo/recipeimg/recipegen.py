# Import module
import os
from PIL import Image

# Assign directory
directory = ".\\original"

# Iterate over files in directory
with Image.open("background.png") as bg:
    for name in os.listdir(directory):
        with Image.open(os.path.join(directory, name)) as im:
            cropped = im.crop([1080,420,1800,816])
            cbg = bg.copy()
            cbg.paste(cropped,[66,24])
            cbg =  cbg.resize([420,240],Image.Resampling.NEAREST)
            cbg.save(name)