import sys

ip, op = sys.stdin, sys.stdout



"""
n(2~20만), m(1~20만), x(1~10억)
연산반복: 반드시 정점N에 도달함
i번째 ui->vi, 방향성이 있다
처음 정점1
이동(비용1): v->u
모든 간선방향뒤집기(비용X) => flag
뒤집기 => flag로 
가는데 필요한 최소의 비용
bfs로
1 -> N으로 가는데 
뒤집고 가는비용 1+x

최소비용 => 
1 -> N으로 갈때 

"""