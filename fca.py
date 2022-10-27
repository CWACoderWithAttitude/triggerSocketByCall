from fritzconnection.lib.fritzcall import FritzCall
pwd='proben8453'
fc = FritzCall(address='192.168.178.1', password=pwd)
calls = fc.get_missed_calls()
for call in calls:
    print(call)
