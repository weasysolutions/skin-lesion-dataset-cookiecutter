import tensorflow

def model_archichecture():
    
    

mobile = tensorflow.keras.applications.mobilenet.MobileNet()

model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples // batch_size)

model.save_weights('first_try.h5')