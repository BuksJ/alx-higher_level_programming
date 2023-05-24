#!/usr/bin/python3
"""
This module takes in GitHub credentials (username and personal access token)
and uses the GitHub API to display the user's id.
"""

import requests
import sys


def get_user_id(username, token):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, auth=(username, token))
    if __name__ == "__main__":
        if len(sys.argv) != 3:
            print("Usage: ./github_id.py <username> <token>")
            sys.exit(1)
