import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título do Dashboard
st.title('Dashboard de Hedge Cambial - Importadora & Exportadora São Francisco')

# Descrição e Explicação
st.header('Política de Hedge Cambial')
st.write('Este dashboard ajuda importadores e exportadores da Importadora & Exportadora São Francisco na definição de políticas de hedge cambial usando futuros de dólar.')

# Inputs do Usuário
st.sidebar.header('Parâmetros do Hedge')
valor_exportacao = st.sidebar.number_input('Valor da Exportação (em USD)', min_value=0.0, value=100000.0)
valor_importacao = st.sidebar.number_input('Valor da Importação (em USD)', min_value=0.0, value=50000.0)
taxa_cambio_atual = st.sidebar.number_input('Taxa de Câmbio Atual (USD/BRL)', min_value=0.0, value=5.25)

# Cálculo do Hedge
if valor_exportacao > 0 and valor_importacao > 0 and taxa_cambio_atual > 0:
    valor_total = valor_exportacao - valor_importacao
    valor_hedge = valor_total * taxa_cambio_atual

    st.sidebar.subheader('Resultado do Hedge')
    st.sidebar.write(f'Valor Hedge Necessário: R$ {valor_hedge:.2f}')

    # Gráfico de Resultado do Hedge
    valores = np.linspace(3.5, 6.0, 100)
    lucro_perda = np.maximum(0, valores - taxa_cambio_atual) * valor_total

    fig, ax = plt.subplots()
    ax.plot(valores, lucro_perda, label='Lucro/Perda')
    ax.axhline(0, color='gray', linewidth=0.5, linestyle='--')
    ax.axvline(taxa_cambio_atual, color='red', linewidth=0.5, linestyle='--', label='Taxa Atual')
    ax.set_xlabel('Taxa de Câmbio (USD/BRL)')
    ax.set_ylabel('Lucro/Perda (R$)')
    ax.legend()
    st.pyplot(fig)

else:
    st.sidebar.warning('Insira os valores de exportação, importação e a taxa de câmbio atual.')

# Rodapé
st.sidebar.write('Desenvolvido por Importadora & Exportadora São Francisco')
