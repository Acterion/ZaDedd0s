import pytest

from src.actions_executors.iexecutors import PersonInfo
from src.states.state_actions import format_today, format_next_month
from tests.test_states.test_state_actions.utils import make_actions_and_boys


@pytest.mark.asyncio
async def test_get_current_month_and_solve_captcha(mocker):
    actions_and_boys = make_actions_and_boys(mocker)
    actions_and_boys.extractor.extract_captcha.return_value = 'captcha'

    await actions_and_boys.actions.get_current_month_and_solve_captcha()

    assert actions_and_boys.ddoser.get_month_was_called_with == (format_today(), None)
    actions_and_boys.extractor.extract_captcha.assert_called_with('<html> captcha <html>')
    assert actions_and_boys.solver.solve_was_called_with == 'captcha'


@pytest.mark.asyncio
async def test_check_free_places_in_current_month_without_detected_captcha(mocker):
    actions_and_boys = make_actions_and_boys(mocker)
    actions_and_boys.extractor.extract_captcha.return_value = ''

    result = await actions_and_boys.actions.check_free_places_in_current_month()

    assert result

    target = (format_today(), actions_and_boys.solver.get_last_solution())
    assert actions_and_boys.ddoser.get_month_was_called_with == target
    actions_and_boys.extractor.extract_day_href.assert_called_with('<html> captcha <html>')


@pytest.mark.asyncio
async def test_check_free_places_in_current_month_when_detected_captcha(mocker):
    actions_and_boys = make_actions_and_boys(mocker)
    actions_and_boys.extractor.extract_captcha.return_value = 'captcha'

    result = await actions_and_boys.actions.check_free_places_in_current_month()

    assert not result

    target = (format_today(), actions_and_boys.solver.get_last_solution())
    assert actions_and_boys.ddoser.get_month_was_called_with == target


@pytest.mark.asyncio
async def test_check_free_places_in_next_month(mocker):
    actions_and_boys = make_actions_and_boys(mocker)
    actions_and_boys.extractor.extract_captcha.return_value = ''

    result = await actions_and_boys.actions.check_free_places_in_next_month()

    assert result

    target = (format_next_month(), actions_and_boys.solver.get_last_solution())
    assert actions_and_boys.ddoser.get_month_was_called_with == target
    actions_and_boys.extractor.extract_day_href.assert_called_with('<html> captcha <html>')


@pytest.mark.asyncio
async def test_try_to_reserve_place(mocker):
    actions_and_boys = make_actions_and_boys(mocker)
    actions_and_boys.extractor.extract_time_href.return_value = '11:00'
    fields = {'date': 'today'}
    actions_and_boys.extractor.extract_hidden_fields.return_value = fields
    actions_and_boys.extractor.extract_captcha.return_value = 'captcha'
    person = PersonInfo('name', 'surname', 'email', 'residence', 'passport')
    actions_and_boys.info_getter.get_person_info.return_value = person
    actions_and_boys.extractor.check_success.return_value = True

    result = await actions_and_boys.actions.try_to_reserve_place('today')

    assert result

    assert actions_and_boys.ddoser.get_day_was_called_with == 'today'
    actions_and_boys.extractor.extract_time_href.assert_called_with('day form')
    assert actions_and_boys.ddoser.get_time_slot_was_called_with == '11:00'
    assert actions_and_boys.solver.solve_was_called_with == 'captcha'
    target = (actions_and_boys.solver.get_last_solution(), fields, person)
    assert actions_and_boys.ddoser.send_final_form_was_called_with == target

