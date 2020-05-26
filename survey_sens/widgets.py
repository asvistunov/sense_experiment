from django import forms


class LikertWidget(forms.RadioSelect):
    template_name = 'survey_sens/likert.html'

    class Media:
        css = {
            'all': ('global/likert.css',)
        }

    def __init__(self, quote, label, left, right, *args, **kwargs, ):
        self.quote = quote
        self.label = label
        self.left = left
        self.right = right
        self.html_class = kwargs.pop('html_class', None)

        super().__init__(*args, **kwargs)

    def get_context(self, *args, **kwargs):
        context = super().get_context(*args, **kwargs)

        context.update({'choices': self.choices,
                        'quote': self.quote,
                        'label': self.label,
                        'left': self.left,
                        'right': self.right,
                        'html_class': self.html_class,
                        'optimal_width': round(85 / len(self.choices), 2),

                        })
        return context
