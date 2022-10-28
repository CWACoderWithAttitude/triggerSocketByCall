# Fritzbox Call Agent
Detect incoming calls and do something.    
Like switchng on lights, send notifications...

## Setup
```python
python3 -m venv ven
source ./venv/bin/activate
pip install -r requirements.txt
```


## Something
As a result of an incoming call we want to do something like switching on a lamp.   


* [A library for 433MHz remote control](https://github.com/peterhinch/micropython_remote)
* [micropython-rfsocket](https://github.com/wuub/micropython-rfsocket)
* [Transmitting and Receiving messages through RF433 using Raspberry Pico](https://raspberrypi.stackexchange.com/questions/132771/transmitting-and-receiving-messages-through-rf433-using-raspberry-pico)


### Identify your Chip
```shell
❯ esptool.py --port /dev/tty.usbserial-140 flash_id
esptool.py v2.8
Serial port /dev/tty.usbserial-140
Connecting....
Detecting chip type... ESP8266
Chip is ESP8266EX
Features: WiFi
Crystal is 26MHz
MAC: a0:20:a6:17:52:a5
Uploading stub...
Running stub...
Stub running...
Manufacturer: e0
Device: 4016
Detected flash size: 4MB
Hard resetting via RTS pin...
```

The `Detected flash size: 4MB` indicates we can use the latest regular [MicroPython image](https://micropython.org/resources/firmware/esp8266-20220618-v1.19.1.bin).   

1. Erase flash memory
```shell
❯ esptool.py --port /dev/tty.usbserial-140 erase_flash
esptool.py v2.8
Serial port /dev/tty.usbserial-140
Connecting....
Detecting chip type... ESP8266
Chip is ESP8266EX
Features: WiFi
Crystal is 26MHz
MAC: a0:20:a6:17:52:a5
Uploading stub...
Running stub...
Stub running...
Erasing flash (this may take a while)...
Chip erase completed successfully in 11.2s
Hard resetting via RTS pin...
```

2. Deploy MicroPython
```shell
❯ esptool.py --port /dev/tty.usbserial-140 --baud 460800 write_flash --flash_size=detect 0 ~/Downloads/esp8266-20220618-v1.19.1.bin
esptool.py v2.8
Serial port /dev/tty.usbserial-140
Connecting....
Detecting chip type... ESP8266
Chip is ESP8266EX
Features: WiFi
Crystal is 26MHz
MAC: a0:20:a6:17:52:a5
Uploading stub...
Running stub...
Stub running...
Changing baud rate to 460800
Changed.
Configuring flash size...
Auto-detected Flash size: 4MB
Flash params set to 0x0040
Compressed 634844 bytes to 419808...
Wrote 634844 bytes (419808 compressed) at 0x00000000 in 10.5 seconds (effective 485.9 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
```
3. Enable WebRepl

4. Setup WiFi
Fort now i'd refer you to [the excellent documentation here](http://docs.micropython.org/en/latest/esp8266/quickref.html#networking)

5. Accessing MicropPython
Once the Board joined your network it's time to [use the webrepl](git@github.com:micropython/webrepl.git).   
WebRepl is an interactive client to connect to your Board
