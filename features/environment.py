"""
environment.py: File to manage Behave events
"""

GLOBAL_DICTIONARY = {}

def global_add(key, value):
    if key not in GLOBAL_DICTIONARY:
        GLOBAL_DICTIONARY[key] = [value]
    else:
        GLOBAL_DICTIONARY[key].append(value)

def global_get(key, index=None):
    count = len(GLOBAL_DICTIONARY[key])
    if key not in GLOBAL_DICTIONARY:
        return None
    if index is not None:
        index = abs(index)
        if index < 1 or index > count:
            raise Exception('Response status not passed\nIndex error')
    if index is None:
        return GLOBAL_DICTIONARY[key][-1]
    return GLOBAL_DICTIONARY[key][-1 * index]

def global_pop(key, index=None):
    if key not in GLOBAL_DICTIONARY:
        return None
    if index is not None and (index < len(GLOBAL_DICTIONARY[key]) * -1 or index >= len(GLOBAL_DICTIONARY[key])):
        return None
    if index is None:
        result = GLOBAL_DICTIONARY[key].pop()
    else:
        result = GLOBAL_DICTIONARY[key].pop(index)
    if len(GLOBAL_DICTIONARY[key]) == 0:
        del GLOBAL_DICTIONARY[key]
    return result

def global_count(key):
    if key not in GLOBAL_DICTIONARY:
        return None
    return len(GLOBAL_DICTIONARY[key])

def global_clear():
    GLOBAL_DICTIONARY.clear()

def before_all(context):
    """Event that activates before running Behave"""
    context.global_add = global_add
    context.global_clear = global_clear
    context.global_get = global_get
    context.global_pop = global_pop
    context.global_count = global_count
    context.global_dictionary = GLOBAL_DICTIONARY

def after_scenario(context, scenario):
    """Event that  activates after executing each scenario"""
    stack = getattr(context, "_stack")[0]
    if scenario.error_message is None and 'object' in stack:
        context.global_dictionary[stack['object_type']] = stack['object']
