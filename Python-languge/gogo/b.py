import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 필요한 컬럼 목록 정의
columns_needed = ['건물명', '계약일', '물건금액(만원)', '권리구분', '건축년도', '자치구명', '건물용도']

# 사용자로부터 년도 입력 받기
input_year = input("조회할 년도를 입력하세요 (예: 2023): ")

# 파일 경로 설정
file_path = f'C:/Users/young/OneDrive/바탕 화면/코드공간/Python-languge/gogo/아카이브/서울시 부동산 실거래가 정보_{input_year}.csv'

# matplotlib의 폰트 설정을 변경하여 한글이 깨지지 않도록 함
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows 운영체제
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 파일 읽기 시도
try:
    
    # 지정된 컬럼만 읽기
    df = pd.read_csv(file_path, usecols=columns_needed, encoding='cp949')

    # 자치구명 별 데이터 개수 계산
    data_counts = df['자치구명'].value_counts()

    # 데이터 개수 시각화
    plt.figure(figsize=(10, 8))
    data_counts.sort_values().plot(kind='barh', color='skyblue')
    plt.title(f'{input_year}년 서울시 자치구명 별 부동산 실거래가 데이터 개수')
    plt.xlabel('데이터 개수')
    plt.ylabel('자치구명')
    plt.show()
except FileNotFoundError:
    print(f"{input_year}년 데이터 파일을 찾을 수 없습니다.")
except Exception as e:
    print(f"데이터를 로딩하는 중 오류가 발생했습니다: {e}")
