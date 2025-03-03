from bs4 import BeautifulSoup
from progarchivespy.services import Service
from progarchivespy.models import AlbumQueryResult, Album, Artist
from progarchivespy.common.definitions import (
    PROGARCHIVES_BASE_URL,
    Subgenre,
    Country,
    AlbumType,
)
from progarchivespy.parsers.top_albums import AlbumTableBreadcrumb
from progarchivespy.common import logger


class TopAlbumsService(Service[list[AlbumQueryResult]]):
    def parse_response(self, raw_response: str) -> list[AlbumQueryResult]:
        """
        Parse the raw response from the TopAlbums page
        into a list of AlbumQueryResult objects.

        Args:
            raw_response (str): Raw HTML content of the TopAlbums page.

        Returns:
            list[AlbumQueryResult]: List of AlbumQueryResult objects.
        """
        album_table = AlbumTableBreadcrumb(
            BeautifulSoup(raw_response, "html.parser")
        ).parse()

        return [
            AlbumQueryResult(
                position=row.position.position,
                weighted_score=row.rating.weighted_rating,
                album=Album(
                    id=row.summary.album_id,
                    name=row.summary.album_name,
                    score=row.rating.score,
                    ratings=row.rating.ratings,
                    cover=row.cover.url,
                    year=row.genre.release_year,
                    genre=row.genre.genre,
                    type=row.genre.album_type,
                ),
                artist=Artist(id=row.summary.artist_id, name=row.summary.artist_name),
            )
            for row in album_table.rows
        ]

    def query(
        self,
        subgenres: list[Subgenre] | None = None,
        countries: list[Country] | None = None,
        album_types: list[AlbumType] | None = None,
        years: list[int] | None = None,
        min_avg_rating: float = 0.0,
        min_num_ratings: int = 0,
        max_num_ratings: int = 0,
        max_results: int = 100,
    ) -> list[AlbumQueryResult]:
        """Query the top albums from ProgArchives.

        Args:
            subgenres (list[Subgenre] | None, optional): A list of Subgenres. Defaults to None.
            countries (list[Country] | None, optional): A list of Countries. Defaults to None.
            album_types (list[AlbumType] | None, optional): A list of Album Types. Defaults to None.
            years (list[int] | None, optional): A list of years. Defaults to None.
            min_avg_rating (float, optional): Minimal average rating. Defaults to 0.0.
            min_num_ratings (int, optional): Minimal amount of ratings. Defaults to 0.
            max_num_ratings (int, optional): Maximum amount of rating. Defaults to 0.
            max_results (int, optional): Maximum amount of results. Defaults to 100, maximum 250.

        Raises:
            requests.HTTPError: If the HTTP request fails.

        Returns:
            list[AlbumQueryResult]: List of results.
        """

        args = locals()
        params: dict = {
            "smaxresults": str(max_results),
        }

        for arg_name, arg in args.items():
            if not arg:
                continue

            match arg_name:
                case "years":
                    params["syears"] = ",".join([str(year) for year in arg])
                case "subgenres":
                    params["ssubgenres"] = ",".join(
                        [str(subgenre.id) for subgenre in arg]
                    )
                case "countries":
                    params["scountries"] = ",".join(
                        [str(country.id) for country in arg]
                    )
                case "album_types":
                    params["salbumtypes"] = ",".join(
                        [str(album_type.id) for album_type in arg]
                    )
                case "min_avg_rating":
                    params["sminavgratings"] = str(min_avg_rating)
                case "min_num_ratings":
                    params["sminratings"] = str(min_num_ratings)
                case "max_num_ratings":
                    params["smaxratings"] = str(max_num_ratings)

        res = self.http_client.get(
            f"{PROGARCHIVES_BASE_URL}/top-prog-albums.asp", params=params
        )
        logger.debug(
            "TopAlbumService: Response from ProgArchives",
            input_url=res.request.url,
        )
        print(
            f"TopAlbumService: Response from ProgArchives {res.request.url}",
        )
        res.raise_for_status()

        return self.parse_response(res.text)
