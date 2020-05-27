from hopkins.hopkins import Hopkins
import chess


h = Hopkins()


def test_material_evaluation():
    game = chess.Board()
    assert h.material_eval(game) == 0
