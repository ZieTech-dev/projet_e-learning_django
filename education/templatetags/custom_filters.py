from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def filter_by_score(evaluations, condition):
    if condition == "excellent":
        return [e for e in evaluations if e.score >= 80]
    elif condition == "good":
        return [e for e in evaluations if 70 <= e.score < 80]
    elif condition == "average":
        return [e for e in evaluations if 50 <= e.score < 70]
    elif condition == "weak":
        return [e for e in evaluations if e.score < 50]
    return evaluations