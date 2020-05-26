from otree.api import Currency as c, currency_range
from ._builtin import Page
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['name', 'age']




class Results(Page):
    pass


page_sequence = [MyPage, Results]
