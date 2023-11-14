# 5.4 BeautifulSoup

# from requests import get
# from bs4 import BeautifulSoup

# base_url = "http://weworkremotely.com/remote-jobs/serch?term="
# search_term = "python"
#
# response = get(f"{base_url}{search_term}")
# if response.status_code != 200:
#     print("Can't request website")
# else:
#     soup = BeautifulSoup(response.text, "html.parser")
#     job = soup.find_all('section', class_="jobs")


from requests import get
from bs4 import BeautifulSoup

base_url = "https://blog.feedback.io/?cat=120602&s="
search_term = "ux"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find_all("h4")
