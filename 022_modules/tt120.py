#"main.py"

from framework.http.response import as_json


def main():
    print(as_json('Hello, World!'))


if __name__ == '__main__':
    main()

# {"message": "Hello, World"}