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

# 자치구명을 기준으로 데이터프레임을 나누기
dfs = {region: df for region, df in df_all_years.groupby('자치구명')}

# 지역 입력 받기
input_region = input("조회할 지역을 입력하세요: ")

# 입력된 지역에 해당하는 데이터프레임 선택
df_region = dfs[input_region]

# 각 년도별 데이터 개수 계산
data_counts = df_region['년도'].value_counts().sort_index()

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.bar(data_counts.index.astype(str), data_counts.values)  # x축을 문자열로 변환
plt.xlabel('년도')
plt.ylabel('데이터 개수')
plt.title(f'{input_region} 2015~2024년 각 년도별 부동산 실거래가 데이터 개수')
plt.xticks(rotation=45)  # x축 라벨 회전
plt.show()
