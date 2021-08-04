## 리스트 스캔 2 : 인덱스와 원소를 짝지어 enumerate() 함수로 반복해서 꺼냅니다.
# 리스트의 모든 원소를 enumerate() 함수로 스캔 ➞ enumerate() 함수는 인덱스와 원소를 짝지어 튜플로 꺼내는 내장 함수

x = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x):
    print(f'x[{i}] = {name}')

