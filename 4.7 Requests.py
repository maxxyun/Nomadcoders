# 4.7 Requests
# https://www.pypi.org  Python Standard Library에 포함되지 않은 package를 찾는 곳.

import requests

websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com",
)
for website in websites:
    if not website.startswith(
        "https://"
    ):  # => if website.startswith("https://")==False:
        website = f"https://{website}"
    print(website)
