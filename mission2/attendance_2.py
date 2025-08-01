from constants import *

class Player():
    def __init__(self, name, grade, point):
        self.name = name
        self.grade = grade
        self.point = point
        self.wednesday_point = 0
        self.weekend_point = 0

    def update_score(self, dayofweek, name_index):
        add_point = 0
        week_index = 0

        if dayofweek == "monday":
            week_index = MONDAY
            add_point += 1
        elif dayofweek == "tuesday":
            week_index = TUESDAY
            add_point += 1
        elif dayofweek == "wednesday":
            week_index = WEDNESDAY
            add_point += 3
            point_wednesday[name_index] += 1
            self.wednesday_point += 1
        elif dayofweek == "thursday":
            week_index = THURSDAY
            add_point += 1
        elif dayofweek == "friday":
            week_index = FRIDAY
            add_point += 1
        elif dayofweek == "saturday":
            week_index = SATURDAY
            add_point += 2
            point_weekend[name_index] += 1
            self.weekend_point += 1
        elif dayofweek == "sunday":
            week_index = SUNDAY
            add_point += 2
            point_weekend[name_index] += 1
            self.weekend_point += 1

        attendants_point_data[name_index][week_index] += 1
        points[name_index] += add_point

        self.point = points[name_index]


class FileManager():
    def __init__(self):
        pass

    def print_removed_player(self):
        print("\nRemoved player")
        print("==============")
        for id in range(1, total_id_cnt + 1):
            if grade[id] not in (1, 2) and point_wednesday[id] == 0 and point_weekend[id] == 0:
                print(names[id])

    def add_player(self, name: str) -> None:
        global total_id_cnt
        if name not in unique_name_list:
            total_id_cnt += 1
            unique_name_list[name] = total_id_cnt
            names[total_id_cnt] = name
            player = Player(name, 0, 0)
            player_list.append(player)

    def check_point(self, name: str, dayofweek: str) -> None:

        self.add_player(name)
        name_index = unique_name_list[name]
        for p in player_list:
            if p.name == name:
                p.update_score(dayofweek, name_index)

    def file_read(self):
        try:
            with open("attendance_weekday_500.txt", encoding='utf-8') as f:
                for _ in range(500):
                    line = f.readline()
                    if not line:
                        break
                    parts = line.strip().split()
                    if len(parts) == 2:
                        self.check_point(parts[0], parts[1])

            for id in range(1, total_id_cnt + 1):
                calculate_point(id)
                print_point(id)

            self.print_removed_player()

        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.")


player_list = []
unique_name_list = {}
total_id_cnt = 0

# attendants_point_data[사용자ID][요일]
attendants_point_data = [[0] * 100 for _ in range(100)]
points = [0] * 100
grade = [0] * 100
names = [''] * 100
point_wednesday = [0] * 100
point_weekend = [0] * 100


def print_point(id: int) -> None:
    print(f"NAME : {names[id]}, POINT : {points[id]}, GRADE : ", end="")
    if grade[id] == GOLD:
        print("GOLD")
    elif grade[id] == SILVER:
        print("SILVER")
    else:
        print("NORMAL")


def calculate_point(id: int):
    if attendants_point_data[id][2] > 9:
        points[id] += 10
    if attendants_point_data[id][5] + attendants_point_data[id][6] > 9:
        points[id] += 10
    if points[id] >= 50:
        grade[id] = GOLD
    elif points[id] >= 30:
        grade[id] = SILVER
    else:
        grade[id] = NORMAL


def input_file():
    f = FileManager()
    f.file_read()


if __name__ == "__main__":
    input_file()
