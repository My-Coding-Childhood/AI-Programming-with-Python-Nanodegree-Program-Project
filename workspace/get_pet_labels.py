from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files.
    Parameters:
        image_dir - The (full) path to the folder of images (string)
    Returns:
        results_dic - Dictionary with 'key' as image filename and 'value' as a list.
                      The list contains the pet image label (string) at index 0.
    """
    # Get the list of files in the image directory
    filename_list = listdir(image_dir)
    
    # Create an empty dictionary to store the results
    results_dic = {}
    
    # Iterate through each file in the directory
    for filename in filename_list:
        # Skip files starting with a dot (hidden files)
        if filename.startswith('.'):
            continue
        
        # Extract the pet image label from the filename
        # Remove the file extension and split the filename into words
        file_label = filename.split('.')[0].lower().split('_')
        
        # Join the words in the label with spaces
        pet_label = ' '.join(file_label)
        
        # Add the filename and the pet label to the results dictionary
        results_dic[filename] = [pet_label]
    
    return results_dic
