import pymysql
import pymysql.cursors
import requests
from bs4 import BeautifulSoup
import os
import datetime

def Show_list(L_value): #리스트를 띄우는 함수
    count=0  #페이지수와 값을 바꾸는데 사용한다.
    while(1):
        for x in range(10): #10개씩 값을 띄우며 count에 따라 페이지 수를 조정한다.
            print(x+1,L_value[x+10*count]["분실물명"],"/",L_value[x+10*count]["분실지역"],"/",str(L_value[x+10*count]["수령일자"]))
        a=input("%d페이지입니다.\n이전:B 다음:N 상세정보:I 그만보기:Q" % int(count+1))
        if a=="N":
            count=count+1
        elif a=="B" and count!=0:
            count=count-1
        elif a=="I":
            info=int(input("상세정보를 보고 싶으신 분실물의 번호를 입력해주세요 : "))
            print(L_value[info+(count*10)-1])
            input("다봤으면 엔터")
        elif a=="Q":
            break
        os.system('cls') #화면을 지워 깔끔하게 한다.

#사전작업 MYSQL연결 및 공통 테이블에 담긴 내용 딕셔너리 형태로 가져오기  user/password/db에 자신에게 맞는 내용 적기
conn = pymysql.connect(host='220.67.115.32',port=11102, user='stdt013', password='gg', db='stdt013', charset='utf8',connect_timeout=100000)
cur=conn.cursor(pymysql.cursors.DictCursor)
cur.execute("SELECT * FROM 공통 ORDER BY 수령일자 DESC;")
L_value= cur.fetchall()

#공공데이터 인증키
url = 'http://apis.data.go.kr/1320000/LostGoodsInfoInqireService/getLostGoodsInfoAccToClAreaPd'

#메뉴창
while(1):
    choice=input("원하시는 메뉴를 입력해주세요 \n전체분실물LIST 보기:L 분실물LIST 검색:S 알림설정하기:O 새로고침:R 종료하기:Q ")
    
    #분실물 리스트 구문
    if choice=="L":
        os.system('cls')
        Show_list(L_value)

    #분실물 리스트 검색 구문
    elif choice=="S":
        choice= int(input("1.분실물 종류 검색\n2.분실 날짜 검색\n3.통합 검색"))
        if choice==1:
            S_jongryu=input("분실물 종류를 입력해주세요.(ex:지갑)")
            cur.execute("SELECT * FROM stdt013.공통 where 물품분류 like\"%%%s%%\";"%S_jongryu) #검색부분
            J_value=cur.fetchall()
            os.system('cls')
            Show_list(J_value)
        elif choice==2:
            S_day=input("분실 날짜를 입력해주세요.(ex:2023-12-01)")
            cur.execute("SELECT * FROM stdt013.공통 where 수령일자 like\"%%%s%%\";"%S_day) #검색부분
            D_value=cur.fetchall()
            os.system('cls')
            Show_list(D_value)
        elif choice==3:
            S_plus=input("분실물 종류와 분실 날짜를 공백으로 구분해 입력해주세요. (ex:지갑 2023-12-01)").split()
            cur.execute("SELECT * FROM stdt013.공통 where 물품분류 like\"%%%s%%\" and 수령일자 like\"%%%s%%\";"% (S_plus[0],S_plus[1])) #검색부분
            P_value=cur.fetchall()
            os.system('cls')
            Show_list(P_value)
    
    #알림설정 칸 만들기 
    elif choice=="O":
        choice=input("알림설정 추가:Y, 삭제:D ")
        if choice=="Y":
            alarm=input("공백으로 구분하여 전화번호/물품분류/장소로 적어주세요. (ex:01012345678 지갑 지하철)").split()
            cur.execute("insert into 알림설정 values( \'%s\', \'% s\', \'%s\')"%(alarm[0],alarm[1],alarm[2])) #사용자 정보 및 알림 내용 삽입부분 
        elif choice=="D":
            alarm=input("알림설정을 취소할 전화번호을 입력해주세요")
            cur.execute("DELETE FROM 알림설정 WHERE 사용자전화번호 = \'%s\';"%alarm)  #삭제 기능

    #새로고침 구문
    elif choice=="R":
        os.system('cls')
        print("최근 정보를 불러오는 중입니다.")
        cur.execute("SELECT * FROM 알림설정;") #알림설정 테이블의 값을 딕셔너리 형태로 가져온다.
        O_value= cur.fetchall()
        
        P_day=L_value[0]['수령일자'].strftime("%Y%m%d") #공통 테이블의 가장 최근 날짜를 불러옴
        N_day=datetime.datetime.now().strftime("%Y%m%d") #현재의 날짜를 불러옴

        #오픈 api 사용 구문 (lxml parser를 이용하여 xml형식의 데이터를 변수에 담는다.)
        params ={'serviceKey' : 'm2fohO4ITYMYTzUwPkjSLuCSZPSfeFDP8OUOLE5Le34YcoF/I0F01Zy7aCPe1mE493R1ARskVx7spnuqBzUMXA==', 
         'START_YMD' : '%s'%P_day, 'END_YMD' : '%s'%N_day, 'PRDT_CL_CD_01' : '', 'PRDT_CL_CD_02' : '', 'LST_LCT_CD' : '', 'pageNo' : '1', 'numOfRows' : '10000' } #공통테이블의 가장 최근날짜 부터 현재의 날짜까지의 정보를 불러온다.
        response = requests.get(url, params=params)
        soup=BeautifulSoup(response.text,"lxml") 
        items= soup.find_all("item")

        #삽입구문
        for item in items:
            atcid=item.find('atcid').get_text()
            lstplace=item.find('lstplace').get_text()          
            lstprdtnm=item.find('lstprdtnm').get_text()
            lstsbjt=item.find('lstsbjt').get_text()
            lstymd=item.find('lstymd').get_text() 
            prdtclnm=item.find('prdtclnm').get_text()
            prdtclnm = prdtclnm.split(">", 1)[0]
            for row in O_value:
                if prdtclnm.strip() in row["분실물종류"].strip():
                    if lstplace.strip() in row["장소"].strip():
                        print("%s와 %s에 알림을 설정한 %s번호로 알림을 보냅니다"% (lstplace,prdtclnm,row['사용자전화번호']))
            #sql에 공공데이터 튜플을 넣는 구문
            sql = "insert ignore into 공통 values(%s, %s, %s, %s,%s,%s)" #중복으로 인한 오류 방지
            vals=(atcid,lstplace,lstsbjt,lstprdtnm,lstymd,prdtclnm)
            cur.execute(sql,vals)
        print("정보 갱신이 완료되었습니다.")

    #종료 구문
    elif choice=="Q":
        break

#사용 종료 구문
conn.commit()
conn.close()