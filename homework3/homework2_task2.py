from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple

if __name__ == '__main__':
    @dataclass
    class Movie:
        title: str
        dates: List[Tuple[datetime, datetime]]

        def schedule(self) -> Generator[datetime, None, None]:
            for i in self.dates:
                tmp = i[0]
                while tmp <= i[1]:
                    yield tmp
                    tmp += timedelta(days=1)

    m = Movie('sw', [
        (datetime(2020, 1, 1), datetime(2020, 1, 7)),
        (datetime(2020, 1, 15), datetime(2020, 2, 7))
    ])

    for d in m.schedule():
        print(d)
