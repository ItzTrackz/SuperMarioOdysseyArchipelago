from enum import IntEnum, StrEnum
from .ItemData import SMOItemData
from .LocationData import SMOLocationData
from .RegionData import SMORegion
from .EntranceData import SMOEntranceData

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
    TRICK_INTERMEDIATE= 8
    TRICK_HARD = 9
    GLITCH_EASY = 10
    GLITCH_INTERMEDIATE = 11
    GLITCH_HARD = 12
    ABILITY = 13
    LOCATION = 14
    PARENTHESIS_OPEN = 98
    PARENTHESIS_CLOSE = 99

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
    UNIQUE_EXIT = "Unique Exit End"
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
moon_rule_data : dict[str, list] = {
    #region Cap Moons 
    SMOLocationData.frog_jumping_above_the_fog: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.NONE),
    ],
    SMOLocationData.frog_jumping_from_the_top_deck: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.NONE),
    ],
    SMOLocationData.cap_kingdom_timer_challenge_1: [],
    SMOLocationData.shopping_in_bonneton: [],
    SMOLocationData.the_forgotten_treasure: [
        (SMORuleCondition.ABILITY, [SMOItemData.ground_pound], SMORuleOperation.NONE),
    ],
    SMOLocationData.taxi_flying_through_bonneton: [
        (SMORuleCondition.CAPTURE, [SMOItemData.binoculars], SMORuleOperation.NONE),
    ],
    SMOLocationData.bonnetter_blockade: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.peach_in_the_cap_kingdom: [
        (SMORuleCondition.REGION, [SMORegion.mushroom_kingdom], SMORuleOperation.NONE)
    ],
    #endregion

    #region Cap Moons Top of Top Hat Tower
    SMOLocationData.good_evening_captain_toad: [],
    SMOLocationData.cap_kingdom_regular_cup: [],
    #endregion

    #region Cap Moons Moon Rock
    SMOLocationData.next_to_glasses_bridge: [],
    SMOLocationData.danger_sign: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.under_the_big_ones_brim: [],
    SMOLocationData.fly_to_the_edge_of_the_fog: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.NONE),
    ],
    SMOLocationData.spin_the_hat_get_a_prize: [],
    SMOLocationData.hidden_in_a_sunken_hat: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_NONE),
    ],
    SMOLocationData.fog_shrouded_platform: [
        (SMORuleCondition.ABILITY, [SMOItemData.ground_pound], SMORuleOperation.NONE),
    ],
    SMOLocationData.bird_traveling_in_the_fog: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, None, SMORuleOperation.NONE),
    ],
    SMOLocationData.caught_hopping_near_the_ship: [],
    SMOLocationData.taking_notes_in_the_fog: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.cap_kingdom_timer_challenge_2: [],
    #endregion

    #region Cap Moons Top of Top Hat Tower Moon Rock
    SMOLocationData.cap_kingdom_master_cup: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.long_jump], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.roll], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.triple_jump], SMORuleOperation.NONE),
    ],
    #endregion

    #region Cap Moons Poson Tide
    SMOLocationData.skimming_the_poison_tide: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.slipping_through_the_poison_tide: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE),
    ],
    #endregion

    #region Cap Moons Push Block
    SMOLocationData.push_block_peril: [
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.spark_pylon], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.double_jump], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.triple_jump], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.side_flip], SMORuleOperation.PARENTHESIS_NONE),
    ],
    SMOLocationData.hidden_among_the_push_blocks: [
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.spark_pylon], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.double_jump], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.triple_jump], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.side_flip], SMORuleOperation.PARENTHESIS_NONE),
    ],
    #endregion

    #region Cap Moons Frog Pond
    SMOLocationData.searching_the_frog_pond: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.backflip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.ground_pound_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.backflip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.ground_pound_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.vault], SMORuleOperation.NONE), 
    ],
    #endregion

    #region Cap Moons Rolling Lane
    SMOLocationData.roll_on_and_on: [],
    SMOLocationData.precision_rolling: [],
    #endregion

    #region Cascade Moons
    SMOLocationData.our_first_power_moon: [
        SMORuleCondition.CAPTURE, [SMOItemData.chain_chomp], SMORuleOperation.NONE
    ],
    SMOLocationData.chomp_through_the_rocks: [
        (SMORuleCondition.CAPTURE, [SMOItemData.chain_chomp], SMORuleOperation.OR),
        (SMORuleCondition.CAPTURE, [SMOItemData.t_rex], SMORuleOperation.NONE)
    ],
    SMOLocationData.behind_the_waterfall: [
        (SMORuleCondition.CAPTURE, [SMOItemData.chain_chomp], SMORuleOperation.OR),
        (SMORuleCondition.CAPTURE, [SMOItemData.t_rex], SMORuleOperation.NONE)        
    ],
    SMOLocationData.multi_moon_atop_the_falls: [
        (SMORuleCondition.CAPTURE, [SMOItemData.broodes_chain_chomp], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.CAPTURE, [SMOItemData.t_rex], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.CAPTURE, [SMOItemData.broodes_chain_chomp], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.CAPTURE, [SMOItemData.big_chain_chomp], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.broodes_chain_chomp], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.backflip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_AND)
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.ledge_grab], SMORuleOperation.PARENTHESIS_NONE)
    ],
    
}

regional_rule_data : dict[str, list] = {
    #region Cap Kingdom Regional Coins
    SMOLocationData.cap_kingdom_regional_coin_group_1: [],
    SMOLocationData.cap_kingdom_regional_coin_1: [],
    SMOLocationData.cap_kingdom_regional_coin_2: [],
    SMOLocationData.cap_kingdom_regional_coin_3: [],
    SMOLocationData.cap_kingdom_regional_coin_group_2: [],
    SMOLocationData.cap_kingdom_regional_coin_4: [],
    SMOLocationData.cap_kingdom_regional_coin_5: [],
    SMOLocationData.cap_kingdom_regional_coin_6: [],
    SMOLocationData.cap_kingdom_regional_coin_group_3: [],
    SMOLocationData.cap_kingdom_regional_coin_7: [],
    SMOLocationData.cap_kingdom_regional_coin_8: [],
    SMOLocationData.cap_kingdom_regional_coin_9: [],
    SMOLocationData.cap_kingdom_regional_coin_group_4: [],
    SMOLocationData.cap_kingdom_regional_coin_10: [],
    SMOLocationData.cap_kingdom_regional_coin_11: [],
    SMOLocationData.cap_kingdom_regional_coin_12: [],
    SMOLocationData.cap_kingdom_regional_coin_group_5: [],
    SMOLocationData.cap_kingdom_regional_coin_13: [],
    SMOLocationData.cap_kingdom_regional_coin_14: [],
    SMOLocationData.cap_kingdom_regional_coin_15: [],
    SMOLocationData.cap_kingdom_regional_coin_16: [],
    SMOLocationData.cap_kingdom_regional_coin_group_6: [],
    SMOLocationData.cap_kingdom_regional_coin_17: [],
    SMOLocationData.cap_kingdom_regional_coin_18: [],
    SMOLocationData.cap_kingdom_regional_coin_19: [],
    SMOLocationData.cap_kingdom_regional_coin_group_7: [
    (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE)
    ],
    SMOLocationData.cap_kingdom_regional_coin_20: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE)
    ],
    SMOLocationData.cap_kingdom_regional_coin_21: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE)
    ],
    SMOLocationData.cap_kingdom_regional_coin_22: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE)
    ],
    SMOLocationData.cap_kingdom_regional_coin_23: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE)
    ],
    SMOLocationData.cap_kingdom_regional_coin_group_8: [
    (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.OR),
    (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
    (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_NONE)        
    ],
    SMOLocationData.cap_kingdom_regional_coin_24: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_NONE)
    ],
    SMOLocationData.cap_kingdom_regional_coin_25: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_NONE)
    ],
    SMOLocationData.cap_kingdom_regional_coin_26: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_NONE)
    ],
    SMOLocationData.cap_kingdom_regional_coin_27: [
    (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_NONE)
    ],
    SMOLocationData.cap_kingdom_regional_coin_group_9: [],
    SMOLocationData.cap_kingdom_regional_coin_28: [],
    SMOLocationData.cap_kingdom_regional_coin_29: [],
    SMOLocationData.cap_kingdom_regional_coin_30: [],
    SMOLocationData.cap_kingdom_regional_coin_31: [],
    #endregion

    #region Top Hat Tower Regional Coins
    SMOLocationData.top_hat_tower_regional_coin_group_1: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.backflip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.side_flip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.ledge_grab], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.triple_jump], SMORuleOperation.PARENTHESIS_OR),
    ],
    SMOLocationData.top_hat_tower_regional_coin_1: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.backflip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.side_flip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.ledge_grab], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.triple_jump], SMORuleOperation.PARENTHESIS_OR),
    ],
    SMOLocationData.top_hat_tower_regional_coin_2: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.backflip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.side_flip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.ledge_grab], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.triple_jump], SMORuleOperation.PARENTHESIS_OR),
    ],
    SMOLocationData.top_hat_tower_regional_coin_3: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.backflip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.side_flip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.ledge_grab], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.triple_jump], SMORuleOperation.PARENTHESIS_OR),
    ],
    SMOLocationData.top_hat_tower_regional_coin_4: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.backflip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.side_flip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.ledge_grab], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.triple_jump], SMORuleOperation.PARENTHESIS_OR),
    ],
    SMOLocationData.top_hat_tower_regional_coin_group_2: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.triple_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.ENTRANCE, [SMOEntranceData.top_hat_tower_end], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.up_throw], SMORuleOperation.PARENTHESIS_NONE),
    ],
    SMOLocationData.top_hat_tower_regional_coin_5: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.triple_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.ENTRANCE, [SMOEntranceData.top_hat_tower_end], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.up_throw], SMORuleOperation.PARENTHESIS_NONE),
    ],
    SMOLocationData.top_hat_tower_regional_coin_6: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.triple_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.ENTRANCE, [SMOEntranceData.top_hat_tower_end], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.up_throw], SMORuleOperation.PARENTHESIS_NONE),
    ],
    SMOLocationData.top_hat_tower_regional_coin_7: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.triple_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.ENTRANCE, [SMOEntranceData.top_hat_tower_end], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.up_throw], SMORuleOperation.PARENTHESIS_NONE),
    ],
    SMOLocationData.top_hat_tower_regional_coin_8: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.triple_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.ENTRANCE, [SMOEntranceData.top_hat_tower_end], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.up_throw], SMORuleOperation.PARENTHESIS_NONE),
    ],
    SMOLocationData.top_hat_tower_regional_coin_9: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.triple_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.ENTRANCE, [SMOEntranceData.top_hat_tower_end], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.up_throw], SMORuleOperation.PARENTHESIS_NONE),
    ],
    #endregion

    #region Cap Kingdom Frog Pond Regional Coins
    SMOLocationData.frog_pond_regional_coin_group_1: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.backflip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.ground_pound_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.backflip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.ground_pound_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_NONE),
    ],
    SMOLocationData.frog_pond_regional_coin_1: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.backflip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.ground_pound_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.backflip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.ground_pound_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_NONE),
    ],
    SMOLocationData.frog_pond_regional_coin_2: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.backflip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.ground_pound_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.backflip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.ground_pound_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_NONE),
    ],
    SMOLocationData.frog_pond_regional_coin_3: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.backflip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.ground_pound_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.backflip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.ground_pound_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_NONE),
    ],
    SMOLocationData.frog_pond_regional_coin_4: [    
    (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.backflip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.ground_pound_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.backflip], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.ground_pound_jump], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_HARD, [SMOItemData.wall_jump], SMORuleOperation.PARENTHESIS_NONE),
    ],    
    #endregion

    #region Cap Kingdom Poison Tides Regional Coins
    SMOLocationData.poison_tides_regional_coin_group_1: [
        (SMORuleCondition.CAPTURE,[SMOItemData.paragoomba], SMORuleOperation.NONE)
    ],
    SMOLocationData.poison_tides_regional_coin_1: [
        (SMORuleCondition.CAPTURE,[SMOItemData.paragoomba], SMORuleOperation.NONE)
    ],
    SMOLocationData.poison_tides_regional_coin_2: [
        (SMORuleCondition.CAPTURE,[SMOItemData.paragoomba], SMORuleOperation.NONE)
    ],
    SMOLocationData.poison_tides_regional_coin_3: [
        (SMORuleCondition.CAPTURE,[SMOItemData.paragoomba], SMORuleOperation.NONE)
    ],
    #endregion

    #region Cap Kingdom Push Block Regional Coins
    SMOLocationData.pushblocks_regional_coin_group_1: [
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.spark_pylon], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.double_jump], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.triple_jump], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.side_flip], SMORuleOperation.PARENTHESIS_NONE),
    ],
    SMOLocationData.pushblocks_regional_coin_1: [
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.spark_pylon], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.double_jump], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.triple_jump], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.side_flip], SMORuleOperation.PARENTHESIS_NONE),
    ],
    SMOLocationData.pushblocks_regional_coin_2: [
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.spark_pylon], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.double_jump], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.triple_jump], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.side_flip], SMORuleOperation.PARENTHESIS_NONE),        
    ],
    SMOLocationData.pushblocks_regional_coin_3: [
        (SMORuleCondition.TRICK_INTERMEDIATE, [SMOItemData.spark_pylon], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.double_jump], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.vault], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.triple_jump], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.dive], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.spark_pylon], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, [SMOItemData.side_flip], SMORuleOperation.PARENTHESIS_NONE),
    ],
    #endregion
}

