"""
Main.py
--------------
In this file we can control the entire situation.
Means that here we run the entire program, change constants, etc.

Written by:
"""
import os

from ExcelExporter import ExcelExporter
from Satisfaction import borda_count_evaluation, investment_evaluation
from Strategy import Strategy

"""
General Constants - relevant for the entire situation we run.
"""
# Number of strategies in the game.
NUM_OF_STRATEGIES = len(Strategy)

# Number of students.
NUM_OF_STUDENTS = 100

# Size of class.
CLASS_SIZE = 0

"""
Relevant for the each student.
"""
# Number of points each student have to share between courses.
POINTS_FOR_EACH_STUDENT = 100

# The satisfaction func each student use to evaluate his assignments.
SATISFACTION_FUNC = borda_count_evaluation

# Boolean value weather to upload the course list from a file.
UPLOAD_COURSES_LIST_FROM_FILE = False

# Boolean which indicates whether students has a random courses selection.
RANDOM_COURSES_SELECTION_FOR_EACH_STUDENT = False

"""
Technical Constants - relevant to data files and files uploading.
"""
# The name of the text file which Runner.py outputs the data to.
DATA_TEXT_FILE = "combinations_2.txt"

# The name of the excel file which ExcelExporter.py converts the data from the text file to.
DATA_EXCEL_FILE = ""


def main():
    """
    Runs the entire process.
    Also checks that the needed file exists.
    """

    # Check if text file exists.
    if not is_text_file_exist():
        get_text_file()

    # If text file exists, convert it to excel.
    if not is_excel_file_exist():
        get_excel_file()

    # todo : complete the other process which is needed (Graphs for example)

    return 0


# ---- Methods: ---- #

def is_text_file_exist():
    """
    Checks if the text file which includes the analysis of Runner.py exist in
    current directory.
    :return: boolean. true if exists, false otherwise.
    """
    return os.path.exists(DATA_TEXT_FILE)


def get_text_file():
    """
    If the text file doesn't exist, calls Runner.py to prepare the text file.
    """
    # todo
    return


def is_excel_file_exist():
    """
    Checks if the text file which includes the analysis of Runner.py exist in
    current directory.
    :return: boolean. true if exists, false otherwise.
    """
    return os.path.exists(DATA_EXCEL_FILE)


def get_excel_file():
    """
    If the excel file doesn't exist, calls ExcelExporter.py to prepare the text file.
    """
    exporter = ExcelExporter(DATA_TEXT_FILE, DATA_EXCEL_FILE)
    exporter.run()
    return


if __name__ == '__main__':
    main()