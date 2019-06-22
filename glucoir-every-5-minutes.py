import time
import requests
from py_irsend import irsend

# Set up where we'll be fetching data from
DATA_SOURCE = "https://go-t1d.azurewebsites.net/api/v1/entries.json?count=1"
BG_VALUE = [0, 'sgv']
BG_DIRECTION = [0, 'direction']
 
RED = "red"
ORANGE = "orange"
YELLOW = "yellow"
GREEN = "green"
 
def get_bg_color(val):
    if val > 220:
        return RED
    elif val > 170:
        return YELLOW
    elif val < 70:
        return RED
    elif val < 80:
        return ORANGE
    return GREEN
 
def text_transform_bg(val):
    return str(val) + ' mg/dl'
     
response = requests.get(DATA_SOURCE)
data = response.json()

 
try:
    value = data[0]['glucose']
    print("Current glucose is ", value)
    color = get_bg_color(value)
    irsend.send_once('desk0', [color]) 
except RuntimeError as e:
    print("Some error occured, retrying! -", e)
