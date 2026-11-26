#!/bin/bash
# Displays only the status code of a response from a URL
curl -s -o /dev/null -w "%{http_code}\n" "$1"
