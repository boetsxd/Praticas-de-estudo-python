"""
1. Mapeamento de Notas: 
Crie um dicionário para armazenar o nome de 5 alunos e suas respectivas notas. 
Em seguida, use um loop for para percorrer o dicionário e imprimir o nome do aluno e se ele foi Aprovado (nota >= 7) ou Reprovado (usando if/else).    
"""
#%%
notas_alunos = {
    "bruno": 10,
    "Ana": 8,
    "Pedro": 7.5,
    "Lucas": 5.9,
    "Anderson":9.4
}

for nome, nota in notas_alunos.items():
    print(f'{nome}')
    if nota >= 7:
        print(f'Aprovado! nota {nota}\n')
    else:
        print(f'Reprovado! nota {nota}\n')
