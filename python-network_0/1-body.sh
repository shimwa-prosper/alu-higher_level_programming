#!/bin/bash
# Displays the body of a 200 status code response from a URL
[ "$(curl -sL -o /tmp/b -w "%{http_code}" "$1")" = "200" ] && cat /tmp/b && rm -f /tmp/b || rm -f /tmp/b
