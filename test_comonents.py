import pytest
from timer import Timer
from component import Component
from logger import Logger
import time

# Fixtures
@pytest.fixture
def timer():
    """Fixture die een nieuwe Timer instantie aanmaakt voor tests."""
    return timer()

@pytest.fixture
def logger():
    """Fixture die een verse Logger instantie maakt."""
    return logger()

@pytest.fixture
def component():
    """Geeft een eenvoudige Component-instantie terug."""
    return component()

# Timer Tests
def test_timer_starts_correct(timer):
    """Test of Timer correct start."""
    timer.start()
    assert timer.running == True
    assert timer.start_time != None

def test_timer_stops_correct(timer):
    """Test of Timer correct stopt."""
    timer.start()
    timer.stop()
    assert timer.running == False
    assert timer.stop_time != None

def test_timer_duration(timer):
    """Test of getDuration() tijd telt."""
    timer.start()
    time.sleep(1)
    duration = timer.getDuration()
    assert duration >= 1

def test_timer_remaining(timer):
    """Test of getRemaining() minder wordt."""
    timer.start()
    time.sleep(2)
    remaining = timer.getRemaining()
    assert 0 <= remaining <= 5

def test_stop_time_sets_stop_time(timer):
    """Test of stop() de stoptijd instelt."""
    timer.start()
    time.sleep(1)
    timer.stop()
    assert timer.stop_time != None

# Logger Tests
def test_add_message(logger):
    """Test of berichten worden toegevoegd."""
    logger.add_message("Testbericht")
    assert logger.get_messages() == ["Testbericht"]

def test_multiple_messages(logger):
    """Test meerdere berichten."""
    logger.add_message("Eén")
    logger.add_message("Twee")
    assert logger.get_messages() == ["Eén", "Twee"]

def test_get_messages_type(logger):
    """Test of get_messages een lijst teruggeeft."""
    assert isinstance(logger.get_messages(), list)

def test_start_sets_running_true(logger):
    """Test of start() running op True zet."""
    logger.start()
    assert logger.running == True

def test_stop_sets_running_false(logger):
    """Test of stop() running op False zet."""
    logger.start()
    logger.stop()
    assert logger.running == False

# Component Tests
def test_start_sets_running_true_component(component):
    """Test of start() running op True zet."""
    component.start()
    assert component.running == True

def test_stop_sets_running_false_component(component):
    """Test of stop() running op False zet."""
    component.start()
    component.stop()
    assert component.running == False
