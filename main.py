import json

with open("quiz.json", "r", encoding="utf-8") as file:
    quiz_data = json.load(file)

print("=== 퀴즈 게임 ===")
print("1. 퀴즈 시작")
print("2. 종료")

choice = input("메뉴를 선택하세요: ")

if choice == "1":
    print("퀴즈를 시작합니다.")

    quiz = quiz_data[0]
    print("문제:", quiz["question"])

    for i, option in enumerate(quiz["options"], start=1):
        print(f"{i}. {option}")

    answer = input("정답 번호를 입력하세요: ")

    if answer == quiz["answer"]:
        print("정답입니다!")
    else:
        print("틀렸습니다.")
elif choice == "2":
    print("프로그램을 종료합니다.")
else:
    print("올바른 번호를 입력해주세요.")