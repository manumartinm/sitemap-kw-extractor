from bs4 import BeautifulSoup
import requests
import streamlit as st
import re

stop_words = ['wp-content', 'media', 'static', 'public']

def get_all_urls(url):
    res = requests.get(url)
    xml = res.text
    soup = BeautifulSoup(xml, 'xml')
    loc_tags = soup.find_all("loc")
    urls = []
    for url in loc_tags:
        if not any(value in url.text for value in stop_words):
            urls.append(url.text)
    return urls

def extract_keywords(urls, position):
    kws = []
    for url in urls:
        url = url.split('//')
        url = url[1].split('/')
        kw = url[position]
        kw = re.sub('\/', '', kw)
        kw = re.sub('-', ' ', kw)
        kws.append(kw)
    return kws

