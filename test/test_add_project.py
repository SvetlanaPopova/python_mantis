__author__ = 'User'


def test_add_project(app, json_projects,  orm, check_ui):
    old_project_list = orm.get_project_list()
    project = json_projects
    app.project.add_project(project)
    app.project.check_add_new_project_success(orm, old_project_list, project, check_ui)