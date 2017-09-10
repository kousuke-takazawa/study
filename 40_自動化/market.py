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

# トークンとAPIを設定
line_notify_token = 'o4kRLJltbxWg3xgVvmg2XDq7JilBtBmShFDegPZsCKp'
line_notify_api = 'https://notify-api.line.me/api/notify'

# メッセージを作成
message = '\n' \
    + 'zaif:' + str(zaif_price) + '\n' \
    + 'btc:' + str(btc_price) + '\n' \
    + '日経平均:' + nikkei + '\n' \

# 送信
payload = {'message': message}
headers = {'Authorization': 'Bearer ' + line_notify_token}  # 発行したトークン
line_notify = requests.post(line_notify_api, data=payload, headers=headers)