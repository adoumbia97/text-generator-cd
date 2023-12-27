from my_lib.predict import predict, read_file


def test_predict():
    assert "Topic" in predict(read_file("text.txt"))
