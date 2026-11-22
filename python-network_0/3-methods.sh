#!/bin/bash
# Displays all the HTTP methods the server of a URL will accept
curl -si -X OPTIONS "$1" | grep -i '^Allow:' | cut -d ' ' -f 2- | tr -d '\r'
