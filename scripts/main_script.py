from scripts.parser_script import parser_script
from scripts.film_crop import film_crop
from scripts.correct_file_name import correct_file_name


class FindError(Exception):
    pass


class DefaultNameError(Exception):
    pass


def main_script(script_file, phrase, file_name, target_name):
    try:
        if not correct_file_name(file_name) or not correct_file_name(target_name):
            raise DefaultNameError

        scenario_dict = parser_script(script_file)

        if phrase not in scenario_dict:
            raise FindError

        if len(scenario_dict[phrase]) == 1:
            start_time, end_time = scenario_dict[phrase][0]

            film_crop(start_time, end_time, file_name, target_name)

            return 'Фрагмент с данной фразой был вырезан.'
        else:
            num = 1
            for elem in scenario_dict[phrase]:
                start_time, end_time = elem

                film_crop(start_time, end_time, file_name, target_name + str(num))
                num += 1

            return 'Несколько фрагментов с данной фразой были вырезаны.'

    except FindError:
        return 'Такой фразы нет в сценарии.'

    except DefaultNameError:
        return 'Неверное имя файла.'


if __name__ == '__main__':
    print(main_script('C:/Users/dobry/PycharmProjects/proj1/scenario.txt',
                      'Lean and hungry.',
                      'C:/Users/dobry/PycharmProjects/proj1/test1.mp4',
                      'C:/Users/dobry/OneDrive/Рабочий стол/ptst.mp4'))

    print(main_script('C:\\Users\\dobry\\PycharmProjects\\proj1\\scenario.txt', 'General.',
                      'C:\\Users\\dobry\\PycharmProjects\\proj1\\test2.mp4',
                      'C:\\Users\\dobry\\PycharmProjects\\proj1\\ptest2.mp4'))
