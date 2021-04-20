import os
import shutil
import unittest

from file_sync import file_sync


class TestFileSync(unittest.TestCase):
    def test_copy_one_file(self):
        source_dir_name = "source_dir"
        target_dir_name = "target_dir"

        os.mkdir(source_dir_name)
        os.mkdir(target_dir_name)

        file_name = "file_1.txt"
        file_contents = "file contents"
        with open(f"{source_dir_name}/{file_name}", "w") as source_file:
            source_file.write(file_contents)

        try:
            file_sync(source_dir=source_dir_name, target_dir=target_dir_name)
            self.assertTrue(os.path.isfile(f"{target_dir_name}/{file_name}"))

            with open(f"{target_dir_name}/{file_name}", "r") as target_file:
                target_file_contents = target_file.read()
                self.assertEqual(file_contents, target_file_contents)
        finally:
            shutil.rmtree(source_dir_name)
            shutil.rmtree(target_dir_name)

