from configs import get_headers
import requests
from datetime import datetime as dt


class APIRequest:
    actualSeason = int(dt.now().year)

    def __init__(self):
        self.headers: dict = get_headers()

    def team_player(self, id_team: str | int, page: str | int, season: int = actualSeason) -> dict[any:any]:
        url: str = f"https://v3.football.api-sports.io/players?team={id_team}&season={season}&page={page}"

        req = requests.get(url, headers=self.headers)
        return req.json()

    def leagues_search(self, league_name: str) -> dict[any:any]:
        url: str = f"https://v3.football.api-sports.io/leagues?search={league_name}"

        req = requests.get(url, headers=self.headers)
        response = req.json().get("response")
        return response

    def leagues(self, country: str, camp_type: str) -> dict[any:any]:
        url: str = f"https://v3.football.api-sports.io/leagues?country={country}&type={camp_type}"

        req = requests.get(url, headers=self.headers)
        response = req.json().get("response")
        return response

    def league_by_id(self, id_league: int | str, season: int = actualSeason):
        url: str = f"https://v3.football.api-sports.io/leagues?id={id_league}&season={season}"

        req = requests.get(url, headers=self.headers)
        response = req.json().get("response")
        return response

    def team_stadium(self, id_league: str | int, season: int = actualSeason) -> dict[any:any]:
        url: str = f"https://v3.football.api-sports.io/teams?league={id_league}&season={season}"

        req = requests.get(url, headers=self.headers)
        response = req.json().get("response")
        return response

    def team_squad(self, id_team: str | int) -> dict[any:any]:
        url = f"https://v3.football.api-sports.io/players/squads?team={id_team}"
        req = requests.get(url, headers=self.headers)
        response = req.json().get("response")
        return response

    def league_fixtures(self, id_champ: str | int, season: str | int = actualSeason):
        url = f"https://v3.football.api-sports.io/fixtures?league={id_champ}&season={season}"
        req = requests.get(url, headers=self.headers)
        response = req.json().get("response")
        return response

    def fixture_stats(self, id_fixture: str | int) -> list[dict[str:any]]:
        url = f"https://v3.football.api-sports.io/fixtures/statistics?fixture={id_fixture}"
        req = requests.get(url, headers=self.headers)
        response = req.json().get("response")
        return response

    def fixture_events(self, id_fixture: str | int) -> list[dict[str:any]]:
        url = f"https://v3.football.api-sports.io/fixtures/events?fixture={id_fixture}"
        req = requests.get(url, headers=self.headers)
        response = req.json().get("response")
        return response

    def player_stats(self, id_player: str | int, season: int = actualSeason):
        url = f"https://v3.football.api-sports.io/players?id={id_player}&season={season}"
        req = requests.get(url, headers=self.headers)
        response = req.json().get("response")
        return response

    def team_league_stats(self, id_team: str | int, id_league: str | int, season: int = actualSeason):
        url = f"https://v3.football.api-sports.io/teams/statistics?league={id_league}&season={season}&team={id_team}"
        req = requests.get(url, headers=self.headers)
        response = req.json().get("response")
        return response

    def fixture_lineups(self, id_fixture: str | int):
        url = f"https://v3.football.api-sports.io/fixtures/lineups?fixture={id_fixture}"
        req = requests.get(url, headers=self.headers)
        response = req.json().get("response")
        return response

    def fixture_basics(self, id_fixture: str | int):
        url = f"https://v3.football.api-sports.io/fixtures?id={id_fixture}"
        req = requests.get(url, headers=self.headers)
        response = req.json().get("response")
        return response
