from facebook_scraper import get_posts
import time


def scrape():
    for post in get_posts('whitehouseinternationalcollege'):
        time.sleep(30)
        return post
        break
