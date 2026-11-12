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
        return cls(
            data["question"],
            data["choices"],
            data["answer"]
        )


if __name__ == "__main__":
    sample_quiz = Quiz(
        "Python에서 리스트의 길이를 구하는 함수는?",
        ["size()", "length()", "len()", "count()"],
        3
    )

    sample_quiz.display()
    print("정답 확인:", sample_quiz.check_answer(3))
    print("딕셔너리 변환:", sample_quiz.to_dict())