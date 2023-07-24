import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)


from src import create_app

app = create_app()

if __name__ == '__main__':
    # with app.app_context():
    #     app.db.create_all()
    app.run(debug=True, port=5555)
