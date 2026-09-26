def parse_line(line: str) -> tuple[str, str]:
    level, message = line.split(":", 1)
    return level, message.strip()


def parse_many(lines: list[str]) -> list[tuple[str, str]]:
    return [parse_line(line) for line in lines]
