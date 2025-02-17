from .constants import ALLOWED_DELIMITERS
from .utils import validate_delimiter, create_nrc_regex, is_valid_nrc


# A function to check if the nrc is valid.
def validate_nrc(nrc_number: str, delimiter: str = None) -> bool:
    nrc_number = nrc_number.strip()
    is_valid = validate_delimiter(delimiter)
    if delimiter is None:
        return len(nrc_number) == 9
    if not is_valid:
        raise Exception(f'NRC delimiter is invalid! values should be seperated by {ALLOWED_DELIMITERS}')
    if delimiter not in nrc_number:
        raise Exception(f'NRC not separated by assigned delimiter!')
    nrc_pattern = create_nrc_regex(delimiter)
    return is_valid_nrc(nrc_number, nrc_pattern)
