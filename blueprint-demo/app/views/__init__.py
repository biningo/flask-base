from app.views.article import article
from app.views.books import books
from app.views.goods import goods
from app.views.tags import tags

ROUTERS = (
    [article,'/article'],
    [books, '/books'],
    [goods, '/goods'],
    [tags, '/tags']
)



def blueprint_setup(app):
    for view,pre in ROUTERS:
        app.register_blueprint(view,url_prefix=pre)
