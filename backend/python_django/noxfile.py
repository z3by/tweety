"""nox config file.

https://github.com/theacodes/nox
"""
import nox


@nox.session
def tests(session: nox.Session):
    """Run all tests and linters.

    Parameters
    ----------
    session : nox.Session
        current nox session
    """
    session.install("poetry")
    session.run("poetry", "install")
    session.run("black", "--check", ".")
    session.run("flake8", ".")
    session.run("isort", "--check", ".")
    session.run("dotenv-linter", ".env.dev")
    session.run("mypy", ".")
    session.run("safety", "check")
    session.run("pytest")
