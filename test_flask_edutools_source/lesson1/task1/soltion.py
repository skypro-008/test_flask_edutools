from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    page_content = ""
    # раскомментируйте строчку ниже
    # page_content = "It works!"
    return page_content


if __name__ == '__main__':
    app.run()



