# package time
"""
This code creates a datetime.time object from a string.

- Is it easy to verify that it works correctly?
- Do you see any obvious errors?
- How would you modify it to be easier to read?
"""

import datetime


def create_time_from_times_tamp(timestamp: str) -> datetime.time:
    """Create a datetime.time object from a string in the form 'hh:mm:ss'.

    Args:
    timestamp - string containing a timestamp in the format 'hh:mm:ss'

    Returns:
    a datetime.time object with value equal to the timestamp

    Raises:
    ValueError if timestamp is not a string in form "hh:mm:ss"

    Example:
    >>> t = create_time_from_times_tamp("9:23:15")
    >>> type(t)
    <class 'datetime.time'>
    >>> print(t)
    09:23:15
    """
    time_stamp = timestamp.split(":")
    if len(time_stamp) != 3:
        raise ValueError('Timestamp must be "hh:mm:ss"')
        # if the timestamp is not valid, this may raise TypeError or ValueError
    if is_valid_time(time_stamp):
        return datetime.time(int(time_stamp[0]), int(time_stamp[1]), int(time_stamp[2]))

    raise ValueError('Timestamp must be "hh:mm:ss"')




def is_valid_time(time_stamp):
    """Verify the timestamp are valid time.

    Raise:
        ValueError if timestamp doesn't contain integer value.
    """
    return 0 <= int(time_stamp[0]) <= 23 and 0 <= int(time_stamp[1]) < 60 and 0 <= int(time_stamp[2]) < 60
