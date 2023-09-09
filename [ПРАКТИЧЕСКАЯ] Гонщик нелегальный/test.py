from typing import TypeAlias
from import_this import (
    generate_race_data,
    RaceInfo,
)


def sort_racers() -> list:
    return sorted(race_data.values(), key=lambda d: d['FinishedPlace'])


def print_separator() -> None:
    winner: str = ""
    for i in race_data.values():
        if i.get("FinishedPlace", -1) == 1:
            winner = f"Выиграл - {i.get('RacerName','').upper()}!!! Поздравляем!"
            break
    print(winner)
    print("_" * len(winner))


def print_top3_racers() -> None:
    print("Первые три места:\n")
    for d in (sorted_racers[:3]):
        hours: int = d['FinishedTimeSeconds'] // 3600
        minute: int = (d['FinishedTimeSeconds'] // 60) % 60
        seconds: int = d['FinishedTimeSeconds'] % 60
        print_racer(place=d['FinishedPlace'],
                    name=d['RacerName'],
                    team=d['RacerTeam'],
                    hours=hours,
                    minute=minute,
                    seconds=seconds)


def print_racer(place: str, name: str, team: str, hours: int, minute: int, seconds: int) -> None:
    print(f"Гонщик на {place} месте: ")
    print(f"\tИмя: {name}")
    print(f"\tКоманда: {team}")
    print(f"\tВремя: {hours}:{minute}:{seconds} (H:M:S)")


if __name__ == '__main__':
    race_data: RaceInfo = generate_race_data(10)
    sorted_racers: list = sort_racers()
    print_separator()
    print_top3_racers()
