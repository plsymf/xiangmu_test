import happybase as db
conn = db.Connection(host='192.168.19.10', port=9090)
conn.open()
# table = conn.table('pls_hbase:xm')
conn = db.Connection(host='192.168.19.10', port=9090)
conn.open()
table = conn.table('pls_hbase:xm')
# for i in table.scan():
#     try:
#         for k,v in i.items():
#             try:
#                 print(v.decode('utf-8'))
#             except:
#                 pass
#     except:
#         pass
search_condition=['北京','上海','广州','深圳']
i=0
data2=[]
while i < 4:
    data1 = []
    for key, value in table.scan(filter="RowFilter(=,'regexstring:\.*" +search_condition[i]+ ".*')"):
        data = []
        for j, v in value.items():
            # if 'notshow' in i.decode('utf-8'):
            #     pass
            # else:
            try:
                data.append(i.decode('utf-8'))
            except:
                pass
            print(v.decode('utf-8'))
            # data.update({str(i.decode('utf-8')).split('show:'): v.decode('utf-8')})
        data1.append(data)

    result=len(data1)
    data2.append(result)
    i+=1
print(data2)























# data1 = []
# for key, value in table.scan(filter="RowFilter(=,'regexstring:\.*" + '北京' + ".*')"):
#     data =[]
#     for i, v in value.items():
#         # if 'notshow' in i.decode('utf-8'):
#         #     pass
#         # else:
#         data.append(v.decode('utf-8'))
#             # data.update({str(i.decode('utf-8')).split('show:'): v.decode('utf-8')})
#     data1.append(data)
# print(len(data1))



# print(result)