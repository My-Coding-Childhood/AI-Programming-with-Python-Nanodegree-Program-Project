from classifier import classifier

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels using the classifier function, compares pet labels to
    the classifier labels, and adds the classifier label and the comparison of the labels
    to the results dictionary.
    Args:
        images_dir - The (full) path to the folder of images that are to be classified (string)
        results_dic - Results Dictionary with 'key' as image filename and 'value' as a list.
                      The list contains the pet image label (string) at index 0.
                      The classifier label (string) will be added at index 1.
                      The match result (int) will be added at index 2.
        model - Indicates the CNN model architecture used by the classifier function (string)
    Returns:
        None - results_dic is a mutable data type so no return needed.
    """
    for key in results_dic:
        # Create the image file path
        image_path = images_dir + key
        
        # Use the classifier function to get the classifier label
        classifier_label = classifier(image_path, model).lower().strip()
        
        # Get the pet label from the results dictionary
        pet_label = results_dic[key][0]
        
        # Compare the pet label and the classifier label
        match = 1 if pet_label in classifier_label else 0
        
        # Add the classifier label and the match result to the results dictionary
        results_dic[key].extend([classifier_label, match])