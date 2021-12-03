from invoke import task 

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def robot(ctx):
    ctx.run("robot src/tests")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")
    ctx.run("coverage report -m")

@task
def lint(ctx):
    ctx.run("pylint src")
