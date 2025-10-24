def inputcheck(user_input, input_type):
    match input_type:
        case "int":
            try: int(user_input); return True
            except: pass
        case "str":
            try: str(user_input); return True
            except: pass
        case "float":
            try: float(user_input); return True
            except: pass
        case _: return False
    return False
