# AWS JSON Resource checker

This code allows to check if in the JSON file the field Resource contains single '*'. The aim of it is to verify 
the input file and execute the method which checks one of the JSON's fields. 

The initial input file is *JSON.json* which can be found in the repository.
To use this code, install Python 3.12 and clone this whole repository to your device. 
To run the code for this file:

## From CMD (for Windows):
__Run main code__
1. Open CMD in the directory where the repository is saved. 
2. Type in command `python main.py` to see the result of the provided code. 

__Run tests for the code__
1. Open CMD in the directory where are the unittests: *..\aws_json_resource_checker\tests*
2. Type in command `python -m unittest` and then all the tests run.
3. To see verbose of the output type in `python -m unittest -v`.

## From PyCharm:
__Run main code__
1. Open *main.py*.
2. Hover over *Select Run/Debug Configuration* button and choose *main.py* or *Current File*.
3. Press button *Run*.

__Run tests for the code__
1. Open *tests\tests_main.py*.
2. Hover over *Select Run/Debug Configuration* button and choose *main.py* or *Current file*.
3. Press button Run to run all the tests or press *Run* button next to each test or class to check desired tests.