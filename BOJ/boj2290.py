# 문제
# 지민이는 새로운 컴퓨터를 샀다. 하지만 새로운 컴퓨터에 사은품으로 온 LC-디스플레이
# 모니터가 잘 안나오는 것이다. 지민이의 친한 친구인 지환이는 지민이의 새로운
# 모니터를 위해 테스트 할 수 있는 프로그램을 만들기로 하였다.
#
# 입력
# 첫째 줄에 두 개의 정수 s와 n이 들어온다. (1 ≤ s ≤ 10, 0 ≤ n ≤ 9,999,999,999)
# 이다. n은 LCD 모니터에 나타내야 할 수 이며, s는 크기이다.
#
# 출력
# 길이가 s인 '-'와 '|'를 이용해서 출력해야 한다. 각 숫자는 모두 s+2의 가로와
# 2s+3의 세로로 이루어 진다. 나머지는 공백으로 채워야 한다. 각 숫자의 사이에는
# 공백이 한 칸 있어야 한다.
#
# 예제 입력 1
# 2 1234567890
# 예제 출력 1
#       --   --        --   --   --   --   --   --
#    |    |    | |  | |    |       | |  | |  | |  |
#    |    |    | |  | |    |       | |  | |  | |  |
#       --   --   --   --   --        --   --
#    | |       |    |    | |  |    | |  |    | |  |
#    | |       |    |    | |  |    | |  |    | |  |
#       --   --        --   --        --   --   --



s, n = input().split(' ')
sint = int(s)
nint = int(n)

for h in range(sint*2+3):
    for i in range(len(n)):
        # 상
        if h == 0:
            if n[i] == '1' or n[i] == '4':
                for _ in range(sint+2):
                    print(' ',end='')
            else:
                print(' ', end='')
                for _ in range(sint):
                    print('-',end='')
                print(' ', end='')
            print(' ', end='')

        # 좌상, 우상
        elif h >= 1 and h <= sint:
            if n[i] == '0' or n[i] == '4' or n[i] == '8' or n[i] == '9':
                print('|', end='')
                for _ in range(sint):
                    print(' ', end='')
                print('|', end='')

            elif n[i] == '1' or n[i] == '2' or n[i] == '3' or n[i] == '7':
                for _ in range(sint + 1):
                    print(' ', end='')
                print('|', end='')
            else:
                print('|', end='')
                for _ in range(sint + 1):
                    print(' ', end='')
            print(' ', end='')

        # 중
        elif h == (sint+1):
            if n[i] == '0' or n[i] == '1' or n[i] == '7':
                for _ in range(sint + 2):
                    print(' ', end='')
            else:
                print(' ', end='')
                for _ in range(sint):
                    print('-', end='')
                print(' ', end='')
            print(' ', end='')

        # 좌하, 우하
        elif h >= (sint+2) and h <= (2*sint+1):
            if n[i] == '2':
                print('|', end='')
                for _ in range(sint+1):
                    print(' ', end='')

            elif n[i] == '0' or n[i] == '6' or n[i] == '8':
                print('|', end='')
                for _ in range(sint):
                    print(' ', end='')
                print('|', end='')
            else:
                for _ in range(sint+1):
                    print(' ', end='')
                print('|', end='')
            print(' ', end='')

        # 하
        elif h == (2*sint+2):
            if n[i] == '1' or n[i] == '4' or n[i] == '7':
                for _ in range(sint + 2):
                    print(' ', end='')
            else:
                print(' ', end='')
                for _ in range(sint):
                    print('-', end='')
                print(' ', end='')
            print(' ', end='')
    print()













