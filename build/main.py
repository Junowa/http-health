import requests
import time
import sys
import os

url = os.environ['HEALTH_URL']

while True:
  try:
    r = requests.get(url)
    r.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xxx
  except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
    sys.stderr.write('Connection Timeout\n')  
  except requests.exceptions.HTTPError:
    sys.stdout.write('HTTP Error\n')  
  else:
    sys.stdout.write('All Good\n')  
  time.sleep(5)
