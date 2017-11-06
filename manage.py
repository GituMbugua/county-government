import unittest
from app import create_app
from flask_script import Manager, Server
from flask_migrate import Migrate, MigateCommand
from app.models import County, Constituency, Party, Mca, Governor, DeputyGovernor, Senator, WomanRep, User

app = create_app('development')

#  app = create_app('production')


manager = Manager(app)

manager.add_command('server', Server)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    '''
    run unittests
    '''
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, County=County, Constituency=Constituency, Party=Party, Mca=Mca, Governor=Governor, Senator=Senator, DeputyGovernor=DeputyGovernor, WomanRep=WomanRep, User=User)


if __name__ == '__main__':
    manager.run()
