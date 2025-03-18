import re
from datetime import date
from common import utils
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



class Validate:


    def valid_name(name:str):

        namews = name.replace(' ', '')
        if len(namews) <= 2:
            raise ValidationError(_('Nome inválido.'))
        else:
            for i in range(len(namews)):
                if not namews[i].isalpha():
                    raise ValidationError(_('O nome pode conter apenas letras.'))


    def valid_date(_date:date):

        if _date:
            if _date >= date.today() or _date <= date(date.today().year - 110, date.today().month, date.today().day):
                raise ValidationError("Data inválida.")
            if _date > date(date.today().year - 18, date.today().month, date.today().day):
                raise ValidationError("Menor de idade.")


    def valid_cpf(CPF:str):

        try:

            CPF = CPF.replace('.','').replace('-','')

            def first_digit(CPF):

                CPF_sum = 0
                counter = 10
                for number in CPF[:9]:
                    CPF_sum += int(number) * counter
                    counter -= 1
                CPF_first_digit = (CPF_sum * 10) % 11
                CPF_first_digit = CPF_first_digit if CPF_first_digit < 10 else 0
                
                return True if CPF_first_digit == int(CPF[9]) else False

            def second_digit(CPF):

                CPF_sum = 0
                counter = 11
                for number in CPF[:10]:
                    CPF_sum += int(number) * counter
                    counter -= 1
                CPF_second_digit = (CPF_sum * 10) % 11
                CPF_second_digit = CPF_second_digit if CPF_second_digit < 10 else 0
                
                return True if CPF_second_digit == int(CPF[10]) else False

            if not first_digit(CPF) or not second_digit(CPF) or not CPF != (CPF[0] * len(CPF)):
                raise ValidationError(_('Número de CPF inválido.'))

        except:
            raise ValidationError(_('Número de CPF inválido.'))
        

    def valid_cnpj(cnpj:str):

        cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')

        if len(cnpj) == 14:
            validar = True
            digitos_verificadores = cnpj[13:]
        else:
            validar = False

        cnpj = cnpj[:12]

        try:

            dig_1 = int(cnpj[0]) * 6
            dig_2 = int(cnpj[1]) * 7
            dig_3 = int(cnpj[2]) * 8
            dig_4 = int(cnpj[3]) * 9
            dig_5 = int(cnpj[4]) * 2
            dig_6 = int(cnpj[5]) * 3
            dig_7 = int(cnpj[6]) * 4
            dig_8 = int(cnpj[7]) * 5
            dig_9 = int(cnpj[8]) * 6
            dig_10 = int(cnpj[9]) * 7
            dig_11 = int(cnpj[10]) * 8
            dig_12 = int(cnpj[11]) * 9

        except IndexError:

            raise ValidationError(_('Número de CNPJ inválido.'))

        dig_1_ao_12_somados = (dig_1 + dig_2 + dig_3 + dig_4 + dig_5 + dig_6 + dig_7 + dig_8 + dig_9 + dig_10 + dig_11 + dig_12)

        dig_13 = dig_1_ao_12_somados % 11

        if dig_13 > 9:
            dig_13 = 0

        cnpj += str(dig_13)

        dig_1 = int(cnpj[0]) * 5
        dig_2 = int(cnpj[1]) * 6
        dig_3 = int(cnpj[2]) * 7
        dig_4 = int(cnpj[3]) * 8
        dig_5 = int(cnpj[4]) * 9
        dig_6 = int(cnpj[5]) * 2
        dig_7 = int(cnpj[6]) * 3
        dig_8 = int(cnpj[7]) * 4
        dig_9 = int(cnpj[8]) * 5
        dig_10 = int(cnpj[9]) * 6
        dig_11 = int(cnpj[10]) * 7
        dig_12 = int(cnpj[11]) * 8
        dig_13 = int(cnpj[12]) * 9

        dig_1_ao_13_somados = (dig_1 + dig_2 + dig_3 + dig_4 + dig_5 + dig_6 + dig_7 + dig_8 + dig_9 + dig_10 + dig_11 + dig_12 + dig_13)

        dig_14 = dig_1_ao_13_somados % 11

        if dig_14 > 9:
            dig_14 = 0

        cnpj_validado = cnpj + str(dig_14)

        cnpj = (cnpj_validado[0:2] + '.' + cnpj_validado[2:5] + '.' + cnpj_validado[5:8] + '/' + cnpj_validado[8:12] + '-' + cnpj_validado[12:])

        if validar:
            if not digitos_verificadores == cnpj_validado[13:]:
                raise ValidationError(_('Número de CNPJ inválido.'))
        else:
            raise ValidationError(_('Número de CNPJ inválido.'))


    def valid_email(email:str):
        
        if re.search(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email) == None:

            raise ValidationError(_('E-mail inválido.'))


    def valid_phone(phone:str):

        phone = utils.remove_chars(phone,'[() -]')

        if len(phone) >= 10 or len(phone) <= 11:
            for i in range(len(phone)):
                if not phone[i].isnumeric():
                    raise ValidationError(_('Telefone inválido.'))
            
        raise ValidationError(_('Telefone inválido.'))
    

    def valid_duration(duration:int):

        if duration < 1 or duration > 365:
            raise ValidationError(_('Duração inválida.'))
        

    def valid_price(price:str):

        for i in range(len(price.replace('.',''))):
            if not price[i].isnumeric():
                raise ValidationError(_('Preço inválido.'))



class ValidateFile:


        def valid_type(filename:str, types:list):
        
            extension = utils.file_extension(filename)

            for type in types:
                if not type == extension:
                    raise ValidationError(_('Tipo de arquivo inválido.'))