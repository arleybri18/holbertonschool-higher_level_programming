#!/bin/bash
# script that filter the Header methods accept by server
curl -sI $1 | grep Allow | cut -d":" -f2 | sed 's/ //'
