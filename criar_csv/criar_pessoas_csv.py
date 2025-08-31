import csv
import random

def criar_csv_pessoas(arquivo_saida, num_pessoas=10):
    nomes = [
        "Ana Silva", "Bruno Santos", "Carla Oliveira", "Daniel Costa", "Eva Ferreira",
        "Fernando Lima", "Gabriela Rocha", "Henrique Alves", "Isabela Martins", "João Pereira",
        "Karina Souza", "Lucas Mendes", "Mariana Costa", "Nicolas Silva", "Olivia Santos",
        "Pedro Almeida", "Quiteria Lima", "Rafael Costa", "Sabrina Oliveira", "Thiago Santos"
    ]
    
    cidades = [
        "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Fortaleza",
        "Curitiba", "Recife", "Porto Alegre", "Brasília", "Manaus",
        "Belém", "Goiânia", "Guarulhos", "Campinas", "São Luís"
    ]
    
    try:
        with open(arquivo_saida, 'w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            
            writer.writerow(['Nome', 'Idade', 'Cidade'])
            
            for i in range(num_pessoas):
                nome = random.choice(nomes)
                idade = random.randint(18, 80)
                cidade = random.choice(cidades)
                
                writer.writerow([nome, idade, cidade])
        
        print(f"Arquivo CSV criado com sucesso: {arquivo_saida}")
        print(f"Total de pessoas criadas: {num_pessoas}")
        
    except Exception as e:
        print(f"Erro ao criar arquivo CSV: {e}")

def criar_csv_pessoas_manual(arquivo_saida):
    pessoas = [
        ["Ana Silva", 27, "São Paulo"],
        ["Bruno Santos", 32, "Rio de Janeiro"],
        ["Carla Oliveira", 24, "Belo Horizonte"],
        ["Daniel Costa", 29, "Salvador"],
        ["Eva Ferreira", 35, "Fortaleza"],
        ["Fernando Lima", 26, "Curitiba"],
        ["Gabriela Rocha", 31, "Recife"],
        ["Henrique Alves", 28, "Porto Alegre"]
    ]
    
    try:
        with open(arquivo_saida, 'w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            
            writer.writerow(['Nome', 'Idade', 'Cidade'])
            
            for pessoa in pessoas:
                writer.writerow(pessoa)
        
        print(f"Arquivo CSV criado com sucesso: {arquivo_saida}")
        print(f"Total de pessoas criadas: {len(pessoas)}")
        
    except Exception as e:
        print(f"Erro ao criar arquivo CSV: {e}")

if __name__ == "__main__":
    print("CRIANDO CSV COM DADOS ALEATORIOS")
    criar_csv_pessoas("pessoas_aleatorias.csv", 15)
    
    print("CRIANDO CSV COM DADOS ESPECIFICOS")
    criar_csv_pessoas_manual("pessoas_especificas.csv")
