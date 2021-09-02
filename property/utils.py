import jdatetime


def j_to_g(date):
    return jdatetime.date(year=date.year, month=date.month, day=date.day, locale='fa_IR').strftime("%d %b %Y")