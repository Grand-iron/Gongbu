import pandas as pd
import matplotlib.pyplot as plt

# 필요한 컬럼 목록 정의
columns_needed = ['건물명', '계약일', '물건금액(만원)', '권리구분', '건축년도', '자치구명', '건물용도']

# 2015년부터 2024년까지 데이터를 불러와서 하나의 데이터프레임으로 합치기
df_all_years = pd.DataFrame()
for year in range(2015, 2025):
    df_temp = pd.read_csv(
        #파일 경로 수정 필수
        f'{year}.csv',
        usecols=columns_needed,
        encoding='cp949'
    )
    df_temp['년도'] = year  # 각 데이터프레임에 '년도' 컬럼 추가
    df_all_years = pd.concat([df_all_years, df_temp])

# 각 년도별 데이터 개수 계산
data_counts = df_all_years['년도'].value_counts().sort_index()

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 선 그래프로 데이터 개수 변화량 보여주기
plt.figure(figsize=(10, 6))
plt.plot(data_counts.index.astype(str), data_counts.values, marker='o', linestyle='-', color='b')  # x축을 문자열로 변환
plt.xlabel('년도')
plt.ylabel('데이터 개수')
plt.title('2015~2024년 각 년도별 부동산 실거래가 데이터 개수 변화량')
plt.xticks(rotation=45)  # x축 라벨 회전
plt.grid(True)  # 그리드 추가
plt.show()