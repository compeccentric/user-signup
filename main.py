from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True  


@app.route("/username", methods=['POST'])
def validate():
    user_name = request.form['username']
    p_word = request.form['pword']
    vp_word = request.form['vpword']
    e_mail = request.form['email']
    err_user_name=""
    err_p_word=""
    err_vp_word=""
    err_e_mail=""
    bcount=0   
    ccount=0
    if user_name == "":
        err_user_name="Please enter a valid username"
    if p_word == "":
        err_p_word="Please enter a valid password"
    if vp_word == "":
        err_vp_word="Please enter a valid password"
    for a in user_name: 
        if a.isspace(): 
            err_user_name="Username cannot have a space" 
        else:
            if len(user_name) < 3 or len(user_name) > 20:
                err_user_name="Username must be betwen 3 and 20 characters"
    for b in p_word: 
        if b.isspace(): 
            err_p_word="Password cannot have a space" 
        else:
            if len(p_word) < 3 or len(p_word) > 20:
                err_p_word="Password must be betwen 3 and 20 characters"
    if p_word != vp_word:
        err_vp_word="Passwords don't match"
    if e_mail !="":
        for a in e_mail: 
            if a.isspace(): 
                err_e_mail="Email cannot have a space"
        for b in e_mail:
            if b=="@":
                bcount += 1
        for c in e_mail:
            if c==".":
                ccount += 1        
        if bcount != 1:
            err_e_mail="Email needs to have one @"
        if ccount != 1:
            err_e_mail="Email needs to have one ."  
        if len(e_mail) < 3 or len(e_mail) > 20:
                err_e_mail="Email must be betwen 3 and 20 characters"

    if err_user_name=="" and err_p_word=="" and err_vp_word=="" and err_e_mail=="":
        return redirect('/welcome?username={0}'.format(user_name))
    return render_template("index.html", username=user_name,email=e_mail,
        eusername=err_user_name,epword=err_p_word,evpword=err_vp_word,eemail=err_e_mail)
    
#return render_template('welcome.html', username=user_name)

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('index.html')
@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)
app.run()