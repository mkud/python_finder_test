# Objective

The purpose of this test is to give us a small sample of your code and to see how you approach and solve a simple problem. Ideally you should not spend more than an hour or two on this.

This is a simple class to extract matching strings from a list regardless of the characters order.

You will design & write a Python class that accepts a list of strings in the constructor. The class will expose a find function that accepts a string. The function will return all strings from the list that contain the exact same characters as the string passed into it. The order of the characters in the strings is not relevant.

For example, the constructor should take an array as follows:

	string_list = ['asd', 'asdd', 'fre', 'glk', 'lkm']; finder = Finder(string_list);

Calling `finder.find('sad')` should return a list containing the string `asd`.
In the case where more than one member of the initialization list matches the key the return list will have more than one member.

# Requirements

State your assumptions. Anywhere you feel that the requirements are unclear please make an assumption and document that assumption. Please comment your code where needed. Find the right balance between comments and self-documenting code. Code quality is of high importance. Strive to minimize the number of external dependencies The performance of your code matters, so please try to keep your code as optimized as possible. Choose a testing framework and write tests to showcase the quality of your solution, its performance (e.g. 50k+ runs, large initialization arrays etc.) and its edge cases. Deliver 3-4 bullet points detailing the reasons for choosing the testing framework Python 3, PEP 8

# Deliverables

python source-code and tests Instructions on how to run your project as well as tests Simple way of installing dependencies if needed Any other material that you feel is relevant for your solution