## 블랙잭
# 딜러와 1:1인 상황 가정
# 카드가 무제한
# 배팅금액은 100
# 올인이되거나 종료하고싶을때 종료

## 과정
# 딜러,플레이어 카드 2장씩 받고 플레이어 2장 오픈 딜러 1장 오픈
# 플레이어 카드 받기 말기 결정 -> 플레이어 카드의 점수 구하기
# 딜러 17 이상까지 카드 받기 -> 딜러 카드의 점수 구하기
# 결과 확인

# 초기세팅
money = 100
playerCards = []
dealerCards = []

# 배팅
# 함수화 시키기
def 배팅():
    while True:
        betting = int(input("배팅 금액 입력 : "))
        if betting > money:
            print("보유자금보다 배팅금액이 큽니다")
        else:
            break
    return betting


# 카드받기
# 1~10중 하나 뽑기
import random
def 카드받기():
    for i in range(2):
        card = random.randrange(1, 11)
        playerCards.append(card)
        card = random.randrange(1, 11)
        dealerCards.append(card)
    print("플레이어의 카드 : ", playerCards)    
    print("딜러 카드 1장 오픈 : ", dealerCards[0])




# 플레이어 카드 받기 결정

def 카드받기결정():
    while True:
        receive = input("카드를 받으시겠습니까?(y/n) : ")
        if receive == "y":
            card = random.randrange(1, 11)
            playerCards.append(card)
            print("플레이어의 카드 : ", playerCards)
            # 21을 넘었을 경우 ==> 1 == 1
            sumPlayerCards = sum(playerCards)
            if sumPlayerCards > 21:
                print("21을 초과하였습니다(버스트)")
                break
        elif receive == "n":
            sumPlayerCards = sum(playerCards)
            break    
    print("플레이어의 카드 : ", playerCards)
    # 딜러 카드 오픈
    print("딜러의 카드 : ", dealerCards)
    sumPlayerCards = sum(playerCards)

    return sumPlayerCards #우리가 알고싶은 플레이어 카드의 총합


# 딜러 카드 받기
# 17이상이 될때까지 계속 받기
def 딜러카드받기():
    sumDealerCards = sum(dealerCards)
    while sumDealerCards < 17:
        card = random.randrange(1, 11)
        dealerCards.append(card)
        print("딜러의 카드 : ", dealerCards)
        sumDealerCards = sum(dealerCards)
        # 21을 넘었을 경우 ==> 1 == 1
        if sumDealerCards > 21:
            print("21을 초과하였습니다(버스트)")
            break
    print("딜러의 카드 : ", dealerCards)
    return sumDealerCards #우리가 알고싶은 딜러 카드의 총합


# 결과
def 결과(sumPlayerCards, sumDealerCards):
    if 1 in playerCards and sumPlayerCards < 12:
        sumPlayerCards += 10
    print("플레이어 카드 총합 : ", sumPlayerCards)
    print("딜    러 카드 총합 : ", sumDealerCards)
    # case1 : 둘다 bust가 아닌경우
    if sumPlayerCards < 22 and sumDealerCards < 22:
        if sumPlayerCards > sumDealerCards:
            print("플레이어가 승리했습니다")
        elif sumPlayerCards < sumDealerCards:
            print("딜러가 승리했습니다")
        else:
            print("비겼습니다")
    # case2 : 둘다 버스트
    elif sumPlayerCards > 21 and sumDealerCards > 21:
        print("플레이어 딜러 모두 버스트 입니다")

    # case3 : 어느 한쪽이 버스트
    else:
        if sumPlayerCards > 21:
            print("딜러가 승리하였습니다")
        else:
            print("플레이어가 승리하였습니다")

# 함수 사용하기
def 게임():
    while True:
        playerCards = []
        dealerCards = []
        if money <= 0:
            print("배팅금액이 없습니다")
            break
        betting = 배팅()
        카드받기()
        플레이어_카드_총합 = 카드받기결정()
        딜러_카드_총합 = 딜러카드받기()
        결과(플레이어_카드_총합, 딜러_카드_총합)

게임()
