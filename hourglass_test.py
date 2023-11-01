
import torch
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt

def hourglass_test():
    
    # Charger le modèle pré-entraîné (remplacez par le chemin de votre modèle)
    model = torch.load('checkpoints/checkpoint.pt')
    model.eval()
    
    # Charger l'image
    image = Image.open('pixIn/30.png')
    
    # Prétraiter l'image
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
    ])
    image = transform(image).unsqueeze(0)
    
    # Faire passer l'image dans le modèle
    with torch.no_grad():
        output = model(image)
    
    # Visualiser les résultats
    # (Remplacez cette partie par le code approprié pour visualiser vos résultats)
    # Par exemple, si output est une heatmap, vous pouvez utiliser plt.imshow pour la visualiser
    heatmap = output[0, 0].numpy()
    plt.imshow(heatmap, cmap='hot', interpolation='nearest')
    plt.show()

if __name__ == "__main__":
    hourglass_test()
    