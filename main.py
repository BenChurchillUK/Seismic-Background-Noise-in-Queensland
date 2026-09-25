from obspy import UTCDateTime
from obspy.clients.fdsn import Client
client = Client("EARTHSCOPE")

st = client.get_waveforms(network="AU", station="QIS", 
                          location="00", channel="BHZ", 
                          starttime=UTCDateTime("2024-08-09T06:35:09"), endtime=UTCDateTime("2024-08-09T18:35:09"))
print(st)
st.plot()

stations = client.get_stations(
    network = "AU",
    station = "QIS",
    location= "00",
    channel = "BHZ",
    level= "channel"
)

for network in stations:
    for station in network:
        for channel in station:
            print("Channel:", channel.code)
            print("Location:", channel.location_code)
            print("Start:", channel.start_date)
            print("End:", channel.end_date)

# print(stations)
# print(vars(stations))
# print(type(stations))