import glob
import os
from PIL import Image

#estensione delle immagini, directory di partenza e di destinazione
extension='.jpg'
path='/home/pviscone/Scrivania/WhatsApp Images'
destination='/home/pviscone/Scrivania/bianche/'

#setting del range rgb e della threshold sulla percentuale
r_under_threshold=150
r_up_threshold=255
g_under_threshold=150
g_up_threshold=255
b_under_threshold=150
b_up_threshold=255
percentage_threshold=0.3

for filename in glob.glob(os.path.join(path,'*'+extension)):
    print(filename.split('/')[-1])
    a=0
    try:
        im=Image.open(filename).convert('RGB')
        pix=im.load()
        w=im.size[0]
        h=im.size[1]
        for i in range(w):
            for j in range(h):
                if (pix[i,j][0]>r_under_threshold) and (pix[i,j][1]>g_under_threshold) and (pix[i,j][2]>b_under_threshold) and (pix[i,j][0]<r_up_threshold) and (pix[i,j][1]<g_up_threshold) and (pix[i,j][2]<b_up_threshold):
                    a=a+1
        if a/(w*h)>percentage_threshold:
            print('    MOVED    ')
            os.rename(filename,destination+filename.split('/')[-1])
    except:
        print ('!!ERROR!!')
    print(' ')
print('fine')
