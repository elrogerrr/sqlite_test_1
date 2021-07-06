from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///databases/tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db  = SQLAlchemy(app)

class Task(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(200))
    done=db.Column(db.Boolean)


@app.route('/')
def index():
    title='home'
    tasks=Task.query.all()
    return render_template('index.html', title=title, tasks=tasks)

@app.route('/create-task',methods=['POST'])
def createtask():
    title='home'
    task = Task(content=request.form['content'],done=False)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

