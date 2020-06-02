from otree.api import Currency as c, currency_range
from ._builtin import WaitPage
from survey_sens.generic_pages import Page
from .models import Constants


class IntroGame(Page):
    pass


class GameDescription(Page):
    show_instructions = True


page_sequence = [
    IntroGame,
    GameDescription
]
