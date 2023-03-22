from config import app, login
from flask import render_template, flash, redirect, url_for, request, make_response
# from flask_migrate import Migrate
from forms import LoginForm,  RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from models import User, db
from prompts_v3 import prompt_maker, model_builder, question_writer
# migrate = Migrate(app,db)
login.login_view = 'login'

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home Page')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', category = 'error')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user! Please sign in.', category = 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles', methods = ['POST', 'GET'])
def articles():
    if request.method == 'POST':
        questions = False
        user_input = []
        words = ""
        form_data = request.form
        print("form data" , form_data)
        for item in form_data.items():
            user_input.append(item)
        genre = user_input[0][1]
        topic = user_input[1][1]
        words = user_input[2][1]
        topic.strip()
        words.strip()
        if len(user_input)>3:
            if user_input[3][1] == "on":
                questions=True

        prompt = prompt_maker(genre, topic, words)
        text= model_builder(genre, prompt)
        if questions ==True:
            questions_prompt = question_writer(genre, text)
            print("question prompt" , questions_prompt)
            question_text = model_builder("write_questions", questions_prompt)
            return render_template('articles.html', genre = genre, topic = topic, main_text = text, question_text = question_text)
        else:
            question_text = " "
            return render_template('articles.html', genre = genre, topic = topic, main_text = text, question_text = question_text)




@app.route('/download_text', methods=['GET', 'POST'])
def download_text():
    text = request.form['text']
    response = make_response(text)
    response.headers.set('Content-Disposition', 'attachment', filename='text.txt')
    response.headers.set('Content-Type', 'text/plain')
    return response

# for dialog, temperature high (0.95) frequence penalty high (0.75)
# for article temperature(0.7), frequency penalty 0
