import xgboost as xgb

# XGBoost 모델 초기화
model = xgb.XGBClassifier(
    n_estimators=100,               # 트리의 개수 (100개의 트리 생성)
    learning_rate=0.1,              # 학습률 (0.1로 설정, 낮은 값일수록 안정적 학습)
    max_depth=6,                    # 트리의 최대 깊이 (6으로 설정, 깊이가 클수록 모델 복잡성 증가)
    min_child_weight=1,             # 자식 노드에서의 최소 가중치 합 (1로 설정, 과적합 방지)
    gamma=0,                        # 리프 노드 추가 시 손실 함수 개선에 대한 최소 손실 감소 (0으로 설정, 추가 분할 없이 사용)
    subsample=0.8,                  # 각 트리를 학습할 때 사용할 샘플 비율 (0.8로 설정, 과적합 방지)
    colsample_bytree=0.8,           # 각 트리를 학습할 때 사용할 특성 비율 (0.8로 설정, 과적합 방지)
    scale_pos_weight=1,             # 클래스 불균형 처리 (1로 설정, 두 클래스의 비율이 비슷할 경우)
    objective='binary:logistic',    # 목표 함수 (이진 분류를 위한 로지스틱 회귀 사용)
    eval_metric='auc',               # 평가 메트릭 (AUC 사용, 모델 성능 평가)
    early_stopping_rounds=50,        # 조기 종료 기준 (50번 반복 동안 개선이 없을 경우 종료)
    verbose=1                       # 훈련 중 진행 상황 출력 (출력 레벨 설정, 1은 기본적인 정보 출력)
)
