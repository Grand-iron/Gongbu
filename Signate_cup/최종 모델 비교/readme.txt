최종 모델 구성

하이퍼파라미터 구성 :
    learning_rate=0.1,
    n_estimators=1000,
    max_depth=3,
    min_child_weight=1,
    gamma=0.4,
    subsample=0.67,
    colsample_bytree=0.8,
    reg_alpha=0.1,
    objective='binary:logistic',
    nthread=-1,
    scale_pos_weight=10,

결측치 처리 방식 : 수치형 - KNN Imputer , 범주, 순서형 - SimpleImputer
이상치 처리 : 클리핑 처리 방식
소득 컬럼의 범주화
추가 feature 엔지니어링 작업