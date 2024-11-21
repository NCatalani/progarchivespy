import pytest
from bs4 import BeautifulSoup
from progarchivespy.parsers.top_albums import (
    PositionBreadcrumb,
    CoverBreadcrumb,
    RatingBreadcrumb,
    SummaryBreadcrumb,
    GenreBreadcrumb,
    AlbumTableBreadcrumb,
)
from progarchivespy.common.exceptions import ParseException
from progarchivespy.parsers.data import (
    PositionColumn,
    CoverColumn,
    RatingColumn,
    SummaryColumn,
    GenreColumn,
    AlbumTable,
)
from progarchivespy.common.definitions import Subgenre, AlbumType


@pytest.fixture
def mock_html():
    return {
        "position": '<td align="center"><strong>1</strong></td>',
        "cover": """
            <td align="center">
                <img src="https://example.com/cover.jpg" style="border: solid 3px #ddd;padding:3px;" width="150"/>
            </td>
        """,
        "rating": """
            <td align="center" height="50">
                <div class="discographyStar"></div>
                <span>4.68</span> | <span>5155</span> ratings
                <div style="font-size:80%;">QWR = 4.6702</div>
            </td>
        """,
        "summary": """
            <td>
                <a href="album.asp?id=1827"><strong>Close to the Edge</strong></a>
                <br/>
                <a href="artist.asp?id=105">Yes</a>
            </td>
        """,
        "genre": """
            <td><strong>Symphonic Prog</strong><br />Studio, 1971</td>
        """,
        "table": """
            <table></table> <!-- First table -->
            <table>
                <tr>
                    <td><strong>1</strong></td>
                    <td><img src="cover.jpg" /></td>
                    <td>
                        <div title="Average PA members rating"></div>
                        <span>4.5</span> | <span>500</span> ratings
                        <div>QWR = 4.3</div>
                    </td>
                    <td>
                        <a href="album.asp?id=123"><strong>Album Name</strong></a>
                        <br/>
                        <a href="artist.asp?id=456">Artist Name</a>
                    </td>
                    <td><strong>Symphonic Prog</strong><br />Studio, 2020</td>
                    <td><strong>Zoo</strong></td>
                </tr>
            </table>
        """,
    }


def test_breadcrumb_invalid_initialization():
    with pytest.raises(ValueError, match="element must be a bs4 Tag"):
        PositionBreadcrumb(element=None)


@pytest.mark.parametrize(
    "breadcrumb_class, html, expected",
    [
        (
            PositionBreadcrumb,
            '<td align="center"><strong>1</strong></td>',
            PositionColumn(position=1),
        ),
        (
            CoverBreadcrumb,
            """
            <td align="center">
                <img src="https://example.com/cover.jpg" style="border: solid 3px #ddd;padding:3px;" width="150"/>
            </td>
            """,
            CoverColumn(url="https://example.com/cover.jpg"),
        ),
        (
            RatingBreadcrumb,
            """
            <td align="center" height="50">
                <div class="discographyStar"></div>
                <span>4.68</span> | <span>5155</span> ratings
                <div style="font-size:80%;">QWR = 4.6702</div>
            </td>
            """,
            RatingColumn(score=4.68, ratings=5155, weighted_rating=4.6702),
        ),
        (
            SummaryBreadcrumb,
            """
            <td>
                <a href="album.asp?id=1827"><strong>Close to the Edge</strong></a>
                <br/>
                <a href="artist.asp?id=105">Yes</a>
            </td>
            """,
            SummaryColumn(
                album_name="Close to the Edge",
                album_id=1827,
                artist_name="Yes",
                artist_id=105,
            ),
        ),
        (
            GenreBreadcrumb,
            """
            <td><strong>Symphonic Prog</strong><br />Studio, 1971</td>
            """,
            GenreColumn(
                genre=Subgenre.SYMPHONIC_PROG,
                album_type=AlbumType.STUDIO,
                release_year=1971,
            ),
        ),
    ],
)
def test_breadcrumb_parsing(breadcrumb_class, html, expected):
    soup = BeautifulSoup(html, "html.parser")
    breadcrumb = breadcrumb_class(soup)
    data = breadcrumb.parse()
    assert data == expected


def test_album_table_breadcrumb(mock_html):
    soup = BeautifulSoup(mock_html["table"], "html.parser")
    breadcrumb = AlbumTableBreadcrumb(soup)
    data = breadcrumb.parse()

    assert isinstance(data, AlbumTable)
    assert len(data.rows) == 1

    row = data.rows[0]
    assert row.position.position == 1
    assert row.cover.url == "cover.jpg"
    assert row.rating.score == 4.5
    assert row.rating.ratings == 500
    assert row.rating.weighted_rating == 4.3
    assert row.summary.album_name == "Album Name"
    assert row.summary.artist_name == "Artist Name"
    assert row.genre.genre == Subgenre.SYMPHONIC_PROG
    assert row.genre.release_year == 2020


@pytest.mark.parametrize(
    "breadcrumb_class, html",
    [
        (PositionBreadcrumb, "<td></td>"),
        (CoverBreadcrumb, "<td></td>"),
        (CoverBreadcrumb, "<td><img /></td>"),
        (RatingBreadcrumb, "<td></td>"),
        (SummaryBreadcrumb, "<td></td>"),
        (GenreBreadcrumb, "<td></td>"),
        (GenreBreadcrumb, "<td><strong>asdasd</strong></td>"),
        (GenreBreadcrumb, "<td><strong>Symphonic Prog</strong><br />asdasd, 1971</td>"),
        (GenreBreadcrumb, "<td><strong>asd</strong><br />Studio, 1971</td>"),
        (AlbumTableBreadcrumb, "<table></table>"),
    ],
)
def test_breadcrumb_error_handling(breadcrumb_class, html):
    breadcrumb = breadcrumb_class(BeautifulSoup(html, "html.parser"))
    with pytest.raises(ParseException):
        breadcrumb.parse()
