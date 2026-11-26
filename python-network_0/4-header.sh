#!/bin/bash
# Sends a GET request with X-HolbertonSchool-User-Id: 98 header and displays the response body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
