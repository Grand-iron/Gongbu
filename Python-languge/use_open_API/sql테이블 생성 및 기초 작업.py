import requests
from bs4 import BeautifulSoup
import pymysql

# sql 연결 부분
conn = pymysql.connect(host='220.67.115.32',port=11102, user='stdt013', password='gg', db='stdt013', charset='utf8',connect_timeout=100000)
cur=conn.cursor()
cur.execute("CREATE TABLE `stdt013`.`경찰` (`분실물SEQ` VARCHAR(45) NOT NULL,\
            `수령위치` VARCHAR(500) NULL,\
            `분실물명` VARCHAR(500) NULL,\
            `상세내용` VARCHAR(1000) NULL,\
            `수령일자` DATETIME NULL,\
            `물품분류` VARCHAR(45) NULL,\
            PRIMARY KEY (`분실물SEQ`));")

#공공데이터 연결 부분
url = 'http://apis.data.go.kr/1320000/LostGoodsInfoInqireService/getLostGoodsInfoAccToClAreaPd'
params ={'serviceKey' : 'm2fohO4ITYMYTzUwPkjSLuCSZPSfeFDP8OUOLE5Le34YcoF/I0F01Zy7aCPe1mE493R1ARskVx7spnuqBzUMXA==', 
         'START_YMD' : '20231127', 'END_YMD' : '20231201', 'PRDT_CL_CD_01' : '', 'PRDT_CL_CD_02' : '', 'LST_LCT_CD' : '', 'pageNo' : '1', 'numOfRows' : '10000' }
response = requests.get(url, params=params)
soup=BeautifulSoup(response.text,"lxml")
items= soup.find_all("item")

for item in items:
    atcid=item.find('atcid').get_text()
    lstplace=item.find('lstplace').get_text()
    lstprdtnm=item.find('lstprdtnm').get_text()
    lstsbjt=item.find('lstsbjt').get_text()
    lstymd=item.find('lstymd').get_text() 
    prdtclnm=item.find('prdtclnm').get_text()
    prdtclnm = prdtclnm.split(" ", 1)[0]
    prdtclnm = prdtclnm.split(">", 1)[0]
    #sql에 공공데이터 튜플을 넣는 구문
    sql = "insert into 경찰    values(%s, %s, %s, %s,%s,%s)"
    vals=(atcid,lstplace,lstprdtnm,lstsbjt,lstymd,prdtclnm)
    cur.execute(sql,vals)
conn.commit()
conn.close()