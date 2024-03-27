import unittest
import sys
from json.decoder import JSONDecodeError

sys.path.append('..')

from main import JsonHandler
from utils import read_file

class TestInputFile(unittest.TestCase):
    def test_input_file_is_not_json(self):
        filename = 'test_sample_files/YAML.yaml'
        with self.assertRaises(JSONDecodeError):
            read_file(filename)

    def test_input_file_does_not_exist(self):
        filename = 'sample.json'
        with self.assertRaises(FileNotFoundError):
            read_file(filename)

    def test_input_file_is_empty(self):
        filename = 'test_sample_files/mock_iam_empty.json'
        with self.assertRaises(JSONDecodeError):
            read_file(filename)


class LoadedFile(unittest.TestCase):

    # it doesn't have '*' in Resource
    def test_file_has_no_resource(self):
        json_handler = JsonHandler('test_sample_files/mock_iam_no_resource.json')
        returned_value = json_handler.is_asterisk_resource()
        self.assertTrue(returned_value)

    def test_file_has_no_asterisk_in_resource(self):
        json_handler = JsonHandler('test_sample_files/mock_iam_no_asterisk_in_resource.json')
        returned_value = json_handler.is_asterisk_resource()
        self.assertTrue(returned_value)

    # it has '*' in Resource
    def test_file_has_resource_as_list(self):
        json_handler = JsonHandler('test_sample_files/mock_iam_list.json')
        returned_value = json_handler.is_asterisk_resource()
        self.assertFalse(returned_value)

    def test_file_has_single_resource_key(self):
        json_handler = JsonHandler('test_sample_files/mock_iam_string.json')
        returned_value = json_handler.is_asterisk_resource()
        self.assertFalse(returned_value)

    def test_file_has_two_resources_string(self):
        json_handler = JsonHandler('test_sample_files/mock_iam_two_resources_string.json')
        returned_value = json_handler.is_asterisk_resource()
        self.assertFalse(returned_value)

    def test_file_has_two_resources_list(self):
        json_handler = JsonHandler('test_sample_files/mock_iam_two_resources_list.json')
        returned_value = json_handler.is_asterisk_resource()
        self.assertFalse(returned_value)

    # it has more than one '*' in Resource
    def test_file_has_more_asterisks_in_resource(self):
        json_handler = JsonHandler('test_sample_files/mock_iam_more_asterisks_in_resource.json')
        returned_value = json_handler.is_asterisk_resource()
        self.assertTrue(returned_value)

    # it has more elements in Resource than just '*'
    def test_file_has_more_elements_in_resource_list(self):
        json_handler = JsonHandler('test_sample_files/mock_iam_more_elements_in_resource_list.json')
        returned_value = json_handler.is_asterisk_resource()
        self.assertTrue(returned_value)

    def test_file_has_more_elements_in_resource_string(self):
        json_handler = JsonHandler('test_sample_files/mock_iam_more_elements_in_resource_string.json')
        returned_value = json_handler.is_asterisk_resource()
        self.assertTrue(returned_value)


if __name__ == "__main__":
    unittest.main()
