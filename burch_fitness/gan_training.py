# core/gan_training.py
import torch
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
from gan import Generator, Discriminator, train_gan

# Load your dataset
data = np.load('path_to_your_data.npy')
data = torch.tensor(data, dtype=torch.float32)

# Create DataLoader
dataloader = DataLoader(TensorDataset(data), batch_size=64, shuffle=True)

# Initialize GAN
generator = Generator()
discriminator = Discriminator()

# Train GAN
train_gan(generator, discriminator, dataloader, epochs=50)

# Save the trained generator model
torch.save(generator.state_dict(), 'generator.pth')
