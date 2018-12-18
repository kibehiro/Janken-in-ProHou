import numpy as np

import MakeProbability

JankenHand = ['グー', 'チョキ', 'パー']

PlayerSu = 2
JankenKaisu = 100

Player1 = [1, 1, 1]  # ぐーちょきぱーの順番で確率を指定
Player1WinCount = [0] * 3
Player1 = MakeProbability.makeprobability(Player1)

Player2 = [1, 1, 5]
Player2WinCount = [0] * 3
Player2 = MakeProbability.makeprobability(Player2)

Aiko = [0] * 3

np.random.seed(seed=38328)  # 再現性のためにSeedを固定

for i in range(JankenKaisu):
    print(i + 1, '戦目')
    PlayerHand = []
    Player1Hand = np.random.choice(len(JankenHand), p=Player1)
    Player2Hand = np.random.choice(len(JankenHand), p=Player2)
    print('Player1の手は「', JankenHand[Player1Hand], '」Player2の手は「', JankenHand[Player2Hand], '」')
    if Player1Hand == 0:  # グーの時
        if Player2Hand == 0:
            Aiko[0] += 1
            print('あいこです')
        elif Player2Hand == 1:
            Player1WinCount[0] += 1
            print('Player1が「グー」で勝ちました')
        elif Player2Hand == 2:
            Player2WinCount[2] += 1
            print('Player2が「パー」で勝ちました')
    elif Player1Hand == 1:  # チョキのとき
        if Player2Hand == 0:
            Player2WinCount[0] += 1
            print('Player2が「グー」で勝ちました')
        elif Player2Hand == 1:
            Aiko[1] += 1
            print('あいこです')
        elif Player2Hand == 2:
            Player1WinCount[1] += 1
            print('Player1が「チョキ」で勝ちました')
    elif Player1Hand == 2:  # パーの時
        if Player2Hand == 0:
            Player1WinCount[2] += 1
            print('Player1が「パー」で勝ちました')
        elif Player2Hand == 1:
            Player2WinCount[1] += 1
            print('Player2が「チョキ」で勝ちました')
        elif Player2Hand == 2:
            Aiko[2] += 1
            print('あいこです')
    print('-----------------------')

print('Player1', sum(Player1WinCount), '勝　グー', Player1WinCount[0], '勝　チョキ', Player1WinCount[1], '勝　パー', Player1WinCount[2], '勝')
print('Player2', sum(Player2WinCount), '勝　グー', Player2WinCount[0], '勝　チョキ', Player2WinCount[1], '勝　パー', Player2WinCount[2], '勝')
print('あいこ　グー', Aiko[0], 'チョキ', Aiko[1], 'パー', Aiko[2])

