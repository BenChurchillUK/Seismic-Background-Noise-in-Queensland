from obspy import UTCDateTime
from obspy.clients.fdsn import Client
import pandas as pd

def set_client():
    cl= Client("EARTHSCOPE")
    return cl

def check_channels():
    return

def export_to_csv(df, file):
    df.to_csv(file)
    return