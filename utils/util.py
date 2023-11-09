## NEEDS ERROR HANDLING


def read_text_to_dict():
    return dict([[x.strip().strip('\n') for x in line.split(',')] for line in open("menu.txt", 'r').readlines()])