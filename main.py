import json


class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        print(f"\n문제: {self.question}")
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["question"], data["choices"], data["answer"])


class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.load_state()

    def load_default_quizzes(self):
        self.quizzes = [
            Quiz(
                "Python에서 리스트의 길이를 구하는 함수는?",
                ["size()", "length()", "len()", "count()"],
                3
            ),
            Quiz(
                "Python에서 문자열을 정수로 변환하는 함수는?",
                ["str()", "int()", "float()", "input()"],
                2
            ),
            Quiz(
                "Python에서 반복문에 사용하는 키워드는?",
                ["if", "for", "def", "class"],
                2
            )
        ]

    def load_state(self):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            self.best_score = data.get("best_score", 0)
            self.quizzes = [
                Quiz.from_dict(quiz_data)
                for quiz_data in data.get("quizzes", [])
            ]

            if not self.quizzes:
                self.load_default_quizzes()
                self.save_state()

        except (FileNotFoundError, json.JSONDecodeError):
            self.best_score = 0
            self.load_default_quizzes()
            self.save_state()

    def save_state(self):
        data = {
            "best_score": self.best_score,
            "quizzes": [quiz.to_dict() for quiz in self.quizzes]
        }

        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def show_menu(self):
        print("\n===== 퀴즈 게임 =====")
        print("1. 퀴즈 시작")
        print("2. 퀴즈 목록 보기")
        print("0. 종료")

    def show_quizzes(self):
        print("\n[퀴즈 목록]")
        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"{index}. {quiz.question}")

    def play_quiz(self):
        print("\n퀴즈 시작!")
        print("아직 상세 로직은 다음 단계에서 구현합니다.")

    def run(self):
        while True:
            self.show_menu()
            choice = input("메뉴를 선택하세요: ")

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.show_quizzes()
            elif choice == "0":
                print("게임을 종료합니다.")
                break
            else:
                print("올바른 메뉴 번호를 입력하세요.")


if __name__ == "__main__":
    game = QuizGame()
    game.run()