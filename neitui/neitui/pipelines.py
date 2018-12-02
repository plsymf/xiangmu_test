# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import happybase
class NeituiPipeline(object):
    def __init__(self):
        self.conn_mysql = MySQLdb.Connection(host='127.0.0.1', port=3306, user='root', db='boss', charest='utf8',
                                             password='111111')
        self.conn_hbase = happybase.Connection(host='192.168.19.10', port=9090)

    def process_item(self, item, spider):
        self.save(item)
        return item

    def save(self, item):
        sql = 'select count(id) from t_boss'
        self.conn_mysql.cursor.execute(sql)
        result = self.conn_mysql.cursor.fetchall()
        if result <= 1000:
            # 存储Mysql
            sql = 'insert into t_boss (position,salary,company,company_address,position_info,company_size,company_ip,company_nature,company_business,exp_require,edu_require,recruit_num)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            self.conn_mysql.cursor(sql, [item[''], item[''], item[''], item[''], item[''], item[''], item[''], item[''],
                                         item[''], item[''], item[''], item['']])
            self.conn_mysql.commit()
        else:
            # 存储Hbase
            self.conn_hbase.open()
            hbase_table = self.conn_hbase.table('pls')
            hbase_table.put(row=item[''] + item[''] + item[''] + item[''],
                            data={'show_data': (item[''], item['']), 'noshow_data': (item[''], item[''])})
