import requests
import time
from lxml import etree
import json
import chaojiying as cj
#内推网
# for i in range(1,100):
#     url='http://www.neitui.me/?name=job&handle=lists&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&page='+str(i)
#     html=etree.HTML(requests.get(url).text)
# # 获取详情页面的路径
# url_details=[]
#
# for url_detail in html.xpath('//ul[@class="list-items"]/li'):
#     # for i in url_detail.getchildren():
#     url_details.append(url_detail.xpath('//div[@class="mt5 clearfix"]/a/@href'))
#     # print(url_detail.xpath('//div[@class="mt5 clearfix"]/a/@href'))
# print(url_details[0])
#拉钩网
# {'msg': '您操作太频繁,请稍后再访问', 'success': False, 'clientIp': '223.104.3.55'}

#https://www.lagou.com/jobs/4871878.html
#获取数据
class DFS():
    def __init__(self):
        self.detail_url=[]
    def addToDetail_url(self,url):
        if url not in self.detail_url:
            self.detail_url.append(url)

    def getUrl(self):
        return self.detail_url.pop()
    def detail_urlIsEmpty(self):
        return self.detail_url
class GetUrl():
    def __init__(self,start_url,dfs,headers,params):
        self.start_url=start_url
        self.params=params
        self.headers=headers
        self.dfs=dfs
    def url(self):
        datas=json.loads(requests.post(self.start_url,headers=self.headers,params=self.params).text)
        print(datas)
        print(datas['content']['positionResult']['result'])
        # for data in datas['content']['positionResult']['result']:
        #     print('https://www.lagou.com/jobs/'+data['positionId']+'.html')
        #     self.dfs.addToDetail_url('https://www.lagou.com/jobs/'+data['positionId']+'.html')
class Crawler():
    def __init__(self,dfs):
        self.dfs=dfs
    def data(self):
        url=self.dfs.getUrl()
        print(url,'this is url')
        #爬取数据
if __name__=='__main__':
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
        'kd': '大数据',
        'cookie': 'JSESSIONID=ABAAABAAAGGABCBEB404CAC2E831656FF2217AC3F2D4C67'
    }
    #start_url,dfs,headers,params
    t=DFS()
    test=GetUrl(url,t,headers,params)
    test.url()
    crawler=Crawler(t)
    crawler.data()





# boss
# class DFS():
#     def __init__(self):
#         self.url_detail=[]
#     def addToDetail(self,url):
#         if url not in self.url_detail:
#             self.url_detail.append(url)
#     def getFromDetail(self):
#         return self.url_detail.pop()
#     def detailIsEmpty(self):
#         return self.url_detail
# class Crawler():
#     def __init__(self,start_url,dfs):
#         self.start_url=start_url
#         self.dfs=dfs
#     def url(self):
#         self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
#         params = {'query':'大数据','page':'2','ka':'page-2'}
#         querys=['AI','大数据','爬虫','pythonweb']
#         # proxy = {'http': 'http://' + ip + ':' + port}
#         # proxy={'http':'http://1.202.122.239:8060'}
#         html = etree.HTML(requests.get(self.start_url,headers=self.headers,params=params,timeout=3).text).xpath('//ul/li')
#         ka=1
#         for query in querys:
#                 params.update({'query':query})
#                 params.update({'page':ka})
#                 params.update({'ka':'page-'+str(ka)})
#                 html=etree.HTML(requests.get(self.start_url,headers=self.headers,params=params).text).xpath('//ul/li')
#                 print(html)
#                 url_detail = []
#                 for i in html:
#                     self.dfs.addToDetail(i.xpath('//a/@data-jid'))
#                 ka+=1
#                 if ka >15:
#                     break
#     def data(self):
#         if self.dfs.detailIsEmpty():
#             url= 'https://www.zhipin.com/job_detail/' +self.dfs.getFromDetail().pop() + '.html?ka=search_list_1'
#             html = etree.HTML(requests.get(url,headers=self.headers).text)
#             print(requests.get(url,headers=self.headers),'asdfasdfsadfas')
#             try:
#                 position = html.xpath('//h1/text()')[0]
#                 # salary = html.xpath('//span[@class="badge"]/text()')[-1]
#                 # company = html.xpath('//div[@class="job-sec"]/div[@class="name"]/text()')[0]
#                 # com_address=html.xpath('//div[@class="job-location"]/div[@class="location-address"]/text()')[0]
#                 # com_size=html.xpath('//div[@class="info-company"]/p/text()')[1]
#                 # com_ip=html.xpath('//div[@class="info-company"]/p/text()')[2]
#                 # exp_req=html.xpath('//div[@class="info-primary"]/p/text()')[1]
#                 # edu_req=html.xpath('//div[@class="info-primary"]/p/text()')[2]
#             except:
#                 pass
#             # return position,salary,company,com_address,com_size,com_ip,exp_req,edu_req
#             return position
#
# if __name__=='__main__':
#     url='https://www.zhipin.com/c101010100/?query=%E5%A4%A7%E6%95%B0%E6%8D%AE&page=2&ka=page-2'
#     dfs=DFS()
#     test=Crawler(url,dfs)
#     test.data()






























# def fun():
#     url_detail = []
#     for i in test.xpath('//ul/li'):
#         url_detail.append(i.xpath('//a/@data-jid'))
#     while url_detail:
#         url1 = 'https://www.zhipin.com/job_detail/' + url_detail[0].pop() + '.html?ka=search_list_1'
#         html = etree.HTML(requests.get(url1, headers=headers).text)
#         try:
#             position = html.xpath('//h1/text()')[0]
#             salary = html.xpath('//span[@class="badge"]/text()')[-1]
#             company = html.xpath('//div[@class="job-sec"]/div[@class="name"]/text()')[0]
#             com_address=html.xpath('//div[@class="job-location"]/div[@class="location-address"]/text()')[0]
#             com_size=html.xpath('//div[@class="info-company"]/p/text()')[1]
#             com_ip=html.xpath('//div[@class="info-company"]/p/text()')[2]
#             exp_req=html.xpath('//div[@class="info-primary"]/p/text()')[1]
#             edu_req=html.xpath('//div[@class="info-primary"]/p/text()')[2]
#         except:
#             pass
#         print(position)
# url='https://www.zhipin.com/c101010100/?query=%E5%A4%A7%E6%95%B0%E6%8D%AE&page=2&ka=page-2'
# headers={
# 'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
# }
# params={'query':'大数据','page':'1','ka':'page-1'}
# test=etree.HTML(requests.get(url,headers=headers).text)
# title=test.xpath('//title/text()')[0]
# if '验证码' in title:
#     print('this is 验证码')
#     im = requests.get('https://www.zhipin.com/captcha?randomKey=0zW9PGgRAFPuVpjcnCYAjefgoZcAUFis',headers=headers).content
#     with open('bb.jpg','wb') as w:
#         w.write(im)
#     code = cj.get_code(im)
#     print(code)
#     # 验证 验证码
#     check_code_url = 'https://www.zhipin.com/c101010100/?query='
#     resp = requests.get(check_code_url+code,headers=headers)
#     test = etree.HTML(requests.get(url,headers=headers).text)
#     print(requests.get(url,headers=headers).text)
#     print(test.xpath('//ul/li'))
#     fun()
# else:
#     fun()

