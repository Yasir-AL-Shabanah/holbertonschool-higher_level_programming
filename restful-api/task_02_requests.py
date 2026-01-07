#!/usr/bin/python3
import csv
import requests


URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    r = requests.get(URL, timeout=10)
    print("Status Code: {}".format(r.status_code))
    if r.status_code != 200:
        return
    data = r.json()
    for post in data:
        title = post.get("title", "")
        print("{}".format(title))


def fetch_and_save_posts():
    r = requests.get(URL, timeout=10)
    if r.status_code != 200:
        return
    data = r.json()
    rows = []
    for post in data:
        rows.append({
            "id": post.get("id"),
            "title": post.get("title", ""),
            "body": post.get("body", "")
        })

    with open("posts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(rows)
