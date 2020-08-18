import src.actions_executors.html_extractor as ext

import tests.test_extractors.utility as samples


def test_extract_captcha():
    extractor = ext.HtmlExtractor()
    target = "CapTch4/Zq=="
    res = extractor.extract_captcha(samples.html_doc_with_captcha)
    assert res == target


def test_extract_day_href():
    extractor = ext.HtmlExtractor()
    target = "extern/appointment_showDay.do?locationCode=nowo&realmId=1098&categoryId=2266&dateStr=26.08.2020"
    res = extractor.extract_day_href(samples.html_doc_with_day)
    assert res == target


def test_extract_time_slot_href():
    extractor = ext.HtmlExtractor()
    target = "extern/appointment_showForm.do?locationCode=nowo&realmId=1098&categoryId=2266&dateStr=26.08.2020&openingPeriodId=51082"
    res = extractor.extract_time_href(samples.html_doc_with_time_slot)
    assert res == target


def test_extract_hidden_fields():
    extractor = ext.HtmlExtractor()
    res = extractor.extract_hidden_fields(samples.html_doc_with_form)
    assert res == samples.hidden_inputs_target


def test_check_success():
    extractor = ext.HtmlExtractor()
    res = extractor.check_success(samples.html_doc_with_error)
    assert not res
