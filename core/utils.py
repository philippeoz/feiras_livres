from django.utils import six

import datetime

import re


date_re = re.compile(
    r'(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})$'
)


def parse_date(value):
    """
    Função que realiza um parse de datas
    do formato "YYYY/mm/dd" para um objeto datetime

    param value: Data no formato YYYY/mm/dd
    return: Datetime caso esteja no padrão correto, se não, None
    """
    match_1 = date_re.match(value)
    if match_1:
        kw = {k: int(v) for k, v in six.iteritems(match_1.groupdict())}
        return datetime.date(**kw)
