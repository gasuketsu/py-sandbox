#!/usr/bin/env bash

if type pycodestyle > /dev/null 2>&1; then
  pycodestyle .
else
  echo "no pycodestyle found." >&2
  exit 2
fi
