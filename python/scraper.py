from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as url
import html5lib

yt = 'https://www.youtube.com/channel/UCLlTANFO1ZsgrT7q0lM_6uA?view_as=subscriber'

page = url(yt)
html = page.read()

pageSoup = bs(html, 'html.parser')
channelName = pageSoup.findAll('yt-formatted-string', {'class':'style-scope ytd-channel-name'})

print(channelName)