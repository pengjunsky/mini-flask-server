from flask import jsonify

from app.libs.redprint import RedPrint
from app.models.comment import Comment
from app.validators.params import Count

api = RedPrint('comment')


@api.route('/<int:pid>', methods=['GET', 'POST'])
def get_comment(pid):
    form = Count().validate_for_api()
    comments = Comment.get_comment_by_pid(pid, form.count.data, form.page.data)
    return jsonify(comments)