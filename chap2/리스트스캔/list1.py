## 리스트 스캔 1 : 원소 수를 len() 함수로 미리 알아내서  0에서 원소 수 -1까지 반복합니다.
# 리스트의 모든 원소를 스캔하기(원소 수를 미리 파악)

x = ['John', 'George', 'Paul', 'Ringo']

for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')
