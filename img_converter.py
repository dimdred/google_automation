#!/usr/bin/env python3

import os
from PIL import Image

files_path = os.getcwd() + '/images/'
new_path = '/opt/icons/'

if not os.path.exists(new_path):
  os.makedirs(new_path)

for (root, dirs, files) in os.walk(files_path):
  for file in files:
    if not file.startswith('.'):
      with Image.open(files_path + file) as im:
        im.convert('RGB').rotate(-90).resize((128,128)).save(new_path + file,'JPEG')