import sys
import math

A, B, V = map(int, sys.stdin.readline().split())

day = (V-B) / (A-B)  #올라갈 수 있는 기간을 한 번에 계산    
print(math.ceil(day)) #걸리는 시간이 소수점일 경우, 올림