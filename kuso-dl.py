#!/../usr/bin/python
# Start  > Sabtu 8 Agustus 2020, - 20:01:43 WIB
# Finish > Sabtu 8 Agustus 2020, - 21:10:13 WIB
# Kusonime : https://www.kusonime.com
# MyGithub : https://www.github.com/Ezz-Kun
# Copyright © Ezz-Kun (2020)

from bs4 import BeautifulSoup as bs
from os import system
from time import sleep
import re,sys
import requests as req

m = '\033[1;31m'
k = '\033[1;33m'
h = '\033[1;32m'
b = '\033[1;34m'
p = '\033[1;37m'
bgb = '\033[1;44m'
cl = '\033[0m'

__banner__ = (
f'\t  {b}╦╔═{p}┬ ┬┌─┐{b}╔═╗{p}┌┐┌┬┌┬┐{b}╔═╗  ╔═╗{p}┌─┐{b}╔╗╔\n'
f'\t  ╠╩╗{p}│ │└─┐{b}║ ║{p}│││││││{b}║╣{p}───{b}║ ╦{p}├┤ {b}║║║\n'
f'\t  ╩ ╩{p}└─┘└─┘{b}╚═╝{p}┘└┘┴┴ ┴{b}╚═╝  ╚═╝{p}└─┘{b}╝╚╝\n'
f'{p}      ──────────────────────────────────────────\n'
f'        ( •̀ω•́ )σ{bgb}Kusonime.com Url Generator{cl}\n\n'
f'{b}【 {p}Ezz-Kun{b} 】{m}~{b}!{p}\n'
)

Argument_ = (
f'{b}【{p}01{b}】{p}Start \n{b}【{p}02{b}】{p}Help\n{b}【{p}03{b}】{p}Exit'
)

class Print(object):
	def __init__(self,string):
		for i in string +'\n':
			sys.stdout.write(str(i))
			sys.stdout.flush()
			sleep(0.00050)

class clean:
	def __init__(self):
		system('clear')

right = 0
class KusoNime(object):
	def __init__(self,title):
		self.title = title
		self.tamper = (f"https://kusonime.com/?s={self.title.replace(' ','+')}&post_type=post")
		self.GetTitle_(self.tamper)
	def GetTitle_(self,link):
		var = 0
		lef = 0
		next_ = []
		prev = 0
		judul = []
		global right
		pages = req.get(link).text
		html = bs(pages,'html.parser')
		page_ = html.find('span',class_="navileft") # find next page
		if page_ is not None:
			siskon = page_.find('strong').findNextSiblings()
			for jokes in range(len(siskon)-1):
				next_.append(siskon[lef]["href"].replace('amp;',''))
				lef +=1
		lef -= lef
		puki = html.find_all('h2',class_={"episodeye"})
		if len(puki) != 0:
			while True:
				if len(puki) > var:
					judul.append(puki[var].find('a')["title"]) # find anime tittle & append to list
					var +=1
				else:
					break
			var -= var
			clean()
			Print(__banner__)
			for x,i in enumerate(judul):
				Print(f'{b}[{p}{x}{b}]{h} ⌲ {p}{i}')
			if len(next_) != 0:
				Print(f'\n\t\t{b}[ {p}Type {b}[{p}99{b}]{p} For Next {b}[{p}00{b}]{p} For Prev {b}]{p} ')
			fu = int(input(f'\n{b}[{p}Kuso{b}]{h} ⌲ {p}Your Choice? : {p}'))
			if (fu) < len(judul):
				su = puki[fu].find('a')["href"] # url for page anime information
				self.PageInfo(su)
			elif fu == 99:
				if len(next_) > int(right):
					self.GetTitle_(next_[right])
					del judul[:]
					del next_[:]
					right +=1
				else:
					Print('\n\t\t [ Nothing Found ] ')
			elif fu == 00:
				right -= right
				del judul[:]
				del next_[:]
				self.GetTitle_(self.tamper)
			else:
				exit(f'{b}[{m}Kuso{b}]{p} Nothing Choice ! ')
		else:
			exit(f'{b}[{m}Kuso{b}]{p} Error : Title `{self.title}` Cannot Be Found !')
	def PageInfo(self,url):
		sum = 0
		gen = []
		xu = req.get(url).text
		fo = bs(xu,'html.parser')
		posted = fo.find('div',class_="kategoz").contents[1]
		genre = fo.findAll('a',attrs={"rel":"tag"})
		season = genre[-1].get_text()
		produk = re.search('<b>Producers</b>\: (.*?)\</p>',xu).group(1)
		status = re.search('<b>Status</b>\:\ (.*?)</p>',xu).group(1)
		eps = re.search('<b>\w.+Episode</b>\:\ (.*?)</p>',xu).group(1)
		skor = re.search('<b>Score</b>\:\ (.*?)</p>',xu).group(1)
		durasi = re.search('<b>Duration</b>\:\ (.*?)</p>',xu).group(1)
		rilis = re.search('<b>Released on</b>\:\ (.*?)</p>',xu).group(1)
		sinop = fo.find('strong').get_text() + ':' + bs(re.search('</strong>(.*?)<strong>',xu).group(1),'html.parser').get_text()
		for x in range(int(len(genre)-1)):
			gen.append(genre[sum].get_text())
			sum +=1
		clean()
		Print(__banner__)
		Print(f'{b}[{p}Kuso{b}]{h} ⌲{p} Post {h}:{p} {posted}')
		Print(f"{b}[{p}Kuso{b}]{h} ⌲{p} Genre {h}:{p} {', '.join(gen)}")
		Print(f'{b}[{p}Kuso{b}]{h} ⌲{p} Score {h}:{p} {skor}')
		Print(f'{b}[{p}Kuso{b}]{h} ⌲{p} Season {h}:{p} {season}')
		Print(f'{b}[{p}Kuso{b}]{h} ⌲{p} Status {h}:{p} {status}')
		Print(f'{b}[{p}Kuso{b}]{h} ⌲{p} Duration {h}:{p} {durasi}')
		Print(f'{b}[{p}Kuso{b}]{h} ⌲{p} Producers {h}:{p} {produk}')
		Print(f'{b}[{p}Kuso{b}]{h} ⌲{p} Released On {h}:{p} {rilis}')
		Print(f'{b}[{p}Kuso{b}]{h} ⌲{p} Total Episode {h}:{p} {eps}')
		Print(f'{b}[{p}Kuso{b}]{h} ⌲{p} Sinopsis {h}:{p} {sinop}')
		show = input(f'{b}[{p}Kuso{b}]{h} ⌲{p} Show Url Download? {b}[{p}y{b}/{p}n{b}] >>{p} ')
		if show.lower() == 'y':
			self.Download(url)
		elif show.lower() == 'n':
			Main()
		else:
			exit(f'{b}[{m}Kuso{b}]{p} Nothing Choice')
	def Download(self,levi):
		satu = []
		dua = []
		tiga = []
		empat = []
		res_satu = []
		res_dua = []
		res_tiga = []
		res_empat = []
		fu = req.get(levi).text
		fi = bs(fu,'html.parser')
		go = fi.findAll('div',class_="smokeurl")
		for c in go:
			sun = c.find('strong').get_text()
			poko = c.find_all('a')
			if '360P' in sun:
				for ko in poko:
					satu.append(ko["href"])
					res_satu.append(ko.get_text())
			elif '480P' in sun:
				for ko in poko:
					dua.append(ko["href"])
					res_dua.append(ko.get_text())
			elif '720P' in sun:
				for ko in poko:
					tiga.append(ko["href"])
					res_tiga.append(ko.get_text())
			elif '1080P' in sun:
				for ko in poko:
					empat.append(ko["href"])
					res_empat.append(ko.get_text())
			else:
				continue
		while True:
			try:
				clean()
				Print(__banner__)
				Print(f'{b}【{p}01{b}】{h}⌲ {p}360P\n{b}【{p}02{b}】{h}⌲ {p}480P\n{b}【{p}03{b}】{h}⌲ {p}720P\n{b}【{p}04{b}】{h}⌲ {p}1080P\n{b}【{p}05{b}】{h}⌲ Exit Tools\n{b}【{p}06{b}】{h}⌲ Back To Home')
				chos = int(input(f'\n{b}[{p}Kuso{b}]{h} ⌲{p} Type : '))
				if chos == 1:
					for sa,s in enumerate(satu):
						Print(f'{b}({p}{sa}{b}){h} ⌲ {p}{res_satu[sa]} :{p} \n{s}')
					si = int(input(f'\n{b}[{p}kuso{b}] {h}⌲{p} Open With Browser? : '))
					if si < len(satu):
						system(f'termux-open {satu[si]}')
					else:
						exit(f'{b}[{m}Kuso{b}]{p} Out Of Index ! ')
				elif chos == 2:
					for sa,s in enumerate(dua):
						Print(f'{b}({p}{sa}{b}){h} ⌲ {p}{res_dua[sa]} :{p} \n{s}')
					si = int(input(f'\n{b}[{p}kuso{b}] {h}⌲{p} Open With Browser? : '))
					if si < len(dua):
						system(f'termux-open {dua[si]}')
					else:
						exit(f'{b}[{m}Kuso{b}]{p} Out Of Index ! ')
				elif chos == 3:
					for sa,s in enumerate(tiga):
						Print(f'{b}({p}{sa}{b}){h} ⌲ {p}{res_tiga[sa]} :{p} \n{s}')
					si = int(input(f'\n{b}[{p}kuso{b}] {h}⌲{p} Open With Browser? : '))
					if si < len(tiga):
						system(f'termux-open {tiga[si]}')
					else:
						exit(f'{b}[{m}Kuso{b}]{p} Out Of Index ! ')
				elif chos == 4:
					for sa,s in enumerate(empat):
						Print(f'{b}({p}{sa}{b}){h} ⌲ {p}{res_empat[sa]} :{p} \n{s}')
					si = int(input(f'\n{b}[{p}kuso{b}] {h}⌲{p} Open With Browser? : '))
					if si < len(empat):
						system(f'termux-open {empat[si]}')
					else:
						exit(f'{b}[{m}Kuso{b}]{p} Out Of Index ! ')
				elif chos == 5:
					exit(f'{b}[{m}Kuso{b}]{p} Exit Tuul ')
				elif chos == 6:
					Main()
				else:
					exit(f'{b}[{m}Kuso{b}]{p} Nothing Choice ! ')
			except ValueError:
				continue

class Main():
	def __init__(self):
		clean()
		Print(__banner__)
		comsi = input(f'{b}[{p}Kuso{b}] {p}Title {h}⌲ {p}: ')
		if comsi == '':
			Print(f'{b}[{m}Kuso{b}]{p} Tittle Is None {m}({p}Back To Home{m}){p}')
			sleep(0.3)
			Main()
		else:
			KusoNime(comsi)

if __name__=="__main__":
	try:
		clean()
		Print(__banner__)
		Print(Argument_)
		fi = int(input(f'\n{b}[{p}Kuso{b}]{h} ⌲{p} '))
		if fi == 1:
			Main()
		elif fi == 2:
			clean()
			Print(__banner__)
			Print('Ingat Broh , Ini Bukan Tuul Downloader ... \nAku Bikin Ini Niat Nya cuman buat sendiri Biar Gak Ribet\nUpload Ke Github Juga Sengaja Biar Gak Ke Hapus\nJadi Terserah Mau Pakai Atau Enggak :v\nKenapa Gak sekalian Aja Buat Function Downloader nya?\nYa karna Internal Aku Sedikit :v Mana \nBisa Buat Nampung File Ber Gb²\nDan Juga Termos Kan Gak Bisa Write Eksternal \nJadi Kalau Mau Nambahin Fitur Ya Tambahin Aja Sendiri\nUdah Itu Doang.... \nMakasih Buat Loe Smua Ngentod!!\n\nContact Wa : 085325463021')
		elif fi == 3:
			exit(f'{b}[{m}Kuso{b}]{p} Exit Tuul ')
		else:
			exit(f'{b}[{m}Kuso{b}]{p} Nothing Choice ')
	except (EOFError,ValueError,KeyboardInterrupt):
		exit('\n')

