from PIL import Image
import os

# Diretório de entrada e saída
input_directory = 'images'
output_directory = 'outputImages'

# Tamanho desejado
desired_width = 500
desired_height = 500

# Certifique-se de que o diretório de saída existe
os.makedirs(output_directory, exist_ok=True)

# Função para redimensionar e centralizar uma imagem
def resize_and_center(input_path, output_path, width, height):
    image = Image.open(input_path)
    
    # Redimensionar a imagem mantendo a proporção
    image.thumbnail((width, height))
    
    # Calcular a posição central
    left = (width - image.width) // 2
    top = (height - image.height) // 2
    
    # Criar uma imagem com fundo transparente do tamanho desejado
    new_image = Image.new('RGBA', (width, height))
    
    # Colocar a imagem redimensionada no centro da imagem com fundo transparente
    new_image.paste(image, (left, top))
    
    # Salvar a imagem resultante
    new_image.save(output_path)

# Loop através de todas as imagens no diretório de entrada
for filename in os.listdir(input_directory):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        input_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, filename)
        resize_and_center(input_path, output_path, desired_width, desired_height)

print("Imagens redimensionadas e centralizadas com sucesso.")
