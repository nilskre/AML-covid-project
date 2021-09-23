""" Module for hyperparameters """
# Training hyperparameters
num_epochs_pretraining = 50
num_epochs_training = 500
batch_size = 32
learning_rate_pretraining = 5e-3
learning_rate_generator = 1e-3
learning_rate_discriminator = 3e-5
save_model_every = 10

# Model hyperparameters
embedding_size = 32  # Must be dividable by 4 and num_heads
num_heads = 8
num_encoder_layers = 3
num_decoder_layers = 3
dropout = 0.10
dim_feed_forward = 64

# Models
pretraining_model = "20_09_2021_17_59_10.pth.tar"
training_model = "20_09_2021_17_33_20.pth.tar"
evaluation_model = "23_09_2021_23_01_50.pth.tar"
