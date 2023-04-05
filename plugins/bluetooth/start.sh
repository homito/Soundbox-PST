#!/usr/bin/env bash

if [[ -n "$SOUND_DISABLE_BLUETOOTH" ]]; then
  echo "Bluetooth is disabled, exiting..."
  exit 0
fi

touch /shared/logs/bluetooth.logs
exec /usr/src/bluetooth-agent