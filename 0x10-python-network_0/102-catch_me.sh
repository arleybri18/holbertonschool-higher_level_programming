#!/bin/bash
# script that return respond of server
curl -sLX PUT '' -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me -d "user_id=98"
