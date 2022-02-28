#from urllib import request
#from bs4 import BeautifulSoup
#
#content = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")
#soup = BeautifulSoup(content, 'html.parser')
#
#for data in soup.select("data"):
#    print("시간: ", data.select_one("tmef").string)
#    print("날짜: ", data.select_one("wf").string)
#    print("-" * 20)

# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

"""
$ set FLASK_APP = 07-2_ex.py
$ flask run
"""