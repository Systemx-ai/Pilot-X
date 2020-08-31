
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from conv_vae import ConvVAE
from data_utils import read_dataset
import time
from scipy.stats import norm



# import tensorflow.keras
# from tensorflow.keras.layers import Conv2D, Conv2DTranspose, Input, Flatten, Dense, Lambda, Reshape
# from tensorflow.keras.layers import BatchNormalization
# from tensorflow.keras.models import Model

# from data_utils import read_dataset
# from tensorflow.keras.losses import binary_crossentropy

# import numpy as np
# import time
# from tensorflow.keras import backend as K   

#Load the data and read the data

# read data set
train_ds, valid_ds = read_dataset('prop/frames', test_size = 0.097)
print (train_ds.images().shape)
# print (train_ds.images().nbytes + valid_ds.images().nbytes) / (1024.0 * 1024.0), 'MB'

latent_dim = 10
batch_size = 50

# let's create ConvVAE
cvae = ConvVAE(latent_dim, batch_size)


# let's train ConvVAE
num_epochs = 10
interval = 200

saver = tf.train.Saver(max_to_keep = 2)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    t = time.time()
    # for num of epochs    
    while(train_ds.epochs_completed() < num_epochs):
        
        current_epoch = train_ds.epochs_completed()
        step = 0
        print ('[----Epoch {} is started ----]'.format(current_epoch))
        
        # take next batch until epoch is completed        
        while(train_ds.epochs_completed() < current_epoch + 1):
            input_images = train_ds.next_batch(batch_size)
            # do training step
            cvae.training_step(sess, input_images)
            step += 1
            
            if step % interval == 0:
                print ('loss: {} validation loss: {}'.format(cvae.loss_step(sess, input_images),\
                                                            cvae.loss_step(sess, valid_ds.next_batch(batch_size))))
                
        print ('[----Epoch {} is finished----]'.format(current_epoch))
        saver.save(sess, 'checkpoints/', global_step=current_epoch)
        print ('[----Checkpoint is saved----]')
     
    print ('Training time: {}s'.format(time.time() - t))
    # let's see how well our model reconstructs input images       
    input_images = train_ds.next_batch(batch_size)

    output_images = cvae.recognition_step(sess, input_images)
    output_images = output_images * 255
    output_images = output_images.astype(np.uint8)
    print ('Shape= ', output_images.shape)

    # Let's plot them!!!


import cv2
import numpy as np

 # choose codec according to format needed
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
video=cv2.VideoWriter('video.avi', fourcc, 1,(64,64))

for j in range(0,50):
    
    video.write(output_images[j])

cv2.destroyAllWindows()
video.release()