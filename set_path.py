import os.path

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
RESOURCES_DIR = os.path.join(CURRENT_DIR, 'resources')
ZIP_DIR = os.path.join(CURRENT_DIR, 'zip')
ZIP_FILE = os.path.join(ZIP_DIR, 'new_archive.zip')