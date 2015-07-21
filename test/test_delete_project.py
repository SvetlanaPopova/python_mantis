__author__ = 'User'
from model.project import Project
import string
import random

def random_string (prefix, maxlen):
    symbols = string.ascii_letters*3 + string.digits + " "*10 #+ string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_delete_some_project(app, check_ui):
    old_project_list = app.soap.get_project_list(username=app.config['webadmin']['username'],
                                     password=app.config['webadmin']['password'])
    if len(old_project_list) == 0:
        app.project.add_project(Project(name=random_string("Project", 10)))
    project = random.choice(old_project_list)
    app.project.delete_project_by_id(project.id)
    old_project_list.remove(project)
    new_project_list = app.soap.get_project_list(username=app.config['webadmin']['username'],
                                     password=app.config['webadmin']['password'])
    app.project.compare_contact_lists(new_project_list, old_project_list, check_ui)