#https://github.com/mozman/dxfwrite
from dxfwrite import DXFEngine as dxf


'''
Constantes
'''
ruler_width = 30 #largura da régua
tick_width = .25 #largura de cada traço, em milimetros
tick_offset = 5 - tick_width / 2

'''
Funções
'''
#Cria uma camada na cor preta e desenha o contorno da régua
def drawRuler(ruler_length):
    file.add_layer('CUT', color = 7)
    file.add(dxf.rectangle([0, 0], 10 * ruler_length + 10, ruler_width, layer = 'CUT'))

#Cria uma camada na cor azul e chama a função que desenha os milimetros pelo
#número de vezes igual ao número de centímetros
def drawCentimeter(ruler_length):
    file.add_layer('SCAN', color = 5)
    for cm in range(ruler_length + 1):
        drawMilimeter(cm)

#Desenha cada marcação de um centímetro, com diferentes tamanhos para 0 e 5 milimetros
def drawMilimeter(cm):
    for mm in range(10):
        x_pos = tick_offset + 10 * cm + mm
        if mm == 0: #desenha o traço mais comprido na marcação de cada centímetro
            y_pos = 20
            file.add(dxf.text(str(cm), [x_pos - 1, 20], height = 2, rotation = 90, layer = 'SCAN'))
        elif mm == 5: #desenha o traço médio na marcação de cada meio centímetro
            y_pos = 25
        else: #desenha o traço curto na marcação de cada milimetro
            y_pos = 27.5
        file.add(dxf.rectangle([x_pos, y_pos], tick_width, ruler_width - y_pos, layer = 'SCAN'))
        if cm == ruler_length: break

'''
Programa principal
'''
ruler_length = int(input('Comprimento da régua (cm): '))
file = dxf.drawing('rulers/ruler_%dcm.dxf' %ruler_length)
file.header['$INSUNITS'] = 4
drawRuler(ruler_length)
drawCentimeter(ruler_length)
file.save()
