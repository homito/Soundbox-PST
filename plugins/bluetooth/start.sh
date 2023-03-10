#!/usr/bin/env bash

if [[ -n "$SOUND_DISABLE_BLUETOOTH" ]]; then
  echo "Bluetooth is disabled, exiting..."
  exit 0
fi

exec /usr/src/bluetooth-agent.py

exec /usr/src/metadata.py