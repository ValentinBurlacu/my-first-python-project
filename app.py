from jnpr.junos import Device
from pprint import pprint
import requests
import json

def write_to_file(device, payload):
    filename = f"./output/{device}"
    file1 = open(filename, "a")
    file1.write(str(payload) + '\n')
    file1.close()
    pass

devices = [
    'branch0-fw0.dmz.home',
    'branch0-fw1.dmz.home',
    'branch1-fw0.dmz.home'
]

list_of_devices = []

for device in devices:
    with Device(host=device, user='automation', password='juniper123') as dev:
        try:
            show_version = dev.rpc.get_software_information({'format': 'json'})
            payload = {'dns_hostname': device, 'device_hostname': show_version['software-information'][0]['host-name'][0]['data']}
            list_of_devices.append(payload)
            write_to_file(device, payload)
        except:
            pass