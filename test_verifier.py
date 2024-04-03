import unittest
from Verifier import Verifier

class TestVerifier(unittest.TestCase):
    def test_verify_json_resource_asterisk(self):
        #test1.json has a "Resource" field with single "*"
        self.assertFalse(Verifier.verify_json("./test_examples/test1.json"))

    def test_verify_json_resource_other(self):
        # test2.json has a "Resource" field with something other than single "*"
        self.assertTrue(Verifier.verify_json("./test_examples/test2.json"))

    def test_verify_json_invalid_json(self):
        # test3.json is not a valid json file
        with self.assertRaises(ValueError):
            Verifier.verify_json("./test_examples/test3.json")

    def test_verify_json_no_resource_field(self):
        # test3.json does not have a "Resource" field
        self.assertTrue(Verifier.verify_json("./test_examples/test4.json"))

    def test_verify_json_file_not_found(self):
        # path_not_existent.json does not exist
        with self.assertRaises(FileNotFoundError):
            Verifier.verify_json("path_not_existent.json")

if __name__ == '__main__':
    unittest.main()