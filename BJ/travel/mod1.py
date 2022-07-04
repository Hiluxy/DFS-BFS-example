n,m =map(int,input().split())

#n*m을 0으로 초기화
d=[[0]*m for _ in range(n)]

x,y,direction=map(int,input().split())
d[x][y]=1 #현재 좌표 방문 처리

#맵 정보 입력 받기
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))

#북(0) 동(1) 남(2) 서(3)
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

#왼쪽으로 회전
def left():
    global direction
    direction -=1
    if direction ==-1:
        direction=3

#시뮬레이션 시작
cnt=1
turn_cnt=0
while True:
    #회전
    left()
    nx=x+dx[direction]
    ny=y+dy[direction]
    #가보지 않은 칸이 존재하면 이동
    if d[nx][ny]==0 and a[nx][ny]==0:
        d[nx][ny]=1
        x=nx
        y=ny
        cnt+=1
        turn_cnt=0
        continue
    #가봤던 곳이나 바다인 경우
    else:
        turn_cnt +=1
    #네 방향 모두 갈 수 없음->뒤로 한칸 이동
    if turn_cnt==4:
        nx=x-dx[direction]
        ny=y-dy[direction]
        #뒤가 0
        if a[nx][ny]==0:
            x=nx
            y=ny
        #뒤가 1
        else:
            break
        turn_cnt=0

print(cnt)