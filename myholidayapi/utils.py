
def clear_params(params: dict) -> dict:
    """
    Delete None values from dictionary
    """
    clean_params = {}
    for key, value in params.items():
        if value is not None:
            clean_params[key] = value
    return clean_params