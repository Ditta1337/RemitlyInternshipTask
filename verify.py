import sys
from Verifier import Verifier

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 verify.py <file_path>")
        sys.exit(-1)

    file_path = sys.argv[1]
    print(f"File {file_path} is {'Valid' if Verifier.verify_json(file_path) else 'Invalid'}")
    
    sys.exit(0)