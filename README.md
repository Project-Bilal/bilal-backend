# Bilal backend Flask app #

## To run the server: ##

1. `sudo -H pip3 install -U pipenv` pipenv needs to be installed
2. `pipenv install` to setup the environment and install pacakges
3. `pipenv run python3 app.py` start the server

## To install new packages: ##

1. `pipenv shell`
2. `pipenv install xxxx`

## Install WiFi Connect - OPTIONAL ##
An easy way to connect the device to a new WiFi access point using a mobile device.
Credit to: https://github.com/balena-os/wifi-connect
Upon reboot the device will establish a WiFi access to point to connect to called `Project Bilal WiFi`. Connect to this access point on your mobile device and follow the prompt to enter in the desired WiFi connection. Once the connection is established `Project Bilal WiFi` will disappear.

1. Run the install script `bash <(curl -L https://github.com/balena-io/wifi-connect/raw/master/scripts/raspbian-install.sh)`
2. Navigate to the location where the you want the startup script to execute from, preferably the user's home.
3. Copy the startup script curl `https://raw.githubusercontent.com/Project-Bilal/bilal-backend/80dea6ce33ef122e88859c7b955a2da9cb5ef5b4/bilal_backend/scripts/start-wifi-connect.sh > start-wifi-connect.sh`
4. Create a startup service `sudo vi /lib/systemd/system/wifi-connect-start.service`. Make sure to modify the start path accordingly.
```
[Unit]
Description=Balena wifi connect service
After=NetworkManager.service

[Service]
Type=simple
ExecStart=/home/bilal/start-wifi-connect.sh
Restart=on-failure
StandardOutput=syslog
SyslogIdentifier=wifi-connect
Type=idle
User=root

[Install]
WantedBy=multi-user.target
```
5. Enable the service `sudo systemctl enable wifi-connect-start.service`
6. Reboot `sudo reboot`
OPTIONAL: edit the SVG file in `/usr/local/share/wifi-connect/ui/static/media` for branding
