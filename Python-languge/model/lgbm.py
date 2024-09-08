import lightgbm as lgb

# LightGBM 모델 초기화
model = lgb.LGBMClassifier(
    boosting_type='gbdt',          # 부스팅 방식 ('gbdt', 'dart', 'goss' 중 선택)
    num_leaves=31,                 # 리프 노드의 수 (31로 설정, 클수록 모델 복잡성 증가)
    max_depth=-1,                  # 트리의 최대 깊이 (-1로 설정하면 제한 없음)
    learning_rate=0.1,             # 학습률 (0.1로 설정, 낮은 값일수록 안정적 학습)
    n_estimators=100,              # 부스팅 반복 횟수 (100으로 설정, 더 많은 트리를 사용할 수 있음)
    subsample=0.8,                 # 각 트리를 학습할 때 사용할 샘플 비율 (0.8로 설정, 과적합 방지)
    colsample_bytree=0.8,          # 각 트리를 학습할 때 사용할 특성 비율 (0.8로 설정, 과적합 방지)
    reg_alpha=0.0,                 # L1 정규화 매개변수 (0.0으로 설정, 정규화 없음)
    reg_lambda=0.0,                # L2 정규화 매개변수 (0.0으로 설정, 정규화 없음)
    min_child_weight=1e-3,         # 자식 노드에서의 최소 가중치 합 (1e-3으로 설정, 과적합 방지)
    random_state=42,               # 난수 생성 시드 (모델의 재현성을 위해 설정)
    class_weight=None,              # 클래스 가중치 (None으로 설정하면 모든 클래스에 동일한 가중치 부여)
    verbose=-1                     # 로그 출력 수준 (-1로 설정하면 출력 없음)
)

