import sys
import time
import requests
from py_irsend import irsend
import argparse

# Set up where we'll be fetching data from
DATA_SOURCE = "https://yournightscoutinstance.herokuapp.com/api/v1/entries.json?count=1"
BG_VALUE = [0, 'sgv']
BG_DIRECTION = [0, 'direction']

RED = "red"
ORANGE = "orange"
YELLOW = "yellow"
GREEN = "green"

parser = argparse.ArgumentParser()
parser.add_argument("-bg", "--bloodglucose", type=int,
                    help="Send IR command depending on blood glucose level")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()
value = args.bloodglucose

if args.verbose:
    if args.manualBG:
        print("Manually set the Blood Glucose Value to ", value)
    else:
        print("Being more verbose on no manual input of Blood Glucose.")

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

if value is None:
    response = requests.get(DATA_SOURCE)
    data = response.json()
    # print(data[0])
    value = data[0]['sgv']


try:
    print("Current glucose is ", value)
    color = get_bg_color(value)
    irsend.send_once('desk0', ['ON'])
    irsend.send_once('desk0', [color])
    irsend.send_once('desk0', ['darker'])
    irsend.send_once('desk0', ['darker'])
    irsend.send_once('desk0', ['darker'])
    irsend.send_once('desk0', ['lighter'])
    irsend.send_once('desk0', ['lighter'])
    irsend.send_once('desk0', ['lighter'])
except RuntimeError as e:
    print("Some error occured, retrying! -", e)
