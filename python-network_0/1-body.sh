#!/bin/bash
# Displays the body of a 200 status code response from a URL
if [ "$(curl -s -L -o /tmp/curl_body -w "%{http_code}" "$1")" -eq 200 ]; then
    cat /tmp/curl_body
fi
