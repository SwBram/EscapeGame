import pytest

from player import Player
from admin import Admin


#--------------Player tests--------------#

@pytest.fixture
def player():
    return Player("Alazar", 0, 0)

def test_player_GetName(player):
    """Test of the player GetName function."""
    assert player.GetName() != "Aladin"
    assert player.GetName() == "Alazar"

def test_player_GetHintsCount(player):
    """Test of the player GetHintsCount function. """
    assert player.GetHintsCount() == 0
    assert player.GetHintsCount() != -1
    assert player.GetHintsCount() != 2

def test_player_GetPuzzlesSolved(player):
    """Test of the player GetPuzzlesSolved function."""
    assert player.GetPuzzlesSolved() == 0
    assert player.GetPuzzlesSolved() != -1
    assert player.GetPuzzlesSolved() != 2

def test_player_GetRole(player): 
    """Test of the player GetRole function.""" 
    assert player.GetRole() == "Player"
    assert player.GetRole() != "Admin"

def test_player_ShowInfo(player):
    """Test of the player Showinfo function."""
    assert player.ShowInfo() == "name: Alazar, Hints count: 0, Puzzles solved: 0"
    assert player.ShowInfo() != "name: Lennert, Hints count: 0, Puzzles solved: 10"


#--------------Admin tests--------------#

@pytest.fixture
def admin():
    return Admin("Bram", ["ResetGame"])

def test_admin_ResetGame(admin):
    """Test of the admin ResetGame function."""
    assert admin.ResetGame() == "Game has been reset by Admin"
    assert admin.ResetGame() != "skibidi"

def test_admin_GetRole(admin):
    """Test of the admin GetRole function.""" 
    assert admin.GetRole() == "Admin"
    assert admin.GetRole() != "Player"

def test_admin_GetName(admin):
    """Test of the admin GetName function."""
    assert admin.GetName() != "bam"
    assert admin.GetName() == "Bram"

def test_admin_permissions(admin):
    """Test of the admin permissions"""
    assert "ResetGame" in admin.permissions
    assert admin.GetPermissions() == ["ResetGame"]

def test_admin_ShowInfo(admin):
    """Test of the admin Showinfo function."""
    assert admin.ShowInfo() == "Admin: Bram, Permissions: ['ResetGame']"
    assert admin.ShowInfo() != "Admin: bam, Permissions: ['StopGame']"
