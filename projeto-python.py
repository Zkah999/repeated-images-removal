# PROJETO - Eliminar imagens repetidas numa galeria


import PIL
from PIL import Image
from PIL import ImageChops

# Preparar imagens
def prepara_imagem(imagem):
  imagem=imagem.resize([16,16])
  imagem=imagem.convert("L")
  return imagem

# Tamanho de imagem
def tamanho(imagem):
  tamanho=imagem.size
  return tamanho

# Nivel de diferenças
def diff(imagem1,imagem2):
  im=PIL.ImageChops.difference(imagem1,imagem2)
  return im
 
# Redimensionar e converter para cinza
ponte = Image.open("images/bridge.jpeg")
ponte_preparada = prepara_imagem(ponte)

gaivota = Image.open("images/seagull1.jpeg")
gaivota_preparada = prepara_imagem(gaivota)

# Saida de diferença
diferenca=diff(ponte_preparada,gaivota_preparada)

# Tamanho
tam=tamanho(diferenca)
largura=tam[0]
altura=tam[1]

def soma_pixeis(imagem):
  somapix=0
  for i in range(largura):
    for j in range(altura):
      somapix+=imagem.getpixel((i,j))
  return somapix

def cinzento_medio(imagem):
  n_pixeis=largura*altura
  cinza=soma_pixeis(imagem)/(n_pixeis)
  return cinza
 
# Percentagem da dif
def tom_medio_em_percentagem(cinza):
  nivel_cinza=(cinza*100)/255
  return nivel_cinza

# Nivel de diferença das imagens
def nivel_diferenca(imagem1,imagem2):
  dif=diff(imagem1,imagem2)
  cinz=cinzento_medio(dif)
  nivel_dif=tom_medio_em_percentagem(cinz)
  return nivel_dif

ponte = prepara_imagem(Image.open("images/bridge.jpeg"))
gaivota1 = prepara_imagem(Image.open("images/seagull1.jpeg"))
gaivota2 = prepara_imagem(Image.open("images/seagull2.jpeg"))


# Listar imagens

from pathlib import Path

def imagens(pasta):
  p=list((Path(pasta).glob("*.jpeg")))
  return p
  
for i in imagens("images"):
  img=Image.open(i)
  
def abre_pasta(pasta):
  for i in imagens(pasta):
    for j in imagens(pasta):
      print("Vou abrir as imagens: " + str(i) + " " + str(j)+"\n")
      im=Image.open(i)
      im1= prepara_imagem(im)
      im=Image.open(j)
      im2= prepara_imagem(im)
      if nivel_diferenca(im1,im2)<10 and str(i)!=str(j):
        print("Podes apagar " +str(i)+" ou "+str(j)+"\n")

print("")
print("GALERIA:")
print("")
abre_pasta("images")
abre_pasta("seagulls")
