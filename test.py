
# Define transforms (resize, normalize, convert to tensor)
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5]*3, std=[0.5]*3)  # Normalize RGB
])

# Load dataset
dataset = datasets.ImageFolder(root='data/', transform=transform)

# Wrap in DataLoader
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# Example: iterate through one batch
for images, labels in dataloader:
    print(images.shape)  # [32, 3, 224, 224]
    print(labels.shape)  # [32]
    break