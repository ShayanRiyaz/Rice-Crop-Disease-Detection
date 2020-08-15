from PIL import Image
import os

def resize(input_path,folder,column_name):
    dirs = os.listdir(input_path)
    for item in dirs:
        item_path = input_path +'/' +item
        if os.path.isfile(item_path):
            #print('CHECK')
            im = Image.open(item_path)

            # Check whether the specified 
            # path exists or not 
            outpath = f'{folder}/{column_name}'
            temp_out_path = outpath+'/'+item
            f, e = os.path.splitext(temp_out_path)

            imResize = im.resize((150,150), Image.ANTIALIAS)
            #print('CHECK 3')
            imResize.save(f + '.jpg', 'JPEG', quality=90)



