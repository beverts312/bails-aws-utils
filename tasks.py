from invoke import task


def black(c, check):
    cmd = f"black . --line-length=79 {'--check' if check is True else ''}"
    return c.run(cmd)


@task(aliases=["f"])
def format(c):
    c.run("isort .")
    return black(c, False)


@task(aliases=["cf", "fc"])
def check_format(c):
    return black(c, True)


@task(aliases=["t"])
def test_and_cover(c):
    c.run("coverage run -m pytest --junitxml=junit.xml")
    return c.run("coverage xml")


@task(aliases=["c"])
def clean(c):
    return c.run("rm -rf dist bails_lambda_utils.egg-info build")


@task(aliases=["b"])
def build(c):
    return c.run("python3 setup.py bdist_wheel")


@task(aliases=["bp"])
def build_and_publish(c):
    clean()
    build()
    return c.run("python3 -m twine upload dist/*.whl --verbose")
