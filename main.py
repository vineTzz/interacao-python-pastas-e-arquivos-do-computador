# Importar Bibliotecas e Criar Arquivo #
from pathlib import Path
import shutil

caminho = Path(r'C:\Users\alxia\OneDrive\Área de Trabalho\github\Integração pyhton + Arquivos e Pastas do Computador\Arquivos_Lojas')
arquivos = caminho.iterdir()

# Verificando se um Arquivo Existe #
if (caminho / Path('202004_Shopping Cidade_MG.csv')).exists():
    print('Arquivo Existe')

# Criar Pasta no Computador #
#Path(r'C:\Users\alxia\OneDrive\Área de Trabalho\github\Integração pyhton + Arquivos e Pastas do Computador\Pasta Auxiliar\Pasta2').mkdir()

# Criar Cópia de Arquivo e Mover para Pasta que Criamos #
arquivo_copiar = (caminho / Path('202004_Shopping Cidade_MG.csv'))
arquivo_mover = Path(r'C:\Users\alxia\OneDrive\Área de Trabalho\github\Integração pyhton + Arquivos e Pastas do Computador\Pasta Auxiliar\copia_202004_Shopping Cidade_MG.csv')
shutil.copy2(arquivo_copiar, arquivo_mover)

# Movendo um Arquivo em definitivo para uma Pasta #
arquivo_para_mover = arquivo_mover
arquivo_onde_mover = Path(r'C:\Users\alxia\OneDrive\Área de Trabalho\github\Integração pyhton + Arquivos e Pastas do Computador\Pasta Auxiliar\Pasta2')
shutil.move(arquivo_para_mover, arquivo_onde_mover)
