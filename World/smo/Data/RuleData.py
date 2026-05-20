from enum import IntEnum, StrEnum

class SMORuleCondition(IntEnum):
    """
    Enumeration of Super Mario Odyssey access rule conditions.
    """
    REGION = 0
    ITEM = 1
    MOONS = 2
    TOTAL_MOONS = 3
    CAPTURE = 4
    REGIONAL_COINS = 5
    ENTRANCE = 6
    TRICK_EASY = 7
    TRICK_INTERMEDIATE = 8
    TRICK_HARD = 9
    GLITCH_EASY = 10
    GLITCH_INTERMEDIATE = 11
    GLITCH_HARD = 12
    ABILITY = 13

class SMORuleOperation(IntEnum):
    NONE = -1
    AND = 0
    OR = 1
    PARENTHESIS_NONE = 2
    PARENTHESIS_AND = 3
    PARENTHESIS_OR = 4

class SMOEntranceDataType(StrEnum):
    ENTER = "Entrance"
    EXIT = "End"
    START = "Beginning"

class SMOKingdoms(StrEnum):
    CAP = "Cap"
    CASCADE = "Cascade"
    SAND = "Sand"
    WOODED = "Wooded"
    LAKE = "Lake"
    CLOUD = "Cloud"
    LOST = "Lost"
    METRO = "Metro"
    SEASIDE = "Seaside"
    SNOW = "Snow"
    LUNCHEON = "Luncheon"
    RUINED = "Ruined"
    BOWSER = "Bowser's"
    MOON = "Moon"
    MUSHROOM = "Mushroom"
    DARK = "Dark Side"
    DARKER = "Darker Side"

kingdom_name_to_id = {
    SMOKingdoms.CAP : 0,
    SMOKingdoms.CASCADE: 1,
    SMOKingdoms.SAND: 2,
    SMOKingdoms.WOODED: 3,
    SMOKingdoms.LAKE: 4,
    SMOKingdoms.CLOUD: 5,
    SMOKingdoms.LOST: 6,
    SMOKingdoms.METRO: 7,
    SMOKingdoms.SEASIDE: 8,
    SMOKingdoms.SNOW: 9,
    SMOKingdoms.LUNCHEON: 10,
    SMOKingdoms.RUINED: 11,
    SMOKingdoms.BOWSER: 12,
    SMOKingdoms.MOON: 13,
    SMOKingdoms.MUSHROOM: 14,
    SMOKingdoms.DARK: 15,
    SMOKingdoms.DARKER: 16,
}