import logging
import requests
url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
         'Referer': 'https://www.lagou.com/jobs/list_%E5%A4%A7%E6%95%B0%E6%8D%AE?labelWords=&fromSearch=true&suginput='
         }
proxy={}
params={
    'needAddtionalResult':'false'
}
print(requests.post(url,headers=headers,params=params).text)
# logging.error()
# logging.r