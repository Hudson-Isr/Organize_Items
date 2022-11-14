import os

#Lista das extensão dos arquivos.
audios_ext = ['.mp3','.wav'] #Se necessário, pode ser adicionado a extensão.
videos_ext = ['.mp4','.mov','.avi','.mkv']
imganes_ext = ['.jpg','.jpeg','.png','.gif','.bmp']
documentos_ext = ['.pdf','.txt','.log','.csv','.xlsx','.docx','.xls']
compat_ext = ['.rar','.zip']
instaladores_ext = ['.exe','.msi']

#Função para adquirir a extensão do arquivo.
def get_extension(name):
    idx = name.rfind('.')
    return name[idx:]

#Função para organizar os diretórios dos arquivos.
def organize(directory):
    AUDIOS_DIR = os.path.join(directory, "audios")
    IMAGENS_DIR = os.path.join(directory, "imagens")
    DOCS_DIR = os.path.join(directory, "documentos")
    VIDEOS_DIR = os.path.join(directory, "videos")
    INSTALADORES_DIR = os.path.join(directory, "instaladores")
    COMPAT_DIR = os.path.join(directory, "compatados")
    OUTROS_DIR = os.path.join(directory, "outros")

    #Lista das funções criadas
    list_dirs = [AUDIOS_DIR, IMAGENS_DIR, DOCS_DIR, VIDEOS_DIR, INSTALADORES_DIR, COMPAT_DIR, OUTROS_DIR]

    #Caso a pasta não esteja criar o for ficará responsável por criá-la
    for dir in list_dirs:
        if not os.path.isdir(dir):
            os.mkdir(dir)
    

    name_arq = os.listdir(directory)
    new_folder = ''
    for arq in name_arq:
        if os.path.isfile(os.path.join(directory, arq)):

            #Transformando a extensão do arquivo em letras minúsculas.
            extension = str.lower(get_extension(arq))

            #Atribuindo os arquivos em suas pastas respectivas.
            if extension in audios_ext:
                new_folder = AUDIOS_DIR
            elif extension in videos_ext:
                new_folder = VIDEOS_DIR
            elif extension in imganes_ext:
                new_folder = IMAGENS_DIR
            elif extension in documentos_ext:
                new_folder = DOCS_DIR
            elif extension in instaladores_ext:
                new_folder = INSTALADORES_DIR
            elif extension in compat_ext:
                new_folder = COMPAT_DIR
            else:
                new_folder = OUTROS_DIR

            old_folder = os.path.join(directory, arq)
            new = os.path.join(new_folder, arq)
            #O método renomeia o diretório para o destinatario novo
            os.rename(old_folder, new)

#Local onde o programas será executado.
organize(r"")