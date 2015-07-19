__author__ = 'User'
from model.project import Project
import string
import random

def random_string (prefix, maxlen):
    symbols = string.ascii_letters*3 + string.digits + " "*10 #+ string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_delete_some_project(app, orm, check_ui):
    #old_project_list = app.project.get_project_list()
    old_project_list = orm.get_project_list()
    if len(old_project_list) == 0:
        app.project.add_project(Project(name=random_string("Project", 10)))
    project = random.choice(old_project_list)
    app.project.delete_project_by_id(project.id)
    app.project.check_delete_success(orm, project, old_project_list, check_ui)