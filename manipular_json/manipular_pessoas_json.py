import json
import os

def criar_pessoa_json(arquivo_saida, dados_pessoa):
    try:
        with open(arquivo_saida, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_pessoa, arquivo, indent=2, ensure_ascii=False)
        
        print(f"Arquivo JSON criado com sucesso: {arquivo_saida}")
        return True
        
    except Exception as e:
        print(f"Erro ao criar arquivo JSON: {e}")
        return False

def ler_pessoa_json(arquivo_json):
    try:
        with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        
        print(f"Arquivo JSON lido com sucesso: {arquivo_json}")
        return dados
        
    except FileNotFoundError:
        print(f"Erro: Arquivo {arquivo_json} não encontrado")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro: Arquivo JSON invalido - {e}")
        return None
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return None

def exibir_dados_pessoa(dados):
    if not dados:
        return
    
    print("DADOS DA PESSOA:")
    print("=" * 30)
    
    for campo, valor in dados.items():
        if campo == 'idade':
            print(f"   {campo.capitalize()}: {valor} anos")
        else:
            print(f"   {campo.capitalize()}: {valor}")
    
    print("=" * 30)

def atualizar_pessoa_json(arquivo_json, novos_dados):
    try:
        dados_existentes = ler_pessoa_json(arquivo_json)
        
        if dados_existentes:
            dados_existentes.update(novos_dados)
            
            with open(arquivo_json, 'w', encoding='utf-8') as arquivo:
                json.dump(dados_existentes, arquivo, indent=2, ensure_ascii=False)
            
            print(f"Arquivo JSON atualizado: {arquivo_json}")
            return True
        
        return False
        
    except Exception as e:
        print(f"Erro ao atualizar arquivo: {e}")
        return False

def criar_exemplos_json():
    pessoas_exemplo = [
        {
            "nome": "Ana Silva",
            "idade": 27,
            "cidade": "São Paulo",
            "profissao": "Engenheira",
            "email": "ana.silva@email.com"
        },
        {
            "nome": "Bruno Santos",
            "idade": 32,
            "cidade": "Rio de Janeiro",
            "profissao": "Medico",
            "email": "bruno.santos@email.com"
        },
        {
            "nome": "Carla Oliveira",
            "idade": 24,
            "cidade": "Belo Horizonte",
            "profissao": "Designer",
            "email": "carla.oliveira@email.com"
        }
    ]
    
    for i, pessoa in enumerate(pessoas_exemplo, 1):
        nome_arquivo = f"pessoa_{i}.json"
        criar_pessoa_json(nome_arquivo, pessoa)
        print(f"   Criado: {nome_arquivo}")
    
    arquivo_lista = "lista_pessoas.json"
    with open(arquivo_lista, 'w', encoding='utf-8') as arquivo:
        json.dump(pessoas_exemplo, arquivo, indent=2, ensure_ascii=False)
    
    print(f"   Criado: {arquivo_lista}")

if __name__ == "__main__":
    print("SERVICO DE MANIPULACAO DE JSON")
    
    print("1. CRIANDO ARQUIVO JSON DE EXEMPLO")
    pessoa_exemplo = {
        "nome": "João da Silva",
        "idade": 30,
        "cidade": "Curitiba",
        "profissao": "Desenvolvedor",
        "email": "joao.silva@email.com"
    }
    
    arquivo_exemplo = "pessoa_exemplo.json"
    criar_pessoa_json(arquivo_exemplo, pessoa_exemplo)
    
    print("2. LENDO ARQUIVO JSON CRIADO")
    dados_lidos = ler_pessoa_json(arquivo_exemplo)
    exibir_dados_pessoa(dados_lidos)
    
    print("3. ATUALIZANDO ARQUIVO JSON")
    novos_dados = {
        "idade": 31,
        "cidade": "São Paulo",
        "telefone": "(11) 99999-9999"
    }
    
    atualizar_pessoa_json(arquivo_exemplo, novos_dados)
    
    print("4. LENDO ARQUIVO ATUALIZADO")
    dados_atualizados = ler_pessoa_json(arquivo_exemplo)
    exibir_dados_pessoa(dados_atualizados)
    
    print("5. CRIANDO MULTIPLOS EXEMPLOS")
    criar_exemplos_json()
    
    print("Todos os servicos foram executados com sucesso!")
