def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly
    classified dogs and incorrectly classified dog breeds if the user indicates
    they want those printouts.
    Args:
        results_dic - Dictionary with key as image filename and value as a list.
                       The list contains the pet image label (string) at index 0,
                       the classifier label (string) at index 1, the match result (int)
                       at index 2, the pet image 'is-a' dog result (int) at index 3,
                       and the classifier classifies image 'as-a' dog result (int) at index 4.
        results_stats_dic - Dictionary that contains the results statistics.
        model - CNN model architecture used.
        print_incorrect_dogs - Flag indicating whether to print incorrectly classified dog images.
        print_incorrect_breed - Flag indicating whether to print incorrectly classified dog breeds.
    Returns:
        None - simply printing results.
    """
    # Print summary results
    print("\nModel: {}".format(model))
    print("Number of Images: {}".format(results_stats_dic['n_images']))
    print("Number of Dog Images: {}".format(results_stats_dic['n_dogs_img']))
    print("Number of Non-Dog Images: {}".format(results_stats_dic['n_notdogs_img']))
    print("Percentage of Correct Matches: {:.1f}%".format(results_stats_dic['pct_match']))
    print("Percentage of Correct Dog Classifications: {:.1f}%".format(results_stats_dic['pct_correct_dogs']))
    print("Percentage of Correct Breed Classifications: {:.1f}%".format(results_stats_dic['pct_correct_breed']))
    print("Percentage of Correct Non-Dog Classifications: {:.1f}%".format(results_stats_dic['pct_correct_notdogs']))

    # Print incorrectly classified dogs
    if print_incorrect_dogs:
        print("\nIncorrectly Classified Dogs:")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 1:
                print("Pet Image: {}, Classifier Label: {}".format(results_dic[key][0], results_dic[key][1]))

    # Print incorrectly classified dog breeds
    if print_incorrect_breed:
        print("\nIncorrectly Classified Dog Breeds:")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
                print("Pet Image: {}, Classifier Label: {}".format(results_dic[key][0], results_dic[key][1]))

