from sklearn.svm import SVC

# SVC 모델 초기화
model = SVC(
    C=1.0,                          # 정규화 매개변수 (1.0으로 설정, 값이 클수록 과적합 가능성 증가)
    kernel='rbf',                   # 커널 유형 ('linear', 'poly', 'rbf', 'sigmoid' 등)
    degree=3,                       # 다항식 커널의 차수 (기본값 3, 'poly' 커널을 사용할 때만 해당)
    gamma='scale',                  # 커널 계수 (기본값 'scale', 'rbf', 'poly', 'sigmoid' 커널에서 사용)
    coef0=0.0,                      # 커널 함수의 상수 항 (다항식 및 시그모이드 커널에서 사용)
    shrinking=True,                 # 수축 여부 (True로 설정하면 수축 기법 사용)
    probability=False,              # 확률 추정 여부 (True로 설정하면 확률 출력을 위한 추가 훈련 수행)
    tol=1e-3,                       # 수렴 허용 오차 (기본값 1e-3, 더 작은 값일수록 수렴 기준 엄격)
    max_iter=-1,                   # 최대 반복 횟수 (-1로 설정하면 제한 없음)
    class_weight=None,              # 클래스 가중치 (None으로 설정하면 모든 클래스에 동일한 가중치 부여)
    verbose=False                   # 진행 상황 출력 여부 (True로 설정하면 훈련 상태 출력)
)