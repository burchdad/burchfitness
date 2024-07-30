import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms

# Define the generator and discriminator networks
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.main = nn.Sequential(
            nn.Linear(100, 256),
            nn.ReLU(),
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Linear(512, 784),
            nn.Tanh()
        )

    def forward(self, input):
        return self.main(input)

class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.main = nn.Sequential(
            nn.Linear(784, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )

    def forward(self, input):
        return self.main(input)

# Function to train the GAN
def train_gan(generator, discriminator, dataloader, epochs=50):
    criterion = nn.BCELoss()
    optimizer_g = optim.Adam(generator.parameters(), lr=0.0002)
    optimizer_d = optim.Adam(discriminator.parameters(), lr=0.0002)

    for epoch in range(epochs):
        for i, (data, _) in enumerate(dataloader):
            # Train Discriminator
            real_data = data.view(-1, 784)
            real_labels = torch.ones(real_data.size(0), 1)
            fake_labels = torch.zeros(real_data.size(0), 1)

            outputs = discriminator(real_data)
            d_loss_real = criterion(outputs, real_labels)
            real_score = outputs

            z = torch.randn(real_data.size(0), 100)
            fake_data = generator(z)
            outputs = discriminator(fake_data.detach())
            d_loss_fake = criterion(outputs, fake_labels)
            fake_score = outputs

            d_loss = d_loss_real + d_loss_fake
            optimizer_d.zero_grad()
            d_loss.backward()
            optimizer_d.step()

            # Train Generator
            z = torch.randn(real_data.size(0), 100)
            fake_data = generator(z)
            outputs = discriminator(fake_data)
            g_loss = criterion(outputs, real_labels)

            optimizer_g.zero_grad()
            g_loss.backward()
            optimizer_g.step()

        print(f'Epoch [{epoch+1}/{epochs}], d_loss: {d_loss.item()}, g_loss: {g_loss.item()}')

# Function to generate synthetic data
def generate_synthetic_data(generator, num_samples=100):
    z = torch.randn(num_samples, 100)
    synthetic_data = generator(z)
    return synthetic_data
