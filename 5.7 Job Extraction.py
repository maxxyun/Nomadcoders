# 5.7 Job Extraction
# from requests import get
# from bs4 import BeautifulSoup
#
# base_url = "http://weworkremotely.com/remote-jobs/serch?term="
# search_term = "python"
#
# response = get(f"{base_url}{search_term}")
# if response.status_code != 200:
#     print("Can't request website")
# else:
#     soup = BeautifulSoup(response.text, "html.parser")
#     job = soup.find_all("section", class_="jobs")
#     print(len(jobs))
#     for job_section in jobs:
#         job_posts = job_section.find_all("li")
#         job_posts.pop(-1)       # 0부터 숫자를 샌다.
#         for post in job_posts:
#             print(post)
#             print("//////////////////////")  # 분리 기호

