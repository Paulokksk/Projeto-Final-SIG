import folium
import pandas as pd
import geopandas as gpd
import os
from branca.colormap import LinearColormap

# Criar pasta de saída, se não existir
os.makedirs('resultados', exist_ok=True)

# Carregar camada geográfica com variáveis já unidas
try:
    malha = gpd.read_file('dados/geograficos/mapa_final.gpkg')
    print("✅ Malha carregada com sucesso!")
except Exception as e:
    print(f"❌ Erro ao carregar a malha: {e}")
    exit()

# Criar mapa base centrado em Canindé
m = folium.Map(location=[-4.35, -39.31], zoom_start=12)

# Colormap para acesso a esgoto (%)
colormap_esgoto = LinearColormap(
    ['red', 'green'],
    vmin=0, vmax=1,
    caption='Acesso a esgoto (%)'
)

# Função de estilo com tratamento de erro para valores inválidos
def style_function(feature):
    valor = feature['properties'].get('V00091')
    try:
        return {
            'fillColor': colormap_esgoto(float(valor) / 100),
            'color': 'black',
            'weight': 0.5,
            'fillOpacity': 0.7
        }
    except (ValueError, TypeError):
        return {
            'fillColor': 'gray',
            'color': 'black',
            'weight': 0.5,
            'fillOpacity': 0.3
        }

# Adicionar camada geográfica com tooltip
folium.GeoJson(
    malha,
    style_function=style_function,
    tooltip=folium.GeoJsonTooltip(
        fields=[
            'CD_SETOR',
            'V0001',
            'V0002',
            'V00091',
            'V00644',
            'V01318',
        ],
        aliases=[
            'Setor:',
            'População residente:',
            'Domicílios:',
            'Esgoto adequado (%):',
            'Alfabetizados (%):',
            'População preta/parda (%):'
        ],
        localize=True,
        sticky=True
    )
).add_to(m)


# Adicionar legenda de cores
colormap_esgoto.add_to(m)

# Salvar o mapa
saida = 'resultados/mapa_interativo.html'
m.save(saida)
print(f"🎉 Mapa salvo em: {saida}")


