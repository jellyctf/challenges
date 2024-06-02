import subprocess

if __name__ == "__main__":
    input_name = input("Enter your name: ")
    result = subprocess.check_output("python3 ./awafier.py " + input_name, shell=True, universal_newlines=True)
    print(result)
