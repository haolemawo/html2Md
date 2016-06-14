#coding:utf-8

from BeautifulSoup import BeautifulSoup, Tag

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b

tag.name = "blockquote"
tag['class'] = 'verybold'
tag['id'] = 1
print tag
# <blockquote class="verybold" id="1">Extremely bold</blockquote>

del tag['class']
del tag['id']
print tag
# <blockquote>Extremely bold</blockquote>