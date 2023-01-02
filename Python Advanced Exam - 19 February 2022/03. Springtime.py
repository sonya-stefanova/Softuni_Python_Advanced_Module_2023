def start_spring(**kwargs):
    new_dict = {}

    for spring_object, type in kwargs.items():
        if type not in new_dict:
            new_dict[type] = []
        new_dict[type].append(spring_object)

    result = ''
    for type, spring_object in sorted(new_dict.items(), key=lambda x: (-len(x[1]), x[0])):
        result+=f'{type}:\n'
        for el in sorted(spring_object):
            result+=f'-{el}\n'


    return result







example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}


print(start_spring(**example_objects))
