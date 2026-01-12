#!/usr/bin/env python3
# Minimal example: create an issue and include labels on creation.
# Requires: set GITHUB_TOKEN in env, pip install requests

import os
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise SystemExit("Set GITHUB_TOKEN env var (with repo scope)")

OWNER = "ChillCrunch37"
REPO = "game-algorithms-watch"
API = f"https://api.github.com/repos/{OWNER}/{REPO}/issues"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

title = "[Discovery] example-repo — Example pathfinding demo"
body = """
Repository: https://github.com/example/example-repo

Notes:
- Appears to implement A* on grids.
- Has runnable demo and screenshots.

Suggested tags: pathfinding, python, beginner
"""

# Labels to apply on creation
labels = ["discovery", "triage-needed", "topic:pathfinding", "language:python"]

payload = {
    "title": title,
    "body": body,
    "labels": labels
}

resp = requests.post(API, json=payload, headers=headers)
if resp.status_code == 201:
    print("Issue created:", resp.json()["html_url"])
else:
    print("Failed to create issue:", resp.status_code, resp.text)
