from django import template


register = template.Library()


@register.filter
def get(questions, index):
    return questions[index]


@register.filter
def get_title(question):
    return question.title


@register.filter
def plus_one(number):
    return number+1

