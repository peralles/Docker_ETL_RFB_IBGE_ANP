import os
import platform

from B_Def_Global import (Criar_Var_Ambiente, VerifPath, gerenciar_bancos,
                          gerenciar_diretorios, log_retorno_erro,
                          print_divisor_inicio_fim)
from C_Script_RFB import *
from D_Script_IBGE import *
from E_Script_ANP import *
from I_Script_VARIAVEIS_ESTRUTURANTES import *


def clear_screen():
    """Cross-platform screen clearing"""
    os.system('cls' if platform.system() == 'Windows' else 'clear')


def Menu(titulo, opcoes):
    while True:
        clear_screen()
        print("=" * len(titulo), titulo, "=" * len(titulo), sep="\n")
        for i, (opcao, funcao) in enumerate(opcoes, 1):
            print("[{}] - {}".format(i, opcao))
        print("[{}] - Retornar/Sair".format(len(opcoes) + 1))

        try:
            op = input("Opção: ")
            if op.isdigit():
                op_num = int(op)
                if op_num == len(opcoes) + 1:
                    clear_screen()
                    break
                if 1 <= op_num <= len(opcoes):
                    opcoes[op_num - 1][1]()
                    continue
            print("Opção inválida. \n\n")
        except Exception as e:
            print(f"Erro: {e}")
            input("Pressione Enter para continuar...")


def Principal():
    clear_screen()
    opcoes = [
        ("1 - Ler path de trabalho", PathTrab),
        ("2 - Criar variáveis de ambiente", Definir_Var_Ambiente),
        ("3 - Criar/Exibir/Remover banco de dados", Banco_Dados),
        ("4 - Criar/Ler/Excluir diretórios de arquivos", caminhosDeArquivos),
        ("5 - Executar downloads RFB", executar_script_rfb),
        ("6 - Executar script IBGE", baixar_dados_ibge),
        ("7 - Executar script ANP", baixar_dados_anp)
    ]
    return Menu("ETL - Dados Públicos CNPJ", opcoes)


def PathTrab():
    clear_screen()
    opcoes = [
        ("1 - Ler path atual", VerifPath),
        ("2 - vazio", lambda: None)
    ]
    return Menu("1 - Ler path de trabalho", opcoes)


def Definir_Var_Ambiente():
    clear_screen()
    print_divisor_inicio_fim(
        '=== Operações com o arquivo de configuração de ambiente', 3)
    opcoes = [
        ("1 - Definir/Criar arquivo de configuração de ambiente em '.env' ",
         Criar_Var_Ambiente)
    ]
    return Menu("2 - Criar variáveis de ambiente", opcoes)


def Banco_Dados():
    clear_screen()
    print_divisor_inicio_fim('=== Operações com o banco de dados', 3)
    opcoes = [
        ("1 - Criar banco de dados", lambda: gerenciar_bancos('CriarBancoDados')),
        ("2 - Exibir banco de dados existentes",
         lambda: gerenciar_bancos('ListarBancoDados')),
        ("3 - !!!CUIDADO!!! Remover banco de dados dados_rfb existente...",
         lambda: gerenciar_bancos('ExcluirBancoDados'))
    ]
    return Menu("3 - Criar/Exibir/Remover banco de dados", opcoes)


def caminhosDeArquivos():
    clear_screen()
    print_divisor_inicio_fim('=== Operações com diretórios', 3)
    opcoes = [
        ("1 - Ler diretórios", lambda: gerenciar_diretorios('LerDiretorios')),
        ("2 - Criar diretórios", lambda: gerenciar_diretorios('CriarDiretorios')),
        ("3 - !!!CUIDADO!!! Excluir diretórios",
         lambda: gerenciar_diretorios('ExcluirDiretorios'))
    ]
    return Menu("4 - Criar/Ler/Excluir diretórios de arquivos", opcoes)


def executar_script_rfb():
    clear_screen()
    print_divisor_inicio_fim('=== Operações com o banco de dados', 3)
    opcoes = [
        ("1 - Baixar arquivos da RFB (Estabelecimentos) ", baixar_arq_rfb_estab),
        ("2 - Extrair arquivos da RFB (Estabelecimentos) ", descompactar_arq_rfb_estab),
        ("3 - Converter para Utf8, divisão de arquivos e criação da coluna cnpj completo",
         converter_utf8_arq_rfb_estab),
        ("4 - Inserir no banco de dados os dados da RFB", inserir_dados_estab_bd),
        ("5 - Verificar/remover valores repetidos", cnpj_repetidos_rfb),
        ("6 - Verificar/inserir valores faltantes", dados_faltantes_rfb),
        ("7 - Criar chaves primárias e estrangeiras", criar_indices_rfb),
        ("8 - Executar todos os passos acima em sequencia", sequencia_RFB)
    ]
    return Menu("5 - Executar downloads RFB", opcoes)


def baixar_dados_ibge():
    clear_screen()
    print_divisor_inicio_fim('=== Baixar dados extras dados', 3)
    opcoes = [
        ("1 - Baixar tabela municípios IBGE", municipios_ibge),
        ("2 - Baixar tabela população 2021", populacao_2022_ibge),
        ("3 - Baixar tabela PIB 2021", pib_ibge),
        ("4 - Baixar tabela área urbana 2019", area_ter_urb_ibge),
        ("5 - Baixar tabela área total 2020", total_area_ter_2022_ibge),
        ("6 - Baixar tabela CNAE detalhado", cnae_detalhado_ibge),
        ("7 - Inserir dados no banco", inserir_dados_ibge_bd),
        ("8 - Criar índices", criar_indices_ibge),
        ("9 - Executar sequência completa", sequencia_IBGE)
    ]
    return Menu("6 - Executar script IBGE", opcoes)


def baixar_dados_anp():
    clear_screen()
    print_divisor_inicio_fim('=== Baixar dados extras dados', 3)
    opcoes = [
        ("1 - Baixar dados revendedores combustíveis", postos_combustiveis_anp),
        ("2 - Inserir dados no banco", inserir_dados_anp_bd),
        ("3 - Verificar valores faltantes", dados_faltantes_anp),
        ("4 - Criar índices", criar_indices_anp),
        ("5 - Executar sequência completa", sequencia_anp)
    ]
    return Menu("7 - Executar script ANP", opcoes)


if __name__ == "__main__":
    try:
        Principal()
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário")
    except Exception as e:
        print(f"\nErro não esperado: {e}")
