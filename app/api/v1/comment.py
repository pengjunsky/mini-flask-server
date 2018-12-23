from flask import jsonify, g

from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.comment import Comment
from app.validators.params import Count, CreateCommentValidator

api = RedPrint('comment')


@api.route('/<int:pid>', methods=['GET', 'POST'])
def get_comment(pid):
    form = Count().validate_for_api()
    comments = Comment.get_comment_by_pid(pid, form.count.data, form.page.data)
    return jsonify(comments)


@api.route('/create', methods=['GET', 'POST'])
@auth.login_required
def create_comment():
    uid = g.user.uid
    form = CreateCommentValidator().validate_for_api()
    Comment.create_by_comment(uid, form.order_id.data, form.comment.data)
    return Success(msg='评论成功')