# 포도주 시식
# 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야하고,
# 마신 후에는 원래 위치에 다시 놓아야한다.
# 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.

N = int(input())    # 포도주 잔의 개수

for i in range(N):
    graph_juice = []
