import unittest
from app import create_app
from flask_script import Manager, Server


app = create_app('development')

#  app = create_app('production')


manager = Manager(app)
manager.add_command('server', Server)
@manager.command
def test():
    '''
    run unittests
    '''
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():

    return dict(app=app)

if __name__ == '__main__':
    manager.run()