#! /usr/bin/env python3

import os
import requests

feedback_path = '/data/feedback/'
URL = 'http://34.70.24.188/feedback/'

files = os.listdir(feedback_path)
for file in files:
  with open(feedback_path + file, 'r') as f:
    feedback = {"title": f.readline().strip(), "name": f.readline().strip(), "date": f.readline().strip(), "feedback": f.readline().strip()}
    response = requests.post(URL, data=feedback)
    response.raise_for_status()
