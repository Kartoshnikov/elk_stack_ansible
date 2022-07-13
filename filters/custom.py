def surround_by_s_quote(object):
    if type(object).__name__ in ('list', 'tuple'):
        return [ "'%s'" % i for i in object ]
    else:
        return "'%s'" % object


def to_dict(object):
    object = tuple(object)
    return dict(object)


class FilterModule(object):
    def filters(self):
        return {
            "surround_by_s_quote": surround_by_s_quote,
            "to_dict": to_dict,
        }
