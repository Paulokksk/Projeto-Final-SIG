# 🌍 Mapa Interativo de Vulnerabilidades Urbanas — Canindé (CE)

Este projeto apresenta um ambiente interativo de visualização de indicadores urbanos e socioeconômicos, com base nos dados do Censo Demográfico 2022 do IBGE, focado no município de **Canindé - CE**. A ferramenta permite explorar vulnerabilidades sociais com suporte visual e geográfico, facilitando a análise de desigualdades intraurbanas.

---

## 🎯 Objetivo

Desenvolver um **mapa temático interativo** utilizando os setores censitários como base territorial, com o objetivo de analisar **indicadores de vulnerabilidade social**, promovendo uma leitura geográfica das desigualdades em Canindé.

---

## 🗂️ Indicadores Selecionados

Foram selecionados 5 indicadores de relevância social:

| Indicador | Código IBGE | Descrição |
|----------|--------------|-----------|
| População residente | `V0001` | Quantidade total de habitantes por setor |
| Número de domicílios particulares | `V0002` | Total de domicílios em cada setor |
| Domicílios com esgotamento sanitário adequado | `V00091` | Avalia o acesso a rede de esgoto |
| Pessoas alfabetizadas | `V00644` | Taxa de alfabetização por setor |
| População preta/parda | `V01318` | Indicador racial e étnico |
---

## 🧰 Tecnologias Utilizadas

- 🐍 **Python 3.10**
- 🗺️ **GeoPandas** — manipulação geoespacial
- 📊 **Pandas** — tratamento tabular
- 🧭 **Folium** — geração de mapas interativos
- 🧩 **Shapely**, **Matplotlib**, **Numpy**
- 🧾 **Dados**:
  - Malha setorial: [Malha Territorial IBGE 2022](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais.html)
  - Tabelas de setores: [Resultados do Censo 2022 por Setor](https://censo2022.ibge.gov.br/resultados)

---

## 🗺️ Funcionalidades

- **Visualização interativa** por setores censitários.
- **Dropdown para seleção do indicador** (mapa se atualiza dinamicamente).
- **Coloração coroplética** (tons de azul) conforme valor da variável.
- **Pop-ups/Tooltips** com informações dos setores.
- Base territorial precisa (GPKG + CSVs tratados).

---

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/Mapa-Interativo-Caninde.git
   cd Mapa-Interativo-Caninde
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o script:
   ```bash
   python gerar_mapa.py
   ```

4. Abra o arquivo `mapa_interativo.html` gerado no navegador.

---

## 🧪 Estrutura de Pastas

```
📁 
PROJETO_CANINDÉ/
├── dados/
│ ├── filtrados/ # Dados filtrados para o município escolhido (Canindé)
│ │ ├── caninde_alfabetizacao.csv
│ │ ├── caninde_basico.csv
│ │ ├── caninde_cor_raca.csv
│ │ └── caninde_esgoto.csv
│ └── geograficos/ # Malhas territoriais e dados geográficos processados
│ ├── mapa_final.gpkg # Arquivo geopackage unificado com dados + geometria
│ ├── setores_caninde.cpg
│ ├── setores_caninde.dbf
│ ├── setores_caninde.prj
│ ├── setores_caninde.shp
│ └── setores_caninde.shx
├── resultados/ # Saídas do projeto (mapa, gráficos, relatórios)
│ └── mapa_interativo.html # Mapa interativo gerado em HTML
├── scripts/ # Scripts Python para tratamento e análise dos dados
│ ├── unir_dados.py # Junta dados tabulares com malha geográfica
│ ├── gerar_mapa.py # Gera mapa interativo com Folium
├── README.md # Documentação do projeto
└── requirements.txt # Dependências do projeto

📄 gerar_mapa.py
📄 mapa_interativo.html
📄 README.md
```

---

## 📌 Observações

- Os dados foram tratados e compatibilizados por setor censitário.
- O código pode ser adaptado para outros municípios ou novos indicadores facilmente.

---

## 👨‍💻 Autor

- **Nome:** Paulo Henrique Santos Justino
- **Curso:** Mestrado Acadêmico em Ciência da Computação
- **Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará | Campus Fortaleza
- **Disciplina:** SISTEMAS DE INFORMAÇÃO GEOGRÁFICA
- **Professor:** Reinaldo Braga

---
# Projeto-Final-SIG
