from flask import Flask,render_template
app = Flask(__name__)


all_posts=[
    {
        'title':'First Post',
        'content':'Hello world!',
        'author': 'Sai'
    },
    {
        'title':'2nd Post',
        'content':'Hello Universe!',
        'author': 'Chandran'
    }
]


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html',posts=all_posts)


if __name__=="__main__":
    app.run(debug=True)