from src.parser import parse_line, parse_many


def test_parse_line() -> None:
    assert parse_line("INFO: ready") == ("INFO", "ready")


def test_parse_many() -> None:
    assert parse_many(["INFO: ready", "WARN: retrying"]) == [
        ("INFO", "ready"),
        ("WARN", "retrying"),
    ]
