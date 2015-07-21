__author__ = 'User'


def test_add_project(app, json_projects, check_ui):
    old_project_list = app.soap.get_project_list(username=app.config['webadmin']['username'],
                                     password=app.config['webadmin']['password'])
    project = json_projects
    app.project.add_project(project)
    old_project_list.append(project)
    new_project_list = app.soap.get_project_list(username=app.config['webadmin']['username'],
                                     password=app.config['webadmin']['password'])
    app.project.compare_contact_lists(new_project_list, old_project_list, check_ui)