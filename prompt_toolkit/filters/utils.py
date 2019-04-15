from typing import Dict

from .base import Always, Filter, Never, FilterOrBool

__all__ = [
    'to_filter',
    'is_true',
]

_always = Always()
_never = Never()

_lookup_dict: Dict[FilterOrBool, Filter] = {
    True: _always,
    False: _never,
}


def to_filter(bool_or_filter: FilterOrBool) -> Filter:
    """
    Accept both booleans and Filters as input and
    turn it into a Filter.
    """
    if not isinstance(bool_or_filter, (bool, Filter)):
        raise TypeError('Expecting a bool or a Filter instance. Got %r' % bool_or_filter)

    return _lookup_dict.get(bool_or_filter, bool_or_filter)


def is_true(value: FilterOrBool) -> bool:
    """
    Test whether `value` is True. In case of a Filter, call it.

    :param value: Boolean or `Filter` instance.
    """
    return to_filter(value)()
