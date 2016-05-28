import dateutil.parser

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_adminlte import AdminLTE
from .forms import EmailPasswordForm


class User(object):

    full_name=""
    avatar=""
    created_at=dateutil.parser.parse("May 18, 2016")
    msg_count=0
    
    def changetype(self, userType):

        if(userType=='admin'):
            self.full_name = "Sachin Bhat"
            self.avatar = "/static/sachin.jpg"
            self.created_at = dateutil.parser.parse("May 18, 2016")
            self.msg_count = 4
        elif(userType=='user'):
            self.full_name = "Rutika Muchhala"
            self.avatar = "/static/rutika.jpg"
            self.created_at = dateutil.parser.parse("May 22, 2016")
            self.msg_count = 3

def create_app(configfile=None):
    app = Flask(__name__)
    AdminLTE(app)
    app.config.from_object('config')
    current_user = User()

    @app.route('/', methods=["GET","POST"])
    def index():
        
        form = EmailPasswordForm()
        if form.validate_on_submit():
            if form.data['email']=="admin@shipeasy.com" and form.data['password']=="admin":
                current_user.changetype('admin')
                return redirect(url_for('login', current_user=current_user))
            elif form.data['email']=="user@shipeasy.com" and form.data['password']=="user":
                current_user.changetype('user')
                return redirect(url_for('login', current_user=current_user))
            else:
                flash('wrong username/password')
        return render_template('index.html', form=form)

    @app.route('/login')
    def login():
        return render_template('dashboard2.html', current_user=current_user)

    @app.route('/invoice')
    def invoice():
        return render_template('pages/examples/invoice.html', current_user=current_user)

    @app.route('/track')
    def calendar():
        return render_template('pages/track.html', current_user=current_user)

    @app.route('/quote')
    def quote():
        return render_template('pages/quote.html', current_user=current_user)

    @app.route('/simpleTable')
    def simpleTable():
        return render_template('pages/tables/simple.html', current_user=current_user)

    @app.route('/dataTable')
    def dataTable():
        return render_template('pages/tables/data.html', current_user=current_user)

    @app.route('/profile')
    def profile():
        return render_template('pages/examples/profile.html', current_user=current_user)

    @app.route('/mailbox')
    def mailbox():
        return render_template('pages/mailbox/mailbox.html', current_user=current_user)

    @app.route('/rates')
    def rates():
        return render_template('pages/tables/data.html', current_user=current_user)

    @app.route('/contact')
    def contact():
        return render_template('pages/contact.html', current_user=current_user)

    @app.route('/shipments')
    def shipments():
        return render_template('pages/tables/data.html', current_user=current_user)

    @app.route('/dummy')
    def dummy():
        return render_template('pages/dummy.html', current_user=current_user)

    @app.route('/readMail')
    def readMail():
        return render_template('pages/mailbox/read-mail.html', current_user=current_user)

    @app.route('/compose')
    def compose():
        return render_template('pages/mailbox/compose.html', current_user=current_user)

    return app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    create_app().run(debug=True,host='0.0.0.0', port=port)
    
