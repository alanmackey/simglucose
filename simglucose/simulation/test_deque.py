from collections import deque

que_size = 20
cgm = deque([0]*que_size,maxlen=que_size)

print(cgm)

for _ in range(22):
    cgm.append(1)
    print(cgm)