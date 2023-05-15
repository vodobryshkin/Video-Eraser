def parser_script(filename):
    scenario = open(filename, encoding='utf-8', mode='r').readlines()

    key = ''
    data = ''
    result = {}

    for line in scenario:

        if ' --> ' in line:

            if key != '' and data != '':

                if data[:-1] in result.keys():
                    result[data[:-1]].append(key)
                result[data[:-1]] = [key]

            key = line.split(' --> ')
            key[-1] = key[-1][:-1]
            data = ''
        else:
            data += line

    return result


if __name__ == '__main__':
    print(parser_script('C:\\Users\\dobry\\PycharmProjects\\proj1\\scenario.txt'))