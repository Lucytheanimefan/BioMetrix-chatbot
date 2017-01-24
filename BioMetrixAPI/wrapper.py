import urllib
import requests
import wikipedia

biometrix_id = '812f8b53-a7b7-4167-ba44-312daad33ee2' #dipesh's 

#https://stats-api.biometrixtech.com/stats/aggScores/athMechStress?userId=812f8b53-a7b7-4167-ba44-312daad33ee2&startDate=2016-12-23&endDate=2017-01-22&resolution=1
test_json = {"userId": biometrix_id, "startDate":'2016-12-23','endDate':'2017-01-22','resolution':'1'}
main_url = 'https://stats-api.biometrixtech.com/stats'
wiki = "https://en.wikipedia.org/w/api.php"

wiki_json = {"action":"query","list":"search","srsearch":"replace"}
#https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=Albert%20Einstein&utf8=
def encode_params_get_data(json, url):
	params = urllib.urlencode(json)
	data = requests.get(url+params)
	return data
	

def get_athlete_mech_stress(json):
    url = main_url + '/aggScores/athMechStress?'
    data = encode_params_get_data(json, url)
    print("DATA FROM API")
    print data.content
    return data.content


def get_athlete_move_qual(json):
	url = main_url + '/moveQual/athMQFeatures'
	data = encode_params_get_data(json, url)
	return data.content


#wiki wrapper
def get_wiki_def(word):
	data = wikipedia.search(word)
	page = wikipedia.page(word)
	if page is not None:
		return page.content
	return data
	