import pytest, requests

BASE = "http://localhost:8001"
T = 10


def new_game():
    r = requests.post(f"{BASE}/games", timeout=T)
    assert r.status_code == 201
    return r.json()["id"]


def move(gid, player, choice):
    return requests.post(f"{BASE}/games/{gid}/moves", json={"player": player, "choice": choice}, timeout=T)


def test_create_game():
    r = requests.post(f"{BASE}/games", timeout=T)
    assert r.status_code == 201
    b = r.json()
    assert b["id"] and b["status"] == "waiting" and b["winner"] is None
    assert b["player1_move"] is None and b["player2_move"] is None


def test_documented_curl_flow():
    gid = new_game()
    r1 = move(gid, 1, "rock")
    assert r1.status_code == 200
    assert r1.json()["status"] == "waiting" and r1.json()["player1_move"] == "rock"
    r2 = move(gid, 2, "scissors")
    assert r2.status_code == 200
    b = r2.json()
    assert b["status"] == "complete" and b["winner"] == "player1"


@pytest.mark.parametrize("c1,c2,w", [("rock", "rock", "draw"), ("paper", "rock", "player1"),
                                      ("rock", "paper", "player2"), ("scissors", "paper", "player1")])
def test_outcomes(c1, c2, w):
    gid = new_game()
    move(gid, 1, c1)
    assert move(gid, 2, c2).json()["winner"] == w


def test_unknown_game_404():
    assert move("doesnotexist", 1, "rock").status_code == 404


def test_invalid_choice_422():
    assert move(new_game(), 1, "lizard").status_code == 422


def test_invalid_player_422():
    assert move(new_game(), 3, "rock").status_code == 422


def test_missing_body_422():
    r = requests.post(f"{BASE}/games/{new_game()}/moves", timeout=T)
    assert r.status_code == 422


def test_duplicate_move_422():
    gid = new_game()
    move(gid, 1, "rock")
    assert move(gid, 1, "paper").status_code == 422


def test_move_after_complete_422():
    gid = new_game()
    move(gid, 1, "rock"); move(gid, 2, "rock")
    assert move(gid, 1, "paper").status_code == 422
