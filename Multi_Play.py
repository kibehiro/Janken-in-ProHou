import numpy as np

import MakeProbability

JankenHand = ['グー', 'チョキ', 'パー']  # じゃんけんの手は0がグー　1がチョキ　2がパー

PlayerSu = 2  # プレイヤー数の設定
JankenKaisu = 100  # じゃんけんする回数

PlayerProbability = [[1] * 3] * PlayerSu  # プレイヤーがその手を出す確率 1を入れてるのは、確率を変えない人用
PlayerWinCount = [[]] * PlayerSu  # プレイヤーごとの勝数を設定
PlayerHand = [0] * PlayerSu  # プレイヤーが出す手
RecordWin = [0] * 3
Aiko = 0

StrongPlayerFlag = True

# 確率の設定
# PlayerProbability[0] = [1, 1, 1]  # ぐーちょきぱーの順番で確率を指定
# PlayerProbability[1] = [1, 1, 5]


for i in range(PlayerSu):
    PlayerProbability[i] = MakeProbability.makeprobability(PlayerProbability[i])
    PlayerWinCount[i] = [0, 0, 0]  # プレイヤーごとの勝数を初期化(ここで初期化してるのはPythonの2次元配列の特性による)

# np.random.seed(seed=38328)  # 再現性が必要なら数字を入れる

for i in range(JankenKaisu):
    for j in range(PlayerSu):
        PlayerHand[j] = np.random.choice(len(JankenHand), p=PlayerProbability[j])
    te = list(set(PlayerHand))
    if len(te) == 1 or len(te) == 3:
        Aiko += 1
    else:
        # 勝敗判定
        if (te[0] == 0 and te[1] == 1) or (te[1] == 0 and te[0] == 1):  # グーが勝ち
            WinHand = 0
            LoseHand = 1
            RecordWin[0] += 1
        elif (te[0] == 1 and te[1] == 2) or (te[1] == 1 and te[0] == 2):  # チョキが勝ち
            WinHand = 1
            LoseHand = 2
            RecordWin[1] += 1
        elif (te[0] == 2 and te[1] == 0) or (te[1] == 2 and te[0] == 0):  # パーが勝ち
            WinHand = 2
            LoseHand = 0
            RecordWin[2] += 1

        if StrongPlayerFlag and PlayerSu > 2:
            PlayerHand[0] = WinHand

        # PlayerHandからその手を持つ添字（プレイヤー番号）をもってきて、WinCountにいれる
        # ここで、teはsetで順番が変わるが、PlayerHandはプレイヤーの手を保持している
        # PlayerHand[プレイヤー番号]に出した手が収納されている
        for k in range(PlayerSu):
            if PlayerHand[k] == WinHand:
                PlayerWinCount[k][WinHand] += 1
                # PlayerWinCountは、[プレイヤー番号][出した手]になっていて、勝利数が入る
                # PlayerWinCount[0][1]なら、プレイヤー1のちょきで勝った数が入る

for i in range(PlayerSu):
    print('Player', i + 1,  sum(PlayerWinCount[i]), '勝　グー', PlayerWinCount[i][0], '勝　チョキ',
          PlayerWinCount[i][1], '勝　パー', PlayerWinCount[i][2], '勝')

print(PlayerSu, '人　グー　チョキ　パー　引分')
print('勝敗　', RecordWin[0], '回', RecordWin[1], '回', RecordWin[2], '回', Aiko, '回')
