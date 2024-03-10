# mikroblog.py
from app import app, db
from app.models import User, Post, Book

@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "User": User,
        "Post": Post,
        "Book": Book  # Dodajemy model Book do kontekstu konsoli
    }

def import_data_from_csv():
    with app.app_context():
        Book.load_from_csv('biblioteka.csv')  # Zastąp 'nazwa_pliku.csv' właściwą nazwą twojego pliku CSV

if __name__ == '__main__':
    import_data_from_csv()  # Uruchamiamy import danych z pliku CSV
    app.run()
