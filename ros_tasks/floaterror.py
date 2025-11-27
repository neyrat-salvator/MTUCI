def check_float(value):
    if type(value) == float:
        return value
    else:
        debug_text: str = f"""
        Тип данных должен быть float
        Нынешний тип данных: {type(value)}
        """
        raise ValueError(debug_text)