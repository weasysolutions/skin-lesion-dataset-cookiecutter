
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def data_augmentation(**kwargs):
    
    train_dir = kwargs['train_dir']
    save_to_dir = kwargs['save_to_dir']
    
    datagen = ImageDataGenerator(
                    rotation_range=180,
                    width_shift_range=0.1,
                    height_shift_range=0.1,
                    zoom_range=0.1,
                    horizontal_flip=True,
                    vertical_flip=True,
                    #brightness_range=(0.9,1.1),
                    fill_mode='nearest')
        
    aug_datagen = datagen.flow_from_directory(train_dir,
                                           save_to_dir,
                                           save_format='jpg',
                                           target_size=(224,224),
                                           batch_size = 50)

    
    
    
    tmp_dir = '../data/tmp'

    shutil.copytree(train_dir,tmp_dir)
    print(len(os.listdir(tmp_dir)))

    for subdir in os.listdir(tmp_dir):

        num_files = len(os.listdir(os.path.join(tmp_dir,subdir)))

        print( subdir, '  num_files:', num_files) 