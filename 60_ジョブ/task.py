import requests

# 本日のタスクをJSON形式で取得
token = '3283f4b60008c5f1dceb9c7221975ca7f9fede4b'
filter = '#Private&(today|overdue)'
response = requests.get("https://beta.todoist.com/API/v8/tasks", params={"token": token, "filter": filter}).json()

# 整形
today_task = ''
for task in response:
    today_task = today_task + task['content'] + ' \n' \

# トークンとAPIを設定
line_notify_token = 'o4kRLJltbxWg3xgVvmg2XDq7JilBtBmShFDegPZsCKp'
line_notify_api = 'https://notify-api.line.me/api/notify'

# メッセージを作成
message = '\n' \
    + '【本日のタスク】' + '\n' \
    + today_task

# 送信
payload = {'message': message}
headers = {'Authorization': 'Bearer ' + line_notify_token}  # 発行したトークン
line_notify = requests.post(line_notify_api, data=payload, headers=headers)
