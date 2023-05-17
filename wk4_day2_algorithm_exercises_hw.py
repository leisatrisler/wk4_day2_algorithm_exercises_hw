# Exercises
# Exercise #1
# Write a function that takes a list of integers and returns the median value
import statistics

a_list_of_nums = [
    6,
    87,
    13,
    35,
    98,
]  # arbitrary set of numbers to find the median number


def get_median(nums):
    return statistics.median(
        nums
    )  # Using Python built in statistics to find median ffrom list of numbers


get_median(a_list_of_nums)


# Exercise #2
# Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.

# Example Output:{'in': 1, 'computing': 1, 'a': 5, ...}
a_text = "In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found"


def count_words(words):
    strip_words = []
    arr_words = words.split()  # Spilting the string into an array by words
    word_dict = {}

    for word in arr_words:
        w = word.replace(",", "")  # Stripping out comman and period
        w = w.replace(".", "")  # Replacing period with nothing
        strip_words.append(w)  # Adding stripped words to array of stripped words

    found_words = set(strip_words)  # set is to remove duplicate words

    for w in found_words:
        word_dict[w] = strip_words.count(w)
    print(word_dict)


count_words(a_text)

# Exercise #3
# Write a function implementing a Linear Search Algorithm. A linear search is a method for finding an element within a list. It sequentially checks each element of the list until a match is found or the whole list has been searched. If you do not find a match, return -1

awesome_list = [  # array of words
    "everything",
    "is",
    "awesome",
    "when",
    "you're",
    "part",
    "of",
    "a",
    "team",
]


def find_linear_element(element_list, element):  # iterate over list
    """iterate over the list and find the element specified"""
    for el in element_list:  #
        if el == element:
            return el  #
    return -1


print(
    find_linear_element(awesome_list, "team")
)  # look for the element or index with  "team" and return
print(find_linear_element(awesome_list, "I am groot"))  # return -1
