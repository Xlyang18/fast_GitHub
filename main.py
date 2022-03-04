import time
import driver as driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib import request, parse
import json
import urllib.request
import urllib.parse
import ssl



# 有道翻译：中文→英文
def fy(i):
    req_url = 'http://fanyi.youdao.com/translate'  # 创建连接接口
    # 创建要提交的数据
    Form_Date = {}
    Form_Date['i'] = i
    Form_Date['doctype'] = 'json'
    Form_Date['form'] = 'AUTO'
    Form_Date['to'] = 'AUTO'
    Form_Date['smartresult'] = 'dict'
    Form_Date['client'] = 'fanyideskweb'
    Form_Date['salt'] = '1526995097962'
    Form_Date['sign'] = '8e4c4765b52229e1f3ad2e633af89c76'
    Form_Date['version'] = '2.1'
    Form_Date['keyform'] = 'fanyi.web'
    Form_Date['action'] = 'FY_BY_REALTIME'
    Form_Date['typoResult'] = 'false'

    data = parse.urlencode(Form_Date).encode('utf-8')  # 数据转换
    response = request.urlopen(req_url, data)  # 提交数据并解析
    html = response.read().decode('utf-8')  # 服务器返回结果读取
    # print(html)
    translate_results = json.loads(html)  # 以json格式载入
    translate_results = translate_results['translateResult'][0][0]['tgt']  # json格式调取
    # print(translate_results)  # 输出结果
    return translate_results;  # 返回结果fu


def github():
    if __name__ == '__main__':
        ssl._create_default_https_context = ssl._create_unverified_context

        url = 'https://github.com/search?q='

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62 '
        }

        name = urllib.parse.quote('%s' % res)
        url = url + name

        request = urllib.request.Request(url=url, headers=headers)

        # 模拟浏览器向服务器发送请求
        response = urllib.request.urlopen(request)

        # 获取响应内容
        content = response.read().decode('utf-8')

        # 打印数据
        print(content)

        driver = webdriver.Chrome()
        # 设置浏览器最大化显示
        # driver.maximize_window()
        driver.get("%s" % url)
        time.sleep(10)


content = input("Input Chinese content:")
res = fy('%s' % content)
print(res)
github()
