# base-image for python on any machine using a template variable
# more info about dockerfile templates @ : https://www.balena.io/docs/learn/develop/dockerfile/
FROM balenalib/%%BALENA_MACHINE_NAME%%-python:3-strech-run

# use 'install_packages' for dependencies
# exemple if you need to install git
# RUN install_packages git


# Set our working directory
WORKDIR /usr/src/app

# Copy requirements.txt first for better ache on later pushes (idk if it's necessary lol)
COPY requirements.txt requirements.txt

# pip install python deps from requirements.txt on the resin.io build server (whatever that means, seems important tho)
RUN pip install -r requirements.txt

# This will copy all files in our root to the working directory in the container
COPY . ./

# Enable udevd so that plugged dynamic hardware devices show up in our container.
ENV UDEV=1

# main.py will run when container starts up on the device
CMD ["python","-u","src/main.py"]





# Important sources : 
# https://github.com/chrisys/train-departure-display
# https://github.com/balena-io-examples/balena-python-hello-world
# https://github.com/balena-labs-projects/balena-sound
# https://github.com/homito/Soundbox-PST