## 배열 원소를 역순으로 정렬하기
#뮤터블 시퀀스 원소를 역순으로 정렬

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    """뮤터블 시퀀스 a의 원소를 역순으로 정렬"""
    n = len(a)
    for i in range(n//2): ## 교환 획수는 원소 수 // 2번. // 기호를 사용하여 나누기 연산을 한 후 소수점 이하는 버림.
                          ## 원소 수가 홀수인 경우에는 가운데 원소는 교환할 필요 없음
        a[i],a[n-i-1] = a[n-i-1],a[i]

if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요.: '))
    x = [None] * nx         # 원소 수가 nx인 리스트를 생성

    for i in range(nx):
        x[i] = int(input(f'x[{i}]값을 입력하세요.: '))

    reverse_array(x)       # x를 역순으로 정렬

    print('배열 원소를 역순으로 정렬했습니다.')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')
