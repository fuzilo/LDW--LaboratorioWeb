## python run.py

from api import app

if __name__ == "__main__":
    app.run(debug=True)
    
#app.run(host='localhost', port=5000, debug=True)