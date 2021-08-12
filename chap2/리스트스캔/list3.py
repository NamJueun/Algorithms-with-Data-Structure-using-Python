## 리스트 스캔 3 : list3.py와 같지만 1부터 카운트를 시작합니다.
# 리스트의 모든 원소를 enumerate() 함수로 스캔하기(1부터 카운트)

x = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x,1):
    print(f'x[{i}] = {name}')
