import os
import shutil

def filter_and_copy_images(input_folder, output_folder):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through each file in the input folder
    for filename in os.listdir(input_folder):
        # Check if file has '_syntesided.jpg' in its name
        if '_synthesized_image.jpg' in filename:
            # Build full path to the file
            source_path = os.path.join(input_folder, filename)
            destination_path = os.path.join(output_folder, filename)
            
            # Copy file to the output folder
            shutil.copy2(source_path, destination_path)
            print(f"Copied {filename} to {output_folder}")

# Specify the paths to the input and output folders
input_folder = '/scratch/ghoshs/large_files/pix2pixHD/datasets/NIR_plant/results/multispectral_nir_model/test_latest/images'
output_folder = '/scratch/ghoshs/large_files/FACT_LRDG/Dataset/Data/Multispectral/Plant'

# Call the function
filter_and_copy_images(input_folder, output_folder)
