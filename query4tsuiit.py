import bs4, re
import urllib.parse as urlencode
import datetime
import scraper

class Query4Tsuiit(scraper.Scraper):
	def __init__(self, query, mode):
		if query[0] == "#":
			self.url = self.queryHash(query)
		else:
			self.url = self.querySearch(query)

		super().__init__(self.url)

		if mode == "static":
			self.source = self.staticUrlParser()
		elif mode == "dynamic":
			self.source = self.dynamicUrlParserByTarget("timeline")
		else:
			self.source = "Please select your mode!"

		self.getTimelineIDs()
		self.getSearchTimeline()

	def querySearch(self, query):
		url = "https://twitter.com/search?vertical=default&q="
		url += urlencode.quote(query + " min_faves:5")
		url += "&src=typd&lang=ja"

		return url

	def getTimelineIDs(self):
		soupnized = bs4.BeautifulSoup(self.source,"html.parser")
		timeline = soupnized.select('li')
		useridRegex = re.compile(r'@<b>([a-zA-Z0-9_]+)<\/b>')
		userids = set()
		for tl in soupnized:		
			timeline_source = str(tl)
			matches = useridRegex.findall(timeline_source)
			for m in matches:
				user_id = m.replace(r'@<b>','').replace(r'<\/b>','')
				userids.add(self.cleaner(m))
		self.timeline_IDs = list(userids)

	def getSearchTimeline(self):
		soupnized = bs4.BeautifulSoup(self.source,"html.parser")

		timeline_tweets = soupnized.select('div[id="timeline"] ol > li')
		timelines = []
		for t in timeline_tweets[1:]:
			tl = {}

			twi_div = t.select('div')[0]

			
			try:
				user_id = twi_div.select("b")[0].getText()
			except:
				continue

			user_name = self.cleaner(twi_div["data-name"])
			twi_time = twi_div.select('small[class="time"]')[0]
			twi_rel_url = twi_div["data-permalink-path"]
			twi_abs_url = "https://twitter.com" + twi_rel_url

			digitRegex = re.compile(r'\d+')

			tl_rt_div = twi_div.select('div[class="stream-item-footer"] > div > div')[1]
			tl_fav_div = twi_div.select('div[class="stream-item-footer"] > div > div')[2]

			text_body = self.cleaner(twi_div.select('p')[0].getText())

			mo_rt = digitRegex.search(tl_rt_div.getText().replace(',', ''))
			mo_fav = digitRegex.search(tl_fav_div.getText().replace(',', ''))

			if mo_rt:
				tl_rt_div = mo_rt.group()
			else:
				tl_rt_div = "0"
			if mo_fav:
				tl_fav_div = mo_fav.group()
			else:
				tl_fav_div = "0"

			tl["user_id"] = user_id
			tl["user_name"] = user_name
			tl["twi_abs_url"] = twi_abs_url

			tl["tl_rt_div"] = int(tl_rt_div)
			tl["tl_fav_div"] = int(tl_fav_div)

			tl["text_body"] = text_body
			timelines.append(tl)

		self.timelines = timelines

	def queryHash(self, query):
		url = "https://twitter.com/hashtag/"
		url += urlencode.quote(query)
		url += "?lang=ja"
		return url

	def cleaner(self, sentence):
		cleaned = ""
		for s in sentence:
			try:
				tmp = open('tmp.txt','w')
				tmp.write(s)
				cleaned += s
			except:
				continue
		return cleaned

"""
twi = Query4Tsuiit("#花火", "dynamic")
print(twi.timeline_IDs)
"""
