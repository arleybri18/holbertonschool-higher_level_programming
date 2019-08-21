#!/bin/bash
# script that send a json file
curl -d "@$2" -H "Content-Type: application/json" -X POST $1
