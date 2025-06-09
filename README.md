# 📊 Analisador Fundamentalista de Ações

Ferramenta simples em Python para consultar indicadores fundamentalistas de ações brasileiras ou internacionais usando dados do Yahoo Finance.

---

## 📦 Instalação

Antes de executar o programa, instale os pacotes necessários:

```bash
pip install yfinance pandas tabulate
```
Como funciona:
O programa solicita que você digite os tickers das empresas que deseja consultar (ex: PETR4.SA, VALE3.SA, WEGE3.SA).

Ele busca automaticamente os seguintes dados:

 -Nome da empresa

 -Setor

 -Preço atual da ação

 -Indicadores fundamentalistas:

 -P/L (Preço/Lucro)

 -ROE (%) (Retorno sobre o patrimônio)

 -Dividend Yield (%)

 -Valor de mercado

Os resultados são exibidos de forma organizada em uma tabela no terminal.

Exemplo de uso real do programa com 2 ações brasileiras: https://colab.research.google.com/drive/1mTGTkDIMWM0tIwgqu5UZDkdtpLEMMss1?usp=sharing
![image](https://github.com/user-attachments/assets/d1ea9d12-7024-46bb-852a-d40c7b99756e)
