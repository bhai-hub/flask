from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/get-weather/<city_name>")
def home(city_name):
    q = city_name
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"} 
    URL = f'https://www.bing.com/search?q={q}+temperature&qs=SS&pq=hyderabad+temepera&sc=10-18&cvid=34540A888C294372A9DE79E3014D374F&FORM=QBRE&sp=1&ghc=1&lq=0'
    req = requests.get(url = URL, headers=headers)
    soup = BeautifulSoup(req.content, "html.parser")

    res1 = soup.find('div', attrs= {'class': 'wtr_currTemp'})
    res2 = soup.find('div', attrs={'class':'wtr_currUnit'})
    res3 = soup.find('div',attrs={'class': 'wtr_caption'})
    res4 = soup.find('span',attrs={'class': 'wtr_foreGround'})

    weather = {
        "name" : res4.get_text(),
        "temp": res1.get_text(),
        "units" : res2.get_text(),
        "content": res3.get_text()
    }
    
    return jsonify(weather)

if __name__ == "__main__":
    app.run()
