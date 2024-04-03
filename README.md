# Remitly internship task
#### Artur Dwornik 

### Task: 
Write a method verifying the input JSON data. Input data format is defined as AWS::IAM::Role Policy - definition and example. Input JSON might be read from a file.
Method shall return logical false if an input JSON Resource field contains a single asterisk and true in any other case.

### Usage:
To use the verifier, You need to:

1. Install python3.
2. Clone this repository.
3. Open terminal in the repository folder.
4. Run the following command:
`python3 verify.py <file_path>`
where `<file_path>` is the path to the JSON file You want to verify.

### Tests:
To run tests, You need to:
1. Install python3.
2. Clone this repository.
3. Open terminal in the repository folder.
4. Run the following command:
`python3 test_verifier.py`
