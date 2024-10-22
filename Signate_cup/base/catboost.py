from catboost import CatBoostClassifier

model = CatBoostClassifier(
    iterations=1000,                # 부스팅 반복 횟수 (1000번 반복 학습)
    learning_rate=0.1,              # 학습률 (0.1로 설정, 낮은 값일수록 안정적 학습)
    depth=6,                        # 트리의 깊이 (6으로 설정, 깊이가 클수록 모델 복잡성 증가)
    cat_features=['categorical_column1', 'categorical_column2'],  # 범주형 특성 목록
    l2_leaf_reg=3,                  # L2 정규화 파라미터 (3으로 설정, 과적합 방지)
    bagging_temperature=1,          # 배깅 온도 (1로 설정, 무작위 샘플링에 영향을 미침)
    eval_metric='AUC',              # 평가 메트릭 (AUC 사용, 모델 성능 평가)
    early_stopping_rounds=50,       # 조기 종료 기준 (50번 반복 동안 개선이 없을 경우 종료)
    verbose=100                     # 진행 상황 출력 (100번마다 훈련 상태 출력)
)
