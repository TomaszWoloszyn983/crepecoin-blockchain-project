from website import create_app
from blockchain import get_chain

# app = create_app()
app = get_chain()

if __name__ == '__main__':
    app.run(debug=True)