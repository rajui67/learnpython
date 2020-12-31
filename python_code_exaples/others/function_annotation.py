def function_annotation(param1: str, param2: int = 10) -> int:
    print(function_annotation.__annotations__)
    return param2

function_annotation('a', 10)