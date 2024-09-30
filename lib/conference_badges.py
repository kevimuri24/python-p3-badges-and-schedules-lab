def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    return [f'Hello, my name is {names}.' for names in names]

def assign_rooms(names):
    return [f"Hello, {names}! You'll be assigned to room {i + 1}!" for i, names in enumerate(names)]

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    
    for assignement in assign_rooms(names):
        print(assignement)
