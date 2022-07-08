from django import template


register = template.Library()

bad_words = [
   'собака',
   'кошка',
   'тигр',
   'did'
]

# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def bad_word(value):
   a = value.split()
   for i in bad_words:
      if i in a:
         a[a.index(i)] = '*' * len(i)
   return " ".join(a)