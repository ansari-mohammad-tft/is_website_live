import requests
def is_website_live(web):
    response = requests.get(web)
    if response.status_code == 200:
        return True
    else:
        return False

def send_mail(message):
    # will do it latter after taking approval
    pass