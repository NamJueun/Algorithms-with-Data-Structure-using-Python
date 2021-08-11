## 다양한 자료형인 시퀀스에서 검색: ssearch_while.py에서 작성한 seq_search() 함수는 임의의 자료형인 시퀀스에서 검색할 수 있다.
# seq_search() 함수를 사용하여 실수 검색하기

from ssearch_while import seq_search

print('실수를 검색합니다.')
print('주의: "End"를 입력하면 종료합니다.')

number = 0
x = []                      # 빈 리스트 x를 생성

while True:
    s = input(f'x[{number}]: ')
    if s == 'End':
        break
    x.append(float(s))      # 배열 맨 끝에 원소를 추가
    number += 1

ky = float(input('검색할 값을 입력하세요.: '))    # 검색할 키 ky를 입력받기
idx = seq_search(x,ky)                           # ky와 같이 같은 원소를 x에서 검색

if idx == -1:
    print('검색값을 같는 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 x[{idx}]에 있습니다.')
