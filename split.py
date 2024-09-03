import os
import random
import shutil

# Paths to your images and labels directories
images_dir = 'input_directory/images'  # Replace with the path to your images directory
labels_dir = 'output_directory'  # Replace with the path to your labels directory

# Paths to train and validation directories
train_images_dir = 'train/images'  # Replace with the path to your train/images directory
train_labels_dir = 'train/labels'  # Replace with the path to your train/labels directory
val_images_dir = 'val/images'      # Replace with the path to your val/images directory
val_labels_dir = 'val/labels'      # Replace with the path to your val/labels directory

# Create directories if they don't exist
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# List all image files
images = [f for f in os.listdir(images_dir) if f.endswith('.jpg') or f.endswith('.png')]

# Shuffle the images randomly
random.shuffle(images)

# Calculate the split index
split_index = int(len(images) * 0.8)

# Split into training and validation sets
train_images = images[:split_index]
val_images = images[split_index:]

# Move files to the respective directories
for image in train_images:
    # Move images
    shutil.move(os.path.join(images_dir, image), os.path.join(train_images_dir, image))
    # Move corresponding labels
    label = image.replace('.jpg', '.txt').replace('.png', '.txt')  # Adjust for your image format
    shutil.move(os.path.join(labels_dir, label), os.path.join(train_labels_dir, label))

for image in val_images:
    # Move images
    shutil.move(os.path.join(images_dir, image), os.path.join(val_images_dir, image))
    # Move corresponding labels
    label = image.replace('.jpg', '.txt').replace('.png', '.txt')  # Adjust for your image format
    shutil.move(os.path.join(labels_dir, label), os.path.join(val_labels_dir, label))

print(f'Training set: {len(train_images)} images')
print(f'Validation set: {len(val_images)} images')
