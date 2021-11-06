# Importar bibliotecas
import cv2
from matplotlib import pyplot as plt

imagem = cv2.imread('imagem1.png', 0)  # se colocar ', 0' a imagem fica cinza

altura = imagem.shape[0]

largura = imagem.shape[1]

porcentagem = 40

nova_altura = int(altura * porcentagem / 100)

nova_largura = int(largura * porcentagem / 100)

dimensao = (nova_largura, nova_altura)

imagem_reduzida = cv2.resize(imagem, dimensao, interpolation=cv2.INTER_AREA)  # definir a dimensão da imagem

cv2.imwrite('imagem_cinza.png', imagem_reduzida)  # salvar uma nova imagem 

#imagem_rgb = cv2.cvtColor(imagem_reduzida, cv2.COLOR_BGR2RGB)  # função para converter de BGR para RGB

'''plotar imagem com matplotlib em bgr'''
#plt.imshow(imagem_rgb)
#plt.show()

'''plotar imagem com cv2 em grb'''
#cv2.imshow('IMAGEM', imagem_reduzida)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
