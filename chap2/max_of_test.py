##### max.py의 모듈 max로 정의된 max_of() 함수를 다른 프로그램에서 호출
## 각 배열 원소의 최댓값을 구해서 출력하기(튜플, 문자열, 문자열 리스트)

from max import max_of

t = (4, 7, 7.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{t}의 최댓값은 {max_of(t)}입니다.')
print(f'{s}의 최댓값은 {max_of(s)}입니다.') # 가장 큰 문자 코드인 t 출력
print(f'{a}의 최댓값은 {max_of(a)}입니다.') # 사전 순으로 가장 큰 문자열인 FLAC 출력
