__author__ = 'User'
from model.project import Project
import string
import random


def random_string (prefix, maxlen):
    symbols = string.ascii_letters*3 + string.digits + " "*10 #+ string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_add_project(app):
    old_project_list = app.project.get_project_list()
    app.project.add_project(Project(name=random_string ("Project", 10),
                                    status="stable",
                                    inherit_gl_categories=True,
                                    view_status="public",
                                    description="description asdfgh jkl."))
    #new_project_list = app.project.get_project_list()
    #app.project.check_add_new_project_success(old_project_list, new_project_list)
    pass