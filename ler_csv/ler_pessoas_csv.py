import csv
import sys

def ler_csv_pessoas(arquivo_csv):
    try:
        with open(arquivo_csv, 'r', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo)
            
            try:
                cabecalho = next(reader)
                print("CABECALHO:")
                print(f"   {' | '.join(cabecalho)}")
                print("-" * 50)
            except StopIteration:
                print("Arquivo CSV vazio")
                return
            
            contador = 0
            print("DADOS DAS PESSOAS:")
            
            for linha_num, linha in enumerate(reader, start=1):
                if len(linha) >= 3:
                    nome, idade, cidade = linha[0], linha[1], linha[2]
                    
                    print(f"{linha_num:2d}. {nome:<20} | {idade:>3} anos | {cidade}")
                    contador += 1
                else:
                    print(f"Linha {linha_num}: Dados incompletos - {linha}")
            
            print("-" * 50)
            print(f"Total de pessoas encontradas: {contador}")
            
    except FileNotFoundError:
        print(f"Erro: Arquivo {arquivo_csv} não encontrado")
    except UnicodeDecodeError:
        print(f"Erro: Problema de codificação no arquivo {arquivo_csv}")
        print("   Tente usar encoding='latin-1' ou verifique a codificação do arquivo")
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")

def exibir_estatisticas_csv(arquivo_csv):
    try:
        with open(arquivo_csv, 'r', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo)
            
            next(reader, None)
            
            idades = []
            cidades = set()
            
            for linha in reader:
                if len(linha) >= 3:
                    try:
                        idade = int(linha[1])
                        idades.append(idade)
                        cidades.add(linha[2])
                    except ValueError:
                        continue
            
            if idades:
                print("ESTATISTICAS:")
                print(f"   Idade media: {sum(idades) / len(idades):.1f} anos")
                print(f"   Idade minima: {min(idades)} anos")
                print(f"   Idade maxima: {max(idades)} anos")
                print(f"   Total de cidades unicas: {len(cidades)}")
                
                print(f"   Cidades: {', '.join(sorted(cidades))}")
            
    except Exception as e:
        print(f"Erro ao calcular estatisticas: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arquivo_csv = sys.argv[1]
    else:
        arquivo_csv = "pessoas.csv"
    
    print(f"LENDO ARQUIVO: {arquivo_csv}")
    print("=" * 50)
    
    ler_csv_pessoas(arquivo_csv)
    
    exibir_estatisticas_csv(arquivo_csv)
