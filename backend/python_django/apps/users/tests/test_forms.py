import pytest
from django.utils.translation import gettext_lazy as _

from ..forms import UserCreationForm
from ..models import User

pytestmark = pytest.mark.django_db


def test_username_validation_error_msg(user: User):
    form = UserCreationForm(
        {
            "username": user.username,
            "password1": user.password,
            "password2": user.password,
        }
    )

    assert not form.is_valid()
    assert len(form.errors) == 1
    assert "username" in form.errors
    assert form.errors["username"][0] == _("This username has already been taken.")
