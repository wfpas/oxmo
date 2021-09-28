
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class YuanjiangPipeline(object):
    def __init__(self):
        # 1. 建立数据库的连接
        self.connect = pymysql.connect(
            # localhost连接的是本地数据库
            host='localhost',
            # mysql数据库的端口号
            port=3306,
            # 数据库的用户名
            user='root',
            # 本地数据库密码
            passwd='777',
            # 表名
            db='scrapyDB',
            # 编码格式
            charset='utf8'
        )
        # 2. 创建一个游标cursor, 是用来操作表。
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 3. 将Item数据放入数据库，默认是同步写入。
        insert_sql = """INSERT INTO gsxx(gs, url, info, pmain, cp_url, lx_url, people, phone)
        VALUES ('%s', '%s', '%s','%s', '%s', '%s','%s', '%s')""" % (
            pymysql.escape_string(item['gs']),
            pymysql.escape_string (item['url']),
            item['info'],
            item['pmain'],
            item['cp_url'],
            item['lx_url'],
            item['people'],
            item['phone'],
        )
        self.cursor.execute(insert_sql)

        # 4. 提交操作
        self.connect.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
