import pandas as pd
import matplotlib.pyplot as plt

# 필요한 컬럼 목록 정의
columns_needed = ['건물명', '계약일', '물건금액(만원)', '권리구분', '건축년도', '자치구명', '건물용도']

# 2015년부터 2024년까지 데이터를 불러와서 하나의 데이터프레임으로 합치기
df_all_years = pd.DataFrame()
for year in range(2015, 2025):
    df_temp = pd.read_csv(
        f'C:/Users/young/OneDrive/바탕 화면/코드공간/Python-languge/gogo/아카이브/서울시 부동산 실거래가 정보_{year}.csv',
        usecols=columns_needed,
        encoding='cp949'
    )
    df_temp['년도'] = year  # 각 데이터프레임에 '년도' 컬럼 추가
    df_all_years = pd.concat([df_all_years, df_temp])

# 각 년도별로 자치구의 데이터 개수를 계산하고 순위로 변환
rank_dict = {}
for year in range(2015, 2025):
    df_year = df_all_years[df_all_years['년도'] == year]
    count_by_region = df_year['자치구명'].value_counts().sort_values(ascending=False)
    rank_by_region = count_by_region.rank(method='min', ascending=False).astype(int)
    
    for region, rank in rank_by_region.items():
        if region not in rank_dict:
            rank_dict[region] = []
        rank_dict[region].append(rank)

# 자치구별 순위 출력
for region, ranks in rank_dict.items():
    print(f"{region}: {ranks}")

# 그래프 그리기
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(14, 10))

for region, ranks in rank_dict.items():
    plt.plot(range(2015, 2025), ranks, label=region)

plt.xlabel('년도')
plt.ylabel('순위')
plt.title('2015~2024년 자치구별 부동산 실거래가 데이터 개수 순위')
plt.gca().invert_yaxis()  # 순위는 1이 가장 높으므로 y축을 뒤집음
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.05))
plt.xticks(range(2015, 2025))
plt.grid(True)
plt.show()
