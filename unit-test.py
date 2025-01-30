
"""
create unit tests for the Folders class in the /home/ubuntu/workshop-folder/Amazon-Q-workshop/polymorphism.py 
"""   
import unittest
from polymorphism import Folders

class TestFolders(unittest.TestCase):
    def test_create_folder(self):
        folders = Folders()
        self.assertEqual(folders.create_folder("test_folder"), "test_folder created successfully")

    def test_delete_folder(self):
        folders = Folders()
        self.assertEqual(folders.delete_folder("test_folder"), "test_folder deleted successfully")

    def test_share_folder(self):
        folders = Folders()
        self.assertEqual(folders.share_folder("test_folder"), "test_folder shared successfully")

if __name__ == '__main__':
    unittest.main()           
      



