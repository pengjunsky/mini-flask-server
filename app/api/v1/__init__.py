from flask import Blueprint
from app.api.v1 import user, client, token, banner, category, product, cart, comment, address


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    user.api.register(bp_v1)
    client.api.register(bp_v1)
    token.api.register(bp_v1)
    banner.api.register(bp_v1)
    category.api.register(bp_v1)
    product.api.register(bp_v1)
    cart.api.register(bp_v1)
    comment.api.register(bp_v1)
    address.api.register(bp_v1)
    return bp_v1
