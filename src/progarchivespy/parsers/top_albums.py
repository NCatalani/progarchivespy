from bs4 import Tag
from progarchivespy.parsers import Breadcrumb
from progarchivespy.common.exceptions import ParseException
from progarchivespy.parsers.data import (
    AlbumTable,
    AlbumTableRow,
    CoverColumn,
    GenreColumn,
    PositionColumn,
    RatingColumn,
    SummaryColumn,
)
from progarchivespy.common.definitions import AlbumType, Subgenre


class PositionBreadcrumb(Breadcrumb[PositionColumn]):
    def parse(self) -> PositionColumn:
        """
        Parses a <td> element containing a strong element with the position of the album.

        `<td align="center"><strong>1</strong></td>`

        Raises:
            ParseException: If the strong element is not found.

        Returns:
            PositionColumn: Dataclass
        """
        if not self.element.strong:
            raise ParseException("PositionBreadcrumb: strong element not found")

        return PositionColumn(position=int(self.element.strong.text))


class CoverBreadcrumb(Breadcrumb[CoverColumn]):
    def parse(self) -> CoverColumn:
        """
        Parses a <td> element containing an <img> element with the cover URL.

        ```
            <td align="center">
                <img "=""
                src="https://www.progarchives.com/progressive_rock_discography_covers/105/cover_292931682022_r.jpg"
                style="border: solid 3px #ddd;padding:3px;"
                width="150"/>
            </td>
        ```

        Raises:
            ParseException: If the img element is not found or the src attribute is empty.

        Returns:
            CoverColumn: Data containing the cover URL.
        """
        img = self.element.img

        if not img:
            raise ParseException("CoverBreadcrumbParser: img element not found")

        url = img.get("src")
        if not isinstance(url, str):
            raise ParseException(
                f"CoverBreadcrumbParser: src attribute is not a string, but a {type(url)}"
            )

        return CoverColumn(url=url)


class RatingBreadcrumb(Breadcrumb[RatingColumn]):
    def parse(self) -> RatingColumn:
        """
        Parses a <td> element containing the following:
            -> Two `<span>` elements with the score and ratings successively.
            -> At least two `<div>` elements, the second one containing the weighted rating.

        ```
        <td align="center" height="50">
            <div class="discographyStar" id="readOnlyRating_1_1827" title="Average PA members rating"></div>
            <script language="javascript" type="ff6a15e04a8b22bdc800067a-text/javascript">
                generateReadOnlyStarbox('readOnlyRating_1_1827', 4.67881311816762);
            </script>
            <span id="avgRatings_1" title="4.68 out of 5">4.68</span> | <span id="nbRatings_1">5155</span> ratings
            <div style="font-size:80%;">QWR = 4.6702</div>
            <div class="discographyStar" id="quickRating_1_1827" title="Your rating (updatable anytime)"></div>
            <script language="javascript" type="ff6a15e04a8b22bdc800067a-text/javascript">
                generateQuickRatingStarbox('quickRating_1_1827', 0, '-1');
            </script>
        </td>
        ```

        Raises:
            ParseException: If the span or div elements are not found.

        Returns:
            RatingBreadcrumbData: Data containing the score, ratings and weighted rating.
        """
        col = self.element

        spans = col.find_all("span")
        divs = col.find_all("div")

        if len(spans) < 2 or len(divs) < 2:
            raise ParseException(
                f"RatingBreadcrumbParser: span or div elements not found [spans: {len(spans)}, divs: {len(divs)}]"
            )

        return RatingColumn(
            score=float(spans[0].text),
            ratings=int(spans[1].text),
            weighted_rating=float(divs[1].text.replace("QWR =", "").strip()),
        )


class SummaryBreadcrumb(Breadcrumb[SummaryColumn]):
    def parse(self) -> SummaryColumn:
        """
        Parses a <td> element containing two <a> elements, one for the album and one for the artist.

        ```
        <td>
            <a href="album.asp?id=1827"><strong>Close to the Edge</strong></a>
            <br/>
            <a href="artist.asp?id=105">Yes</a>
        </td>
        ```

        Raises:
            ParseException: If the a elements are not found.

        Returns:
            SummaryColumn: Data containing the album and artist names and IDs.
        """
        links = self.element.find_all("a")

        if len(links) < 2:
            raise ParseException("SummaryBreadcrumbParser: a elements not found")

        album_link = links[0]
        artist_link = links[1]

        return SummaryColumn(
            album_name=album_link.strong.text,
            album_id=int(album_link["href"].split("=")[1]),
            artist_name=artist_link.text,
            artist_id=int(artist_link["href"].split("=")[1]),
        )


class GenreBreadcrumb(Breadcrumb[GenreColumn]):
    def parse(self) -> GenreColumn:
        """
        Parses a <td> element containing a <strong> element with the genre name and a <br> element
        with the album type and release year.

        ```
        <td><strong>Symphonic Prog</strong><br />Studio, 1972></td>
        ```

        Raises:
            ParseException: If the strong or br elements are not found.

        Returns:
            GenreColumn: Data containing the genre name, album type and release year.
        """
        strong = self.element.strong
        br = self.element.br

        if not strong:
            raise ParseException("GenreBreadcrumb: strong element not found")

        if not br:
            raise ParseException("GenreBreadcrumb: br element not found")

        genre_name = strong.text

        # The default html parser has a wierd behavior with the <br> tag
        # Sometimes the text is in the tag itself, sometimes in the next sibling.
        aux = br.text or br.next_sibling.text
        album_type, release_year = aux.split(", ")

        subgenre = Subgenre.build(name=genre_name)
        album_type = AlbumType.build(name=album_type)

        if not subgenre:
            raise ParseException(f"Subgenre {subgenre} not found")

        if not album_type:
            raise ParseException(f"Album type {album_type} not found")

        return GenreColumn(
            genre=subgenre,
            album_type=album_type,
            release_year=int(release_year),
        )


class AlbumTableBreadcrumb(Breadcrumb[AlbumTable]):
    def parse(self) -> AlbumTable:
        """
        Parses the table into a dataclass containing the rows.

        Raises:
            ParseException: If the row does not contain the expected number of columns.

        Returns:
            AlbumTable: Dataclass containing the table.
        """
        rows: list[AlbumTableRow] = []

        tables = self.element.find_all("table")
        if len(tables) < 2:
            raise ParseException(
                "Non-standard page structure: expected at least two tables."
            )

        table = tables[1]
        for element in table.contents:
            # Row's with the "class" attribute are not standard rows
            # We skip everything that is not a Tag or is a standard row
            if not isinstance(element, Tag) or element.get("class"):
                continue

            subelements = [
                subelement for subelement in element if isinstance(subelement, Tag)
            ]

            # Skip rows with less than 6 columns (standard row)
            if len(subelements) != 6:
                raise ParseException(f"Non-standard table row: {subelements}")

            rows.append(
                AlbumTableRow(
                    position=PositionBreadcrumb(element=subelements[0]).parse(),
                    cover=CoverBreadcrumb(element=subelements[1]).parse(),
                    rating=RatingBreadcrumb(element=subelements[2]).parse(),
                    summary=SummaryBreadcrumb(element=subelements[3]).parse(),
                    genre=GenreBreadcrumb(element=subelements[4]).parse(),
                )
            )

        return AlbumTable(rows=rows)
