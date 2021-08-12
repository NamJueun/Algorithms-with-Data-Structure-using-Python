##### max.py의 모듈 max로 정의된 max_of() 함수를 다른 프로그램에서 호출
## 배열의 원소 수, 최댓값, 최솟값은 입력받고, 최댓값과 최솟값 안에서 배열을 구성하는 원솟값은 난수로 결정하는 프로그램.
# 배열 원소의 최댓값을 구해서 출력하기(원솟값을 난수로 생성)

import random
from max import max_of

print('난수의 최댓값을 구합니다.')
num = int(input('난수의 개수를 입력하세요.: '))
lo = int(input('난수의 최솟값을 입력하세요.: '))
hi = int(input('난수의 최댓값을 입력하세요.: '))
x = [None] * num            #원소 수가 num인 리스트를 생성

for i in range(num):
    x[i] = random.randint(lo,hi) # lo 이상 hi 이하인 정수 난수를 반환

print(f'{(x)}')
print(f'이 가운데 최댓값은 {max_of(x)}입니다.')
