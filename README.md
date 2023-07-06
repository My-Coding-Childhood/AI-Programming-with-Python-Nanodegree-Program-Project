# Udacity AI Programming with Python Nanodegree Program Project

# Image Classification for a City Dog Show

This project focuses on using Python programming skills to develop an image classifier for a citywide dog show. The goal is to identify dog breeds and evaluate different classification algorithms.

Project Description
The city dog show organizing committee requires participants to submit an image of their dog along with biographical information. The registration system tags the images based on the provided information. However, some participants may try to register non-dog pets as well.

The project involves using a pre-trained Python classifier to verify if the participants' images contain dogs. The main objectives are as follows:

Identify which pet images are of dogs, even if the breed is misclassified.
Classify the breed of dogs correctly for the images that are of dogs.
Determine the best convolutional neural network (CNN) model architecture (ResNet, AlexNet, or VGG) for achieving objectives 1 and 2.
Consider the runtime of each algorithm and evaluate alternative solutions for achieving satisfactory results within reasonable time constraints.
Project Files and Tasks
The project includes the following main files:

check_images.py: This file contains the main program logic and tasks that need to be completed. It uses other Python files and functions to achieve the objectives.
classifiers.py: This file provides the classifier function used for image classification.
dognames.txt: This file contains a list of dog breed names.
The tasks in check_images.py are organized into TODOs. Here is a summary of the tasks:

Timing Code: Implement timing code to measure the total program runtime.
Get program inputs: Use command line arguments to get user inputs.
Create Pet Images Labels: Generate labels for the pet images based on filenames and store them.
Create Classifier Labels and Compare Labels: Use the classifier function to classify images and compare the results with the pet image labels.
Classify Labels as "Dogs" or "Not Dogs": Classify all labels as either "Dogs" or "Not Dogs" using the dognames.txt file.
Calculate the Results: Determine the performance of the classification algorithms and calculate relevant statistics.
Print the Results: Display a summary of the results, including percentages of correct matches and classifications, and lists of misclassified dogs and breeds.
Project Execution
To run the project, execute the check_images.py file with the required command line arguments, such as the directory of pet images, the CNN model architecture to use, and the dog breed names file.


python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt

The program will process the images, classify them, and provide a summary of the results.

Results
After executing the program, you will see a summary of the classification results, including the number of images, the number of dog images, the number of non-dog images, and the percentages of correct matches and classifications.

Additionally, the program will display a list of incorrectly classified dogs and any misclassified dog breeds.

Conclusion
This project demonstrates the use of Python programming skills to develop an image classifier for a city dog show. By evaluating different CNN model architectures and considering runtime constraints, it aims to achieve accurate classification of dog images and their respective breeds.
