import json
from lxml import etree

import requests
import MySQLdb
conn=MySQLdb.Connection(host='127.0.0.1',port=3306,user='root',db='pls',charset='utf8',password='111111')
cursor = conn.cursor()
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_%E5%A4%A7%E6%95%B0%E6%8D%AE?px=default&city=%E5%8C%97%E4%BA%AC'
}
params = {
    'px': 'default',
    'city': '北京',
    'needAddtionalResult': 'false',
    'first': 'false',
    'pn': '3',
    'kd': 'AI',
    'cookie': 'JSESSIONID=ABAAABAAAGGABCBEB404CAC2E831656FF2217AC3F2D4C67'
}

datas = json.loads(requests.post(url,headers=headers,params=params).text)

for data in datas['content']['positionResult']['result']:
    url1='https://www.lagou.com/jobs/' + str(data['positionId']) + '.html'
    html=etree.HTML(requests.get(url1,headers=headers).content.decode('utf-8'))
    try:
        position=html.xpath('//div[@class="job-name"]/span/text()')
        salary=html.xpath('//dd[@class="job_request"]/p/span/text()')[0]
        exp_require=html.xpath('//dd[@class="job_request"]/p/span/text()')[2]
        edu_require=html.xpath('//dd[@class="job_request"]/p/span/text()')[3]
        info=html.xpath('//dd[@class="job_bt"]/div/p//text()')
        company_address=html.xpath('//div[@class="work_addr"]/text()')[4]
        company_business=html.xpath('//ul[@class="c_feature"]/li/text()')[1]
        company_ip=html.xpath('//ul[@class="c_feature"]/li/a/text()')
        recruit_num=html.xpath('//dd[@class="job_bt"]/div/p/text()')
        company=html.xpath('//h2[@class="fl"]/text()')[0]
        print(salary,company_address)
        sql = 'insert into info (salary,company_address)VALUES(%s)'
        count=cursor.execute(sql,[salary,company_address])
        # sql = 'insert into info (salary,company,company_address,position_info,company_size,company_ip,company_nature,company_business,exp_require,edu_require,recruit_num)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        # count=cursor.execute(sql,[salary,company,company_address,position,info,company_ip,info,company_business,exp_require,edu_require,recruit_num])
        conn.commit()
    except:
        pass
