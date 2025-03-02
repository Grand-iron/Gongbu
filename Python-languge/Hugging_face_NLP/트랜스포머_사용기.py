from transformers import pipeline


# 확인 = pipeline("sentiment-analysis")

#작동체크
# print(확인("your best in the world"))

#한글로 되는지 확인 
#print(확인("너는 최악이야"))
#결과값 [{'label': 'POSITIVE', 'score': 0.6958497762680054}] 어림도 없음

# 종류
# feature-extraction : 특징 추출 (텍스트에 대한 벡터 표현 추출)
# fill-mask : 마스크 채우기
# ner : 개체명 인식 (named entity recognition)
# question-answering : 질의 응답
# sentiment-analysis : 감정 분석
# summarization : 요약
# text-generation : 텍스트 생성
# translation : 번역
# zero-shot-classification : 제로샷 분류

#텍스트 생성 실험
# gen=pipeline("text-generation")

#예상 답안 John Cena is Greatest Of all time 이걸 할려나?
# print(gen("John Cena is Greatest Of",max_length=35))
#결과값 'John Cena is Greatest Of All Time, and he didn\'t want the WWE to be the next WWE.\n\nWhat happened next was a bit surprising. "The WWE got'} 
#max_length가 토큰단위라 변수가 발생 

#마스크 채우기 실험
# mask = pipeline('fill-mask')

#예상 답안 John Cena is Greatest Of all time
# print(mask("John Cena is <mask> Of ALL time",top_k=2))
#결과값 John Cena is Greatest Of ALL time , John Cena is Best Of ALL time


