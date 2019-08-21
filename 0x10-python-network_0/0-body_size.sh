#!/usr/bin/env bash
curl -so /dev/null $1 -w '%{size_download}\n'
