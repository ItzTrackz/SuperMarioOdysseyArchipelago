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
    TRICK_INTERMEDIATE = 8
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
    SMOLocationData.good_evening_captain_toad: [],
    SMOLocationData.shopping_in_bonneton: [],
    SMOLocationData.skimming_the_poison_tide: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.slipping_through_the_poison_tide: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.push_block_peril: [
        (SMORuleCondition.CAPTURE, [SMOItemData.spark_pylon], SMORuleOperation.NONE),
    ],
    SMOLocationData.hidden_among_the_push_blocks: [
        (SMORuleCondition.CAPTURE, [SMOItemData.spark_pylon], SMORuleOperation.NONE),
    ],
    SMOLocationData.searching_the_frog_pond: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.NONE),
    ],
    SMOLocationData.secrets_of_the_frog_pond: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.NONE),
    ],
    SMOLocationData.the_forgotten_treasure: [],
    SMOLocationData.taxi_flying_through_bonneton: [
        (SMORuleCondition.CAPTURE, [SMOItemData.binoculars], SMORuleOperation.NONE),
    ],
    SMOLocationData.bonnetter_blockade: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.cap_kingdom_regular_cup: [],
    SMOLocationData.peach_in_the_cap_kingdom: [],
    SMOLocationData.found_with_cap_kingdom_art: [],
    SMOLocationData.next_to_glasses_bridge: [],
    SMOLocationData.danger_sign: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.under_the_big_ones_brim: [],
    SMOLocationData.fly_to_the_edge_of_the_fog: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.spin_the_hat_get_a_prize: [],
    SMOLocationData.hidden_in_a_sunken_hat: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.fog_shrouded_platform: [],
    SMOLocationData.bird_traveling_in_the_fog: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.caught_hopping_near_the_ship: [],
    SMOLocationData.taking_notes_in_the_fog: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.cap_kingdom_timer_challenge_2: [],
    SMOLocationData.cap_kingdom_master_cup: [],
    SMOLocationData.roll_on_and_on: [],
    SMOLocationData.precision_rolling: [],
    #endregion

    #region Cascade
    SMOLocationData.our_first_power_moon: [
        (SMORuleCondition.CAPTURE, [SMOItemData.chain_chomp], SMORuleOperation.OR),
        (SMORuleCondition.CAPTURE, SMOItemData.t_rex, SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.GLITCH_HARD, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.multi_moon_atop_the_falls: [
        (SMORuleCondition.CAPTURE, SMOItemData.big_chain_chomp, SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.CAPTURE, SMOItemData.t_rex, SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.CAPTURE, SMOItemData.broodes_chain_chomp, SMORuleOperation.NONE),
    ],
    SMOLocationData.chomp_through_the_rocks: [
        (SMORuleCondition.CAPTURE, [SMOItemData.chain_chomp], SMORuleOperation.OR), # big chomp?
        (SMORuleCondition.CAPTURE, [SMOItemData.t_rex], SMORuleOperation.NONE),
    ],
    SMOLocationData.behind_the_waterfall: [
        (SMORuleCondition.CAPTURE, [SMOItemData.t_rex], SMORuleOperation.OR),
        (SMORuleCondition.CAPTURE, [SMOItemData.big_chain_chomp], SMORuleOperation.NONE),
    ],
    SMOLocationData.on_top_of_the_rubble: [],
    SMOLocationData.treasure_of_the_waterfall_basin: [],
    SMOLocationData.above_a_high_cliff: [],
    SMOLocationData.across_the_floating_isles: [],
    SMOLocationData.cascade_kingdom_timer_challenge_1: [],
    SMOLocationData.cascade_kingdom_timer_challenge_2: [],
    SMOLocationData.good_morning_captain_toad: [],
    SMOLocationData.dinosaur_nest_big_cleanup: [],
    SMOLocationData.dinosaur_nest_running_wild: [
        (SMORuleCondition.CAPTURE, [SMOItemData.t_rex], SMORuleOperation.NONE),
    ],
    SMOLocationData.nice_shot_with_the_chain_chomp: [
        (SMORuleCondition.CAPTURE, [SMOItemData.chain_chomp], SMORuleOperation.NONE),
    ],
    SMOLocationData.very_nice_shot_with_the_chain_chomp: [
        (SMORuleCondition.CAPTURE, [SMOItemData.chain_chomp], SMORuleOperation.NONE),
    ],
    SMOLocationData.past_the_chasm_lifts: [],
    SMOLocationData.hidden_chasm_passage: [],
    SMOLocationData.secret_path_to_fossil_falls: [

    ],
    SMOLocationData.a_tourist_in_the_cascade_kingdom: [],
    SMOLocationData.rolling_rock_by_the_falls: [],
    SMOLocationData.peach_in_the_cascade_kingdom: [],
    SMOLocationData.cascade_kingdom_regular_cup: [],
    SMOLocationData.caveman_cave_fan: [
        (SMORuleCondition.ITEM, [SMOItemData.caveman_headwear, SMOItemData.caveman_outfit],
         SMORuleOperation.NONE),
    ],
    SMOLocationData.shopping_in_fossil_falls: [
        (SMORuleCondition.REGION, SMORegion.restored_odyssey, SMORuleOperation.NONE),
    ],
    SMOLocationData.sphynx_traveling_to_the_waterfall: [
        (SMORuleCondition.CAPTURE, [SMOItemData.binoculars], SMORuleOperation.NONE),
    ],
    SMOLocationData.bottom_of_the_waterfall_basin: [],
    SMOLocationData.just_a_hat_skip_and_a_jump: [],
    SMOLocationData.treasure_under_the_cliff: [],
    SMOLocationData.next_to_the_stone_arch: [],
    SMOLocationData.guarded_by_a_colossal_fossil: [],
    SMOLocationData.under_the_old_electrical_pole: [
        (SMORuleCondition.CAPTURE, [SMOItemData.t_rex], SMORuleOperation.NONE),
    ],
    SMOLocationData.under_the_ground: [
        (SMORuleCondition.CAPTURE, [SMOItemData.t_rex], SMORuleOperation.NONE),
    ],
    SMOLocationData.inside_the_busted_fossil: [
        (SMORuleCondition.CAPTURE, [SMOItemData.chain_chomp], SMORuleOperation.NONE),
    ],
    SMOLocationData.caught_hopping_at_the_waterfall: [],
    SMOLocationData.taking_notes_hurry_upward: [],
    SMOLocationData.cascade_kingdom_master_cup: [],
    SMOLocationData.across_the_mysterious_clouds: [],
    SMOLocationData.atop_a_wall_among_the_clouds: [],
    SMOLocationData.across_the_gusty_bridges: [],
    SMOLocationData.flying_far_away_from_gusty_bridges: [],
    #endregion

    #region Sand
    SMOLocationData.atop_the_highest_tower: [],
    SMOLocationData.moon_shards_in_the_sand: [
        (SMORuleCondition.CAPTURE, [SMOItemData.moe_eye], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMORuleCondition.CAPTURE], SMORuleOperation.NONE),
    ],
    SMOLocationData.showdown_on_the_inverted_pyramid: [

    ],
    SMOLocationData.the_hole_in_the_desert: [
        (SMORuleCondition.CAPTURE, [SMOItemData.bullet_bill, SMOItemData.knucklotecs_fist], SMORuleOperation.NONE),
    ],
    SMOLocationData.overlooking_the_desert_town: [],
    SMOLocationData.alcove_in_the_ruins: [],
    SMOLocationData.on_the_leaning_pillar: [],
    SMOLocationData.hidden_room_in_the_flowing_sands: [],
    SMOLocationData.secret_of_the_mural: [],
    SMOLocationData.secret_of_the_inverted_mural: [],
    SMOLocationData.on_top_of_stone_archway: [],
    SMOLocationData.from_a_crate_in_the_ruins: [],
    SMOLocationData.on_the_lone_pillar: [
        (SMORuleCondition.CAPTURE, [SMOItemData.bullet_bill], SMORuleOperation.OR),
        (SMORuleCondition.CAPTURE, [SMOItemData.glydon], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.REGION, SMORegion.top_of_the_inverted_pyramid, SMORuleOperation.PARENTHESIS_NONE),
    ],
    SMOLocationData.on_the_statues_tail: [],
    SMOLocationData.hang_your_hat_on_the_fountain: [],
    SMOLocationData.where_the_birds_gather: [],
    SMOLocationData.top_of_a_dune: [],
    SMOLocationData.lost_in_the_luggage: [],
    SMOLocationData.bullet_bill_breakthrough: [
        (SMORuleCondition.CAPTURE, [SMOItemData.bullet_bill], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMORuleCondition.CAPTURE], SMORuleOperation.NONE),
    ],
    SMOLocationData.inside_a_block_is_a_hard_place: [],
    SMOLocationData.bird_traveling_the_desert: [],
    SMOLocationData.bird_traveling_wastes: [],
    SMOLocationData.the_lurker_under_the_stone: [

    ],
    SMOLocationData.the_treasure_of_jaxi_ruins: [],
    SMOLocationData.desert_gardening_plaza_seed: [],
    SMOLocationData.desert_gardening_ruins_seed: [],
    SMOLocationData.desert_gardening_seed_on_the_cliff: [],
    SMOLocationData.sand_kingdom_timer_challenge_1: [],
    SMOLocationData.sand_kingdom_timer_challenge_2: [],
    SMOLocationData.sand_kingdom_timer_challenge_3: [],
    SMOLocationData.found_in_the_sand_good_dog: [],
    SMOLocationData.taking_notes_jump_on_the_palm: [],
    SMOLocationData.herding_sheep_in_the_dunes: [],
    SMOLocationData.fishing_in_the_oasis: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lakitu], SMORuleOperation.NONE),
    ],
    SMOLocationData.love_in_the_heart_of_the_desert: [
        (SMORuleCondition.CAPTURE, [SMOItemData.goomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.among_the_five_cactuses: [
        (SMORuleCondition.REGION, SMORegion.night_sand_kingdom, SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [], SMORuleOperation.OR),
        (SMORuleCondition.ENTRANCE, [SMORegion.sand_kingdom, SMOEntranceData.jaxi_ruins, SMOEntranceDataType.UNIQUE_EXIT], SMORuleOperation.NONE),
    ],
    SMOLocationData.youre_quite_a_catch_captain_toad: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lakitu], SMORuleOperation.NONE),
    ],
    SMOLocationData.jaxi_reunion: [],
    SMOLocationData.welcome_back_jaxi: [],
    SMOLocationData.wandering_cactus: [
        (SMORuleCondition.CAPTURE, [SMOItemData.cactus], SMORuleOperation.NONE),
    ],
    SMOLocationData.sand_quiz_wonderful: [],
    SMOLocationData.shopping_in_tostarena: [],
    SMOLocationData.employees_only: [],
    SMOLocationData.sand_kingdom_slots: [],
    SMOLocationData.walking_the_desert: [],
    SMOLocationData.hidden_room_in_the_inverted_pyramid: [
        (SMORuleCondition.CAPTURE, [SMOItemData.bullet_bill], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMORuleCondition.CAPTURE], SMORuleOperation.NONE),
    ],
    SMOLocationData.underground_treasure_chest: [
        (SMORuleCondition.CAPTURE, [SMOItemData.bullet_bill], SMORuleOperation.NONE),
        #backwards accessibility
    ],
    SMOLocationData.goomba_tower_assembly: [
        (SMORuleCondition.CAPTURE, [SMOItemData.goomba], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMORuleCondition.CAPTURE], SMORuleOperation.PARENTHESIS_NONE)
    ],
    SMOLocationData.under_the_mummys_curse: [],
    SMOLocationData.ice_cave_treasure: [],
    SMOLocationData.sphynxs_treasure_vault: [],
    SMOLocationData.a_rumble_from_the_sandy_floor: [],
    SMOLocationData.dancing_with_new_friends: [],
    SMOLocationData.the_invisible_maze: [
        (SMORuleCondition.CAPTURE, [SMOItemData.moe_eye], SMORuleOperation.NONE),
    ],
    SMOLocationData.skull_sign_in_the_transparent_maze: [
        (SMORuleCondition.CAPTURE, [SMOItemData.moe_eye], SMORuleOperation.NONE),
    ],
    SMOLocationData.the_bullet_bill_maze_break_through: [
        (SMORuleCondition.CAPTURE, [SMOItemData.bullet_bill], SMORuleOperation.NONE),
    ],
    SMOLocationData.the_bullet_bill_maze_side_path: [
        (SMORuleCondition.CAPTURE, [SMOItemData.bullet_bill], SMORuleOperation.NONE),
    ],
    SMOLocationData.jaxi_driver: [],
    SMOLocationData.jaxi_stunt_driving: [],
    SMOLocationData.strange_neighborhood: [
        (SMORuleCondition.CAPTURE, [SMOItemData.mini_rocket], SMORuleOperation.NONE),
    ],
    SMOLocationData.above_a_strange_neighborhood: [
        (SMORuleCondition.CAPTURE, [SMOItemData.mini_rocket], SMORuleOperation.NONE),
    ],
    SMOLocationData.secret_path_to_tostarena: [

    ],
    SMOLocationData.found_with_sand_kingdom_art: [
        (SMORuleCondition.CAPTURE, [SMOItemData.spark_pylon], SMORuleOperation.NONE),
    ],
    SMOLocationData.jammin_in_the_sand_kingdom: [],
    SMOLocationData.hat_and_seek_in_the_sand: [],
    SMOLocationData.sand_kingdom_regular_cup: [],
    SMOLocationData.binding_band_returned: [],
    SMOLocationData.round_the_world_tourist: [],
    SMOLocationData.peach_in_the_sand_kingdom: [],
    SMOLocationData.mighty_leap_from_the_palm_tree: [],
    SMOLocationData.on_the_north_pillar: [],
    SMOLocationData.into_the_flowing_sands: [],
    SMOLocationData.in_the_skies_above_the_canyon: [],
    SMOLocationData.island_in_the_poison_swamp: [],
    SMOLocationData.an_invisible_gleam: [],
    SMOLocationData.on_the_eastern_pillar: [],
    SMOLocationData.caught_hopping_in_the_desert: [],
    SMOLocationData.poster_cleanup: [],
    SMOLocationData.taking_notes_running_down: [],
    SMOLocationData.taking_notes_in_the_wall_painting: [],
    SMOLocationData.love_at_the_edge_of_the_desert: [
        (SMORuleCondition.CAPTURE, [SMOItemData.goomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.more_walking_in_the_desert: [],
    SMOLocationData.sand_kingdom_master_cup: [],
    SMOLocationData.where_the_transparent_platforms_end: [
        (SMORuleCondition.CAPTURE, [SMOItemData.moe_eye], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMORuleCondition.CAPTURE], SMORuleOperation.NONE),
    ],
    SMOLocationData.jump_onto_the_transparent_lift: [
        (SMORuleCondition.CAPTURE, [SMOItemData.moe_eye], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMORuleCondition.CAPTURE], SMORuleOperation.NONE),
    ],
    SMOLocationData.colossal_ruins_dash_jump: [],
    SMOLocationData.sinking_colossal_ruins_hurry: [],
    SMOLocationData.through_the_freezing_waterway: [
        (SMORuleCondition.CAPTURE, [SMOItemData.gushen], SMORuleOperation.NONE),
    ],
    SMOLocationData.freezing_waterway_hidden_room: [
        (SMORuleCondition.CAPTURE, [SMOItemData.gushen], SMORuleOperation.NONE),
    ],
    #endregion

    #region Wooded
    SMOLocationData.road_to_sky_garden: [
        (SMORuleCondition.CAPTURE, [SMOItemData.uproot], SMORuleOperation.NONE),
    ],
    SMOLocationData.flower_thieves_of_sky_garden: [],
    SMOLocationData.path_to_the_secret_flower_field: [
        (SMORuleCondition.CAPTURE, [SMOItemData.sherm], SMORuleOperation.NONE),
    ],
    SMOLocationData.defend_the_secret_flower_field: [
        (SMORuleCondition.CAPTURE, [SMOItemData.uproot], SMORuleOperation.NONE),
    ],
    SMOLocationData.behind_the_rock_wall: [
        (SMORuleCondition.CAPTURE, [SMOItemData.sherm], SMORuleOperation.NONE),
    ],
    SMOLocationData.back_way_up_the_mountain: [],
    SMOLocationData.rolling_rock_in_the_woods: [],
    SMOLocationData.caught_hopping_in_the_forest: [],
    SMOLocationData.thanks_for_the_charge: [],
    SMOLocationData.atop_a_tall_tree: [],
    SMOLocationData.tucked_away_inside_a_tunnel: [
        (SMORuleCondition.CAPTURE, [SMOItemData.uproot], SMORuleOperation.NONE),
    ],
    SMOLocationData.over_the_cliffs_edge: [
        (SMORuleCondition.CAPTURE, [SMOItemData.uproot], SMORuleOperation.NONE),
    ],
    SMOLocationData.the_nut_round_the_corner: [],
    SMOLocationData.climb_the_cliff_to_get_the_nut: [],
    SMOLocationData.the_nut_in_the_red_maze: [
        (SMORuleCondition.CAPTURE, [SMOItemData.uproot], SMORuleOperation.NONE),
    ],
    SMOLocationData.the_nut_at_the_dead_end: [],
    SMOLocationData.cracked_nut_on_a_crumbling_tower: [],
    SMOLocationData.the_nut_that_grew_on_the_tall_fence: [],
    SMOLocationData.fire_in_the_cave: [],
    SMOLocationData.hey_out_there_captain_toad: [
        (SMORuleCondition.CAPTURE, [SMOItemData.glydon], SMORuleOperation.NONE),
    ],
    SMOLocationData.love_in_the_forest_ruins: [
        (SMORuleCondition.CAPTURE, [SMOItemData.goomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.inside_the_rock_in_the_forest: [],
    SMOLocationData.shopping_in_steam_gardens: [],
    SMOLocationData.nut_planted_in_the_tower: [],
    SMOLocationData.stretching_your_legs: [
        (SMORuleCondition.CAPTURE, [SMOItemData.uproot], SMORuleOperation.NONE),
    ],
    SMOLocationData.spinning_platforms_treasure: [],
    SMOLocationData.make_the_secret_flower_field_bloom: [],
    SMOLocationData.rolling_rock_in_the_deep_woods: [],
    SMOLocationData.glowing_in_the_deep_woods: [],
    SMOLocationData.past_the_peculiar_pipes: [],
    SMOLocationData.by_the_babbling_brook_in_the_deep_woods: [
        (SMORuleCondition.CAPTURE, [SMOItemData.t_rex], SMORuleOperation.OR),
        (SMORuleCondition.CAPTURE, [SMOItemData.coin_coffer], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.the_hard_rock_in_deep_woods: [
        (SMORuleCondition.CAPTURE, [SMOItemData.t_rex], SMORuleOperation.OR),
        (SMORuleCondition.CAPTURE, [SMOItemData.coin_coffer], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.a_treasure_made_of_coins: [
        (SMORuleCondition.CAPTURE, [SMOItemData.coin_coffer], SMORuleOperation.NONE),
    ],
    SMOLocationData.beneath_the_roots_of_a_moving_tree: [
        (SMORuleCondition.CAPTURE, [SMOItemData.tree], SMORuleOperation.NONE),
    ],
    SMOLocationData.deep_woods_treasure_trap: [],
    SMOLocationData.exploring_for_treasure: [],
    SMOLocationData.wooded_kingdom_timer_challenge_1: [],
    SMOLocationData.wooded_kingdom_timer_challenge_2: [],
    SMOLocationData.flooding_pipeway: [],
    SMOLocationData.flooding_pipeway_ceiling_secret: [],
    SMOLocationData.wandering_in_the_fog: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.nut_hidden_in_the_fog: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.flower_road_run: [],
    SMOLocationData.flower_road_reach: [
        # (SMORuleCondition.CAPTURE, [SMOItemData.goomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.elevator_escalation: [
        (SMORuleCondition.CAPTURE, [SMOItemData.sherm], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.elevator_blind_spot: [
        (SMORuleCondition.CAPTURE, [SMOItemData.sherm], SMORuleOperation.NONE),
    ],
    SMOLocationData.walking_on_clouds: [
        (SMORuleCondition.CAPTURE, [SMOItemData.uproot], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.above_the_clouds: [
        (SMORuleCondition.CAPTURE, [SMOItemData.uproot], SMORuleOperation.NONE),
    ],
    SMOLocationData.secret_path_to_the_steam_gardens: [

    ],
    SMOLocationData.found_with_wooded_kingdom_art: [],
    SMOLocationData.swing_around_secret_flower_field: [],
    SMOLocationData.jammin_in_the_wooded_kingdom: [],
    SMOLocationData.wooded_kingdom_regular_cup: [],
    SMOLocationData.peach_in_the_wooded_kingdom: [],
    SMOLocationData.high_up_in_the_cave: [
        (SMORuleCondition.CAPTURE, [SMOItemData.uproot], SMORuleOperation.NONE),
    ],
    SMOLocationData.lost_in_the_tall_trees: [
        (SMORuleCondition.CAPTURE, [SMOItemData.glydon, SMOItemData.sherm], SMORuleOperation.NONE),
    ],
    SMOLocationData.looking_down_on_the_goombas: [
        (SMORuleCondition.CAPTURE, [SMOItemData.glydon], SMORuleOperation.NONE),
    ],
    SMOLocationData.high_up_on_a_rock_wall: [
        (SMORuleCondition.CAPTURE, [SMOItemData.uproot], SMORuleOperation.NONE),
    ],
    SMOLocationData.the_nut_in_the_robot_storeroom: [
        (SMORuleCondition.CAPTURE, [SMOItemData.uproot], SMORuleOperation.NONE),
    ],
    SMOLocationData.above_the_iron_mountain_path: [],
    SMOLocationData.the_nut_under_the_observation_deck: [],
    SMOLocationData.bird_traveling_the_forest: [],
    SMOLocationData.invader_in_the_sky_garden: [
        (SMORuleCondition.CAPTURE, [SMOItemData.goomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.hot_hot_hot_from_the_campfire: [
        (SMORuleCondition.CAPTURE, [SMOItemData.fire_bro], SMORuleOperation.NONE),
    ],
    SMOLocationData.wooded_kingdom_timer_challenge_3: [],
    SMOLocationData.moon_shards_in_the_forest: [
        (SMORuleCondition.CAPTURE, [SMOItemData.uproot], SMORuleOperation.NONE),
    ],
    SMOLocationData.taking_notes_on_top_of_the_wall: [],
    SMOLocationData.taking_notes_stretching: [
        (SMORuleCondition.CAPTURE, [SMOItemData.uproot], SMORuleOperation.NONE),
    ],
    SMOLocationData.wooded_kingdom_master_cup: [],
    SMOLocationData.i_met_an_uproot: [
        (SMORuleCondition.CAPTURE, [SMOItemData.uproot], SMORuleOperation.NONE),
    ],
    SMOLocationData.invisible_road_danger: [],
    SMOLocationData.invisible_road_hidden_room: [],
    SMOLocationData.herding_sheep_above_the_forest_fog: [],
    SMOLocationData.herding_sheep_on_the_iron_bridge: [],
    SMOLocationData.down_and_back_breakdown_road: [],
    SMOLocationData.below_breakdown_road: [
        (SMORuleCondition.CAPTURE, [SMOItemData.banzai_bill], SMORuleOperation.NONE),
    ],
    #endregion

    #region Lake
    SMOLocationData.broodals_over_the_lake: [],
    SMOLocationData.dorrie_back_rider: [],
    SMOLocationData.cheep_cheep_crossing: [],
    SMOLocationData.end_of_the_hidden_passage: [
        (SMORuleCondition.CAPTURE, [SMOItemData.zipper], SMORuleOperation.NONE),
    ],
    SMOLocationData.whats_in_the_box: [],
    SMOLocationData.on_the_lakeshore: [],
    SMOLocationData.from_the_broken_pillar: [],
    SMOLocationData.treasure_in_the_spiky_waterway: [],
    SMOLocationData.lake_gardening_spiky_passage_seed: [],
    SMOLocationData.lake_kingdom_timer_challenge_1: [],
    SMOLocationData.lake_kingdom_timer_challenge_2: [],
    SMOLocationData.moon_shards_in_the_lake: [],
    SMOLocationData.taking_notes_dive_and_swim: [],
    SMOLocationData.taking_notes_in_the_cliffside: [],
    SMOLocationData.lake_fishing: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lakitu], SMORuleOperation.NONE),
    ],
    SMOLocationData.i_met_a_lake_cheep_cheep: [
        (SMORuleCondition.CAPTURE, [SMOItemData.cheep_cheep], SMORuleOperation.NONE),
    ],
    SMOLocationData.our_secret_little_room: [],
    SMOLocationData.lets_go_swimming_captain_toad: [
        (SMORuleCondition.CAPTURE, [SMOItemData.cheep_cheep], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.shopping_in_lake_lamode: [],
    SMOLocationData.a_successful_repair_job: [
        (SMORuleCondition.CAPTURE, [SMOItemData.puzzle_part_lake_kingdom], SMORuleOperation.NONE),
    ],
    SMOLocationData.i_feel_underdressed: [
        (SMORuleCondition.ITEM, [SMOItemData.swim_goggles, SMOItemData.swimwear], SMORuleOperation.OR),
        (SMORuleCondition.ITEM, SMOItemData.boxer_shorts, SMORuleOperation.NONE)
    ],
    SMOLocationData.unzip_the_chasm: [
        (SMORuleCondition.CAPTURE, [SMOItemData.zipper], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.super_secret_zipper: [
        (SMORuleCondition.CAPTURE, [SMOItemData.zipper], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.jump_grab_cling_and_climb: [],
    SMOLocationData.jump_grab_and_climb_some_more: [],
    SMOLocationData.secret_path_to_lake_lamode: [
        # lake clip
    ],
    SMOLocationData.found_with_lake_kingdom_art: [],
    SMOLocationData.taxi_flying_through_lake_lamode: [
        (SMORuleCondition.CAPTURE, [SMOItemData.binoculars], SMORuleOperation.NONE),
    ],
    SMOLocationData.that_trendy_pirate_look: [
        (SMORuleCondition.ITEM, [SMOItemData.pirate_hat, SMOItemData.pirate_outfit], SMORuleOperation.NONE),
    ],
    SMOLocationData.space_is_in_right_now: [
        (SMORuleCondition.ITEM, [SMOItemData.space_helmet, SMOItemData.space_suit], SMORuleOperation.NONE),
    ],
    SMOLocationData.that_old_west_style: [
        (SMORuleCondition.ITEM, [SMOItemData.cowboy_hat, SMOItemData.cowboy_outfit], SMORuleOperation.NONE),
    ],
    SMOLocationData.lake_kingdom_regular_cup: [],
    SMOLocationData.peach_in_the_lake_kingdom: [],
    SMOLocationData.behind_the_floodgate: [],
    SMOLocationData.high_flying_leap: [],
    SMOLocationData.deep_deep_down: [
        (SMORuleCondition.CAPTURE, [SMOItemData.cheep_cheep], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.rooftop_of_the_water_plaza: [],
    SMOLocationData.bird_traveling_over_the_lake: [],
    SMOLocationData.love_by_the_lake: [
        (SMORuleCondition.CAPTURE, [SMOItemData.goomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.lake_kingdom_master_cup: [],
    SMOLocationData.waves_of_poison_hoppin_over: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.waves_of_poison_hop_to_it: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],

    SMOLocationData.picture_match_basically_a_goomba: [
        (SMORuleCondition.CAPTURE, [SMOItemData.picture_match_part_goomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.peach_in_the_cloud_kingdom: [],
    SMOLocationData.digging_in_the_cloud: [],
    SMOLocationData.high_high_above_the_clouds: [],
    SMOLocationData.crossing_the_cloud_sea: [],
    SMOLocationData.taking_notes_up_and_down: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE),
        # maybe
    ],
    SMOLocationData.picture_match_a_stellar_goomba: [
        (SMORuleCondition.CAPTURE, [SMOItemData.picture_match_part_goomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.king_of_the_cube: [],
    SMOLocationData.the_sixth_face: [],
    #endregion

    #region Lost
    SMOLocationData.atop_a_propeller_pillar: [],
    SMOLocationData.below_the_cliffs_edge: [],
    SMOLocationData.inside_the_stone_cage: [],
    SMOLocationData.on_a_tree_in_the_swamp: [
        (SMORuleCondition.CAPTURE, [SMOItemData.tropical_wiggler], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.over_the_fuzzies_above_the_swamp: [],
    SMOLocationData.avoiding_fuzzies_inside_the_wall: [],
    SMOLocationData.inside_the_rising_stone_pillar: [],
    SMOLocationData.enjoying_the_view_of_forgotten_isle: [],
    SMOLocationData.on_the_mountain_road: [],
    SMOLocationData.a_propeller_pillars_secret: [],
    SMOLocationData.wrecked_rock_block: [],
    SMOLocationData.a_butterflys_treasure: [],
    SMOLocationData.caught_hopping_in_the_jungle: [],
    SMOLocationData.cave_gardening: [],
    SMOLocationData.moon_shards_in_the_jungle: [
        (SMORuleCondition.CAPTURE, [SMOItemData.tropical_wiggler], SMORuleOperation.NONE),
    ],
    SMOLocationData.peeking_out_from_under_the_bridge: [
        (SMORuleCondition.CAPTURE, [SMOItemData.tropical_wiggler], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.twist_n_turn_up_treasure: [
        (SMORuleCondition.CAPTURE, [SMOItemData.tropical_wiggler], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.CAPTURE, [SMOItemData.glydon], SMORuleOperation.PARENTHESIS_NONE),
    ],
    SMOLocationData.soaring_over_the_forgotten_isle: [
        (SMORuleCondition.CAPTURE, [SMOItemData.glydon], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.the_caged_gold: [],
    SMOLocationData.get_some_rest_captain_toad: [
        (SMORuleCondition.CAPTURE, [SMOItemData.tropical_wiggler], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.shopping_on_forgotten_isle: [],
    SMOLocationData.taxi_flying_through_forgotten_isle: [
        (SMORuleCondition.CAPTURE, [SMOItemData.binoculars], SMORuleOperation.NONE),
    ],
    SMOLocationData.i_met_a_tropical_wiggler: [
        (SMORuleCondition.CAPTURE, [SMOItemData.tropical_wiggler], SMORuleOperation.NONE),
    ],
    SMOLocationData.lost_kingdom_regular_cup: [],
    SMOLocationData.peach_in_the_lost_kingdom: [],
    SMOLocationData.the_shining_fruit: [],
    SMOLocationData.jump_down_to_the_top_of_a_tree: [],
    SMOLocationData.line_it_up_blow_it_up: [],
    SMOLocationData.taking_notes_stretch_and_shrink: [
        (SMORuleCondition.CAPTURE, [SMOItemData.tropical_wiggler], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.lost_kingdom_master_cup: [],
    SMOLocationData.lost_kingdom_timer_challenge: [],
    SMOLocationData.stretch_and_traverse_the_jungle: [
        (SMORuleCondition.CAPTURE, [SMOItemData.tropical_wiggler], SMORuleOperation.NONE),
    ],
    SMOLocationData.aglow_in_the_jungle: [
        (SMORuleCondition.CAPTURE, [SMOItemData.tropical_wiggler], SMORuleOperation.NONE),
    ],
    SMOLocationData.chasing_klepto: [],
    SMOLocationData.extremely_hot_bath: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    #endregion

    #region Metro
    SMOLocationData.new_donk_citys_pest_problem: [
        (SMORuleCondition.CAPTURE, [SMOItemData.sherm, SMOItemData.spark_pylon], SMORuleOperation.NONE),
    ],
    SMOLocationData.drummer_on_board: [],
    SMOLocationData.guitarist_on_board: [],
    SMOLocationData.bassist_on_board: [],
    SMOLocationData.trumpeter_on_board: [],
    SMOLocationData.powering_up_the_station: [
        (SMORuleCondition.CAPTURE, [SMOItemData.manhole], SMORuleOperation.NONE),
    ],
    SMOLocationData.a_traditional_festival: [],
    SMOLocationData.inside_an_iron_girder: [],
    SMOLocationData.swaying_in_the_breeze: [],
    SMOLocationData.girder_sandwich: [],
    SMOLocationData.glittering_above_the_pool: [],
    SMOLocationData.dizzying_heights: [],
    SMOLocationData.secret_girder_tunnel: [],
    SMOLocationData.who_piled_garbage_on_this: [],
    SMOLocationData.hidden_in_the_scrap: [],
    SMOLocationData.left_at_the_cafe: [],
    SMOLocationData.caught_hopping_on_a_building: [],
    SMOLocationData.how_do_they_take_out_the_trash: [],
    SMOLocationData.metro_kingdom_timer_challenge_1: [],
    SMOLocationData.metro_kingdom_timer_challenge_2: [],
    SMOLocationData.city_gardening_building_planter: [],
    SMOLocationData.city_gardening_plaza_planter: [],
    SMOLocationData.city_gardening_rooftop_planter: [],
    SMOLocationData.how_you_doin_captain_toad: [],
    SMOLocationData.free_parking_rooftop_hop: [],
    SMOLocationData.bench_friends: [],
    SMOLocationData.shopping_in_new_donk_city: [],
    SMOLocationData.metro_kingdom_slots: [],
    SMOLocationData.jump_rope_hero: [],
    SMOLocationData.jump_rope_genius: [],
    SMOLocationData.remotely_captured_car: [
        (SMORuleCondition.CAPTURE, [SMOItemData.rc_car], SMORuleOperation.NONE),
        #scooter clip
    ],
    SMOLocationData.rc_car_pro: [
        (SMORuleCondition.CAPTURE, [SMOItemData.rc_car], SMORuleOperation.NONE),
    ],
    SMOLocationData.taking_notes_in_the_private_room: [],
    SMOLocationData.city_hall_lost_and_found: [],
    SMOLocationData.sewer_treasure: [],
    SMOLocationData.celebrating_in_the_streets: [],
    SMOLocationData.pushing_through_the_crowd: [],
    SMOLocationData.high_over_the_crowd: [],
    SMOLocationData.rewiring_the_neighborhood: [
        (SMORuleCondition.CAPTURE, [SMOItemData.spark_pylon], SMORuleOperation.NONE),
    ],
    SMOLocationData.off_the_beaten_wire: [
        (SMORuleCondition.CAPTURE, [SMOItemData.spark_pylon], SMORuleOperation.NONE),
    ],
    SMOLocationData.moon_shards_under_siege: [
        (SMORuleCondition.CAPTURE, [SMOItemData.sherm], SMORuleOperation.NONE),
    ],
    SMOLocationData.sharpshooting_under_siege: [
        (SMORuleCondition.CAPTURE, [SMOItemData.sherm], SMORuleOperation.NONE),
    ],
    SMOLocationData.inside_the_rotating_maze: [
        (SMORuleCondition.CAPTURE, [SMOItemData.manhole], SMORuleOperation.NONE),
    ],
    SMOLocationData.outside_the_rotating_maze: [
        (SMORuleCondition.CAPTURE, [SMOItemData.manhole], SMORuleOperation.NONE),
    ],
    SMOLocationData.hanging_from_a_high_rise: [
        (SMORuleCondition.CAPTURE, [SMOItemData.mini_rocket], SMORuleOperation.NONE),
    ],
    SMOLocationData.vaulting_up_a_high_rise: [
        (SMORuleCondition.CAPTURE, [SMOItemData.mini_rocket], SMORuleOperation.NONE),
    ],
    SMOLocationData.bullet_billding: [],
    SMOLocationData.one_mans_trash: [
        (SMORuleCondition.CAPTURE, [SMOItemData.bullet_bill], SMORuleOperation.NONE),
    ],
    SMOLocationData.motor_scooter_escape: [],
    SMOLocationData.big_jump_escape: [],
    SMOLocationData.secret_path_to_new_donk_city: [

    ],
    SMOLocationData.a_tourist_in_the_metro_kingdom: [],
    SMOLocationData.found_with_metro_kingdom_art: [],
    SMOLocationData.bird_traveling_in_the_city: [],
    SMOLocationData.mario_signs_his_name: [
        (SMORuleCondition.CAPTURE, [SMOItemData.letter], SMORuleOperation.NONE),
    ],
    SMOLocationData.surprise_clown: [],
    SMOLocationData.a_request_from_the_mayor: [],
    SMOLocationData.jammin_in_the_metro_kingdom: [],
    SMOLocationData.sphynx_in_the_city: [
        (SMORuleCondition.CAPTURE, [SMOItemData.binoculars], SMORuleOperation.NONE),
    ],
    SMOLocationData.free_parking_leap_of_faith: [],
    SMOLocationData.metro_kingdom_regular_cup: [],
    SMOLocationData.hat_and_seek_in_the_city: [],
    SMOLocationData.powering_up_the_power_plant: [
        (SMORuleCondition.CAPTURE, [SMOItemData.puzzle_part_metro_kingdom, SMOItemData.manhole], SMORuleOperation.NONE),
    ],
    SMOLocationData.up_on_the_big_screen: [],
    SMOLocationData.down_inside_the_big_screen: [],
    SMOLocationData.peach_in_the_metro_kingdom: [],
    SMOLocationData.hanging_between_buildings: [],
    SMOLocationData.crossing_lines: [
        (SMORuleCondition.CAPTURE, [SMOItemData.spark_pylon], SMORuleOperation.NONE),
    ],
    SMOLocationData.out_of_a_crate_in_the_city: [],
    SMOLocationData.bird_traveling_in_the_park: [],
    SMOLocationData.metro_kingdom_timer_challenge_3: [],
    SMOLocationData.found_in_the_park_good_dog: [],
    SMOLocationData.rc_car_champ: [
        (SMORuleCondition.CAPTURE, [SMOItemData.rc_car], SMORuleOperation.NONE),
    ],
    SMOLocationData.metro_kingdom_master_cup: [],
    SMOLocationData.hat_and_seek_in_the_crowd: [],
    SMOLocationData.scaling_pitchblack_mountain: [],
    SMOLocationData.reaching_pitchblack_island: [],
    SMOLocationData.swinging_scaffolding_jump: [],
    SMOLocationData.swinging_scaffolding_break: [
        (SMORuleCondition.CAPTURE, [SMOItemData.hammer_bro], SMORuleOperation.NONE),
    ],
    SMOLocationData.moto_scooter_daredevil: [],
    SMOLocationData.full_throttle_scooting: [],
    #endregion

    #region Seaside
    SMOLocationData.the_stone_pillar_seal: [
        (SMORuleCondition.CAPTURE, [SMOItemData.gushen], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.the_lighthouse_seal: [
        (SMORuleCondition.CAPTURE, [SMOItemData.cheep_cheep], SMORuleOperation.NONE),
    ],
    SMOLocationData.the_hot_spring_seal: [
        (SMORuleCondition.CAPTURE, [SMOItemData.gushen], SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.ENTRANCE,
         [SMORegion.seaside_kingdom, f"{SMOEntranceData.underwater_tunnel} Unique Exit", SMOEntranceDataType.EXIT],
         SMORuleOperation.NONE)

    ],
    SMOLocationData.the_seal_above_the_canyon: [],
    SMOLocationData.the_glass_is_half_full: [
        (SMORuleCondition.CAPTURE, [SMOItemData.gushen], SMORuleOperation.NONE),
    ],
    SMOLocationData.on_the_cliff_overlooking_the_beach: [
        (SMORuleCondition.CAPTURE, [SMOItemData.gushen], SMORuleOperation.NONE),
    ],
    SMOLocationData.ride_the_jetstream: [
        (SMORuleCondition.CAPTURE, [SMOItemData.gushen], SMORuleOperation.NONE),
    ],
    SMOLocationData.ocean_bottom_maze_treasure: [],
    SMOLocationData.ocean_bottom_maze_hidden_room: [],
    SMOLocationData.underwater_highway_tunnel: [
        (SMORuleCondition.CAPTURE, [SMOItemData.cheep_cheep], SMORuleOperation.NONE),
    ],
    SMOLocationData.shh_its_a_shortcut: [
        (SMORuleCondition.CAPTURE, [SMOItemData.cheep_cheep], SMORuleOperation.NONE),
    ],
    SMOLocationData.gap_in_the_ocean_trench: [
        (SMORuleCondition.CAPTURE, [SMOItemData.cheep_cheep], SMORuleOperation.NONE),
    ],
    SMOLocationData.slip_through_the_nesting_spot: [
        (SMORuleCondition.CAPTURE, [SMOItemData.cheep_cheep], SMORuleOperation.NONE),
    ],
    SMOLocationData.merci_dorrie: [],
    SMOLocationData.bonjour_dorrie: [
        (SMORuleCondition.CAPTURE, [SMOItemData.gushen, SMOItemData.glydon], SMORuleOperation.NONE),
    ],
    SMOLocationData.under_a_dangerous_ceiling: [
        (SMORuleCondition.CAPTURE, [SMOItemData.cheep_cheep], SMORuleOperation.NONE),
    ],
    SMOLocationData.what_the_waves_left_behind: [],
    SMOLocationData.the_back_canyon_excavate: [],
    SMOLocationData.bubblaine_northern_reaches: [
        (SMORuleCondition.CAPTURE, [SMOItemData.cheep_cheep], SMORuleOperation.NONE),
    ],
    SMOLocationData.wriggling_on_the_sandy_bottom: [
        (SMORuleCondition.CAPTURE, [SMOItemData.cheep_cheep], SMORuleOperation.NONE),
    ],
    SMOLocationData.glass_palace_treasure_chest: [
        (SMORuleCondition.CAPTURE, [SMOItemData.cheep_cheep], SMORuleOperation.NONE),
    ],
    SMOLocationData.treasure_trap_hidden_in_the_inlet: [],
    SMOLocationData.sea_gardening_inlet_seed: [],
    SMOLocationData.sea_gardening_canyon_seed: [],
    SMOLocationData.sea_gardening_hot_spring_seed: [],
    SMOLocationData.sea_gardening_ocean_trench_seed: [],
    SMOLocationData.seaside_kingdom_timer_challenge_1: [],
    SMOLocationData.seaside_kingdom_timer_challenge_2: [],
    SMOLocationData.found_on_the_beach_good_dog: [],
    SMOLocationData.moon_shards_in_the_sea: [],
    SMOLocationData.taking_notes_ocean_surface_dash: [],
    SMOLocationData.love_by_the_seaside: [
        (SMORuleCondition.CAPTURE, [SMOItemData.goomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.lighthouse_leaper: [
        (SMORuleCondition.CAPTURE, [SMOItemData.glydon], SMORuleOperation.NONE),
    ],
    SMOLocationData.good_job_captain_toad: [],
    SMOLocationData.ocean_quiz_good: [],
    SMOLocationData.shopping_in_bubblaine: [],
    SMOLocationData.beach_volleyball_champ: [],
    SMOLocationData.beach_volleyball_hero_of_the_beach: [],
    SMOLocationData.looking_back_in_the_dark_waterway: [
        (SMORuleCondition.CAPTURE, [SMOItemData.cheep_cheep], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.the_sphynxs_underwater_vault: [],
    SMOLocationData.a_rumble_on_the_seaside_floor: [],
    SMOLocationData.a_relaxing_dance: [],
    SMOLocationData.wading_in_the_cloud_sea: [
        # (SMORuleCondition.CAPTURE, [SMOItemData.mini_rocket], SMORuleOperation.NONE),
    ],
    SMOLocationData.sunken_treasure_in_the_cloud_sea: [
        # (SMORuleCondition.CAPTURE, [SMOItemData.mini_rocket], SMORuleOperation.NONE),
    ],
    SMOLocationData.fly_through_the_narrow_valley: [
        (SMORuleCondition.CAPTURE, [SMOItemData.gushen], SMORuleOperation.NONE),
    ],
    SMOLocationData.treasure_chest_in_the_narrow_valley: [
        (SMORuleCondition.CAPTURE, [SMOItemData.gushen], SMORuleOperation.NONE),
    ],
    SMOLocationData.hurry_and_stretch: [
        (SMORuleCondition.CAPTURE, [SMOItemData.uproot], SMORuleOperation.NONE),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.stretch_on_the_side_path: [
        (SMORuleCondition.CAPTURE, [SMOItemData.uproot], SMORuleOperation.NONE),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.secret_path_to_bubblaine: [],
    SMOLocationData.found_with_seaside_kingdom_art: [],
    SMOLocationData.seaside_kingdom_regular_cup: [],
    SMOLocationData.peach_in_the_seaside_kingdom: [],
    SMOLocationData.above_the_parasol_catch: [],
    SMOLocationData.what_shines_inside_the_glass: [],
    SMOLocationData.a_fine_detail_on_the_glass: [],
    SMOLocationData.underwater_highway_west_explore: [],
    SMOLocationData.underwater_highway_east_explore: [],
    SMOLocationData.rapid_ascent_on_hot_spring_island: [
        (SMORuleCondition.CAPTURE, [SMOItemData.gushen], SMORuleOperation.NONE),
        # maybe skip
    ],
    SMOLocationData.a_light_next_to_the_lighthouse: [],
    SMOLocationData.the_tall_rock_shell_in_the_deep_ocean: [],
    SMOLocationData.at_the_base_of_the_lighthouse: [],
    SMOLocationData.bird_traveling_over_the_ocean: [
        (SMORuleCondition.CAPTURE, [SMOItemData.glydon], SMORuleOperation.OR),
        (SMORuleCondition.CAPTURE, [SMOItemData.gushen], SMORuleOperation.NONE),
    ],
    SMOLocationData.caught_hopping_at_glass_palace: [],
    SMOLocationData.seaside_kingdom_timer_challenge_3: [],
    SMOLocationData.taking_notes_ocean_bottom_maze: [],
    SMOLocationData.taking_notes_in_the_sea: [],
    SMOLocationData.seaside_kingdom_master_cup: [],
    SMOLocationData.aim_poke: [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE),
    ],
    SMOLocationData.poke_roll: [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE),
    ],
    SMOLocationData.the_spinning_maze_search: [],
    SMOLocationData.the_spinning_maze_open: [],
    #endregion

    #region Snow
    SMOLocationData.the_icicle_barrier: [],
    SMOLocationData.the_ice_wall_barrier: [],
    SMOLocationData.the_gusty_barrier: [
        (SMORuleCondition.CAPTURE, [SMOItemData.ty_foo], SMORuleOperation.NONE),
    ],
    SMOLocationData.the_snowy_mountain_barrier: [],
    SMOLocationData.the_bound_bowl_grand_prix: [
        (SMORuleCondition.CAPTURE, [SMOItemData.shiverian_racer], SMORuleOperation.NONE),
    ],
    SMOLocationData.entrance_to_shiveria: [],
    SMOLocationData.behind_the_snowy_mountain: [],
    SMOLocationData.shining_in_the_snow_in_town: [],
    SMOLocationData.atop_a_blustery_arch: [],
    SMOLocationData.caught_hopping_in_the_snow: [],
    SMOLocationData.the_shiverian_treasure_chest: [],
    SMOLocationData.treasure_in_the_ice_wall: [],
    SMOLocationData.snow_kingdom_timer_challenge_1: [],
    SMOLocationData.snow_kingdom_timer_challenge_2: [],
    SMOLocationData.moon_shards_in_the_snow: [],
    SMOLocationData.taking_notes_snow_path_dash: [],
    SMOLocationData.fishing_in_the_glacier: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lakitu], SMORuleOperation.NONE),
    ],
    SMOLocationData.ice_dodging_goomba_stack: [
        (SMORuleCondition.CAPTURE, [SMOItemData.goomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.captain_toad_is_chilly: [],
    SMOLocationData.im_not_cold: [
        (SMORuleCondition.ITEM, SMOItemData.boxer_shorts, SMORuleOperation.NONE)
    ],
    SMOLocationData.shopping_in_shiveria: [],
    SMOLocationData.walking_on_ice: [],
    SMOLocationData.snowline_circuit_class_s: [],
    SMOLocationData.dashing_over_cold_water: [],
    SMOLocationData.dashing_above_and_beyond: [],
    SMOLocationData.jump_n_swim_in_the_freezing_water: [],
    SMOLocationData.freezing_water_near_the_ceiling: [],
    SMOLocationData.blowing_and_sliding: [
        (SMORuleCondition.CAPTURE, [SMOItemData.ty_foo], SMORuleOperation.NONE),
    ],
    SMOLocationData.moon_shards_in_the_cold_room: [],
    SMOLocationData.slip_behind_the_ice: [],
    SMOLocationData.spinning_above_the_clouds: [],
    SMOLocationData.high_altitude_spinning: [],
    SMOLocationData.secret_path_to_shiveria: [

    ],
    SMOLocationData.found_with_snow_kingdom_art: [],
    SMOLocationData.snow_kingdom_regular_cup: [],
    SMOLocationData.hat_and_seek_in_the_snow: [],
    SMOLocationData.peach_in_the_snow_kingdom: [],
    SMOLocationData.shining_on_high: [],
    SMOLocationData.above_the_freezing_fish_pond: [],
    SMOLocationData.ice_floe_swimming: [],
    SMOLocationData.icy_jump_challenge: [],
    SMOLocationData.forgotten_in_the_holding_room: [],
    SMOLocationData.it_popped_out_of_the_ice: [],
    SMOLocationData.deep_in_the_cold_cold_water: [],
    SMOLocationData.water_pooling_in_the_crevasse: [],
    SMOLocationData.squirming_under_the_ice: [],
    SMOLocationData.snow_kingdom_timer_challenge_3: [
        (SMORuleCondition.CAPTURE, [SMOItemData.cheep_cheep_snow_kingdom], SMORuleOperation.NONE),
    ],
    SMOLocationData.stacked_up_ice_climb: [
        (SMORuleCondition.CAPTURE, [SMOItemData.goomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.i_met_a_snow_cheep_cheep: [
        (SMORuleCondition.CAPTURE, [SMOItemData.cheep_cheep_snow_kingdom], SMORuleOperation.NONE),
    ],
    SMOLocationData.even_more_walking_on_ice: [],
    SMOLocationData.snow_kingdom_master_cup: [
        (SMORuleCondition.CAPTURE, [SMOItemData.shiverian_racer], SMORuleOperation.NONE),
    ],
    SMOLocationData.iceburn_circuit_class_a: [
        (SMORuleCondition.CAPTURE, [SMOItemData.shiverian_racer], SMORuleOperation.NONE),
    ],
    SMOLocationData.iceburn_circuit_class_s: [
        (SMORuleCondition.CAPTURE, [SMOItemData.shiverian_racer], SMORuleOperation.NONE),
    ],
    SMOLocationData.running_the_flower_road: [],
    SMOLocationData.looking_back_on_the_flower_road: [],
    #endregion

    #region Luncheon
    SMOLocationData.the_broodals_are_after_some_cookin: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.under_the_cheese_rocks: [
        (SMORuleCondition.CAPTURE, [SMOItemData.hammer_bro, SMOItemData.lava_bubble], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.CAPTURE, [SMOItemData.hammer_bro], SMORuleOperation.PARENTHESIS_NONE),
    ],
    SMOLocationData.big_pot_on_the_volcano_dive_in: [
        (SMORuleCondition.CAPTURE, [SMOItemData.meat, SMOItemData.lava_bubble], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.PARENTHESIS_AND),
        (SMORuleCondition.CAPTURE, [SMOItemData.meat], SMORuleOperation.PARENTHESIS_NONE),
    ],
    SMOLocationData.climb_up_the_cascading_magma: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE),
        # Backwards access
    ],
    SMOLocationData.cookatiel_showdown: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE),
    ],
    SMOLocationData.piled_on_the_salt: [],
    SMOLocationData.lurking_in_the_pillars_shadow: [],
    SMOLocationData.atop_the_jutting_crag: [],
    SMOLocationData.is_this_an_ingredient_too: [],
    SMOLocationData.atop_a_column_in_a_row: [],
    SMOLocationData.surrounded_by_tall_mountains: [],
    SMOLocationData.island_of_salt_floating_in_the_lava: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE),
    ],
    SMOLocationData.overlooking_a_bunch_of_ingredients: [],
    SMOLocationData.light_the_lantern_on_the_small_island: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE),
    ],
    SMOLocationData.golden_turnip_recipe_1: [],
    SMOLocationData.golden_turnip_recipe_2: [],
    SMOLocationData.golden_turnip_recipe_3: [
        (SMORuleCondition.CAPTURE, [SMOItemData.hammer_bro], SMORuleOperation.NONE),
    ],
    SMOLocationData.luncheon_kingdom_timer_challenge_1: [],
    SMOLocationData.luncheon_kingdom_timer_challenge_2: [],
    SMOLocationData.luncheon_kingdom_timer_challenge_3: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE),
    ],
    SMOLocationData.beneath_the_rolling_vegetables: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE),
    ],
    SMOLocationData.all_the_cracks_are_fixed: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE),
    ],
    SMOLocationData.taking_notes_swimming_in_magma: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE),
    ],
    SMOLocationData.love_above_the_lava: [
        (SMORuleCondition.CAPTURE, [SMOItemData.goomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.shopping_in_mount_volbono: [],
    SMOLocationData.luncheon_kingdom_slots: [],
    SMOLocationData.a_strong_simmer: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE),
    ],
    SMOLocationData.an_extreme_simmer: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE),
    ],
    SMOLocationData.alcove_behind_the_pillars_of_magma: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE),
    ],
    SMOLocationData.treasure_beneath_the_cheese_rocks: [
        (SMORuleCondition.CAPTURE, [SMOItemData.hammer_bro], SMORuleOperation.NONE),
    ],
    SMOLocationData.light_the_two_flames: [
        (SMORuleCondition.CAPTURE, [SMOItemData.fire_bro, SMOItemData.lava_bubble], SMORuleOperation.NONE),
    ],
    SMOLocationData.light_the_far_off_lanterns: [
        (SMORuleCondition.CAPTURE, [SMOItemData.fire_piranha_plant], SMORuleOperation.NONE),
    ],
    SMOLocationData.bon_appetit_captain_toad: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE),
    ],
    SMOLocationData.the_treasure_chest_in_the_veggies: [],
    SMOLocationData.caught_hopping_at_the_volcano: [],
    SMOLocationData.taking_notes_big_pot_swim: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE),
    ],
    SMOLocationData.magma_swamp_floating_and_sinking: [],
    SMOLocationData.corner_of_the_magma_swamp: [],
    SMOLocationData.magma_narrow_path: [],
    SMOLocationData.crossing_to_the_magma: [],
    SMOLocationData.fork_flickin_to_the_summit: [
        (SMORuleCondition.CAPTURE, [SMOItemData.volbonan], SMORuleOperation.NONE),
    ],
    SMOLocationData.fork_flickin_detour: [
        (SMORuleCondition.CAPTURE, [SMOItemData.volbonan], SMORuleOperation.NONE),
    ],
    SMOLocationData.excavate_n_search_the_cheese_rocks: [
        (SMORuleCondition.CAPTURE, [SMOItemData.hammer_bro], SMORuleOperation.NONE),
    ],
    SMOLocationData.climb_the_cheese_rocks: [
        (SMORuleCondition.CAPTURE, [SMOItemData.hammer_bro], SMORuleOperation.NONE),
    ],
    SMOLocationData.spinning_athletics_end_goal: [],
    SMOLocationData.taking_notes_spinning_athletics: [],
    SMOLocationData.secret_path_to_mount_volbono: [

    ],
    SMOLocationData.a_tourist_in_the_luncheon_kingdom: [],
    SMOLocationData.found_with_luncheon_kingdom_art: [],
    SMOLocationData.the_rooftop_lantern: [
        (SMORuleCondition.CAPTURE, [SMOItemData.fire_bro], SMORuleOperation.NONE),
    ],
    SMOLocationData.jammin_in_the_luncheon_kingdom: [

    ],
    SMOLocationData.mechanic_repairs_complete: [],
    SMOLocationData.diving_from_the_big_pot: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE),
    ],
    SMOLocationData.hat_and_seek_among_the_food: [],
    SMOLocationData.luncheon_kingdom_regular_cup: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE),
    ],
    SMOLocationData.peach_in_the_luncheon_kingdom: [],
    SMOLocationData.from_inside_a_bright_stone: [],
    SMOLocationData.under_the_meat_plateau: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE),
    ],
    SMOLocationData.on_top_of_a_tall_tall_roof: [],
    SMOLocationData.from_a_crack_in_the_hard_ground: [],
    SMOLocationData.by_the_cannon_pointed_at_the_big_pot: [],
    SMOLocationData.luncheon_kingdom_master_cup: [],
    SMOLocationData.stepping_over_the_gears_and_lanterns_on_the_gear_steps: [
        (SMORuleCondition.CAPTURE, [SMOItemData.fire_bro], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.lanterns_on_the_gear_steps: [
        (SMORuleCondition.CAPTURE, [SMOItemData.fire_bro], SMORuleOperation.NONE),
    ],
    SMOLocationData.volcano_cave_cruisin: [],
    SMOLocationData.volcano_cave_and_mysterious_clouds: [],
    SMOLocationData.treasure_of_the_lava_islands: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE),
    ],
    SMOLocationData.flying_over_the_lava_islands: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE),
    ],

    SMOLocationData.battle_with_the_lord_of_lightning: [
        (SMORuleCondition.CAPTURE, [SMOItemData.spark_pylon], SMORuleOperation.NONE),
    ],
    SMOLocationData.in_the_ancient_treasure_chest: [],
    SMOLocationData.roulette_tower_climbed: [],
    SMOLocationData.roulette_tower_stopped: [],
    SMOLocationData.peach_in_the_ruined_kingdom: [],
    SMOLocationData.caught_in_a_big_horn: [],
    SMOLocationData.upon_the_broken_arch: [],
    SMOLocationData.rolling_rock_on_the_battlefield: [],
    SMOLocationData.charging_through_an_army: [
        (SMORuleCondition.CAPTURE, [SMOItemData.chargin_chuck], SMORuleOperation.NONE),
    ],
    SMOLocationData.the_mummys_curse: [],
    #endregion

    #region Bowser
    SMOLocationData.infiltrate_bowsers_castle: [
        (SMORuleCondition.CAPTURE, [SMOItemData.spark_pylon], SMORuleOperation.NONE),
    ],
    SMOLocationData.smart_bombing: [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE),
    ],
    SMOLocationData.big_broodal_battle: [],
    SMOLocationData.showdown_at_bowsers_castle: [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE),
    ],
    SMOLocationData.behind_the_big_wall: [],
    SMOLocationData.treasure_inside_the_turret: [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE),
    ],
    SMOLocationData.from_the_side_above_the_castle_gate: [],
    SMOLocationData.sunken_treasure_in_the_moat: [],
    SMOLocationData.past_the_moving_wall: [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE),
    ],
    SMOLocationData.above_the_poison_swamp: [],
    SMOLocationData.knocking_down_the_nice_frame: [],
    SMOLocationData.caught_on_the_iron_fence: [],
    SMOLocationData.on_the_giant_bowser_statues_nose: [],
    SMOLocationData.inside_a_block_in_the_castle: [],
    SMOLocationData.caught_hopping_at_bowsers_castle: [],
    SMOLocationData.exterminate_the_ogres: [],
    SMOLocationData.bowsers_kingdom_timer_challenge_1: [],
    SMOLocationData.taking_notes_between_spinies: [],
    SMOLocationData.stack_up_above_the_wall: [
        (SMORuleCondition.CAPTURE, [SMOItemData.goomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.hidden_corridor_under_the_floor: [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
    ],
    SMOLocationData.poking_your_nose_in_the_plaster_wall: [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE),
    ],
    SMOLocationData.poking_the_turret_wall: [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE),
    ],
    SMOLocationData.poking_your_nose_by_the_great_gate: [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE),
    ],
    SMOLocationData.jizo_all_in_a_row: [
        (SMORuleCondition.CAPTURE, [SMOItemData.jizo], SMORuleOperation.NONE),
    ],
    SMOLocationData.underground_jizo: [
        (SMORuleCondition.CAPTURE, [SMOItemData.jizo], SMORuleOperation.NONE),
    ],
    SMOLocationData.found_behind_bars: [
        (SMORuleCondition.CAPTURE, [SMOItemData.spark_pylon], SMORuleOperation.NONE),
    ],
    SMOLocationData.fishing_in_bowsers_castle: [
        (SMORuleCondition.CAPTURE, [SMOItemData.lakitu], SMORuleOperation.NONE),
    ],
    SMOLocationData.good_to_see_you_captain_toad: [],
    SMOLocationData.shopping_at_bowsers_castle: [],
    SMOLocationData.bowsers_castle_treasure_vault: [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE),
    ],
    SMOLocationData.scene_of_crossing_the_poison_swamp: [],
    SMOLocationData.taking_notes_in_the_folding_screen: [],
    SMOLocationData.on_top_of_the_spinning_tower: [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE),
    ],
    SMOLocationData.down_and_up_the_spinning_tower: [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE),
    ],
    SMOLocationData.jizos_big_adventure: [
        (SMORuleCondition.CAPTURE, [SMOItemData.jizo], SMORuleOperation.NONE),
    ],
    SMOLocationData.jizo_and_the_hidden_room: [
        (SMORuleCondition.CAPTURE, [SMOItemData.jizo], SMORuleOperation.NONE),
    ],
    SMOLocationData.dashing_above_the_clouds: [],
    SMOLocationData.dashing_through_the_clouds: [],
    SMOLocationData.sphynx_over_bowsers_castle: [
        (SMORuleCondition.CAPTURE, [SMOItemData.binoculars], SMORuleOperation.NONE),
    ],
    SMOLocationData.i_met_a_pokio: [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE),
    ],
    SMOLocationData.bowsers_kingdom_regular_cup: [],
    SMOLocationData.a_rumble_under_the_arena_floor: [],
    SMOLocationData.secret_path_to_bowsers_castle: [],
    SMOLocationData.peach_in_bowsers_kingdom: [],
    SMOLocationData.found_with_bowsers_kingdom_art: [],
    SMOLocationData.behind_the_tall_wall_poke_poke: [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE),
    ],
    SMOLocationData.from_crates_in_the_moat: [],
    SMOLocationData.caught_on_the_giant_horn: [],
    SMOLocationData.inside_a_block_at_the_gate: [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE),
    ],
    SMOLocationData.small_bird_in_bowsers_castle: [],
    SMOLocationData.invader_in_bowsers_castle: [
        (SMORuleCondition.CAPTURE, [SMOItemData.goomba], SMORuleOperation.NONE),
    ],
    SMOLocationData.jumping_from_flag_to_flag: [],
    SMOLocationData.bowsers_kingdom_timer_challenge_2: [],
    SMOLocationData.taking_notes_on_the_wall: [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE),
    ],
    SMOLocationData.taking_notes_with_a_spinning_throw: [],
    SMOLocationData.third_courtyard_outskirts: [
        (SMORuleCondition.CAPTURE, [SMOItemData.spark_pylon], SMORuleOperation.NONE),
    ],
    SMOLocationData.stone_wall_circuit: [
        (SMORuleCondition.CAPTURE, [SMOItemData.spark_pylon], SMORuleOperation.NONE),
    ],
    SMOLocationData.bowsers_kingdom_master_cup: [],
    SMOLocationData.searching_hexagon_tower: [
        (SMORuleCondition.CAPTURE, [SMOItemData.parabones], SMORuleOperation.NONE),
    ],
    SMOLocationData.center_of_hexagon_tower: [
        (SMORuleCondition.CAPTURE, [SMOItemData.parabones], SMORuleOperation.NONE),
    ],
    SMOLocationData.climb_the_wooden_tower: [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE),
    ],
    SMOLocationData.poke_the_wooden_tower: [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE),
    ],
    #endregion

    #region Moon
    SMOLocationData.beat_the_game: [
        (SMORuleCondition.CAPTURE, [SMOItemData.bowser], SMORuleOperation.NONE),
    ],
    SMOLocationData.shining_above_the_moon: [],
    SMOLocationData.along_the_cliff_face: [],
    SMOLocationData.the_tip_of_a_white_spire: [],
    SMOLocationData.rolling_rock_on_the_moon: [],
    SMOLocationData.caught_hopping_on_the_moon: [],
    SMOLocationData.cliffside_treasure_chest: [],
    SMOLocationData.moon_kingdom_timer_challenge_1: [],
    SMOLocationData.taking_notes_on_the_moons_surface: [],
    SMOLocationData.under_the_bowser_statue: [
        (SMORuleCondition.CAPTURE, [SMOItemData.bowser_statue], SMORuleOperation.NONE),
    ],
    SMOLocationData.in_a_hole_in_the_magma: [
        (SMORuleCondition.CAPTURE, [SMOItemData.parabones], SMORuleOperation.NONE),
    ],
    SMOLocationData.around_the_barrier_wall: [
        (SMORuleCondition.CAPTURE, [SMOItemData.banzai_bill], SMORuleOperation.NONE),
    ],
    SMOLocationData.on_top_of_the_cannon: [
        (SMORuleCondition.CAPTURE, [SMOItemData.banzai_bill], SMORuleOperation.NONE),
    ],
    SMOLocationData.fly_to_the_treasure_chest_and_back: [
        (SMORuleCondition.CAPTURE, [SMOItemData.banzai_bill], SMORuleOperation.NONE),
    ],
    SMOLocationData.up_in_the_rafters: [],
    SMOLocationData.sneaking_around_in_the_crater: [],
    SMOLocationData.found_on_the_moon_good_dog: [],
    SMOLocationData.moon_shards_on_the_moon: [],
    SMOLocationData.moon_quiz_amazing: [],
    SMOLocationData.thanks_captain_toad: [],
    SMOLocationData.shopping_in_honeylune_ridge: [],
    SMOLocationData.walking_on_the_moon: [],
    SMOLocationData.moon_kingdom_regular_cup: [],
    SMOLocationData.doctor_in_the_house: [],
    SMOLocationData.sphynxs_hidden_vault: [],
    SMOLocationData.a_tourist_in_the_moon_kingdom: [],
    SMOLocationData.peach_in_the_moon_kingdom: [],
    SMOLocationData.found_with_moon_kindgom_art: [],
    SMOLocationData.mysterious_flying_object: [],
    SMOLocationData.hidden_on_the_side_of_the_cliff: [],
    SMOLocationData.jumping_high_as_a_frog: [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.NONE),
    ],
    SMOLocationData.moon_kingdom_timer_challenge_2: [],
    SMOLocationData.walking_on_the_moon_again: [],
    SMOLocationData.moon_kingdom_master_cup: [],
    SMOLocationData.taking_notes_in_low_gravity: [],
    SMOLocationData.center_of_the_galaxy: [],
    SMOLocationData.edge_of_the_galaxy: [],
    SMOLocationData.navigating_giant_swings: [],
    SMOLocationData.a_swing_on_top_of_a_swing: [],
    #endregion

    #region Dark
    SMOLocationData.arrival_at_rabbit_ridge: [],
    SMOLocationData.captain_toad_on_the_dark_side: [],
    SMOLocationData.breakdown_road_hurry: [],
    SMOLocationData.breakdown_road_final_challenge: [],
    SMOLocationData.invisible_road_rush: [],
    SMOLocationData.invisible_road_secret: [],
    SMOLocationData.vanishing_road_rush: [],
    SMOLocationData.vanishing_road_challenge: [],
    SMOLocationData.yoshi_under_siege: [
        (SMORuleCondition.CAPTURE, [SMOItemData.yoshi], SMORuleOperation.NONE),
    ],
    SMOLocationData.fruit_feast_under_siege: [
        (SMORuleCondition.CAPTURE, [SMOItemData.yoshi], SMORuleOperation.NONE),
    ],
    SMOLocationData.yoshi_on_the_sinking_island: [
        (SMORuleCondition.CAPTURE, [SMOItemData.yoshi], SMORuleOperation.NONE),
    ],
    SMOLocationData.fruit_feast_on_the_sinking_island: [
        (SMORuleCondition.CAPTURE, [SMOItemData.yoshi], SMORuleOperation.NONE),
    ],
    SMOLocationData.yoshis_magma_swamp: [
        (SMORuleCondition.CAPTURE, [SMOItemData.yoshi], SMORuleOperation.NONE),
    ],
    SMOLocationData.fruit_feast_in_the_magma_swamp: [
        (SMORuleCondition.CAPTURE, [SMOItemData.yoshi], SMORuleOperation.NONE),
    ],
    SMOLocationData.found_with_dark_side_art_1: [
        (SMORuleCondition.CAPTURE, [SMOItemData.big_chain_chomp, SMOItemData.t_rex], SMORuleOperation.NONE),
    ],
    SMOLocationData.found_with_dark_side_art_2: [
        (SMORuleCondition.CAPTURE, [SMOItemData.spark_pylon], SMORuleOperation.NONE),
    ],
    SMOLocationData.found_with_dark_side_art_3: [],
    SMOLocationData.found_with_dark_side_art_4: [],
    SMOLocationData.found_with_dark_side_art_5: [],
    SMOLocationData.found_with_dark_side_art_6: [],
    SMOLocationData.found_with_dark_side_art_7: [],
    SMOLocationData.found_with_dark_side_art_8: [],
    SMOLocationData.found_with_dark_side_art_9: [],
    SMOLocationData.found_with_dark_side_art_10: [],
    #endregion

    #region Darker
    SMOLocationData.a_long_journeys_end: [
        (SMORuleCondition.CAPTURE,
         [SMOItemData.frog, SMOItemData.lava_bubble, SMOItemData.uproot, SMOItemData.yoshi, SMOItemData.glydon,
          SMOItemData.volbonan, SMOItemData.pokio, SMOItemData.bowser], SMORuleOperation.NONE),
    ],
    #endregion

}


regional_rule_data : dict[str, list] = {
    #region Cap
    SMOLocationData.cap_kingdom_regional_coin_group_1: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMORuleCondition.CAPTURE], SMORuleOperation.NONE),
    ],
    SMOLocationData.cap_kingdom_regional_coin_group_2: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMORuleCondition.CAPTURE], SMORuleOperation.NONE),
    ],
    SMOLocationData.cap_kingdom_regional_coin_group_3: [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.OR),
        (SMORuleCondition.TRICK_EASY, [SMORuleCondition.CAPTURE], SMORuleOperation.NONE),
    ],
    SMOLocationData.cap_kingdom_regional_coin_group_4: [],
    SMOLocationData.cap_kingdom_regional_coin_group_5: [],
    SMOLocationData.cap_kingdom_regional_coin_group_6: [],
    SMOLocationData.cap_kingdom_regional_coin_group_7: [],
    SMOLocationData.cap_kingdom_regional_coin_group_8: [],
    SMOLocationData.cap_kingdom_regional_coin_group_9: [],
    SMOLocationData.top_hat_tower_regional_coin_group_1: [],
    SMOLocationData.top_hat_tower_regional_coin_group_2: [],
    SMOLocationData.frog_pond_regional_coin_group_1: [],
    SMOLocationData.pushblocks_regional_coin_group_1: [],
    SMOLocationData.poison_tides_regional_coin_group_1: [],
    #endregion

    #region Cascade

    #endregion

    #region Sand
    # 6 and 7 require Jaxi


    #endregion

    #region Wooded

    #endregion

    #region Lake

    #endregion

    #region Lost

    #endregion

    #region Metro

    #endregion

    #region Seaside

    #endregion

    #region Snow

    #endregion

    #region Luncheon

    #endregion

    #region Ruined

    #endregion

    #region Bowser

    #endregion

    #region Moon
    # capture parade 1 near chargin chuck
    # group 2 on top of pillar
    # group 3 under bridge/catwalk
    # group 4 at end of floating platform
    # group 5 near moeeye
    # group 6 next to banzai launcher


    #endregion

}

rule_data : dict[str, list] = {
    **moon_rule_data,
    **regional_rule_data,

}
