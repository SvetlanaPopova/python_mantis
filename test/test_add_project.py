__author__ = 'User'


def test_add_project(app, json_projects):
    old_project_list = app.project.get_project_list()
    project = json_projects
    app.project.add_project(project)
    app.project.check_add_new_project_success(old_project_list, project)