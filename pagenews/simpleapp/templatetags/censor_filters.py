from django import template

register = template.Library()

CENSOR_SYMBOLS = ['блатняк', 'шансон',]

@register.filter()
def censor(value):
    """
    value: title_news
    """

