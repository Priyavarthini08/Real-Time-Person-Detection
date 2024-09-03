import os

def filter_person_class(label_dir):
    # Loop through each label file in the directory
    for label_file in os.listdir(label_dir):
        if label_file.endswith('.txt'):
            label_path = os.path.join(label_dir, label_file)
            filtered_lines = []
            
            # Read the label file
            with open(label_path, 'r') as f:
                lines = f.readlines()
                
                # Filter out non-person annotations (keep only class ID 0)
                for line in lines:
                    class_id = int(line.split()[0])
                    if class_id == 0:  # Only keep class ID 0 (person)
                        filtered_lines.append(line)
            
            # Write the filtered annotations back to the file
            with open(label_path, 'w') as f:
                f.writelines(filtered_lines)

# Specify the directory where your label files are stored
label_directory = 'output_directory'

# Run the filtering function
filter_person_class(label_directory)

print("Filtering complete. Only 'person' class annotations are kept.")
