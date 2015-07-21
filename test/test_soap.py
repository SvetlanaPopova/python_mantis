__author__ = 'User'

def test_soap(app):
    list = app.soap.get_project_list(username=app.config['webadmin']['username'],
                                     password=app.config['webadmin']['password'])
    pass