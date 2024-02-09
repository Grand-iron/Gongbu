import requests
from bs4 import BeautifulSoup
import pymysql

# sql 연결 부분
conn = pymysql.connect(host='220.67.115.32',port=11102, user='stdt013', password='', db='stdt013', charset='utf8',connect_timeout=100000)
cur=conn.cursor()
cur.execute("CREATE TABLE `stdt013`.`경찰청분실물자료1` (`No` VARCHAR(45) NOT NULL,\
            `lstplace` VARCHAR(45) NULL,\
            `lstprdtnm` VARCHAR(80) NULL,\
            `lstsbjt` VARCHAR(45) NULL,\
            `lstymd` VARCHAR(45) NULL,\
            `prdtclnm` VARCHAR(45) NULL,\
            `rnum` VARCHAR(45) NULL,PRIMARY KEY (`No`));")

#공공데이터 연결 부분
url = 'http://apis.data.go.kr/1320000/LostGoodsInfoInqireService/getLostGoodsInfoAccToClAreaPd'
params ={'serviceKey' : 'm2fohO4ITYMYTzUwPkjSLuCSZPSfeFDP8OUOLE5Le34YcoF/I0F01Zy7aCPe1mE493R1ARskVx7spnuqBzUMXA==', 
         'START_YMD' : '20231012', 'END_YMD' : '20231012', 'PRDT_CL_CD_01' : '', 'PRDT_CL_CD_02' : '', 'LST_LCT_CD' : '', 'pageNo' : '1', 'numOfRows' : '10' }

response = requests.get(url, params=params)
soup=BeautifulSoup(response.text,"lxml")
items= soup.find_all("item")

for item in items:
    params={'serviceKey' : 'm2fohO4ITYMYTzUwPkjSLuCSZPSfeFDP8OUOLE5Le34YcoF/I0F01Zy7aCPe1mE493R1ARskVx7spnuqBzUMXA==', 
         'ATC_ID' : item.find('atcid').get_text()}
    response = requests.get(url, params=params)
    soup=BeautifulSoup(response.text,"lxml")
    real_items=soup.find_all("item")
    for k in real_items:
        atcid=k.find('atcid').get_text()
        lststenm=k.find('lstSteNm').get_text()
        lstprdtnm=k.find('lstprdtnm').get_text()
        lstsbjt=k.find('lstsbjt').get_text()
        lstymd=k.find('lstymd').get_text()
        prdtclnm=k.find('prdtclnm').get_text()
        orgnm=k.find('orgnm').get_text()

    #sql에 공공데이터 튜플을 넣는 구문
    sql = "insert into 경찰청분실물자료1     values(%s, %s, %s, %s,%s,%s,%s)"
    vals=(atcid,lststenm,lstprdtnm,lstsbjt,lstymd,prdtclnm,orgnm)
    cur.execute(sql,vals)
conn.commit()
conn.close()