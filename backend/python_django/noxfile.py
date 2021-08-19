"""nox config file.

https://github.com/theacodes/nox
"""
import nox


@nox.session(python=["3.9"])
def tests(session: nox.Session):
    """Run tests stage.

    Parameters
    ----------
    session : nox.Session
        current nox session
    """
    session.install("poetry")
    session.run("poetry", "install")
    session.run("pytest")


@nox.session
def lint(session: nox.Session):
    """Lint files stage.

    Parameters
    ----------
    session : nox.Session
        current nox session
    """
    session.run("black", "--check", ".")
    session.run("flake8", ".")
    session.run("isort", "--check", ".")
    session.run("dotenv-linter", ".env", ".env.example")


@nox.session
def type_checking(session: nox.Session):
    """Run mypy type checking.

    Parameters
    ----------
    session : nox.Session
        current nox session
    """
    session.run("mypy", ".")


@nox.session
def security(session: nox.Session):
    """Run dependencies analysis.

    Parameters
    ----------
    session : nox.Session
        current nox session
    """
    session.run("safety", "check")
