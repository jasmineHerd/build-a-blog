from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:launchcode@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(400))
    
    def __init__(self,title,body):
        self.title = title
        self.body = body


    

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        task_name = request.form['formName']
        blog_bodys = request.form['blogformname']
        new_task = Blog(task_name,blog_bodys)
        db.session.add(new_task,blog_bodys)
        db.session.commit()



    

    return render_template('blog.html',title="Build A Blog!")

@app.route('/blog', methods= ['POST','GET'])
def displayBlogs():

    blogs= Blog.query.all()
    return render_template('blogdisplay.html',title_entry=blogs, blogs_entry=blogs)



if __name__ == '__main__':
    app.run()