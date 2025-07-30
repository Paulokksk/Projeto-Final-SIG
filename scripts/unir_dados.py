import geopandas as gpd
import pandas as pd
from warnings import filterwarnings
filterwarnings('ignore')

# 1. Configuração baseada nos seus arquivos reais
CONFIG = {
    'basico': {
        'col_juncao': 'CD_SETOR',
        'variaveis': ['V0001', 'V0002']  # População e domicílios
    },
    'esgoto': {
        'col_juncao': 'SETOR',
        'variaveis': ['V00091']  # Acesso a esgoto
    },
    'cor_raca': {
        'col_juncao': 'CD_SETOR',
        'variaveis': ['V01318']  # População parda/negra
    },
    'alfabetizacao': {
        'col_juncao': 'CD_SETOR',
        'variaveis': ['V00644']  # Alfabetização
    }
}

def main():
    # 2. Carregar malha com tratamento especial
    try:
        malha = gpd.read_file('dados/geograficos/setores_caninde.shp')
        malha['CD_SETOR'] = malha['CD_SETOR'].astype(str).str.strip().str.zfill(15)
    except Exception as e:
        print(f"❌ Erro ao carregar a malha: {str(e)}")
        return
    # 3. Processamento robusto
    for nome, config in CONFIG.items():
        try:
            # Carregar CSV
            df = pd.read_csv(
                f'dados/filtrados/caninde_{nome}.csv',
                sep=';',
                dtype={config['col_juncao']: str}
            )
            
            # Padronizar coluna de junção
            df[config['col_juncao']] = df[config['col_juncao']].astype(str).str.zfill(15)
            
            # Verificar se variáveis existem
            variaveis_disponiveis = [v for v in config['variaveis'] if v in df.columns]
            if not variaveis_disponiveis:
                print(f"⚠️ {nome}: Variáveis {config['variaveis']} não encontradas. Use uma destas: {[col for col in df.columns if col.startswith('V')][:5]}")
                continue
            
            # Merge seguro
            malha = malha.merge(
                df[[config['col_juncao']] + variaveis_disponiveis],
                left_on='CD_SETOR',
                right_on=config['col_juncao'],
                how='left'
            )

            
            print(f"✅ {nome}: Adicionadas {len(variaveis_disponiveis)} variáveis")
            
        except Exception as e:
            print(f"⚠️ Erro em {nome}: {str(e)}")
            continue

    # 4. Salvar resultado
    try:
        malha.to_file('dados/geograficos/mapa_final.gpkg', driver='GPKG')
        print("\n🎉 Dados unificados salvos em 'mapa_final.gpkg'")
        print("Variáveis incluídas:", [col for col in malha.columns if col.startswith('V')])
    except Exception as e:
        print(f"❌ Erro ao salvar: {str(e)}")

if __name__ == "__main__":
    main()

