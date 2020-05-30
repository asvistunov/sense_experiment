from otree.api import Currency as c, currency_range
from ._builtin import WaitPage
from survey_sens.generic_pages import Page
from .models import Constants


class FirstWP(WaitPage):
    group_by_arrival_time = True




class QuestionnaireF(Page):
    form_model = 'player'
    form_fields = ['age',
                   'sex', 'marital_status',
                   'religion',
                   'education',
                   'occupation',
                   'relative_income_2',
                   'trust',
                   'happy',
                   'satisfaction',

                   ]


class QuestionnaireS(Page):
    form_model = 'player'
    form_fields = [
        'homosexuality_attitude',
        'average_choice_homosexuality',
        'gender_roles_attitude',
        'average_choice_gender_roles',
        'authority_attitude',
        'average_choice_authority'
    ]


class IntroGame(Page):
    pass


class GameDescription(Page):
    pass


class BeforeDictator(WaitPage):
    pass


class DictatorSender(Page):
    form_model = 'group'
    form_fields = ['sent_amount']

    def is_displayed(self):
        return self.player.role() == 'dictator'


class DictatorReceiver(Page):
    form_model = 'group'
    form_fields = ['expected_receiver']

    def is_displayed(self):
        return self.player.role() == 'receiver'


class DictatorSenderExpected(Page):
    form_model = 'group'
    form_fields = ['expected_sender']

    def is_displayed(self):
        return self.player.role() == 'dictator'


class BeforeResults(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    pass


page_sequence = [
    FirstWP,

    GameDescription,
    QuestionnaireS,
    BeforeDictator,
    DictatorSender,
    DictatorReceiver,
    DictatorSenderExpected,
    BeforeResults,
    Results,
    QuestionnaireF
]
