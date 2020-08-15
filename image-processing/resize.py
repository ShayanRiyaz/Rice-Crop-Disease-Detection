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
            
if '__main__' == __name__:
    input_path = '../input/RiceLeafs/train/Healthy'
    folder = 'train'
    column_name = 'Healthy'
    resize(input_path,folder,column_name)

    input_path = '../input/RiceLeafs/train/BrownSpot'
    folder = 'train'
    column_name = 'BrownSpot'
    resize(input_path,folder,column_name)

    input_path = '../input/RiceLeafs/train/Hispa'
    folder = 'train'
    column_name = 'Hispa'
    resize(input_path,folder,column_name)

    input_path = '../input/RiceLeafs/train/LeafBlast'
    folder = 'train'
    column_name = 'LeafBlast'
    resize(input_path,folder,column_name)

    print('Done with train resizing')

     ## VALIDATION
    input_path = '../input/RiceLeafs/validation/Healthy'
    folder = 'validation'
    column_name = 'Healthy'
    resize(input_path,folder,column_name)

    input_path = '../input/RiceLeafs/validation/BrownSpot'
    folder = 'validation'
    column_name = 'BrownSpot'
    resize(input_path,folder,column_name)

    input_path = '../input/RiceLeafs/validation/Hispa'
    folder = 'validation'
    column_name = 'Hispa'
    resize(input_path,folder,column_name)

    input_path = '../input/RiceLeafs/validation/LeafBlast'
    folder = 'validation'
    column_name = 'LeafBlast'
    resize(input_path,folder,column_name)

    print('Done with Validation resizing')
