from invoke import run, task

@task
def doc():
   run('cd docs && make html')

@task
def publish():
   run('./setup.py sdist upload')

