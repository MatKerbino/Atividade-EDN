import pandas as pd
import numpy as np

def analisar_log_treinamento(arquivo_log):
    try:
        df = pd.read_csv(arquivo_log)
        
        if 'tempo_execucao' not in df.columns:
            print("Erro: Coluna 'tempo_execucao' não encontrada no arquivo")
            return None
        
        tempos = df['tempo_execucao']
        media = np.mean(tempos)
        desvio_padrao = np.std(tempos)
        
        print("ANALISE DE LOG DE TREINAMENTO")
        print(f"Arquivo analisado: {arquivo_log}")
        print(f"Total de epocas: {len(tempos)}")
        print(f"Media do tempo de execucao: {media:.2f} segundos")
        print(f"Desvio padrao do tempo de execucao: {desvio_padrao:.2f} segundos")
        print(f"Tempo minimo: {np.min(tempos)} segundos")
        print(f"Tempo maximo: {np.max(tempos)} segundos")
        
        return {
            'media': media,
            'desvio_padrao': desvio_padrao,
            'total_epocas': len(tempos)
        }
        
    except FileNotFoundError:
        print(f"Erro: Arquivo {arquivo_log} não encontrado")
        return None
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")
        return None

if __name__ == "__main__":
    arquivo_log = "log_treinamento.csv"
    
    resultado = analisar_log_treinamento(arquivo_log)
    
    if resultado:
        print("RESUMO")
        print(f"Media: {resultado['media']:.2f}")
        print(f"Desvio Padrao: {resultado['desvio_padrao']:.2f}")
