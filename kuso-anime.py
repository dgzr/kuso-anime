#!/usr/bin/python
"""
kusonime.com scrapper, anime batch.
update 2021.03.04 © dtz-aditia
contact : https://t.me/aditia_dtz
"""
import bs4
import time
import logging
import requests
import itertools
import threading
import subprocess
import urllib.parse

clear = (lambda : subprocess.call(["clear"]))

class BaseClass(object):
	"""
	Page extractor/ scrapper.
	"""
	def __init__(self):
		self.re = bs4.re
		self.host = "https://kusonime.com"
		self.session = requests.Session()
		self.session.headers.update({
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 OPR/67.0.3575.137"})

	def parse(self, raw):
		raw = raw.text if hasattr(raw,"text") else raw
		return bs4.BeautifulSoup(raw,"html.parser")

	def getpath(self, url):
		return urllib.parse.urlparse(url).path.strip("/")

	def search(self, url):
		try:
			page = self.session.get(url)
			soup = self.parse(page)
			d = {}

			d.update({
				"q":[{
					"title":item.h2.text,
					"id":self.getpath(item.a.attrs["href"])
					} for item in soup.findAll("div",class_="content")]
				})

			if(recomended := soup.find(class_="recomx")):
				d.update({
					"r":[{
						"title":item.h2.text,
						"id":self.getpath(item.a.attrs["href"])
						} for item in recomended.findAll(class_="zeeb")]
					})

			if(next := soup.find(class_="nextpostslink")):
				d.update(
					{"next":next.attrs.get("href")})
			if(prev := soup.find(class_="previouspostslink")):
				d.update(
					{"prev":prev.attrs.get("href")})
			if(nav := soup.find(class_="navigation")):
				for p in nav.findAll("a"):
					if "next" in p.text.lower():
						d.update(
							{"next":p.attrs.get('href')})
					elif "prev" in p.text.lower():
						d.update(
							{"prev":p.attrs.get('href')})	
			return d
		except:
			return False

	def extract(self, id):
		try:
			page = self.session.get(f"{self.host}/{id}")
			soup = self.parse(page)
			d = {}
			for n, smokeddl in enumerate(soup.findAll("div", class_="smokeddl")[:-1], start=1):
				title = smokeddl.find(class_="smokettl").text
				d[title] = {}
				for smokeurl in smokeddl.findAll(class_="smokeurl"):
					res = smokeurl.strong.text
					links = {}
					for a in smokeurl.findAll("a"):
						links[a.text] = a.attrs["href"]
					d[title][res] = links
			return d
		except:
			return False

	def prompt(self, **kwargs):
		if kwargs.get('chs'):
			chs = kwargs.get('chs')
		for k,v in enumerate(chs, start=1):
			print(f" {k}. {v}")
		if kwargs.get('t') is True:
			print(" 99. Next\n 00. Prev")
		cek = int(input("\n + Set -> "))
		try:
			if cek != '' and (cek-1) < len(chs):
				return cek
			elif cek == 99:
				return cek
			elif cek == 88:
				return cek
			else:
				return AssertionError(" Invalid input!")
		except:
			return False

	def wait(self):
		global stop
		stop = []
		for c in itertools.cycle(["○","●○","●●○","●●●○"]):
			if bool(stop) is True:
				break
			print(f" + Wait a few seconds {c}\r",end="")
			time.sleep(0.1)
#		print("\x1b[3A\x1b[K")

class Main(BaseClass):
	"""
	kusonime.com main menu
	"""
	banner = """
 ╦╔═┬ ┬┌─┐┌─┐┌┐┌┬┌┬┐╔═╗
 ╠╩╗│ │└─┐│ ││││││││║╣ 
 ╩ ╩└─┘└─┘└─┘┘└┘┴┴ ┴╚═╝.com

 ~ dtz-aditia © 2021
 ~ Search And download anime batch.
	"""
	urls = None
	loads = (lambda x: threading.Thread(target=BaseClass().wait).start())
	def __main__(self):
		clear()
		print(self.banner)
		query = None
		if(cek := self.prompt(chs=["Home","Search anime","Rekomendasi anime","Contact"],t=False)):
			if cek in (1,3):
				self.urls = self.host
			elif cek == 2:
				query = input(' + query : ')
				if query != '':
					self.urls = f"{self.host}/?s={query}"
				else:
					logging.warning(" + please input a query to search!")
					exit(1)
			elif cek == 4:
				subprocess.call(["xdg-open","https://t.me/aditia_dtz"])
				exit(1)
			self.loads()
			if(result := self.search(self.urls)):
				prog = None
				stop.insert(0,True)
				if cek in (1,2):
					prog = {"x":result["q"],"t":True}
					if cek == 1:
						prog.update(
							{"msg":" This, result from home!\n"})
					elif cek == 2:
						prog.update(
							{"msg":f" This, result from query -> {query}\n"})
				elif cek == 3:
					prog = {"x":result["r"],"t":False,"msg":" This, recomendations anime list for you!\n"}
				cache = [i["title"] for i in prog["x"]]
				while not (False):
					clear()
					print(self.banner)
					print(prog.get("msg"))
					if(cs := self.prompt(chs=cache,t=prog.get("t"))):
						if cs not in (88,99):
							self.loads()
							if(ext := self.extract(prog["x"][cs-1]["id"])):
								stop.insert(0,True)
								key = list(ext.keys())
								if(rv := self.prompt(chs=key,t=False)):
									keys = list(ext[key[rv-1]].keys())
									if(rs := self.prompt(chs=keys,t=False)):
										keyn = list(ext[key[rv-1]][keys[rs-1]].keys())
										if(pil := self.prompt(chs=keyn,t=False)):
											kyy = ext[key[rv-1]][keys[rs-1]][keyn[pil-1]]
											subprocess.call(["termux-clipboard-set",kyy])
											logging.warning(
												f" {kyy}\n + Copied to clipboard!")
											input(" + Enter to main home!")
											Main().__main__()
										else:
											pass
									else:
										pass
								else:
									pass
							else:
								pass
						else:
							inurl = None
							if cs == 99:
								if(result.get("next")):
									inurl = result.get("next")
								else:
									logging.warning(" Cannot Next last pages!")
									break
							elif cs == 88:
								if(result.get("prev")):
									inurl = result.get("prev")
								else:
									logging.warning(" Cannot Prev First Pages!")
									break
							self.loads()
							if(npage := self.search(inurl)):
								stop.insert(0,True)
								result = npage
								cache = [i["title"] for i in npage["q"]]
							else:
								break
					else:
						pass
			else:
				stop.insert(0,True)
				logging.warning(f" - No result found for -> {query}")
				exit(1)
		else:
			pass

if __name__=="__main__":
	try:
		Main().__main__()
	except (ValueError): #,requests.exceptions.ConnectionError):
		exit()
