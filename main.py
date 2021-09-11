from api.app import app
from dotenv import load_dotenv
load_dotenv()


def main():
    app.run()


if __name__ == "__main__":
    main()
