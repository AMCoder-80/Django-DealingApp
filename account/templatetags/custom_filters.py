from django.template import Library

register = Library()


@register.filter()
def placeholder(value, token):
    value.field.widget.attrs['placeholder'] = token
    return value


@register.filter(name='formatter_filter')
def humanize(value):
    output = str()
    value = str(value)

    if 4 <= len(value) <= 6:
        output = str(int(value) / 1000) + " هزار تومان "
    elif 7 <= len(value) <= 9:
        output = str(int(value) / 1000000) + " میلیون تومان"
    elif len(value) > 9:
        output = str(int(value) / 1000000000) + " میلیارد تومان"
    else:
        output = "فرمت قیمت نادرست است"

    return output


@register.filter()
def persian_num(value):
    nums = {
        '0': '۰',
        '1': '۱',
        '2': '۲',
        '3': '۳',
        '4': '۴',
        '5': '۵',
        '6': '۶',
        '7': '۷',
        '8': '۸',
        '9': '۹',
    }

    value = list(str(value))

    for index in range(len(value)):
        if  value[index] in nums.keys():
            value[index] = nums[value[index]]

    return ''.join(value)