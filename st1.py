
# importando bibliotecas
import streamlit as st
#yahoo finance -> que pega dados de ações 
import yfinance as yf

#st = Streamlit()

#método write
st.write("""
Brincando com a bolsa de valores

só para começar

""")

acao = "GOOGL"

# yf = yfinance() -> me devolve um objeto
# podem pensar de forma equivalente
# a uma classe agenda devolver como retorno
#um obejto da classe contato que vc pode manipular
#nesse caso é devolvido um objeto que são os dados das ações
dado = yf.Ticker(acao)

acaodf = dado.history(period="1d", start="2011-11-30", end="2012-12-1")

st.write("""
Preco de fechamento
""")

#cria um gráfico
st.line_chart(acaodf.Close)

st.write("""
Volume da acao
""")
st.line_chart(acaodf.Volume)