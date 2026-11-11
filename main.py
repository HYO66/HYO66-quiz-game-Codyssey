print("=== 퀴즈 게임 ===")
print("1. 퀴즈 시작")
print("2. 종료")

choice = input("메뉴를 선택하세요: ")

if choice == "1":
    print("퀴즈를 시작합니다.")
    print("문제: Python에서 출력할 때 사용하는 함수는?")
    print("1. input")
    print("2. print")
    print("3. int")

    answer = input("정답 번호를 입력하세요: ")

    if answer == "2":
        print("정답입니다!")
    else:
        print("틀렸습니다.")
elif choice == "2":
    print("프로그램을 종료합니다.")
else:
    print("올바른 번호를 입력해주세요.")