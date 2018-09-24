#request package
#BeautifulSoup - cannot make the request on to webpage
import requests
import bs4
# import lxml

res = requests.get('https://www.dataquest.io/blog/web-scraping-tutorial-python/')
print(type(res))
# print(res.text)

#here comes beautifulsoup in the picture
soup = bs4.BeautifulSoup(res.text,'lxml')
print(type(soup))
soup_title = soup.select('title')
print(soup_title[0].getText())


