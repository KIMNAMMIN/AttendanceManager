unique_name_list = {}
id_cnt = 0

# attendants_point_data[사용자ID][요일]
attendants_point_data = [[0] * 100 for _ in range(100)]
points = [0] * 100
grade = [0] * 100
names = [''] * 100
point_wednesday = [0] * 100
point_weekend = [0] * 100


def point_calculation(name, dayofweek):
    
    global id_cnt

    if name not in unique_name_list:
        id_cnt += 1
        unique_name_list[name] = id_cnt
        names[id_cnt] = name

    name_index = unique_name_list[name]

    add_point = 0
    week_index = 0

    if dayofweek == "monday":
        week_index = 0
        add_point += 1
    elif dayofweek == "tuesday":
        week_index = 1
        add_point += 1
    elif dayofweek == "wednesday":
        week_index = 2
        add_point += 3
        point_wednesday[name_index] += 1
    elif dayofweek == "thursday":
        week_index = 3
        add_point += 1
    elif dayofweek == "friday":
        week_index = 4
        add_point += 1
    elif dayofweek == "saturday":
        week_index = 5
        add_point += 2
        point_weekend[name_index] += 1
    elif dayofweek == "sunday":
        week_index = 6
        add_point += 2
        point_weekend[name_index] += 1

    attendants_point_data[name_index][week_index] += 1
    points[name_index] += add_point


def input_file():
    try:
        with open("attendance_weekday_500.txt", encoding='utf-8') as f:
            for _ in range(500):
                line = f.readline()
                if not line:
                    break
                parts = line.strip().split()
                if len(parts) == 2:
                    point_calculation(parts[0], parts[1])

        for i in range(1, id_cnt + 1):
            if attendants_point_data[i][3] > 9:
                points[i] += 10
            if attendants_point_data[i][5] + attendants_point_data[i][6] > 9:
                points[i] += 10

            if points[i] >= 50:
                grade[i] = 1
            elif points[i] >= 30:
                grade[i] = 2
            else:
                grade[i] = 0

            print(f"NAME : {names[i]}, POINT : {points[i]}, GRADE : ", end="")
            if grade[i] == 1:
                print("GOLD")
            elif grade[i] == 2:
                print("SILVER")
            else:
                print("NORMAL")

        print("\nRemoved player")
        print("==============")


        for i in range(1, id_cnt + 1):
            if grade[i] not in (1, 2) and point_wednesday[i] == 0 and point_weekend[i] == 0:
                print(names[i])

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

if __name__ == "__main__":
    input_file()
