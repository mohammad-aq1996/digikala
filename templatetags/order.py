from django import template

register = template.Library()

def order(value):
    if 'ordering=price-l2h' in value:
        g = 'ordering=price-l2h'    
    elif 'ordering=price-h2l' in value:
        g = 'ordering=price-h2l'    
    elif 'ordering=desc' in value:
        g = 'ordering=desc'
    else:
        g = ""
    return value.replace(g,"")

register.filter('order', order)
