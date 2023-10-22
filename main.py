from pathlib import Path
from PyPDF2 import PdfReader

FOLDER = Path(__file__).parent
PASTA_NOVA = Path(__file__).parent / 'images'

def rmtree(root:Path):
    for file in root.glob('*'):

        #Caso seja um diretório é feito  recursividade
        if file.is_dir():
            rmtree(file)
        
        else:
            #Caso seja um arquivo .pdf
            if str(file).endswith('.pdf'):
                PASTA_NOVA.mkdir(exist_ok=True)
                CAMINHO_PDF = Path(__file__).parent / file
                reader = PdfReader(CAMINHO_PDF)

                pages = reader.pages
                
                #Pega todas as imagens da página 
                for i, page in enumerate(pages, start=1):
                    images = page.images
                    if images:
                        for image in images:
                            with open(PASTA_NOVA / image.name, 'wb') as fp:
                                fp.write(image.data)
                    else:
                        print(f'Nenhuma imagem encontrado na página {i}')

rmtree(FOLDER)
                    


            


            



