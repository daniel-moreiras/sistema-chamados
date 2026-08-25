chamados = []
chamado = 1

print('Seja bem-vindo(a) ao Sistema de Suporte da F4 Sistemas!')
print('Por favor, selecione a opção para qual deseja atendimento:')

while True:
    print('[1] Abrir novo chamado, [2] Consultar chamado, [3] Sair')
    opcao = input('')

    if opcao == '1':
            
        solicitante = input('Por favor, informe o nome do solicitante: ')
        print(f'{solicitante}, em qual área o problema está localizado?')
        
        while True:
            print('[1] Cadastros, [2] ERP, [3] Infraestrutura, [4] Acessos')
            area = input(' ')
            
            if area == '1':
                area = "Cadastros"
                break
            elif area == '2':
                area = "ERP"
                break
            elif area == '3':
                area = "Infraestrutura"
                break
            elif area == '4':
                area = "Acessos"
                break
            else:
                print('Opção inválida.')

        descricao = input('Descreva o problema (Limite de 100 Caract.):')
        
        while len(descricao) > 100:
            print('Você excedeu o número de caracteres válidos. Por favor, refaça a descrição do problema.')
            descricao = input('Descreva o problema (Limite de 100 Caract.):')
        
        chamado = chamado + 1
        novo_chamado = {
            "Solicitante": solicitante,
            "Área": area,
            "Descrição": descricao,
            "Status": "Em andamento",
            "Número": chamado
        }
        chamados.append(novo_chamado)
        
        print(f'Seu chamado foi aberto com sucesso! Número: #{chamado}')
        
        reiniciar = input('Deseja realizar outra operação?: [SIM] ou [NAO]')
        if reiniciar == 'NAO':
            print('Você está deixando o sistema. Até logo!')
            break
        
    elif opcao == '2':
        consulta = int(input('Informe o número do chamado para validação: '))
    
        encontrado = False
    
        for chamado in chamados:
            if chamado["Número"] == consulta:
                print(chamado["Status"])
                encontrado = True
    
        if not encontrado:
            print('Chamado não encontrado.')
    
        reiniciar = input('Deseja realizar outra operação?: [SIM] ou [NAO]')
    
        if reiniciar == 'NAO':
            print('Você está deixando o sistema. Até logo!')
            break
                
    elif opcao == '3':
        print('Você está deixando o sistema. Até logo!')
        break
            
    else:
        print('Por favor, digite uma opção válida.')