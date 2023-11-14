# 5.3 Initial Request

# from requests import get
#
# base_url = "http://weworkremotely.com/remote-jobs/serch?term="
# search_term = "python"
#
# response = get(f"{base_url}{search_term}")
# if response.status_code != 200:
#     print("Can't request website")
# else:
#     print(response.text)


from requests import get

base_url = "https://blog.feedback.io/?cat=120602&s="
search_term = "ux"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't request website")
else:
    print(response.text)
