from constants import *


class Player:
    def __init__(self, name):
        self.name = name
        self.attendance = [0] * 7
        self.point = 0
        self.grade = NORMAL
        self.wednesday_count = 0
        self.weekend_count = 0

    def add_attendance(self, weekday_index, point):
        self.attendance[weekday_index] += 1
        self.point += point

        if weekday_index == WEDNESDAY:
            self.wednesday_count += 1
        if weekday_index in (SATURDAY, SUNDAY):
            self.weekend_count += 1

    def calculate_grade(self):

        if self.attendance[WEDNESDAY] > 9:
            self.point += 10

        if self.attendance[SATURDAY] + self.attendance[SUNDAY] > 9:
            self.point += 10

        if self.point >= 50:
            self.grade = GOLD
        elif self.point >= 30:
            self.grade = SILVER
        else:
            self.grade = NORMAL

    def is_removable(self):
        return self.grade == NORMAL and self.wednesday_count == 0 and self.weekend_count == 0

    def print_info(self):
        print(f"NAME : {self.name}, POINT : {self.point}, GRADE : ", end="")
        if self.grade == GOLD:
            print("GOLD")
        elif self.grade == SILVER:
            print("SILVER")
        else:
            print("NORMAL")


class FileManager:
    def __init__(self):
        self.players = {}

    def get_or_create_player(self, name):
        if name not in self.players:
            self.players[name] = Player(name)
        return self.players[name]

    def check_point(self, name: str, dayofweek: str) -> None:
        player = self.get_or_create_player(name)

        weekday_map = {
            "monday": (MONDAY, 1),
            "tuesday": (TUESDAY, 1),
            "wednesday": (WEDNESDAY, 3),
            "thursday": (THURSDAY, 1),
            "friday": (FRIDAY, 1),
            "saturday": (SATURDAY, 2),
            "sunday": (SUNDAY, 2),
        }

        if dayofweek not in weekday_map:
            return

        week_index, point = weekday_map[dayofweek]
        player.add_attendance(week_index, point)

    def print_removed_player(self):
        print("\nRemoved player")
        print("==============")
        for player in self.players.values():
            if player.is_removable():
                print(player.name)

    def file_read(self):
        try:
            with open("attendance_weekday_500.txt", encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split()
                    if len(parts) == 2:
                        self.check_point(parts[0], parts[1])

                for player in self.players.values():
                    player.calculate_grade()

                    player.print_info()

                self.print_removed_player()


        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.")


def input_file():
    f = FileManager()
    f.file_read()


if __name__ == "__main__":
    input_file()

