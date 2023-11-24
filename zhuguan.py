import requests
from datetime import datetime

# 获取当前日期
current_date = datetime.now().strftime('%Y-%m-%d')
realName = ['王小虎','俞桂宝','刘福州','赵海阳','陆殿虎']

# 使用获取的token来访问其他受保护的接口
api_url = "http://abc.whxxzg.com:8001/VisitUser/RecordList"
params = {
    'page': 1,
    'limit': 10,
    'depname': '',
    'realName': '周升',
    'visitclass': -2,
    'begindate': '2023-10-21',
    'enddate': current_date,
    'DepID': '-2',
    'UserDepID': '-2'
}
headers = {'Authorization': '26e04237-7aba-4ed2-a3eb-22505ce2f92b'}

response = requests.get(api_url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error {response.status_code}: {response.text}")