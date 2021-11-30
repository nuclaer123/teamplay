import time as t
import random as r

Dice_list=[]
Dice_last_list=[0,0,0,0,0,0,0,0,0,0,0,0,0]
dice_class=0
check_list=[0,0,0,0,0,0,0,0,0,0,0,0,0]
st = 0
def setdice():
    return r.randrange(1,7)

def rolling_dice():
    global dice_class
    if dice_class<=2:
        print("주사위 굴리기를 시작하겠습니다")
        t.sleep(0.5)
        while True:
            num=setdice()
            Dice_list.append(num)
            if len(Dice_list)>=5:
                break
        print(Dice_list)
        dice_class+=1
        if dice_class<=2:
            check=input('주사위를 변경 하시겠습니까?(Y/N)').lower()
            if check=='y':
                Dice_select1()
            elif check=='n':
                Dice_checking()
            else:
                print("잘못입력하셨습니다 게임을 종료합니다")
                return
        else:
            print("더이상 돌릴 수 없습니다")
            Dice_checking()
    else:
        print("더이상 돌릴 수 없습니다")
        Dice_checking()

def Dice_select1():
    global dice_class,st
    a=int(input("다시 굴릴 주사위의 순번을 선택한 후 엔터를 눌러 주세요. \n전부 다시돌리려면 -1을 입력하세요\n다 고르셨다면 0을 입력하세요"))
    if a>=6:
        print("다시 선택해 주세요")
        Dice_select1()
    elif a==0:
        if st == 0:
            return Dice_checking()
        dice_class += 1
        for i in range(len(Dice_list)):
            if Dice_list[i] == 0:
                Dice_list[i] = setdice()
        print(Dice_list)
        if dice_class < 3:
            Dice_select1()
        else:
            Dice_checking()
    elif a==-1:
        print("주사위를 다시 굴립니다")
        del Dice_list[:6]
        rolling_dice()
    else:
        b=Dice_list[a-1]
        Dice_list[a-1]=0
        print("고정된 주사위",Dice_list)
        st = 1
        Dice_select1()

def ace(choice):
    sum1 = 0
    if check_list[choice-1] == 1:
        print("이미 선택한 족보입니다.")
        Dice_checking()
    else:
        for i in range(len(Dice_list)):
            if Dice_list[i] == choice:
                sum1 += choice
        Dice_last_list[choice-1] = sum1
        check_list[choice-1] = 1
    if (check_list[:5] == [1, 1,1, 1, 1]) and (sum(Dice_last_list[:5]))>=63:
        Dice_last_list[12] = 35

def Dice_checking():
    global dice_class
    msum = 0
    dice_class=0
    ug = 0
    if check_list==[1,1,1,1,1,1,1,1,1,1,1,1,1]:
        sumscore() 
    else:
        Dice_list.sort()
        scoreprint()
        check=int(input('현재 점수는 다음과 같습니다. 어느 족보에 입력할까요? 번호를 입력해주세요'))
        if check in range(1,7):
            if check_list[check-1] == 1:
                print("\n해당칸에 넣을 수 없습니다\n")
                Dice_checking()
            dice_class=0
            ace(check)
            scoreprint()
            ug = 0
            del Dice_list[:6]
            rolling_dice()
                
        elif check==7:
            if check_list[check-1] == 1:
                print("\n해당칸에 넣을 수 없습니다\n")
                Dice_checking()
            check_list[check-1] = 1
            for i in Dice_list:
                msum += i
            Dice_last_list[check-1] = msum
            ug = 0
            scoreprint()
            del Dice_list[:6]
            rolling_dice()

        elif check==8:
            if check_list[check-1] == 1:
                print("\n해당칸에 넣을 수 없습니다\n")
                Dice_checking()
            check_list[check-1] = 1
            if Dice_list[0]==Dice_list[3] or Dice_list[1]==Dice_list[4]:
                for i in len(Dice_list):
                    msum+=i
                Dice_last_list[check-1]=msum
                ug = 0
                scoreprint()
                del Dice_list[:6]
                rolling_dice()
            else:
                print("\n해당칸에 넣을 수 없습니다\n")
                ug = 1
                check_list[check-1] =0
                Dice_checking()

        elif check==9:
            if check_list[check-1] == 1:
                print("\n해당칸에 넣을 수 없습니다\n")
                Dice_checking()
            check_list[check-1] = 1
            if Dice_list[0]==Dice_list[2] and Dice_list[3]==Dice_list[4] and Dice_list[2]!=Dice_list[3]:
                for i in Dice_list:
                    msum+=i
                Dice_last_list[check-1]=msum
                scoreprint()
                del Dice_list[:6]
                rolling_dice()
            elif Dice_list[0]==Dice_list[1] and Dice_list[2]==Dice_list[4] and Dice_list[1]!=Dice_list[2]:
                for i in Dice_list:
                    msum+=i
                Dice_last_list[check-1]=msum
                scoreprint()
                del Dice_list[:6]
                rolling_dice()
            else:
                print("\n해당칸에 넣을 수 없습니다\n")
                check_list[check-1] = 0
                Dice_checking()

        elif check==10:
            if check_list[check-1] == 1:
                print("\n해당칸에 넣을 수 없습니다\n")
                Dice_checking()
            check_list[check-1] = 1
            few_dice=[]
            ch=0
            
            for  i in range(len(Dice_list)-1):
                if Dice_list[i]!=Dice_list[i+1]:
                    few_dice.append(Dice_list[i])
            few_dice.append(Dice_list[4])
            for i in range(len(few_dice)-1):
                if few_dice[i]+1==few_dice[i+1]:
                    ch+=1
                else:
                    ch+=0
            if ch>=3:
                Dice_last_list[check-1]=15
                scoreprint()
                del Dice_list[:6]
                rolling_dice()
            else:
                print("\n해당칸에 넣을 수 없습니다\n")
                check_list[check-1] = 0
                Dice_checking()

        elif check==11:
            if check_list[check-1] == 1:
                print("\n해당칸에 넣을 수 없습니다\n")
                Dice_checking()
            check_list[check-1] = 1
            few_dice=[]
            ch=0
               
            for  i in range(len(Dice_list)-1):
                if Dice_list[i]!=Dice_list[i+1]:
                    few_dice.append(Dice_list[i])
            few_dice.append(Dice_list[4])
            for i in range(len(few_dice)-1):
                if few_dice[i]+1==few_dice[i+1]:
                    ch+=1
                else:
                    ch+=0
            if ch==4:
                Dice_last_list[check-1]=30
                
                scoreprint()
                del Dice_list[:6]
                rolling_dice()
            else:
                print("\n해당칸에 넣을 수 없습니다\n")
                check_list[check-1] = 0
                Dice_checking()

        elif check==12:
            check_list[check-1] =1
            if Dice_list == [Dice_list[0],Dice_list[0],Dice_list[0],Dice_list[0],Dice_list[0]]:
                Dice_last_list[check-1]=50
                dice_class=0
            else:
                ug = 1
        if ug == 0:
            scoreprint()
            del Dice_list[:6]
            rolling_dice()
        else:
            print("족보와 맞지 않습니다.")
            Dice_checking()
            

def scoreprint():
    rule = ["1.Ace :","2.Deuces :","3.Threes :","4.Fours :","5.Fives :","6.Sixes :","7.Choice :","8.4 of a kind :","9.Full House :","10.S. Straight :","11.L.Straight :","12.Yacht :"]
    for i in range(0,12):
        print(rule[i],Dice_last_list[i])

def sumscore():
    msum=0
    for i in range(14):
        msum+=Dice_last_list[i]
    print('최종점수는',msum,'점입니다.')

    
rolling_dice()
