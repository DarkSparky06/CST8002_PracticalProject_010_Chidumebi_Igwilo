"""
stats_api.py
Author: Igwilo Chidumebi
Course: CST8002 010
Description: Calls external API to compute average value.
"""

import requests

def get_average(values):
    """Use external API to compute average."""
    resp = requests.post('https://api.mathjs.org/v4/', json={'expr': values})
    return resp.json()['result']
