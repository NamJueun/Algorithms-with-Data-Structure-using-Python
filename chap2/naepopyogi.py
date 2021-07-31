## 내포 표기 생성: 리스트 안에서 for, if 문을 사용하여 새로운 리스트를 생성하는 기법.

number = [1,2,3,4,5,6]
twise = [num * 2 for num in numbers if num % 2 = 1] # iterator 로 가져온 num이 홀수값이면 num x 2 함  
print(twise)  # [2,6,10]
