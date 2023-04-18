#!/usr/bin/python3

# Script to share QR with Wifi

# Required dependency: wifi_qrcode_generator > use pip install

import wifi_qrcode_generator as wifi

# Generate Wifi QR code
qrcode = wifi.generator.wifi_qrcode(ssid="Wifi Name", hidden= False, authentication_type= "WPA", password="Password")

# Save QR code as image file
qrcode.make_image().save("Wifi.png")
