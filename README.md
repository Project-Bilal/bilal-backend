# Bilal backend Flask app #

## To run the server ##
**Prerequisite:** 
penv is installed `sudo -H pip3 install -U pipenv`

1. Clone and navigate into the repository
2. `pipenv install` to install the the environment
3. `pipenv run python3 app.py` to run the backend

To avoid running in the shell, follow the steps below to run Project Bilal as a service.

## Run Project Bilal as a Service ##
Install the service to autostart Project Bilal on every reboot and run in the background. Update paths as needed.

1. `sudo vi /etc/systemd/system/bilal.service`

```
[Unit]
Description=Bilal Service
After=multi-user.target

[Service]
Type=idle
User=bilal
Restart=always
WorkingDirectory=/home/bilal/bilal-backend
ExecStart=/usr/local/bin/pipenv run python3 app.py

[Install]
WantedBy=multi-user.target
```

2. `sudo systemctl daemon-reload`
3. `sudo systemctl enable bilal.service`
4. `sudo systemctl start bilal.service`

## Install WiFi Connect - OPTIONAL ##

### What does it do? ###
An easy way to connect the device to a new WiFi access point using a mobile device.
Credit to: https://github.com/balena-os/wifi-connect
Upon reboot the device will establish a WiFi access point to connect to called `Project Bilal WiFi`. Connect to this access point on your mobile device and follow the prompt to enter in the desired WiFi connection. Once the connection is established `Project Bilal WiFi` will disappear.

### How do I install it? ###

1. Navigate to the home folder `cd ~`
2. Run the install script `bash <(curl -L https://github.com/balena-io/wifi-connect/raw/master/scripts/raspbian-install.sh)`
3. Copy the startup script `curl https://raw.githubusercontent.com/Project-Bilal/bilal-backend/80dea6ce33ef122e88859c7b955a2da9cb5ef5b4/bilal_backend/scripts/start-wifi-connect.sh > start-wifi-connect.sh`
4. Make the file executable `chmod +x start-wifi=connect.sh`
5. Create a startup service `sudo vi /lib/systemd/system/wifi-connect-start.service`. Update paths as needed.
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
