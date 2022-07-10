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

urls = []
titles = []
count = 1


def fun():
    driver.get("https://codeforces.com/problemset/page/"+str(count))
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    all_ques_div = soup.findAll("table", {"class": "problems"})
    all_ques_div = all_ques_div[0].findAll("tr")
    all_ques = []
    for quest in all_ques_div[1:]:
        t = quest.findAll("td")[1].find("div").find('a')
        all_ques.append(t)
    for ques in all_ques:
        urls.append("https://codeforces.com"+ques['href'])
        titles.append((" ".join(ques.text.split())))


while len(urls) < 1000:
    fun()
    count = count+1

with open("problem_urls.txt", "w+") as f:
    f.write('\n'.join(urls))

print("sleeeping")
time.sleep(10)
print("wake")

with open("problem_titles.txt", "w", encoding="utf-8") as f:
    f.write('\n'.join(titles))

