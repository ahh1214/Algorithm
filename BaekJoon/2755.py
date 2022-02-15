N = int(input())
scores = {
    'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
    'F': 0.0
}

result = 0.0
total_credit = 0
for _ in range(N):
    data = input().split()
    credit = int(data[1])
    total_credit += credit
    grade = data[2]
    result += credit * scores[grade]
result /= total_credit

result = int(result * 1000)
if result % 10 >= 5:
    result += 10
    result -= result % 10
result /= 1000

print(f'{result:.2f}') #소수점 둘째자리까지 출력