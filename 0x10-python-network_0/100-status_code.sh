#!/bin/bash
# This script capture de status code
curl -so /dev/null $1 -w '%{http_code}'
