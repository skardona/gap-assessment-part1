# gap-assessment-part1

## Largest word algorithm
  
Largest word algorithm was implemented as a function inside package file_processor. You can just import it , call it and pass a file path as an argument to the function in order to find the largest word like this:

    from file_processor import get_largest_word_reversed
    
    get_largest_word_reversed("file_relative_path")

Unit tests for the algorithm were created as well inside **test_largest_word_reversed.py** file. They can be run either from your IDE of preference or from a command line using the python virtual environment.

Once you've [activated the venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#activating-a-virtual-environment), you can run the tests on command line:

    python -m unittest test_largest_word_reversed.py
