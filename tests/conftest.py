import os.path
import shutil
from zipfile import ZipFile

import pytest

from set_path import ZIP_DIR, RESOURCES_DIR, ZIP_FILE


@pytest.fixture(scope='session', autouse=True)
def test_create_zip_archive():
    if not os.path.exists(ZIP_DIR):
        os.mkdir(ZIP_DIR)
    with ZipFile(ZIP_FILE, 'w') as zip_file:
        for file in os.listdir(RESOURCES_DIR):
            zip_file.write(os.path.join(RESOURCES_DIR, file), file)

    yield

    shutil.rmtree(ZIP_DIR)

