day = 0
m_day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_list = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
 
x, y = map(int,input().split())
 
for i in range(x-1):
    day = day + m_day_list[i]
day = (day + y) % 7
 
print(week_list[day])