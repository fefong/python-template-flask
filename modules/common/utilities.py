import os
from datetime import datetime, timezone


def format_date(date: datetime, date_format='%d/%m/%Y %H:%M:%S') -> str:
    """Format dates

    Args:
        date (datetime): date
        date_format (str, optional): date format. Defaults to '%d/%m/%Y %H:%M:%S'.

    Returns:
        date (str): formatted date
    """
    return date.strftime(date_format)


def get_timestamp() -> datetime:
    """Get Timestamp

    Returns:
        timestamp (datetime):  Defaults 2000-12-31T23:59:59.000+00:00
    """
    return datetime.now(timezone.utc).replace(microsecond=0)


def get_path_dirname(folder=None):
    """Get full path

    Args:
        folder (str, optional): folder internal path. Defaults to None.

    Returns:
        path (str): full path
    """
    path = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    if folder is not None:
        path = os.path.join(path, folder)
    return path


def check_list_exists_in_dict(mandatory_list: list, object_dict: dict) -> bool:
    """Check list in dictionary

    Args:
        mandatory_list (list): list of mandatory items: ex. ['item 1','item 2']]
        object_dict (dict): all the itens

    Returns:
        bool: check result (True/False)
    """
    if all((key in object_dict) and (object_dict[key]) for key in mandatory_list):
        return True
    else:
        return False


def keys_exists(object_dict: dict, *keys: str) -> bool:
    """Check if *keys (nested) exists in dictionary.

    Args:
        object_dict (dict): all the itens
        *keys (str): nested elements key.

    Returns:
        bool: check result (True/False)
    """
    if len(keys) == 0:
        return False

    _element = object_dict
    for key in keys:
        try:
            _element = _element[key]
        except KeyError:
            return False
    return True
