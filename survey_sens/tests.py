from otree.api import Currency as c, currency_range
from .pages import *
from ._builtin import Bot
from .models import Constants
import random

class PseudoPage:
    def __init__(self, player):
        self.player = player


class PlayerBot(Bot):
    def play_round(self):
        yield RoleAnnouncement,
        qsfields = QuestionnaireS.get_form_fields(PseudoPage(self.player))
        answers = {i: 1 for i in qsfields}
        yield QuestionnaireS, answers
        if self.player.role() == 'dictator':
            yield DictatorSender, dict(sent_amount=random.randint(0,Constants.endowment))
            yield DictatorSenderExpected,dict(expected_sender=random.randint(0,Constants.endowment))
        else:
            yield DictatorReceiver,dict(expected_receiver=random.randint(0,Constants.endowment))
        qsfields = QuestionnaireF.form_fields
        answers = {i: 1 for i in qsfields}
        yield QuestionnaireF,answers
        yield Results,
