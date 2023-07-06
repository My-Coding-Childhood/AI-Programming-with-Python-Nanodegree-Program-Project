#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# TODO 0: Add your information below for Programmer & Date Created.
# PROGRAMMER: Paschal Ugwu
# DATE CREATED: 06/07/2023
# REVISED DATE:
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task.
#          Note that the true identity of the pet (or object) in the image is
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results


# Main program function
def main():
    # Measure total program runtime by collecting start time
    start_time = time()

    # Retrieve command line arguments
    in_arg = get_input_args()

    # Retrieve pet labels using get_pet_labels function
    results = get_pet_labels(in_arg.dir)

    # Classify pet images using classify_images function
    classify_images(in_arg.dir, results, in_arg.arch)

    # Adjust results dictionary using adjust_results4_isadog function
    adjust_results4_isadog(results, in_arg.dogfile)

    # Calculate results statistics using calculates_results_stats function
    results_stats = calculates_results_stats(results)

    # Print results using print_results function
    print_results(results, results_stats, in_arg.arch, True, True)

    # Measure total program runtime by collecting end time
    end_time = time()

    # Compute overall runtime in seconds & print it in hh:mm:ss format
    tot_time = end_time - start_time
    hours = int(tot_time // 3600)
    minutes = int((tot_time % 3600) // 60)
    seconds = int(tot_time % 60)
    print("\n** Total Elapsed Runtime: {:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))


# Call to main function to run the program
if __name__ == "__main__":
    main()
