import speedtest
import datetime

st = speedtest.Speedtest()
now = datetime.datetime.now()
with open("/home/pi/speedlog.txt","a+") as log:
	log.write(f"{now},{st.download()},{st.upload()}\n")

