import json
from datetime import datetime

print("Criador ->https://github.com/joaomota59\n\n")

email = input("Login\ne-mail: ")

strJSON = ""

try:
    arq = open("gastosUsr.json","r", encoding='utf-8')
    strJSON = arq.read()
    arq.close()
except FileNotFoundError:
    pass

try:
    dicio = strJSON

    #exit(0)

    if dicio == "":
        dicio = {}
        dicio[email] = {"referencias":{}}
    else:
        dicio = json.loads(dicio)
    
    if not email in dicio.keys():
        dicio[email] = {"referencias":{}}

    print("\n\n\tMenu")

    escolha = 0

    meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto",
             "Setembro","Outubro","Novembro","Dezembro"]

    while escolha != 4:  
        escolha = int(input("""
1 - Despesa por Referência
2 - Adicionar despesa
3 - Excluir despesa
4 - Sair / Salvar alterações
> """))
        print("\n")
        if escolha == 1:
            if len(dicio[email]["referencias"].keys()) != 0:
                print("Selecione uma Referência (Selecionar o índice da referência)\n")
                for index,ref in enumerate(dicio[email]["referencias"].keys()):
                    print(f"{index+1}-{ref}")
                indexRef = int(input("> ")) - 1
                print(f"\nDespesas de {list(dicio[email]['referencias'].keys())[indexRef]}:\n")

                totalDespesas = 0

                despesasPorReferencia = dicio[email]["referencias"][list(dicio[email]["referencias"].keys())[indexRef]]
                
                for despesas in despesasPorReferencia:
                    totalDespesas += despesasPorReferencia[despesas][list(despesasPorReferencia[despesas].keys())[0]]
                    print(f"{despesasPorReferencia[despesas]}")
                print(f"Total das despesas: {totalDespesas}")
            else:
                print("Não foi achada nenhuma despesa por referência!")
        elif escolha == 2:
            ano = int(input("Qual o ano da despesa?\n> "))
            print("Qual o mes da despesa? (Selecionar o índice do mes)")
            for index,mes in enumerate(meses): print(f"{index+1} - {mes}")
            mes = int(input("\n>"))
            referencia = f"{ano}/{meses[mes-1]}"
            print(f"\nReferência - {referencia}\n")
            nomeDespesa = input(f"Nome da despesa:\n> ")
            valorDespesa = float(input(f"Valor da despesa:(Ex de entrada: R$ 25000.40)\n> R$ "))

            if referencia not in dicio[email]["referencias"].keys(): dicio[email]["referencias"].update({referencia:{}})

            indexNovaDespesa = ''.join(map(lambda x : str(x),list(datetime.now().timetuple())[:6]))

            dicio[email]["referencias"][referencia].update({indexNovaDespesa:{nomeDespesa:valorDespesa}})

            print("Despesa Adicionada!\n")
        elif escolha == 3:
            if len(dicio[email]["referencias"].keys()) != 0:
                print("Selecione uma Referência (Selecionar o índice da referência)\n")
                for index,ref in enumerate(dicio[email]["referencias"].keys()):
                    print(f"{index+1}-{ref}")
                indexRef = int(input("> ")) - 1
                print(f"\nDespesas de {list(dicio[email]['referencias'].keys())[indexRef]}:\n")

                despesasPorReferencia = dicio[email]["referencias"][list(dicio[email]["referencias"].keys())[indexRef]]

                print("Selecione o (número da despesa) que deseja excluir\n")
                for despesas in despesasPorReferencia:
                    print(f"{despesas} - {despesasPorReferencia[despesas]}")
                indexDespesa = input("> ")
                despesasPorReferencia.pop(indexDespesa)                
                print("\nDespesa Excluída!\n")
                
            else:
                print("Não foi achada nenhuma despesa por referência!")
except Exception as e:
    print("Erro",e)
    exit(0)
finally:
    arq = open("gastosUsr.json","w",encoding='utf-8')
    arq.write(json.dumps(dicio, indent = 2))
    arq.close()
