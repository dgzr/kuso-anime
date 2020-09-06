#!/data/data/com.termux/files/usr/bin/python
# Update : (2020-09-03 16:06:52)
# Finish : Now!
# © Copyright 2020 Ezz-Kun (Kyun-Kyunnn)

from bs4 import BeautifulSoup as bs_
from os import system as _Auth
from time import sleep
from string import ascii_letters as _ascii
from random import randint
import sys,re
import requests as req_

b = '\033[1;34m'
h = '\033[1;32m'
p = '\033[1;37m'
m = '\033[1;31m'

class _print(object):
	def __init__(self,string):
		for i in string +'\n':
			sys.stdout.write(str(i))
			sys.stdout.flush()
			sleep(0.00050)

__banner__ = (f"""
 {b}╦╔═{p}┬ ┬┌─┐{b}╔═╗{p}┌┐┌┬┌┬┐{b}╔═╗  ╦ ╦{p}┬─┐{b}╦ 
 ╠╩╗{p}│ │└─┐{b}║ ║{p}│││││││{b}║╣{p}───{b}║ ║{p}├┬┘{b}║ 
 ╩ ╩{p}└─┘└─┘{b}╚═╝{p}┘└┘┴┴ ┴{b}╚═╝  ╚═╝{p}┴└─{b}╩═╝
 {b}┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈{p} ≽
 {b}[{h}▪{b}]{p} Author {b}:{p} Ezz-Kun {h}(๑˃̵ᴗ˂̵)و
 {b}[{h}▪{b}]{p} Tools  {b}:{p} Kusonime.com {m}~{p} url
 {b}[{h}▪{b}]{p} Versi  {b}:{p} {randint(10,999)}.{randint(10,999)} Fix Error{m}!

 {m}→ {b}[{p} KusoNime {b}]{m} ←{p}
""")

class _KusoNime(object):
	def __init__(self,url):
		if 'https://' not in url:
			self.url = f"https://kusonime.com/?s={url.replace(' ','+')}&post_type=post"
		else:
			self.url = url
		self.next = []
		self.prev = []
		self.judul = []
		self._href = []
		self.title = []
		self.reso = []
		self.server = []
		self.links = []
		self.headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/191.0.0.35.96;]"}
		self._ShowAnimeTitle(self.url)
	def _ShowAnimeTitle(self,url_):
		try:
			_shogi = req_.get(url_,headers=self.headers).text
			_bes = bs_(_shogi,'html.parser')
			_jdl = _bes.find('title').text
			page_ = _bes.find('div',class_='navigation').find_all('a')
			tenzo_ = _bes.findAll('h2',class_='episodeye')
			if len(tenzo_) != 0:
				for seki_ in tenzo_:
					self.judul.append(seki_.text)
					self._href.append(seki_.find('a')["href"])
				if len(page_) != 0:
					for page in page_:
						if 'Previous Page' in page.text:
							self.prev.append(page["href"])
						elif 'Next Page' in page.text:
							self.next.append(page["href"])
						else:
							pass
				_Auth('clear')
				_print(__banner__)
				for _ces, ces in enumerate(self.judul):
					_print(f' {b}[{p}{_ces+1}{b}].{p}{ces}')
				if len(self.next) != 0:
					_print(f"""		       {b}[{h}» {p}{_jdl.split('|')[1].strip()} {h}«{b}]{p}
	     {b}[{p} Type {b}[{p}N{b}]{p} For Next Type {b}[{p}P{b}]{p} For Prev {b}]{p}""")
				_cos = input(f'\n {b}[{h}»{p}Kuso{h}«{b}]{p} Choice {b}≽ {p}')
				if _cos == '':
					exit(f' {b}[{m}»{p}Eror{m}«{b}]{p} Choice Is None!')
				elif str(_cos) in _ascii:
					if str(_cos).lower() == 'n':
						_KusoNime(self.next[0])
					elif str(_cos).lower() == 'p':
						if len(self.prev) != 0:
							_Kusonime(self.prev[0])
						else:
							exit(f' {b}[{m}»{p}Eror{m}«{b}]{p} Can Not Previous First Page!')
				elif str(_cos) not in _ascii:
					if (int(_cos)-1) < len(self._href):
#					self._downloadPage(open('toaru.html').read())
						self._downloadPage(self._href[int(_cos)-1])
					else:
						exit(f' {b}[{m}»{p}Eror{m}«{b}]{p} Choice Out Of Range!')
				else:
					exit(f' {b}[{m}»{p}Eror{m}«{b}]{p} Invalid Choice!')
			else:
				exit(' {b}[{m}»{p}Eror{m}«{b}]{p} Title ``{url}`` Not Found In Kusonime{m}!{p}')
		except req_.exceptions.ConnectionError:
			exit(f' {b}[{m}»{p}Kuso{m}«{b}]{p} No Internet Connection{m}!')
		except (EOFError,KeyboardInterrupt):
			exit(f' {b}[{m}»{p}Eror{m}«{b}]{p} Passing!')
	def _downloadPage(self,_url):
		try:
			_shogi = req_.get(_url,headers=self.headers).text
			_Auth('clear')
			_print(__banner__)
			_bes = bs_(_shogi,'html.parser')
			fans_ = _bes.find('div',class_='info')
			_kintel = _bes.find('h1',class_='jdlz').text
			_publis = _bes.find('div',class_='kategoz').find('i').nextSibling
			view_ = _bes.find('span',class_='viewoy').text.strip()
			sinon_ = _bes.find('strong').get_text() + ':' + bs_(re.search('</strong>(.*?)<strong>',_bes.decode()).group(1),'html.parser').get_text()
			info_ = '\n'.join(list(f" {b}[{h}▪{b}]{p} "+ str(__.text) for __ in _bes.find('div',class_='info').findAll('p')))
			_print(f""" {b}[{h}▪{b}]{p} Title : {_kintel}
 {b}[{h}▪{b}]{p} Upload : {_publis}
 {b}[{h}▪{b}]{p} Viewers : {view_}""")
			_print(info_)
			_print(f' {sinon_}')
			input(f' {b}[{h}▪{b}]{p} Enter To Continue{m}!')
			list(self.title.append(_.text) for _ in _bes.findAll('div',class_='smokettl'))
			_data = _bes.findAll('div',class_='smokeddl')
			_Auth('clear')
			_print(__banner__)
			for ara, _ara in enumerate(self.title):
				_print(f' {b}[{p}{ara+1}{b}].{p}{_ara}')
			_ttl = int(input(f'\n {b}[{h}»{p}Kuso{h}«{b}]{p} Choice {b}≽ {p}'))
			print(f'\n ~ {b}[{p} Set Resolution{m}!{b} ]\n')
			list(self.reso.append(x.text) for x in _data[_ttl-1].findAll('strong'))
			for res, res_ in enumerate(self.reso):
				_print(f' {b}[{p}{res+1}{b}].{p}{res_}')
			_doit = _data[_ttl-1].findAll('div',class_='smokeurl')
			fus_ = int(input(f'\n {b}[{h}»{p}Kuso{h}«{b}]{p} Resolusi {b}≽ {p}'))
			print(f'\n ~ {b}[{p} Set Server{m}!{b} ]\n')
			for cek_ in _doit[fus_-1].findAll('a'):
				self.server.append(cek_.text)
				self.links.append(cek_["href"])
			for ui, ui_ in enumerate(self.server):
				_print(f' {b}[{p}{ui+1}{b}].{p}{ui_} {b}≽ {p}{self.links[ui]}')
			_ops = int(input(f'\n {b}[{h}»{p}Kuso{h}«{b}]{p} Open To Browser {b}≽ {p}'))
			if (_ops-1) < len(self.links):
#				print(self.links[_ops-1])
				_Auth(f'termux-open {self.links[_ops-1]}')
				_KusoNime(self.url)
			else:
				exit(f' {b}[{m}»{p}Eror{m}«{b}]{p} Your Choice Out Of Range!')
		except req_.exceptions.ConnectionError:
			exit(f' {b}[{m}»{p}Kuso{m}«{b}]{p} No Internet Connection{m}!')
		except (ValueError,KeyboardInterrupt,EOFError):
			exit(f' {b}[{m}»{p}Eror{m}«{b}]{p} Passing!')

def _MainKusoNime():
	_Auth('clear')
	_print(__banner__)
	_print(f""" {b}[{p}01{b}].{p}Search Anime 
 {b}[{p}02{b}].{p}More Information
 {b}[{p}03{b}].{p}Exit
""")
	try:
		_cek = int(input(f' {b}[{h}»{p}Kuso{h}«{b}]{p} Choice {b}≽ {p}'))
		if _cek == '':
			exit(f' {b}[{m}»{p}Eror{m}«{b}]{p} Choice Is Nothing !')
		elif _cek == 1:
			_Auth('clear')
			_print(__banner__)
			_pico = input(f' {b}[{h}»{p}Kuso{h}«{b}]{p} Title {b}≽ {p}')
			if _pico == '':
				exit(f' {b}[{m}»{p}Eror{m}«{b}]{p} Title Is None !')
			else:
				_KusoNime(_pico)
		elif _cek == 2:
			_print(f"""
 {m}▪{p} Gak Ada Yang Beda ,Cuman Fix Error Doang Gak Ada
   Function Auto Download Nya Sengaja Lewat Open Browser
   Biar Bisa Ke UC Browser& Download Juga Jadi Wuzz.. Wuzz..
 {m}▪{p} Yang Nama Nya Web Anime Ya Pasti Gak Ada Yang
   Lengkap, Kalau Yang Versi Ongoing/Satuan/Ketengan Bisa
   Pakai Oploverz.in & Neonime.Vip.
 {b}▪{p} Versi Oploverz {b}≽{p} https://github.com/Ezz-Kun/oploverz-url
 {b}▪{p} Versi NeoNime {b}≽{p} https://github.com/Ezz-Kun/neonime-url
 {h}▪{p} Contact Wa : 085325463021
""")
			input(f' {b}[{h}»{p}Kuso{h}«{b}]{p} Enter To Back!')
			_MainKusoNime()
		elif _cek == 3:
			exit(f' {b}[{h}»{p}Kuso{h}«{b}]{p} Exit Tools!')
		else:
			exit(f' {b}[{m}»{p}Eror{m}«{b}]{p} Invalid Choice!')
	except (ValueError,KeyboardInterrupt,EOFError):
		exit(f' {b}[{m}»{p}Eror{m}«{b}]{p} Something Error!')
		
if __name__=="__main__":
	_MainKusoNime()
