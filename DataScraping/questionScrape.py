from ctypes import sizeof
from itertools import count
from firebase_admin import firestore
from firebase_admin import credentials
import firebase_admin
from cmath import log
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())


cred = credentials.Certificate({})
firebase_admin.initialize_app(cred)
db = firestore.client()

with open('problem_urls.txt') as f:
    urls = f.readlines()
with open('problem_titles.txt', encoding="utf8") as f:
    names = f.readlines()


cnt = 0
for i in range(0, 100):
    driver.get(urls[i])
    cnt += 1
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    inputHtml = soup.find('div', {'class': "sample-test"})
    problem_text = soup.find(
        'div', {"class": "problem-statement"}).get_text('\n')
    # print(problem_text)
    inputHtml = str(inputHtml)
    # problem_text = problem_text.encode("utf-8")
    problem_text = str(problem_text)
    db.collection('questions').document(str(cnt)).set(
        {'question': problem_text, 'input-output': inputHtml, 'name': names[i], 'count': cnt})
