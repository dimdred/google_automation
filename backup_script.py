#!/usr/bin/env python3

import subprocess
import os

abspath = os.path.abspath('..')
src = abspath + '/data/prod/'

for root, dirs, files in os.walk(src):
  for name in dirs:
    new_folder = os.path.join(root, name).replace("prod","prod_backup")
    #create folder if necessary
    if not os.path.exists(new_folder):
      os.makedirs(new_folder)
  for name in files:
    prod_file = os.path.join(root, name)
    backup_file = prod_file.replace("prod", "prod_backup")
    # sync data recursively from prod to bakup path
    subprocess.call(["rsync","-arg", prod_file, backup_file])