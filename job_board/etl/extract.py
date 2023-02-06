import pandas as pd 
import requests

class Extract():
    '''
    docstring here
    '''
    ## code here
    pass


url = "https://jsearch.p.rapidapi.com/search"

querystring = {"query":"\"Data Analyst\" in USA ","num_pages":"20"}

headers = {
	"X-RapidAPI-Key": "5fec918ab1msh2089eaf59c35a4fp1d2106jsnc87acf303a5f",
	"X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)