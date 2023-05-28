![logo](https://raw.githubusercontent.com/homito/Soundbox-PST/main/docs/images/affiche.png)

**Le projet SoundBox vise à créer une enceinte bluetooth connectée équipée de deux haut-parleurs permettant de diffuser de la musique depuis un smartphone ou un ordinateur via une connexion bluetooth. Ce projet couvre de nombreux sujets importants de notre programme (de la physique à travers l'étude des ondes sonores, l'électronique avec le câblage des appareils et de la programmation avec l’affichage écran et les communications Bluetooth).**


## Highlights

- **source audio**: diffusion de musique depuis les services suivant : Bluetooth, Airplay2, Spotify Connect.
- **Multi-room synchronous playing**: Joue de la musique synchronisée sur plusieurs appareils en meme temps.
- **Affichage d'interface graphique**: Affiche les musiques jouées, durée de la musique et bien d'autres fonctions sur un écran.
- **Gestion du son intégré à la carte**: Possibilité de gérer le son via des boutons sur la carte Raspberry.

## Setup et configuration

Le projet tournant sous balenaOS, il faut déployer l'application avec balena Cloud via le lien ci-dessous:

[![deploy button](https://balena.io/deploy.svg)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/balena-labs-projects/balena-sound&defaultDeviceType=raspberry-pi)

![concept](https://raw.githubusercontent.com/homito/Soundbox-PST/main/docs/images/cablage.png)

## Known issues

- **charactères spéciaux**: Les charactères spéciaux sont remplacés par des '?' sur l'affichage de l'écran.
- **Wi-fi**: La soundbox ne peut pour l'instant pas se connecter à un réseau wi-fi, elle utilisera donc uniquema la connectivité bluetooth. 
- **PIN ou clé de sécurtié incorrecte**: Ce problème intervient lorsqu'on discocie un la soundbox depuis un appareil qui était déjà connecté, dans cette situation, appuyer sur le bouton prévu pour, attendre 5 à 10 secondes et re-connectez vous à la Soundbox.


## To-do list

- **Wi-fi**: Pouvoir connecter la soundbox en wi-fi pour utiliser spotify et autres services.
- **Spotify**: Pas de connectivité spotify car pas de gestion wi-fi pour l'instant
- **Airplay**: pas de connectivité airplay pour l'instant mais les appareils apple peuvent evidemment utiliser la bluetooth.
