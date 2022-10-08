## NEEDS ERROR HANDLING


def read_text_to_dict():
    strDict = dict()
    with open("menu.txt", 'r') as f:
        for line in f:
            x,y = line.split(', ')
            strDict[x]=y.strip('\n')

    return strDict


def pull_from_github():
    # Close Main Program
    # Pull Repository from github using oauth
    # Restart Main Program 
    return None

if __name__ == "__main__":
    temp = read_text_to_dict()
    for key, value in temp.items():
        print(f'{key}: {value}')

    pull_from_github()