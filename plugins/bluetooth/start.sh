#!/usr/bin/env bash

if [[ -n "$SOUND_DISABLE_BLUETOOTH" ]]; then
  echo "Bluetooth is disabled, exiting..."
  exit 0
fi

sh /usr/src/restartpair.sh
exec /usr/src/bluetooth-agent