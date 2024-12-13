from progarchivespy.common.entity import Entity, EntityEnum

PROGARCHIVES_BASE_URL = "https://www.progarchives.com"


class Subgenre(EntityEnum):
    """
    Subgenres of Progressive Rock
    """

    CROSSOVER_PROG = Entity(3, "Crossover Prog")
    SYMPHONIC_PROG = Entity(4, "Symphonic Prog")
    PROG_FOLK = Entity(6, "Prog Folk")
    ZEUHL = Entity(11, "Zeuhl")
    CANTERBURY_SCENE = Entity(12, "Canterbury Scene")
    PSYCHEDELIC_SPACE_ROCK = Entity(15, "Psychedelic/Space Rock")
    KRAUTROCK = Entity(17, "Krautrock")
    NEO_PROG = Entity(18, "Neo-Prog")
    PROGRESSIVE_METAL = Entity(19, "Progressive Metal")
    ROCK_PROGRESSIVO_ITALIANO = Entity(28, "Rock Progressivo Italiano")
    VARIOUS_GENRES_ARTISTS = Entity(29, "Various Genres")
    JAZZ_ROCK_FUSION = Entity(30, "Jazz Rock/Fusion")
    POST_ROCK_MATH_ROCK = Entity(32, "Post Rock/Math rock")
    PROGRESSIVE_ELECTRONIC = Entity(33, "Progressive Electronic")
    INDO_PROG_RAGA_ROCK = Entity(35, "Indo-Prog/Raga Rock")
    RIO_AVANT_PROG = Entity(36, "RIO/Avant-Prog")
    PROTO_PROG = Entity(37, "Proto-Prog")
    PROG_RELATED = Entity(38, "Prog Related")
    HEAVY_PROG = Entity(41, "Heavy Prog")
    ECLECTIC_PROG = Entity(42, "Eclectic Prog")
    TECH_EXTREME_PROG_METAL = Entity(43, "Tech/Extreme Prog Metal")
    EXPERIMENTAL_POST_METAL = Entity(44, "Experimental/Post Metal")


class Country(EntityEnum):
    """
    Countries of the world
    """

    ARGENTINA = Entity(0, "Argentina")
    AUSTRALIA = Entity(12, "Australia")
    AUSTRIA = Entity(13, "Austria")
    NETHERLANDS = Entity(144, "Netherlands")
    NEW_ZEALAND = Entity(146, "New Zealand")
    NICARAGUA = Entity(147, "Nicaragua")
    UNITED_KINGDOM = Entity(205, "United Kingdom")
    UNITED_STATES = Entity(196, "United States")
    ANDORRA = Entity(5, "Andorra")
    ARMENIA = Entity(10, "Armenia")
    BAHRAIN = Entity(17, "Bahrain")
    BANGLADESH = Entity(18, "Bangladesh")
    BELARUS = Entity(20, "Belarus")
    BELGIUM = Entity(21, "Belgium")
    BOLIVIA = Entity(26, "Bolivia")
    BOSNIA_AND_HERZEGOVINA = Entity(27, "Bosnia and Herzegovina")
    BRAZIL = Entity(107, "Brazil")
    BULGARIA = Entity(31, "Bulgaria")
    CANADA = Entity(36, "Canada")
    CHILE = Entity(41, "Chile")
    CHINA = Entity(42, "China")
    COLOMBIA = Entity(45, "Colombia")
    COSTA_RICA = Entity(49, "Costa Rica")
    CROATIA = Entity(51, "Croatia")
    CUBA = Entity(52, "Cuba")
    CZECH_REPUBLIC = Entity(54, "Czech Republic")
    DENMARK = Entity(55, "Denmark")
    DOMINICAN_REPUBLIC = Entity(57, "Dominican Republic")
    ECUADOR = Entity(59, "Ecuador")
    EGYPT = Entity(60, "Egypt")
    EL_SALVADOR = Entity(61, "El Salvador")
    ESTONIA = Entity(64, "Estonia")
    FAROE_ISLANDS = Entity(67, "Faroe Islands")
    FINLAND = Entity(69, "Finland")
    FRANCE = Entity(70, "France")
    GEORGIA = Entity(75, "Georgia")
    GERMANY = Entity(76, "Germany")
    GHANA = Entity(77, "Ghana")
    GREECE = Entity(79, "Greece")
    GUADELOUPE = Entity(82, "Guadeloupe")
    GUATEMALA = Entity(84, "Guatemala")
    HUNGARY = Entity(90, "Hungary")
    ICELAND = Entity(91, "Iceland")
    INDIA = Entity(92, "India")
    INDONESIA = Entity(93, "Indonesia")
    IRAN = Entity(94, "Iran")
    IRAQ = Entity(95, "Iraq")
    IRELAND = Entity(96, "Ireland")
    ISRAEL = Entity(97, "Israel")
    ITALY = Entity(98, "Italy")
    JAPAN = Entity(100, "Japan")
    JORDAN = Entity(101, "Jordan")
    KAZAKHSTAN = Entity(102, "Kazakhstan")
    KOREA = Entity(105, "Korea")
    KUWAIT = Entity(108, "Kuwait")
    LATVIA = Entity(111, "Latvia")
    LEBANON = Entity(112, "Lebanon")
    LITHUANIA = Entity(117, "Lithuania")
    LUXEMBOURG = Entity(118, "Luxembourg")
    MACEDONIA = Entity(219, "Macedonia")
    MADAGASCAR = Entity(120, "Madagascar")
    MALAYSIA = Entity(122, "Malaysia")
    MALTA = Entity(125, "Malta")
    MEXICO = Entity(131, "Mexico")
    MOLDOVA = Entity(133, "Moldova")
    MONACO = Entity(134, "Monaco")
    MONTENEGRO = Entity(218, "Montenegro")
    MOROCCO = Entity(137, "Morocco")
    MULTI_NATIONAL = Entity(209, "Multi-National")
    NORWAY = Entity(152, "Norway")
    PAKISTAN = Entity(154, "Pakistan")
    PANAMA = Entity(156, "Panama")
    PERU = Entity(159, "Peru")
    PHILIPPINES = Entity(160, "Philippines")
    POLAND = Entity(161, "Poland")
    PORTUGAL = Entity(162, "Portugal")
    PUERTO_RICO = Entity(163, "Puerto Rico")
    ROMANIA = Entity(166, "Romania")
    RUSSIA = Entity(167, "Russia")
    SERBIA = Entity(217, "Serbia")
    SINGAPORE = Entity(175, "Singapore")
    SLOVAKIA = Entity(210, "Slovakia")
    SLOVENIA = Entity(211, "Slovenia")
    SOUTH_AFRICA = Entity(214, "South Africa")
    SPAIN = Entity(206, "Spain")
    SWEDEN = Entity(177, "Sweden")
    SWITZERLAND = Entity(178, "Switzerland")
    SYRIA = Entity(179, "Syria")
    TAIWAN = Entity(180, "Taiwan")
    THAILAND = Entity(183, "Thailand")
    TUNISIA = Entity(188, "Tunisia")
    TURKEY = Entity(189, "Turkey")
    TURKMENISTAN = Entity(190, "Turkmenistan")
    UKRAINE = Entity(193, "Ukraine")
    UNITED_ARAB_EMIRATES = Entity(194, "United Arab Emirates")
    URUGUAY = Entity(197, "Uruguay")
    UZBEKISTAN = Entity(198, "Uzbekistan")
    VENEZUELA = Entity(199, "Venezuela")
    YUGOSLAVIA = Entity(202, "Yugoslavia")
    VARIOUS = Entity(139, "Various")


class AlbumType(EntityEnum):
    """
    Types of albums
    """

    STUDIO = Entity(1, "Studio")
    DVD_VIDEO = Entity(2, "DVD/Video")
    BOXSET_COMPILATION = Entity(3, "Boxset/Compilation")
    LIVE = Entity(4, "Live")
    SINGLES_EPS_FAN_CLUB_PROMO = Entity(5, "Singles/EPs/Fan Club/Promo")
