from flask import render_template, url_for, redirect, session
from shorturl.forms import MainForm
from shorturl.model import Reg
from shorturl import app, db
import string
import random


def genRandUrl(length=8):
    var = string.ascii_letters + string.digits
    shortkey = ''
    for i in range(length):
        shortkey += random.SystemRandom().choice(var)
    return shortkey


@app.route("/", methods=['GET', 'POST'])
def mai():
    form = MainForm()
    if form.validate_on_submit():
        website = form.website.data
        sulg = form.slug.data
        session['website'] = website
        print(website, sulg)
        if sulg == '':
            print("ohhhhh")
            session['slug'] = genRandUrl()
        else:
            session['slug'] = form.slug.data
        form.website.data = ''
        form.slug.data = ''

        enty = Reg(website=session['website'], slug=session['slug'])
        db.session.add(enty)
        db.session.commit()
        return redirect(url_for('site'))

    return render_template('home.html', form=form)


@app.route("/site")
def site():
    if 'website' in session:
        temp = url_for('site', _external=True)
        temp = temp.split("site")
        temp = temp[0] + session['slug']
        session.pop('website', None)
        session.pop('slug', None)
        return render_template('site.html', site=temp)
    else:
        return redirect(url_for('mai'))


@app.route("/<re>")
def redir(re):
    query = Reg.query.filter_by(slug=re).first()
    if query is None:
        return render_template('error.html')
    else:
        web = query.website
        return redirect(web)



