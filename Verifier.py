import json
import os
import re

class Verifier:
    @staticmethod
    def verify_json(file_path: str) -> bool:
        """
        Verifies if a AWS::IAM::Role Policy JSON file has a "Resource" field with a single "*"
        """
        # check if path exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Path {file_path} does not exist")
        
        # check if its a JSON
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
        except:
            raise ValueError(f"File {file_path} is not a valid JSON file")
        
        # check if the JSON file is AWS::IAM::Role Policy JSON file
        if not Verifier.__check_Role_Policy_format(data):
            raise ValueError(f"File {file_path} is not a valid AWS::IAM::Role Policy JSON file")
        
        # check if "Resource" field is present in any statement and if so, if it is "*"
        for statement in data["PolicyDocument"]["Statement"]:
            if "Resource" in statement and statement["Resource"] == "*":
                return False
        return True
    
    @staticmethod
    def __check_Role_Policy_format(data: dict) -> bool:
        """
        Check if the JSON file is AWS::IAM::Role Policy JSON file
        """
        # Check if "PolicyName" and "PolicyDocument" keys exist
        if "PolicyName" not in data or "PolicyDocument" not in data:
            return False

        # Check if "PolicyDocument" is a JSON
        if not isinstance(data["PolicyDocument"], dict):
            return False

        # Check if "PolicyName" is a string
        if not isinstance(data["PolicyName"], str):
            return False

        # Check if "PolicyName" matches the pattern and its length is between 1 and 128
        if not re.match(r'^[\w+=,.@-]+$', data["PolicyName"]) or not (1 <= len(data["PolicyName"]) <= 128):
            return False
        return True

            