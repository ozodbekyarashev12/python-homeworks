from PIL import Image
import numpy as np

# Load the image using PIL
image_path = 'images/birds.jpg'
image = Image.open(image_path)

# Convert the image to a NumPy array
image_array = np.array(image)

# Function to flip the image horizontally and vertically
def flip_image(image_array):
    # Flip horizontally and vertically
    flipped_image = np.flipud(np.fliplr(image_array))
    return flipped_image

# Function to add random noise to the image
def add_noise(image_array, noise_factor=0.1):
    # Generate random noise
    noise = np.random.randn(*image_array.shape) * noise_factor * 255
    noisy_image = np.clip(image_array + noise, 0, 255).astype(np.uint8)
    return noisy_image

# Function to brighten the red channel of the image
def brighten_channels(image_array, increase_value=40):
    # Increase the brightness of the red channel (index 0)
    image_array[:, :, 0] = np.clip(image_array[:, :, 0] + increase_value, 0, 255)
    return image_array

# Function to apply a black mask to a region
def apply_mask(image_array, mask_size=(100, 100), top_left=(150, 150)):
    # Set the region to black (0, 0, 0)
    x, y = top_left
    h, w = mask_size
    image_array[x:x+h, y:y+w] = 0
    return image_array

# Flip the image
flipped_image = flip_image(image_array)

# Add random noise
noisy_image = add_noise(image_array)

# Brighten the red channel
brightened_image = brighten_channels(image_array.copy())

# Apply a mask to the center region
masked_image = apply_mask(image_array.copy())

# Convert the manipulated images back to PIL Images and save them
Image.fromarray(flipped_image).save('flipped_image.jpg')
Image.fromarray(noisy_image).save('noisy_image.jpg')
Image.fromarray(brightened_image).save('brightened_image.jpg')
Image.fromarray(masked_image).save('masked_image.jpg')
