#!/bin/bash
# Bash script that takes in a URL, sends a GET request using curl
# Usage: ./1-body.sh <URL>
curl -sLX GET "$1"
