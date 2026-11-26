#!/bin/bash
# Sends a GET request with X-HolbertonSchool-User-Id: 98 header and displays the body
curl -sL -H "X-HolbertonSchool-User-Id: 98" "$1"
