#!/bin/bash
# Use curl to fetch the content and measure its size in bytes
curl -Is "$1" | grep Content-Length | cut -d: -f2
