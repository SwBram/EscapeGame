import pytest

from player import Player
from admin import Admin



@pytest.fixture
def player():
    return Player("Alazar", 0, 0)

@pytest.fixture
def admin():
    return Admin("Bram", ["ResetGame"])

def test_player_name(player):
    assert player.ShowName() == "Alazar"
    assert player.ShowName() != "Aladin"
   




def test_admin_permissions(admin):
    assert "ResetGame" in admin.permissions