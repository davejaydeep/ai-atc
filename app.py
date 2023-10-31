from dotenv import load_dotenv
from application.factory import create_app
from waitress import serve

load_dotenv()

app = create_app()

if __name__ == "__main__":   
    serve(app, host="0.0.0.0", port=5001)