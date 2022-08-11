def calcula_desconto_INSS(base_salary, comission) -> float:
        base_calc_inss = base_salary + comission

        if 1212.01 < base_calc_inss <= 2427.35:
            desconto_faixa1 = 1212*0.075
            desconto_faixa2 = (2427.35 - 1212) * 0.09

            desconto_INSS = desconto_faixa1 + desconto_faixa2
            aliquota = 0.09

        elif 2427.36 < base_calc_inss <= 3641.03:
            desconto_faixa1 = 1212*0.075
            desconto_faixa2 = (2427.35 - 1212) * 0.09
            deconto_faixa3 = (base_calc_inss - 2427.36) * 0.12

            desconto_INSS = desconto_faixa1 + desconto_faixa2 + deconto_faixa3
            aliquota = 0.12

        elif 3641.04 < base_calc_inss <= 7087.22:
            desconto_faixa1 = 1212*0.075
            desconto_faixa2 = (2427.35 - 1212) * 0.09
            deconto_faixa3 = (3641.04 - 2427.35) * 0.12
            desconto_faixa4 = (base_calc_inss - 3641.04) * 0.14

            desconto_INSS = desconto_faixa1 + desconto_faixa2 + \
                deconto_faixa3 + desconto_faixa4
            aliquota = 0.14

        elif 7087.23 <= base_calc_inss:
            desconto_faixa1 = 1212*0.075
            desconto_faixa2 = (2427.35 - 1212) * 0.09
            deconto_faixa3 = (3641.04 - 2427.35) * 0.12
            desconto_faixa4 = (7087.22 - 3641.04) * 0.14

            desconto_INSS = desconto_faixa1 + desconto_faixa2 + \
                deconto_faixa3 + desconto_faixa4
            aliquota = 0.14

        base_calc_inss = round(base_calc_inss, 2) 
        desconto_INSS = round(desconto_INSS, 2) 
        aliquota = round(aliquota, 2)

        return base_calc_inss, desconto_INSS, aliquota

def calcula_IRRF(desconto_INSS, base_salary, comission) -> float:
    base_calc_irrf = base_salary + \
        comission - desconto_INSS

    if 1903.89 <= base_calc_irrf <= 2826.65:
        irrf_discount = (base_calc_irrf*0.075) - 142.8
        aliquota = 0.075

    elif 2826.66 <= base_calc_irrf <= 3751.05:
        irrf_discount = (base_calc_irrf*0.15) - 354.8
        aliquota = 0.15

    elif 3751.06 <= base_calc_irrf <= 4664.68:
        irrf_discount = (base_calc_irrf*0.225) - 636.13
        aliquota = 0.225

    elif 4664.69 <= base_calc_irrf:
        irrf_discount = (base_calc_irrf*0.275) - 869.36
        aliquota = 0.275

    base_calc_irrf = round(base_calc_irrf, 2)
    irrf_discount =  round(irrf_discount, 2) 

    return base_calc_irrf, irrf_discount, aliquota

def calcula_FGTS(base_salary, comission ) -> float:

    base_calc_fgts = base_salary + comission
    fgts_mes = base_calc_fgts*0.08

    base_calc_fgts = round(base_calc_fgts, 2) 
    fgts_mes = round(fgts_mes, 2)
    return base_calc_fgts, fgts_mes