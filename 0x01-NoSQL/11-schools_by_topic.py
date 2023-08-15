#!/usr/bin/env python3

'''11-schools_by_topic module'''

from pymongo import MongoClient

list_all = __import__('8-all').list_all

client = MongoClient()
db = client.logs
nginx_collection = db.nginx
all_logs = list_all(nginx_collection)
num_logs = nginx_collection.estimated_document_count()
logs_with_method_get = 0
logs_with_method_post = 0
logs_with_method_put = 0
logs_with_method_patch = 0
logs_with_method_delete = 0
logs_with_method_get_and_path_status = 0

print(num_logs, 'logs')
print('Methods:')

for log in all_logs:
    if log.get('method') == 'GET':
        logs_with_method_get += 1
    elif log.get('method') == 'POST':
        logs_with_method_post += 1
    elif log.get('method') == 'PUT':
        logs_with_method_put += 1
    elif log.get('method') == 'PATCH':
        logs_with_method_patch += 1
    elif log.get('method') == 'DELETE':
        logs_with_method_delete += 1
    if log.get('method') == 'GET' and log.get('path') == '/status':
        logs_with_method_get_and_path_status += 1

print('''\tmethod GET: {}
      \b\tmethod POST: {}
      \b\tmethod PUT: {}
      \b\tmethod PATCH: {}
      \b\tmethod DELETE: {}'''.format(logs_with_method_get,
                                      logs_with_method_post,
                                      logs_with_method_put,
                                      logs_with_method_patch,
                                      logs_with_method_delete))

print(logs_with_method_get_and_path_status, 'status check')
