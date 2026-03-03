# Python Project
# Write a python program that takes a URL on the command line, fetches the page, and outputs (one per line)
# Page Title (without any HTML tags)
# Page Body (just the text, without any html tags)
# All the URLs that the page points/links to

import sys as system
import requests 
from bs4 import BeautifulSoup

def fetch_page(url):
  try:
    r=requests.get(url,timeout=10)
    if r.status_code!=200:
      print("Page Not Opened")
      system.exit(1)
    return r.text
  except:
    print("Invalid URL or Network Error")
    system.exit(1)

def get_title(soup):
  if soup.title:
    return soup.title.get_text(strip=True)
  else:
    return "Don't get Title"

def get_body(soup):
  if soup.body:
    text=soup.body.get_text(separator="\n",strip=True)
    return text
  else:
    return " "

def get_links(soup):
  link_List=[]
  tags=soup.find_all("a")

  for t in tags:
    h=t.get("href")
    if h!=None:
      link_List.append(h)
  return link_List


def main():
  if len(system.argv)<2:
    print("pass URL on commond line")
    system.exit(1)
  url=system.argv[1]
  if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
  
  html=fetch_page(url)
  soup=BeautifulSoup(html,"html.parser")

  title=get_title(soup)
  print(title)

  body=get_body(soup)
  print(body)

  links=get_links(soup)
  for l in links:
    print(l)

if __name__=="__main__":
  main()
