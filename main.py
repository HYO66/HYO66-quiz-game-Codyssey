import json

def load_quiz_data():
    with open("quiz.json", "r", encoding="utf-8") as file:
        return json.load(file)

def show_menu():
    print("\n=== 퀴즈 게임 ===")
    print("1. 퀴즈 시작")
    print("2. 종료")

def get_valid_answer(quiz):
    while True:
        answer = input("정답 번호를 입력하세요: ")
        if answer.isdigit() and 1 <= int(answer) <= len(quiz["options"]):
            return answer
        else:
            print("보기 번호 중에서 올바르게 입력해주세요.")

def run_quiz():
    print("퀴즈를 시작합니다.")
    quiz_data = load_quiz_data()
    score = 0

    for quiz in quiz_data:
        print()
        print("문제:", quiz["question"])

        for i, option in enumerate(quiz["options"], start=1):
            print(f"{i}. {option}")

        answer = get_valid_answer(quiz)

        if answer == quiz["answer"]:
            print("정답입니다!")
            score += 1
        else:
            correct_index = int(quiz["answer"]) - 1
            correct_option = quiz["options"][correct_index]
            print(f"틀렸습니다. 정답은 {quiz['answer']}번: {correct_option} 입니다.")

    print()
    print(f"총 점수: {len(quiz_data)}문제 중 {score}문제 정답")

def main():
    while True:
        show_menu()
        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            run_quiz()
        elif choice == "2":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 메뉴 번호를 입력해주세요.")

main()