from flask import jsonify

from app.libs.redprint import RedPrint
from app.models.comment import Comment

api = RedPrint('comment')


@api.route('/<int:pid>', methods=['GET', 'POST'])
def get_comment(pid):
    comments = Comment.get_comment_by_pid(pid)
    return jsonify(comments)