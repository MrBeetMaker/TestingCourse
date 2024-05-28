### Introduction
Links to an external site. module implements binary protocols for serializing and de-serializing a Python object structure. “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream (from a binary file Links to an external site. or bytes-like object Links to an external site.) is converted back into an object hierarchy. Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” [1] Links to an external site. or “flattening”; however, to avoid confusion, the terms used here are “pickling” and “unpickling”. [source Links to an external site.]

## Assignment
I would like to understand how stable and correct pickle is: Does the same input always create the same (serialized) output? We define the same input and output as hash-identical (equivalent is insufficient). This means an input must create the same pickle file under all circumstances. Possible options are different operating systems, different Python (but not pickle) versions, floating point accuracy, and recursive data structures. 

Please keep your mind open to other options. Please make sure to consider only the exact same input: Of course, if you alter the input (e.g., x = 2+3 to x = 3+2 or renaming variables), the results may be equivalent but are no longer identical when you hash the resulting pickle file (e.g., sha256).


## Your task is to develop a test suite for the stability and correctness of the pickle. 
## All results and findings must be reproducible.


###  Final report
Your team must submit a final report. Your final report
- discusses your test suite, including applied strategies.
- discusses the completeness of your test suite through a traceability matrix.
- discusses the findings of your test suite.
- discusses the limitations and shortcomings of your test suite.

Your final report does not exceed 8 pages and lists all team members and their contributions to the report and code in detail. Your code must comply with the PEP8 coding style guidelines and must be available on GitHub or Gitlab or similar. Please provide a link to your repository.


        .
-
.



## Student Project Award
For outstanding achievements, the student team(s) with the best final report and best findings will not only be awarded with the glorious and prestigious best student project award in PA1465 with all its fame and glory but also will be invited for a beer (and non-alcoholic beverages).
Some pointer

    https://stackoverflow.com/questions/985294/is-the-pickling-process-deterministic 

Links to an external site.
https://stackoverflow.com/questions/21271479/python-pickle-not-one-to-one-different-pickles-give-same-object
Links to an external site.
https://stackoverflow.com/questions/75927084/are-pickle-files-reproducible