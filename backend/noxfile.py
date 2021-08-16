import nox


@nox.session(python=["3.9"])
def tests(session):
    session.install("poetry")
    session.run("poetry", "install")
    session.run("pytest")


@nox.session
def lint(session):
    session.install("poetry")
    session.run("poetry", "install")
    session.run("black", "--check", ".")
    session.run("flake8", ".")
    session.run("isort", "--check", ".")
    session.run("dotenv-linter", ".env", ".env.example")


@nox.session
def type_checking(session):
    session.install("poetry")
    session.run("poetry", "install")
    session.run("mypy", ".")


@nox.session
def security(session):
    session.install("poetry")
    session.run("safety", "check")
