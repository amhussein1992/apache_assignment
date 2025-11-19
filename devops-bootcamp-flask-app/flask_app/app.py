from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
from models import db, User, Post
from config import Config

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

@app.route('/')
def index():
    # Get all users
    users = User.query.all()
    
    # Get latest 5 posts (CHANGED: Show only latest 5)
    posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
    
    return render_template('index.html', users=users, posts=posts)

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    bio = request.form.get('bio')  # NEW FIELD
    
    # Check for duplicate email
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        flash('A user with this email already exists. Please use another email.', 'error')
        return redirect(url_for('index'))
    
    # Create new user
    new_user = User(name=name, email=email, bio=bio)
    db.session.add(new_user)
    db.session.commit()
    
    flash('User registered successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/add_post', methods=['POST'])
def add_post():
    title = request.form.get('title')
    content = request.form.get('content')
    user_id = request.form.get('user_id')
    
    new_post = Post(title=title, content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    
    flash('Post added successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)