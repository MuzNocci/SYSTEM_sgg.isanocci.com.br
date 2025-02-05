from django.test import TestCase


from datetime import datetime, date
from datetime import timezone

hoje = date.today()
proximo_mes = hoje.replace(month=hoje.month + 1)

print(hoje, type(hoje))
print(proximo_mes, type(proximo_mes))