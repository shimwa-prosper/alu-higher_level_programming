#!/bin/bash
# Displays the body of a 200 status code response from a URL
curl -sL -w "\n%{http_code}" "$1" | awk 'BEGIN{RS="";FS="\n"} $NF=="200"{$NF=""; sub(/\n$/,""); print}'
