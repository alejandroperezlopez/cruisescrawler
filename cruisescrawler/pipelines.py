# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
import datetime
from scrapy import signals
from os import path
from scrapy.xlib.pydispatch import dispatcher


class CruisescrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class SQLiteCruisesPipeline(object):
    db = '/PATH_TO_YOUR_DB/cruises.db'

    def __init__(self):
        self.conn = None
        dispatcher.connect(self.initialize, signals.engine_started)
        dispatcher.connect(self.finalize, signals.engine_stopped)

    def process_item(self, item, domain):
        try:
            generated_id = self.calculate_id(item)
            date = datetime.datetime.strptime(item['date'], "%d/%m/%Y")
            self.conn.execute('insert or replace into cruises values(?,?,?,?,?,?,?,?,?,'
                              'strftime(\'%Y-%m-%d %H-%M-%S\',\'now\'));',
                              (generated_id, date, item['name'],
                              item['origin'], item['destination'], item.get('capacity', 'N/A'),
                              item['arrivalTime'], item['departureTime'], item['port']))
            print ('Inserted cruise with name %s .Port=%s.Date=%s' % (item['name'], item['port'], item['date']))
        except Exception as e:
            print ('ERROR - FAILED to insert cruise with name %s .Port=%s.Date=%s' % (item['name'], item['port'], item['date']))
            print (str(e))
        return item

    def calculate_id(self, item):
        return hash(item['name'] + '-' + item['port'] + "-" + item['date'])

    def initialize(self):
        if path.exists(self.db):
            self.conn = sqlite3.connect(self.db)
        else:
            self.conn = self.create_table(self.db)

    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn = None

    def create_table(self, db):
        print ('creating table..')
        conn = sqlite3.connect(db)
        conn.execute("CREATE TABLE cruises(id INTEGER PRIMARY KEY, date DATE, name TEXT, origin TEXT, "
                     "destination TEXT, capacity TEXT, arrivalTime TEXT, departureTime TEXT, port TEXT, "
                     "lastTouched DATE)")
        conn.commit()
        print ('..table created')
        return conn

