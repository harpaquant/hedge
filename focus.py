# BCB - Focus

from bcb import Expectativas

em = Expectativas()
em.describe()
ep = em.get_endpoint("ExpectativasMercadoAnuais")

def get_previsoes(indicador, ano):
    return (ep.query()
    .filter(ep.Indicador == f"{indicador}")
    .filter(ep.Data >= f'{ano}-01-01')
    .filter(ep.DataReferencia == ano)
    .select(ep.Data, ep.Mediana)
    .collect()
    )

get_previsoes('Câmbio', 2024)