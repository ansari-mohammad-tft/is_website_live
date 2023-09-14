from constants import backend_url,frontend_url
from utilities import is_website_live,send_mail

if not is_website_live(backend_url):
    send_mail("backend is down")
if not is_website_live(frontend_url):
    send_mail("backend is down")



