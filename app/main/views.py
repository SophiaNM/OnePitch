from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import UpdateProfile, PitchForm, CommentForm
from ..models import User, Role, Pitch, Comment
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

    pitch = Pitch.get_all_pitches()

    # print(all_pitches)

    title = 'Home | One Min Pitch'
    return render_template('index.html', title = title, pitch = pitch, interviewpitches = interviewpitches, productpitches = productpitches, promotionpitches = promotionpitches, businesspitches = businesspitches)



@main.route('/user/<uname>')
def profile(uname):
    '''
    View profile page function that returns the profile page and its data
    '''
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort (404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    '''
    View update profile page function that returns the update profile page and its data
    '''
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
    '''
    View update pic profile function that returns the uppdate profile pic page
    '''
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))



@main.route('/home', methods = ['GET', 'POST'])
@login_required
def home():
    '''
    View home function that returns the home page
    '''
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
    '''
    View pitch function that returns the pitch page and data
    '''
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


@main.route('/pitch/<int:pitch_id>/comment',methods = ['GET', 'POST'])
@login_required
def comment(pitch_id):
    '''
    View comments page function that returns the comment page and its data
    '''
    # comment_form = CommentForm()

    comment_form = CommentForm()
    my_pitch = Pitch.query.get(pitch_id)
    if my_pitch is None:
        abort(404)

    if comment_form.validate_on_submit():
        comment_content = comment_form.comment_content.data

        new_comment = Comment(comment_content=comment_content, pitch_id = pitch_id, user = current_user)
        new_comment.save_comment()

        return redirect(url_for('.comment', pitch_id=pitch_id))

    all_comments = Comment.query.filter_by(pitch_id=pitch_id).all()
    # all_comments = Comment.get_all_comments(id)
    # all_comments = Comment.get_all_comments(pitch_id)
    title = 'New Comment | One Min Pitch'

    return render_template('comment.html', title = title, pitch=my_pitch ,comment_form = comment_form, comment = all_comments )
