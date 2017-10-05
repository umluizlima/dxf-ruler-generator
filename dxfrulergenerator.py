#https://github.com/mozman/dxfwrite
from dxfwrite import DXFEngine as dxf

def drawRuler(length):
    file.add_layer('CUT', color = 7)
    file.add(dxf.rectangle([0, 0], 10 * length + 10, 30, layer = 'CUT'))
    

def drawMilimeter(cm):
    for mm in range(10):
        if mm == 0:
            file.add(dxf.rectangle([5 + 10 * cm + mm, 20], .25 , 10, layer = 'SCAN'))
        elif mm == 5:
            file.add(dxf.rectangle([5 + 10 * cm + mm, 25], .25 , 5, layer = 'SCAN'))
        else:
            file.add(dxf.rectangle([5 + 10 * cm + mm, 27.5], .25 , 2.5, layer = 'SCAN'))

def drawCentimeter(length):
    file.add_layer('SCAN', color = 5)
    for cm in range(length):
        drawMilimeter(cm)
    file.add(dxf.rectangle([5 + 10 * length, 20], .25 , 10, layer = 'SCAN'))
   
length = int(input('Ruler size (cm): '))
file = dxf.drawing('rulers/ruler_%dcm.dxf' %length)
file.header['$INSUNITS'] = 4
drawRuler(length)
drawCentimeter(length)
file.save()
