import src.html_extractor.html_extractor as ext

import src.html_extractor.html_samples as samples


def test_extract_captcha():
    extractor = ext.HtmlExtractor()
    target = "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"
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
    res = extractor.extract_time_slot_href(samples.html_doc_with_time_slot)
    assert res == target


def test_extract_hidden_fields():
    extractor = ext.HtmlExtractor()
    target = {
        'fields[0].definitionId': '5481',
        'fields[0].index': '0',
        'fields[1].definitionId': '5467',
        'fields[1].index': '1',
        'fields[2].definitionId': '5473',
        'fields[2].index': '2',
        'locationCode': 'jeka',
        'realmId': '881',
        'categoryId': '1677',
        'openingPeriodId': '51077',
        'date': '26.08.2020',
        'dateStr': '26.08.2020'
    }
    res = extractor.extract_hidden_fields(samples.html_doc_with_form)
    assert res == target
