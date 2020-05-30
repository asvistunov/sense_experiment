from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
from .widgets import LikertWidget

author = 'Alexander Svistunov'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'survey_sens'
    players_per_group = 2
    num_rounds = 1

    endowment = c(100)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        max=c(100),
        min=c(0),
        label="Сколько вы хотите отправить игроку 2?"
    )

    expected_sender = models.CurrencyField(
        max=c(100),
        min=c(0),
        label=""
    )

    expected_receiver = models.CurrencyField(
        max=c(100),
        min=c(0),
        label=""
    )

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.endowment - self.sent_amount
        p2.payoff = self.sent_amount


class Player(BasePlayer):

    def other(self):
        return self.get_others_in_group()[0]

    age = models.IntegerField(
        min=0,
        label="Укажите Ваш возраст:"
    )
    sex = models.IntegerField(
        label="Укажите Ваш пол",
        choices=[
            [0, 'Мужской'],
            [1, 'Женский'],
        ],
        widget=widgets.RadioSelect
    )
    religion = models.IntegerField(
        label="Какую религию Вы исповедуете?",
        choices=[
            [1, 'Не исповедую никакой религии (атеист)'],
            [2, 'Католицизм'],
            [3, 'Протестантизм'],
            [4, 'Православие'],
            [5, 'Иудаизм'],
            [6, 'Ислам'],
            [7, 'Индуизм'],
            [8, 'Буддизм'],
            [9, 'Другую религию']
        ],
        widget=widgets.RadioSelect
    )

    education = models.IntegerField(
        label="Какой у Вас самый высокий уровень образования, по которому Вы получили аттестат, свидетельство, диплом?",
        choices=[
            [1, 'Средняя школа'],
            [2, 'Среднее профессиональное образование'],
            [3, 'Незаконченное высшее образование'],
            [4, 'Высшее образование'],
            [5, 'Два и более диплома / Ученая степень'],
        ],
        widget=widgets.RadioSelect
    )

    occupation = models.IntegerField(
        label="В настоящее время вы трудоустроены?",
        choices=[
            [0, 'Нет'],
            [1, 'Да']
        ],
        widget=widgets.RadioSelect,
    )

    # relative_income = models.IntegerField(
    #     label="Ваш средний ежемесячный доход?",
    #     choices=[
    #         [1, '...ниже, чем в среднем в вашем городе'],
    #         [2, '...такой же, как в среднем в вашем городе'],
    #         [3, '...выше, чем в среднем в вашем городе'],
    #         [4, 'Затрудняюсь ответить'],
    #     ],
    #     widget=widgets.RadioSelect
    # )

    relative_income_2 = models.IntegerField(
        label='Какое высказывание наиболее точно описывает финансовое положение вашей семьи?',
        choices=[
            [1, 'Не хватает денег даже на еду'],
            [2, 'Хватает на еду, но не хватает на покупку одежды и обуви'],
            [3, 'Хватает на одежду и обувь, но не хватает на покупку мелкой бытовой техники'],
            [4,
             'Хватает денег на небольшие покупки, но покупка дорогих вещей (компьютера, стиральной машины, холодильника) требует накоплений или кредита'],
            [5,
             'Хватает денег на покупки для дома, но на покупку машины, дачи, квартиры необходимо копить или брать кредит'],
            [6, 'Можем позволить себе любые покупки без ограничений и кредитов']
        ],
        widget=widgets.RadioSelect,
    )

    trust = models.IntegerField(
        label="Как Вы считаете, в целом большинству людей можно доверять, или же при общении с другими людьми "
              "осторожность никогда не повредит?",
        choices=[
            [0, 'Нужно быть очень осторожным с другими людьми'],
            [1, 'Большинству людей можно вполне доверять'],
        ],
        widget=widgets.RadioSelect,
    )

    marital_status = models.IntegerField(
        label="Ваш семейный статус",
        choices=[
            [1, 'Не женаты/не замужем'],
            [2, 'Женаты/замужем'],
            [3, 'В отношениях, но официально не состоите в браке'],
            [4, 'Разведены'],
            [5, 'Живете отдельно от супруга/и'],
            [6, 'Вдовец/Вдова'],
            [7, 'Затрудняюст ответить'],
        ],
        widget=widgets.RadioSelect,
    )

    happy = models.IntegerField(
        label="В целом я могу сказать, что я",
        choices=[
            [0, 'Несчастливый человек'],
            [1, 'Счастливый человек']
        ],
        widget=widgets.RadioSelect,
    )

    satisfaction = models.IntegerField(
        label='',
        choices=range(1,11),
        widget=LikertWidget(
            quote="Учитывая все обстоятельства, насколько Вы удовлетворены вашей жизнью в целом в эти дни?",
            label="Для ответа выберите значение на шкале от 0 до 10, где 0 - Cовершенно не удовлетворен, а 10 -  Полностью удовлетворен:",
            left="Cовершенно не удовлетворен",
            right="Полностью удовлетворен"
        )

    )

    homosexuality_attitude = models.IntegerField(
        label="",
        choices=range(1, 11),
        widget=LikertWidget(
            quote="Укажите, как вы относитесь к людям гомосексуальной ориентации, геям, лесбиянкам?",
            label="Для ответа выберите значение на шкале от 0 до 10, где 0 - Отрицательно, а 10 - Положительно:",
            left="Отрицательно",
            right="Положительно",
            html_class='bg-primary text-white'
        )
    )

    average_choice_homosexuality = models.IntegerField(
        label="",
        choices=range(1, 11),
        widget=LikertWidget(
            quote="Укажите, как вы думаете, в среднем участники этого исследования будут отвечать на этот вопрос?",
            label="Для ответа выберите значение на шкале от 0 до 10, где 0 - Отрицательно, а 10 - Положительно:",
            left="Отрицательно",
            right="Положительно",

        )
    )
    gender_roles_attitude = models.IntegerField(
        label="",
        choices=range(1, 11),
        widget=LikertWidget(
            quote="Укажите, насколько вы согласны с утверждением, что дело мужа — зарабатывать деньги, а дело жены — "
                  "вести домашнее хозяйство и заниматься семьей.",
            label="Для ответа выберите значение на шкале от 0 до 10, где 0 - Полностью не согласен, 10 - Полностью "
                  "Согласен",
            left="Полностью не согласен",
            right="Полностью согласен",
        )
    )

    average_choice_gender_roles = models.IntegerField(
        label="",
        choices=range(1, 11),
        widget=LikertWidget(
            quote="Укажите, как вы думаете, в среднем участники этого исследования будут отвечать на этот вопрос?",
            label="Для ответа выберите значение на шкале от 0 до 10, где 0 - Полностью не согласен, 10 - Полностью "
                  "Согласен",
            left="Полностью не согласен",
            right="Полностью согласен",
        )
    )

    authority_attitude = models.IntegerField(
        label="",
        choices=range(1, 11),
        widget=LikertWidget(
            quote="Укажите, как вы считаете, насколько В. Путин справляется с обязанностями президента",
            label="Для ответа выберите значение на шкале от 0 до 10, где 0 - Плохо, 10 - Хорошо ",
            left="Плохо",
            right="Хорошо",
            html_class='bg-primary text-white'
        )
    )

    average_choice_authority = models.IntegerField(
        label="",
        choices=range(1, 11),
        widget=LikertWidget(
            quote="Укажите, как вы думаете, в среднем участники этого исследования будут отвечать на этот вопрос?",
            label="Для ответа выберите значение на шкале от 0 до 10, где 0 - Плохо, 10 - Хорошо",
            left="Плохо",
            right="Хорошо",
        )
    )
