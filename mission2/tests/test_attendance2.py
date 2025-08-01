import pytest
from mission2.attendance_2 import *


@pytest.fixture
def p():
    p = Player("nammin");
    return p

def test_플레이어_초기화(p):
    assert p.name == "nammin"


def test_플레이어_add_attendance(p):
    p.add_attendance(MONDAY,3)
    assert p.point == 3
    p.add_attendance(WEDNESDAY, 3)
    p.add_attendance(SUNDAY, 3)
    assert p.point == 9

def test_플레이어_calculate_grade(p):
    p.add_attendance(MONDAY,3)
    p.calculate_grade()
    assert p.grade == NORMAL

def test_플레이어_수요일10번(p):
    for i in range(10):
        p.add_attendance(WEDNESDAY,3)
    p.calculate_grade()
    assert p.point== 40


def test_플레이어_주말20번(p):
    for i in range(20):
        p.add_attendance(SATURDAY, 3)
    p.calculate_grade()
    assert p.point == 70
    
def test_플레이어_리무버블(p):
    assert p.is_removable() == 1

def test_파일매니저_초기화(p):
    f=FileManager()
    f.players = p
    assert f.players.name=="nammin"

def test_플레이어_output(capsys,p):
    p.print_info()
    captured = capsys.readouterr()
    assert captured.out == 'NAME : nammin, POINT : 0, GRADE : NORMAL\n' != 'This is a test message\n'
    p.point = 34
    p.calculate_grade()
    p.print_info()
    captured = capsys.readouterr()
    assert captured.out == 'NAME : nammin, POINT : 34, GRADE : SILVER\n' != 'This is a test message\n'
    p.point = 55
    p.calculate_grade()
    p.print_info()
    captured = capsys.readouterr()
    assert captured.out == 'NAME : nammin, POINT : 55, GRADE : GOLD\n' != 'This is a test message\n'

def test_파일매니저리무버블_output(capsys):
    f = FileManager()
    f.get_or_create_player("sss")
    f.print_removed_player()
    captured = capsys.readouterr()
    assert captured.out == '\nRemoved player\n==============\nsss\n'

def test_addplayer():
    f = FileManager()
    answer = 0
    f.get_or_create_player("sss")
    f.get_or_create_player("aaa")
    for p in f.players:
        if(p=="sss"):
            answer = 1

    assert answer == 1


def test_filemanager_checkpoint():
    f = FileManager()
    f.check_point("nammin",MONDAY)
    player = f.get_or_create_player("nammin")
    assert player.point == 0

