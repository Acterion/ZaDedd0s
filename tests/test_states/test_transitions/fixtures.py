import asyncio

import pytest
from collections import namedtuple

from src.states.states_factory import StatesFactory
from src.states.state_machine import StateMachine
from tests.test_states.test_transitions.utility import FakeStateActions

from tests.test_states.utility import FFinalState

FSMAndBoys = namedtuple('FSMAndBoys', 'fsm actions factory')


def boys(**fake_state_actions_args):
    actions = FakeStateActions(**fake_state_actions_args)
    factory = StatesFactory(actions)
    next_state = FFinalState()
    return actions, factory, next_state


FSMAndDdosingBoys = namedtuple('FSMAndDdosingBoys', FSMAndBoys._fields + ('ddosing',))
FSMAndPenetratingBoys = namedtuple('FSMAndDdosingBoys', FSMAndBoys._fields + ('penetration',))


@pytest.fixture
def fsm_and_ddosing_boys() -> FSMAndDdosingBoys:
    actions, factory, ddosing = boys()
    fsm = StateMachine(factory.make_initial(ddosing), asyncio.get_event_loop())
    return FSMAndDdosingBoys(fsm, actions, factory, ddosing)


@pytest.fixture
def fsm_and_failing_boys() -> FSMAndBoys:
    actions, factory, *_ = boys(network_error=True)
    fsm = StateMachine(factory.make_initial(), asyncio.get_event_loop())
    return FSMAndBoys(fsm, actions, factory)


@pytest.fixture
def fsm_and_penetrating_this_month_boys() -> FSMAndPenetratingBoys:
    actions, factory, penetration = boys(free_places_in_current_month=True)
    fsm = StateMachine(factory.make_ddosing(penetration), asyncio.get_event_loop())
    return FSMAndPenetratingBoys(fsm, actions, factory, penetration)


@pytest.fixture
def fsm_and_penetrating_next_month_boys() -> FSMAndPenetratingBoys:
    actions, factory, penetration = boys(free_places_in_next_month=True)
    fsm = StateMachine(factory.make_ddosing(penetration), asyncio.get_event_loop())
    return FSMAndPenetratingBoys(fsm, actions, factory, penetration)


@pytest.fixture
def fsm_and_failed_penetration_boys() -> FSMAndDdosingBoys:
    actions, factory, ddosing = boys(place_reserved=False)
    fsm = StateMachine(factory.make_penetration(ddosing=ddosing), asyncio.get_event_loop())
    return FSMAndDdosingBoys(fsm, actions, factory, ddosing)


@pytest.fixture
def fsm_and_penetrated_boys() -> FSMAndBoys:
    actions, factory, *_ = boys(place_reserved=True)
    fsm = StateMachine(factory.make_penetration(), asyncio.get_event_loop())
    return FSMAndBoys(fsm, actions, factory)
