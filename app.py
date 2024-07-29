import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title='Hedge Cambial')

# Título do Dashboard
st.title('Hedge Cambial')

# Descrição e Explicação
st.write('Este dashboard ajuda importadores e exportadores na definição de políticas de hedge cambial usando futuros/termo de dólar.')

# Seleção do tipo de análise
tipo_analise = st.sidebar.selectbox('Selecione o Tipo de Análise', ('Exportação', 'Importação'))

# Inputs do Usuário
st.sidebar.header('Parâmetros do Hedge')

if tipo_analise == 'Exportação':
    valor_exportacao = st.sidebar.number_input('Valor da Exportação (em USD)', min_value=0.0, value=100000.0)
    taxa_cambio_atual = st.sidebar.number_input('Taxa de Câmbio Atual (USD/BRL)', min_value=0.0, value=5.25)
    contrato_futuro = st.sidebar.number_input('Taxa do Contrato Futuro (USD/BRL)', min_value=0.0, value=5.30)
    percentual_hedge = st.sidebar.slider('Percentual da Exportação a Ser Hedgeado (%)', min_value=0, max_value=100, value=50)
    
    if valor_exportacao > 0 and taxa_cambio_atual > 0 and contrato_futuro > 0:
        valor_hedgeado = valor_exportacao * (percentual_hedge / 100)
        valor_nao_hedgeado = valor_exportacao - valor_hedgeado

        recebimento_com_hedge = valor_hedgeado * contrato_futuro + valor_nao_hedgeado * taxa_cambio_atual
        recebimento_sem_hedge = valor_exportacao * taxa_cambio_atual

        st.sidebar.subheader('Resultado do Hedge')
        st.sidebar.write(f'Valor Recebido com Hedge: R$ {recebimento_com_hedge:.2f}')
        st.sidebar.write(f'Valor Recebido sem Hedge: R$ {recebimento_sem_hedge:.2f}')

        # Gráfico de Resultado do Hedge
        valores = np.linspace(3.5, 7.0, 100)
        recebimento_hedge_var = valor_hedgeado * contrato_futuro + valor_nao_hedgeado * valores
        recebimento_sem_hedge = valor_exportacao * valores

        fig, ax = plt.subplots()
        ax.plot(valores, recebimento_sem_hedge, label='Recebimento sem Hedge')
        ax.plot(valores, recebimento_hedge_var, label=f'Recebimento com Hedge ({percentual_hedge}%)', linestyle='--')
        ax.axhline(0, color='gray', linewidth=0.5, linestyle='--')
        ax.axvline(taxa_cambio_atual, color='red', linewidth=0.5, linestyle='--', label='Taxa Atual')
        ax.set_xlabel('Taxa de Câmbio (USD/BRL)')
        ax.set_ylabel('Recebimento (R$)')
        ax.legend()
        st.pyplot(fig)
    
    else:
        st.sidebar.warning('Insira o valor de exportação, a taxa de câmbio atual e a taxa do contrato futuro.')

elif tipo_analise == 'Importação':
    valor_importacao = st.sidebar.number_input('Valor da Importação (em USD)', min_value=0.0, value=50000.0)
    taxa_cambio_atual = st.sidebar.number_input('Taxa de Câmbio Atual (USD/BRL)', min_value=0.0, value=5.25)
    contrato_futuro = st.sidebar.number_input('Taxa do Contrato Futuro (USD/BRL)', min_value=0.0, value=5.30)
    percentual_hedge = st.sidebar.slider('Percentual da Importação a Ser Hedgeado (%)', min_value=0, max_value=100, value=50)
    
    if valor_importacao > 0 and taxa_cambio_atual > 0 and contrato_futuro > 0:
        valor_hedgeado = valor_importacao * (percentual_hedge / 100)
        valor_nao_hedgeado = valor_importacao - valor_hedgeado

        custo_com_hedge = valor_hedgeado * contrato_futuro + valor_nao_hedgeado * taxa_cambio_atual
        custo_sem_hedge = valor_importacao * taxa_cambio_atual

        st.sidebar.subheader('Resultado do Hedge')
        st.sidebar.write(f'Custo com Hedge: R$ {custo_com_hedge:.2f}')
        st.sidebar.write(f'Custo sem Hedge: R$ {custo_sem_hedge:.2f}')

        # Gráfico de Resultado do Hedge
        valores = np.linspace(3.5, 7.0, 100)
        custo_hedge_var = valor_hedgeado * contrato_futuro + valor_nao_hedgeado * valores
        custo_sem_hedge = valor_importacao * valores

        fig, ax = plt.subplots()
        ax.plot(valores, custo_sem_hedge, label='Custo sem Hedge')
        ax.plot(valores, custo_hedge_var, label=f'Custo com Hedge ({percentual_hedge}%)', linestyle='--')
        ax.axhline(0, color='gray', linewidth=0.5, linestyle='--')
        ax.axvline(taxa_cambio_atual, color='red', linewidth=0.5, linestyle='--', label='Taxa Atual')
        ax.set_xlabel('Taxa de Câmbio (USD/BRL)')
        ax.set_ylabel('Custo (R$)')
        ax.legend()
        st.pyplot(fig)
    
    else:
        st.sidebar.warning('Insira o valor de importação, a taxa de câmbio atual e a taxa do contrato futuro.')

# Rodapé
# st.sidebar.write('Ferramenta experimental')
