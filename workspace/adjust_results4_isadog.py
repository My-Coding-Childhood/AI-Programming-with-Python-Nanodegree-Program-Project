#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Paschal Ugwu
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if the classifier correctly
    classified images as 'a dog' or 'not a dog'.
    Args:
        results_dic - Dictionary with 'key' as image filename and 'value' as a list.
                      The list contains the pet image label (string) at index 0,
                      the classifier label (string) at index 1, and the match result (int)
                      at index 2.
        dogfile - A text file that contains names of all dogs.
                  Each dog name is in lowercase with spaces separating the distinct words
                  of the dog name. Dog names can be a string of dog names separated by commas
                  when a particular breed of dog has multiple dog names associated with it.
    Returns:
        None - results_dic is a mutable data type so no return needed.
    """
    dog_names = {}

    # Read the dog names from the dogfile and populate the dog_names dictionary
    with open(dogfile, 'r') as file:
        for line in file:
            for name in line.strip().split(','):
                dog_names[name.strip()] = 1

    # Iterate over the results dictionary
    for key in results_dic:
        # Check if the pet label is a dog
        pet_label_is_dog = 1 if results_dic[key][0] in dog_names else 0

        # Check if the classifier label is a dog
        classifier_label_is_dog = 1 if results_dic[key][1] in dog_names else 0

        # Update the results dictionary with the dog indicators
        results_dic[key].extend([pet_label_is_dog, classifier_label_is_dog])
