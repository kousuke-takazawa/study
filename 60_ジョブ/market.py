import requests
import json

# zaifトークンの価格取得
response = requests.get('https://api.zaif.jp/api/1/last_price/zaif_jpy')
if response.status_code != 200:
    raise Exception('return status code is {}'.format(response.status_code))
zaif_jpy = json.loads(response.text)
zaif_price = zaif_jpy['last_price']

# ビットコインの価格取得
response = requests.get('https://api.zaif.jp/api/1/last_price/btc_jpy')
if response.status_code != 200:
    raise Exception('return status code is {}'.format(response.status_code))
btc_jpy = json.loads(response.text)
btc_price = btc_jpy['last_price']

# 日経平均取得
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://stocks.finance.yahoo.co.jp/stocks/detail/?code=998407"
res = urlopen(url)

soup = BeautifulSoup(res,'html.parser')
stoksPrice = soup.select('.stoksPrice')
nikkei = stoksPrice[1].text

# 金価格取得
url = "http://gold.tanaka.co.jp/commodity/souba/d-gold.php"
res = urlopen(url)

soup = BeautifulSoup(res,'html.parser')
goldPrice = soup.select('.retail_tax')
gold = goldPrice[1].text

# 為替レートを取得
# （参考）http://www.yoheim.net/blog.php?q=20160807

import urllib.parse
from pprint import pprint

# USDJPY用
params_usd = {
    "q": 'select * from yahoo.finance.xchange where pair in ("USDJPY")',
    "format": "json",
    "env": "store://datatables.org/alltableswithkeys"
}

url_usd = "https://query.yahooapis.com/v1/public/yql?" + urllib.parse.urlencode(params_usd)
res_usd = urlopen(url_usd)
result_usd = json.loads(res_usd.read().decode('utf-8'))
usdjpy = result_usd['query']['results']['rate']['Ask']


# AUDJPY用
params_aud = {
    "q": 'select * from yahoo.finance.xchange where pair in ("AUDJPY")',
    "format": "json",
    "env": "store://datatables.org/alltableswithkeys"
}

url_aud = "https://query.yahooapis.com/v1/public/yql?" + urllib.parse.urlencode(params_aud)
res_aud = urlopen(url_aud)
result_aud = json.loads(res_aud.read().decode('utf-8'))
audjpy = result_aud['query']['results']['rate']['Ask']

# トークンとAPIを設定
line_notify_token = 'o4kRLJltbxWg3xgVvmg2XDq7JilBtBmShFDegPZsCKp'
line_notify_api = 'https://notify-api.line.me/api/notify'

# メッセージを作成
message = '\n' \
    + 'zaif:' + str(zaif_price) + '\n' \
    + 'btc:' + str(btc_price) + '\n' \
    + '日経平均:' + nikkei + '\n' \
    + 'ドル円:' + usdjpy + '\n' \
    + '豪ドル円:' + audjpy + '\n' \
    + '金:' + gold\


# 送信
payload = {'message': message}
headers = {'Authorization': 'Bearer ' + line_notify_token}  # 発行したトークン
line_notify = requests.post(line_notify_api, data=payload, headers=headers)