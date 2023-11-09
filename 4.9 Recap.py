# 4.9 Recap
from requests import get

websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com",
)

results = {}

for (
    website
) in (
    websites
):  # 현재 실행중인 item에 접근하는 방법으로 variable(website)을 만든다. 한번에 모두 가져오는게 아닌 한개씩 가져온다.
    if not website.startswith(
        "https://"
    ):  # => if website.startswith("https://")==False:
        website = f"https://{website}"  # f를 사용해 번수를 안에 넣을 수 있음
    response = get(website)
    if response.status_code >= 500:
        results[website] = "서버에러응답"
    elif response.status_code >= 400:
        results[website] = "클라이언트 에러 응답"
    elif response.status_code >= 300:
        results[website] = "리다이렉션 메시지"
    elif response.status_code >= 200:
        results[website] = "성공응답"
    elif response.status_code >= 100:
        results[website] = "정보응답"
    else:
        results[website] = "FAILED"
print(results)
