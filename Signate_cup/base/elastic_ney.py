from sklearn.linear_model import ElasticNet

# Elastic Net 모델 초기화
model = ElasticNet(
    alpha=1.0,                     # L1 및 L2 정규화의 강도 (1.0으로 설정, 값이 클수록 정규화 강해짐)
    l1_ratio=0.5,                  # L1 정규화 비율 (0에서 1 사이의 값, 0.5는 L1과 L2의 균형)
    fit_intercept=True,            # 절편 항을 학습할지 여부 (True로 설정하면 절편 항 포함)
    normalize=False,                # 설명 변수 정규화 여부 (True로 설정하면 각 특성을 평균 0, 분산 1로 변환)
    precompute=False,               # 사전 계산 여부 (True로 설정하면 일부 계산을 사전 수행)
    max_iter=1000,                 # 최대 반복 횟수 (1000으로 설정, 더 많은 반복을 사용할 수 있음)
    tol=0.0001,                    # 수렴 허용 오차 (기본값 0.0001, 더 작은 값일수록 수렴 기준 엄격)
    random_state=None,             # 난수 생성 시드 (모델의 재현성을 위해 설정)
    selection='cyclic'             # 특성 선택 방식 ('cyclic' 또는 'random', 기본값은 'cyclic')
)
