from datetime import datetime

import config

EMOJI = {
    'Жених': '🤵🏻‍♂️',
    'Невеста': '👰🏻‍♀️',
    'Оба': '👩‍❤️‍👨',
    'Никто': '❌',

}


class UserAnswers:

    def __init__(self, data: list[str]):
        self.name = data[1]
        self.date = datetime.strptime(data[2], '%d.%m.%Y')
        answers = data[3:] + [''] * (len(config.HEADERS) - len(data[3:]))
        self.answers = {config.HEADERS[i].strip(): answers[i].strip() for i in range(len(config.HEADERS)) if
                        answers[i]}

    def button(self):
        return f'{self.name} ({self.date.strftime('%d/%m/%Y')})'

    def str_answers(self):
        message = self.button() + f' {len(self.answers)} ответов:\n'
        answers = []
        for question, answer in self.answers.items():
            answers.append(f'❔ {question}:\n\t\t{EMOJI[answer]} {answer}')
        message += '\n'.join(answers)
        return message

    def __repr__(self):
        return f'{self.name} ({self.date.strftime('%d/%m/%Y')})'
