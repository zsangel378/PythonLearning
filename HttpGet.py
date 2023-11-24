import requests

# 定义目标API的URL
url = "https://console-mock.apipost.cn/mock/b668352e-e1b8-43d3-96f4-10b2c9915af2/testPythonGet"  # 将这里替换为实际的API地址

# 发起GET请求
response = requests.get(url)

# 检查响应状态码
if response.status_code == 200:
    # 请求成功，可以处理响应数据
    data = response.json()  # 如果响应是JSON格式的数据
    print(data)
else:
    # 请求失败，打印错误信息
    print(f"HTTP请求失败，状态码: {response.status_code}")
    print(response.text)  # 打印响应内容
