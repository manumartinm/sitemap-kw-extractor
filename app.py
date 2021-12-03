from utils import get_all_urls, extract_keywords
import streamlit as st

st.title('Extract Kws from sitemap')

with st.form(key="url_list"):
    position = st.number_input(label="Posicion", min_value=0)
    urls = st.text_area(label='Introduzca las urls....', height=200)
    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    urls_list = urls.split()
    kws = []
    for url in urls_list:
        sitemap_urls = get_all_urls(url)
        kws += extract_keywords(sitemap_urls, position)
    
    kws = list(set(kws))
    kws_textarea = st.text_area(label='Kws extraidas....', height=200, value="\n".join(kws))
