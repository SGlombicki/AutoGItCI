from flask import Flask
import GitCommands
app = Flask(__name__)

@app.route('/update')
def update():
    GitCommands.gitChange()
    return 'Good'

if __name__ == '__main__':
    app.run()
