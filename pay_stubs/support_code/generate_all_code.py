"""Esse script possue as funções que não dependem dos dados da requisição
e podem ficar separados deixando o código mais limpo. """

jmmjaod = ['01', '03', '05', '07', '08', '10', '12']

def this_month(year, month):
    """Essa função gera dados para a pesquisa do holerite apenas no mês atual."""
    if month in jmmjaod:
        day = '31'
    else:     
        day = '30'

    inital_date = year+'-'+month+'-01'   
    final_date = year+'-'+month+'-'+day

    return inital_date, final_date