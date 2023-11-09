# 4.8 Status Codes
# https://developer.mozilla.org/ko/docs/Web/HTTP/Status     http의 상태 코드
# HTTP Status 코드 정리글입니다.
# https://www.whatap.io/ko/blog/40
#
# 1XX : Information responses
# 2XX : Successful responses
# 3XX : Redirection messages
# 4XX : Client error responses
# 5XX : Server error reponses

from requests import get

websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com",
)

results = {}

for website in websites:
    if not website.startswith(
        "https://"
    ):  # => if website.startswith("https://")==False:
        website = f"https://{website}"
    response = get(website)
    if response.status_code == 200:
        results[website] = "OK"
    else:
        results[website] = "FAILED"
print(results)
