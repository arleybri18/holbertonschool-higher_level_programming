#!/bin/bash
# send parameters with POST method
curl -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -sX POST $1
