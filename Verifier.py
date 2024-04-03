import json
import os

class Verifier:
    @staticmethod
    def verify_json(file_path: str) -> bool:
        """
        Verifies if a AWS::IAM::Role Policy JSON file has a "Resource" field with a single "*"
        """
        # check if path exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Path {file_path} does not exist")
        
        # check if its a json
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
        except:
            raise ValueError(f"File {file_path} is not a valid JSON file")
        
        # check if "Resource" field is present in any statement and if so, if it is "*"
        for statement in data["PolicyDocument"]["Statement"]:
            if "Resource" in statement and statement["Resource"] == "*":
                return False
        return True

            