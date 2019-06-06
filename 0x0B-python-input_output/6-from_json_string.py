#!/usr/bin/python3
import json


def from_json_string(my_str):
    data = json.loads(my_str)
    return data
