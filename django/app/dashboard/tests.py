from django.test import TestCase
from dateutil.relativedelta import relativedelta
from datetime import datetime



hoje = datetime.today()
proximo_mes = hoje + relativedelta(months=1)

print(hoje, type(hoje))
print(proximo_mes, type(proximo_mes))