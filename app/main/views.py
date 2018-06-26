from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import UpdateProfile, PitchForm
from ..models import User, Role, Pitch
from flask_login import login_required, current_user
from .. import db, photos

# Views
@main.route('/',methods = ['GET', 'POST'])
def index():

    '''
    View root page function that returns the index page and its data
    '''
    interviewpitches = Pitch.query.filter_by(category="Interview-Pitch").order_by(Pitch.posted.desc()).all()
    productpitches = Pitch.query.filter_by(category="Product-Pitch").order_by(Pitch.posted.desc()).all()
    promotionpitches = Pitch.query.filter_by(category="Promotion-Pitch").order_by(Pitch.posted.desc()).all()
    businesspitches = Pitch.query.filter_by(category="Business-Pitch").order_by(Pitch.posted.desc()).all()
    # all_pitches = Pitch.get_all_pitches()
    pitch = Pitch.get_all_pitches()
    # print(all_pitches)

    title = 'Home | One Min Pitch'
    return render_template('index.html', title = title, pitch = pitch, interviewpitches = interviewpitches, productpitches = productpitches, promotionpitches = promotionpitches, businesspitches = businesspitches)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort (404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))


@main.route('/comment')
@login_required
def comment():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    return render_template('comment.html', title = title )





@main.route('/home', methods = ['GET', 'POST'])
@login_required
def home():
    # pitch_form = PitchForm()
    # pitch = get_pitch(id)
    # my_pitch = Pitch.query.get(id)

    # if pitch_form.validate_on_submit():
    #     pitch = pitch_form.pitch.data
    #     category = pitch_form.my_category.data
    #
    #     new_pitch = Pitch(pitch_desc=pitch, pitch_category = category, user = current_user)
    #     new_pitch.save_pitch()
    #
    #     return redirect(url_for('main.home'))
    # user = User.query.filter_by()
    interviewpitches = Pitch.query.filter_by(category="Interview-Pitch").order_by(Pitch.posted.desc()).all()
    productpitches = Pitch.query.filter_by(category="Product-Pitch").order_by(Pitch.posted.desc()).all()
    promotionpitches = Pitch.query.filter_by(category="Promotion-Pitch").order_by(Pitch.posted.desc()).all()
    businesspitches = Pitch.query.filter_by(category="Business-Pitch").order_by(Pitch.posted.desc()).all()
    # all_pitches = Pitch.get_all_pitches()
    pitch = Pitch.get_all_pitches()
    # print(all_pitches)

    title = 'Home | One Min Pitch'
    return render_template('home.html', title = title, pitch = pitch, interviewpitches = interviewpitches, productpitches = productpitches, promotionpitches = promotionpitches, businesspitches = businesspitches)


@main.route('/pitch/new',methods = ['GET','POST'])
@login_required
def pitch():
    pitch_form = PitchForm()

    if pitch_form.validate_on_submit():
        content = pitch_form.content.data
        category = pitch_form.category.data
        pitch_title = pitch_form.pitch_title.data

        new_pitch = Pitch(pitch_title=pitch_title, content=content, category = category, user = current_user)
        new_pitch.save_pitch()

        return redirect(url_for('main.index'))

    title = 'New Pitch | One Minute Pitch'
    return render_template('pitch.html', title = title, pitch_form = pitch_form,)
