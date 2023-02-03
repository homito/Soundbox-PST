
FROM balenalib/raspberry-pi-python:3.7.9-buster

# This will copy all files in our root to the working directory in the container
COPY . ./app

# Set our working directory
WORKDIR /app

# Enable udevd so that plugged dynamic hardware devices show up in our container. (???)
ENV UDEV=1

# main.py will run when container starts up on the device
CMD [ "python", "src/main.py" ]



# Important sources : 
# https://github.com/chrisys/train-departure-display
# https://github.com/balena-io-examples/balena-python-hello-world
# https://github.com/balena-labs-projects/balena-sound
# https://github.com/homito/Soundbox-PST
# Chat-gpt coming in clutch, dayum.

# more info about dockerfile templates @ : https://www.balena.io/docs/learn/develop/dockerfile/