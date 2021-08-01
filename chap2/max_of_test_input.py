##### max.py의 모듈 max로 정의된 max_of() 함수를 다른 프로그램에서 호출
## 입력받을 때 원소 수를 결정하기
## int형 정숫값을 차례로 입력받아가 End를 입력하면 더 이상 입력받지 않으며 그 시점에서 원소 수를 확정하는 프로그램.

from max import max_of # max_of() 함수 임포트

print('배열의 최댓값을 구합니다.')
print('주의: "End"를 입력하면 종료합니다.')

number = 0
x = []             #빈 리스트

while True:
  s = input(f'x[{number}]값을 입력하세요.: ')
  if s == 'End':
    break
  x.append(int(s)) # 배열의 맨 끝에 추가
  number += 1

print(f'{number}개를 입력했습니다.')
print(f'최댓값은 {max_of(x)}입니다.')
