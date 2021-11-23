# Import Required Module
import requests
from bs4 import BeautifulSoup

# Web URL
Web_url = "https://boards.4chan.org/gif/thread/21270506#p21271714"

# Get URL Content
r = requests.get(Web_url)
# Parse HTML Code
soup = BeautifulSoup(r.content, 'html.parser')

# List of all video tag
video_tags = soup.findAll('div')
print("Total ", len(video_tags), "videos found")

def name(name):
	x = str((name.split('/')[-1]))
	return x

if len(video_tags) != 0:
	for video_tag in video_tags:
		if ".webm" in str(video_tag):
			video_url = video_tag.find("a")['href']
			if ".webm" in str(video_url):
				link = ("https:" + video_url)
				print("link")
				r = requests.get(link, stream = True) 
				
				with open(name(link), 'wb') as f: 
					for chunk in r.iter_content(chunk_size = 1024*1024): 
						if chunk: 
							f.write(chunk) 
else:
	print("no videos found")
