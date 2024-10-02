import os

# URL of the website to automate
URL = 'https://rtmnuresults.org/QuestionPaperSetDownload.aspx'

# Path to the Downloads folder
DOWNLOADS_PATH = os.path.join(os.path.expanduser("~"), "Downloads")

# Ignore values for dropdowns
IGNORE_VALUES = ['0', '-- Select --']

# Text to search in Exam dropdown
EXAM_SEARCH_TEXT = 'LL.B. 3'
