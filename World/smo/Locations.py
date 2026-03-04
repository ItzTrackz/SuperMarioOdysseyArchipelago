from BaseClasses import Location
from .Data.LocationData import SMOLocationData
from .Options import Goal

class SMOLocation(Location):
    game: str = "Super Mario Odyssey"

# Cap
loc_Cap = {
        SMOLocationData.frog_jumping_above_the_fog: 1019,
        SMOLocationData.frog_jumping_from_the_top_deck: 815,
        SMOLocationData.cap_kingdom_timer_challenge_1: 861,
        SMOLocationData.good_evening_captain_toad: 227,
        SMOLocationData.shopping_in_bonneton: 230,
}


loc_Cascade = {
        SMOLocationData.our_first_power_moon: 205,
        SMOLocationData.multi_moon_atop_the_falls: 218,
        SMOLocationData.chomp_through_the_rocks: 206,
        SMOLocationData.behind_the_waterfall: 212,
}


loc_Cascade_Peace = {
        SMOLocationData.on_top_of_the_rubble: 1145,
        SMOLocationData.treasure_of_the_waterfall_basin: 216,
        SMOLocationData.above_a_high_cliff: 210,
        SMOLocationData.across_the_floating_isles: 208,
        SMOLocationData.cascade_kingdom_timer_challenge_1: 669,
        SMOLocationData.cascade_kingdom_timer_challenge_2: 670,
        SMOLocationData.good_morning_captain_toad: 204,
}


loc_Cascade_Revisit = {
        SMOLocationData.rolling_rock_by_the_falls: 1004,
        SMOLocationData.shopping_in_fossil_falls: 211,
}


loc_Cascade_Post_Metro = {
        SMOLocationData.a_tourist_in_the_cascade_kingdom: 906,
}


loc_Cascade_Post_Snow = {
        SMOLocationData.secret_path_to_fossil_falls: 207,
}

loc_Sand = {
        SMOLocationData.atop_the_highest_tower: 497,
        SMOLocationData.moon_shards_in_the_sand: 496,
        SMOLocationData.overlooking_the_desert_town: 517,
        SMOLocationData.alcove_in_the_ruins: 518,
        SMOLocationData.on_the_leaning_pillar: 516,
        SMOLocationData.hidden_room_in_the_flowing_sands: 523,
        SMOLocationData.secret_of_the_mural: 505,
        SMOLocationData.on_top_of_stone_archway: 520,
        SMOLocationData.from_a_crate_in_the_ruins: 507,
        SMOLocationData.on_the_lone_pillar: 522,
        SMOLocationData.where_the_birds_gather: 511,
        SMOLocationData.top_of_a_dune: 506,
        SMOLocationData.lost_in_the_luggage: 510,
        SMOLocationData.inside_a_block_is_a_hard_place: 508,
        SMOLocationData.bird_traveling_the_desert: 526,
        SMOLocationData.the_treasure_of_jaxi_ruins: 530,
        SMOLocationData.desert_gardening_plaza_seed: 1112,
        SMOLocationData.desert_gardening_ruins_seed: 1113,
        SMOLocationData.desert_gardening_seed_on_the_cliff: 1114,
        SMOLocationData.taking_notes_jump_on_the_palm: 525,
        SMOLocationData.among_the_five_cactuses: 893,
        SMOLocationData.wandering_cactus: 509,
        SMOLocationData.sand_quiz_wonderful: 498,
        SMOLocationData.shopping_in_tostarena: 565,
}

loc_Sand_Pyramid = {
        SMOLocationData.showdown_on_the_inverted_pyramid: 495,
        SMOLocationData.on_the_statues_tail: 513,
}


loc_Night_Sand = {
        SMOLocationData.bullet_bill_breakthrough: 519,
}


loc_Sand_Underground = {
        SMOLocationData.the_hole_in_the_desert: 560,
        SMOLocationData.underground_treasure_chest: 953,
        SMOLocationData.goomba_tower_assembly: 558,
}


loc_Sand_Peace = {
        SMOLocationData.herding_sheep_in_the_dunes: 532,
        SMOLocationData.walking_the_desert: 533,
        SMOLocationData.hang_your_hat_on_the_fountain: 534,
        SMOLocationData.found_in_the_sand_good_dog: 512,
        SMOLocationData.sand_kingdom_timer_challenge_1: 531,
        SMOLocationData.sand_kingdom_timer_challenge_2: 536,
        SMOLocationData.sand_kingdom_timer_challenge_3: 539,
        SMOLocationData.fishing_in_the_oasis: 502,
        SMOLocationData.love_in_the_heart_of_the_desert: 493,
        SMOLocationData.youre_quite_a_catch_captain_toad: 692,
        SMOLocationData.jaxi_reunion: 1059,
        SMOLocationData.bird_traveling_wastes: 552,
}


loc_Sand_Pyramid_Peace = {
        SMOLocationData.welcome_back_jaxi: 501,
        SMOLocationData.the_lurker_under_the_stone: 538,
}


loc_Sand_Revisit = {
        SMOLocationData.secret_path_to_tostarena: 524,
}


loc_Lake = {
        SMOLocationData.broodals_over_the_lake: 424,
        SMOLocationData.dorrie_back_rider: 411,
        SMOLocationData.cheep_cheep_crossing: 412,
        SMOLocationData.end_of_the_hidden_passage: 410,
        SMOLocationData.whats_in_the_box: 404,
        SMOLocationData.on_the_lakeshore: 401,
        SMOLocationData.from_the_broken_pillar: 405,
        SMOLocationData.treasure_in_the_spiky_waterway: 415,
        SMOLocationData.lake_gardening_spiky_passage_seed: 1166,
        SMOLocationData.lake_kingdom_timer_challenge_1: 715,
        SMOLocationData.lake_kingdom_timer_challenge_2: 420,
        SMOLocationData.moon_shards_in_the_lake: 413,
        SMOLocationData.taking_notes_dive_and_swim: 402,
        SMOLocationData.taking_notes_in_the_cliffside: 407,
        SMOLocationData.lake_fishing: 416,
        SMOLocationData.i_met_a_lake_cheep_cheep: 409,
        SMOLocationData.our_secret_little_room: 414,
        SMOLocationData.lets_go_swimming_captain_toad: 403,
        SMOLocationData.shopping_in_lake_lamode: 430,
        SMOLocationData.i_feel_underdressed: 406,
        SMOLocationData.found_with_lake_kingdom_art: 1094,
}


loc_Lake_Post_Seaside = {
        SMOLocationData.secret_path_to_lake_lamode: 417,
}


loc_Wooded = {
        SMOLocationData.road_to_sky_garden: 129,
        SMOLocationData.rolling_rock_in_the_woods: 149,
        SMOLocationData.caught_hopping_in_the_forest: 148,
        SMOLocationData.atop_a_tall_tree: 139,
        SMOLocationData.tucked_away_inside_a_tunnel: 143,
        SMOLocationData.the_nut_round_the_corner: 145,
        SMOLocationData.climb_the_cliff_to_get_the_nut: 140,
        SMOLocationData.the_nut_in_the_red_maze: 141,
        SMOLocationData.the_nut_at_the_dead_end: 142,
        SMOLocationData.fire_in_the_cave: 136,
        SMOLocationData.shopping_in_steam_gardens: 138,
        SMOLocationData.nut_planted_in_the_tower: 180,
        SMOLocationData.stretching_your_legs: 179,
        SMOLocationData.rolling_rock_in_the_deep_woods: 183,
        SMOLocationData.glowing_in_the_deep_woods: 1137,
        SMOLocationData.past_the_peculiar_pipes: 1159,
        SMOLocationData.by_the_babbling_brook_in_the_deep_woods: 185,
        SMOLocationData.the_hard_rock_in_deep_woods: 186,
        SMOLocationData.a_treasure_made_of_coins: 1153,
        SMOLocationData.beneath_the_roots_of_a_moving_tree: 184,
}


loc_Wooded_Post_Metro = {
        SMOLocationData.secret_path_to_the_steam_gardens: 137,
}


loc_Wooded_Post_Story1 = {
        SMOLocationData.flower_thieves_of_sky_garden: 130,
        SMOLocationData.path_to_the_secret_flower_field: 159,
        SMOLocationData.cracked_nut_on_a_crumbling_tower: 144,
        SMOLocationData.the_nut_that_grew_on_the_tall_fence: 147,
        SMOLocationData.love_in_the_forest_ruins: 131,
        SMOLocationData.thanks_for_the_charge: 135,
        SMOLocationData.over_the_cliffs_edge: 146,
        SMOLocationData.behind_the_rock_wall: 134,
        SMOLocationData.back_way_up_the_mountain: 150,
}


loc_Wooded_Peace = {
        SMOLocationData.inside_the_rock_in_the_forest: 1026,
        SMOLocationData.hey_out_there_captain_toad: 133,
        SMOLocationData.wooded_kingdom_timer_challenge_1: 157,
        SMOLocationData.wooded_kingdom_timer_challenge_2: 676,
        SMOLocationData.found_with_wooded_kingdom_art: 1089,
}


loc_Cloud = {
}


loc_Lost = {
        SMOLocationData.atop_a_propeller_pillar: 376,
        SMOLocationData.below_the_cliffs_edge: 380,
        SMOLocationData.inside_the_stone_cage: 374,
        SMOLocationData.on_a_tree_in_the_swamp: 377,
        SMOLocationData.over_the_fuzzies_above_the_swamp: 384,
        SMOLocationData.avoiding_fuzzies_inside_the_wall: 387,
        SMOLocationData.inside_the_rising_stone_pillar: 375,
        SMOLocationData.enjoying_the_view_of_forgotten_isle: 385,
        SMOLocationData.on_the_mountain_road: 379,
        SMOLocationData.a_propeller_pillars_secret: 373,
        SMOLocationData.wrecked_rock_block: 942,
        SMOLocationData.a_butterflys_treasure: 388,
        SMOLocationData.cave_gardening: 378,
        SMOLocationData.moon_shards_in_the_jungle: 386,
        SMOLocationData.peeking_out_from_under_the_bridge: 382,
        SMOLocationData.twist_n_turn_up_treasure: 1075,
        SMOLocationData.soaring_over_the_forgotten_isle: 381,
        SMOLocationData.the_caged_gold: 383,
        SMOLocationData.get_some_rest_captain_toad: 372,
        SMOLocationData.shopping_on_forgotten_isle: 398,
}


loc_Lost_Revisit = {
        SMOLocationData.caught_hopping_in_the_jungle: 390,
}


loc_Night_Metro = {
        SMOLocationData.new_donk_citys_pest_problem: 37,
        SMOLocationData.swaying_in_the_breeze: 39,
        SMOLocationData.girder_sandwich: 54,
}


loc_Metro = {
        SMOLocationData.drummer_on_board: 42,
        SMOLocationData.guitarist_on_board: 41,
        SMOLocationData.bassist_on_board: 44,
        SMOLocationData.trumpeter_on_board: 43,
        SMOLocationData.inside_an_iron_girder: 38,
        SMOLocationData.glittering_above_the_pool: 65,
        SMOLocationData.dizzying_heights: 61,
        SMOLocationData.secret_girder_tunnel: 59,
        SMOLocationData.who_piled_garbage_on_this: 49,
        SMOLocationData.hidden_in_the_scrap: 62,
        SMOLocationData.left_at_the_cafe: 77,
        SMOLocationData.how_do_they_take_out_the_trash: 68,
        SMOLocationData.city_gardening_building_planter: 70,
        SMOLocationData.city_gardening_plaza_planter: 71,
        SMOLocationData.city_gardening_rooftop_planter: 69,
        SMOLocationData.how_you_doin_captain_toad: 46,
        SMOLocationData.free_parking_rooftop_hop: 809,
        SMOLocationData.bench_friends: 50,
        SMOLocationData.shopping_in_new_donk_city: 101,
        SMOLocationData.jump_rope_hero: 60,
        SMOLocationData.jump_rope_genius: 51,
        SMOLocationData.remotely_captured_car: 53,
        SMOLocationData.found_with_metro_kingdom_art: 1088,
}


loc_Metro_Post_Sand = {
        SMOLocationData.secret_path_to_new_donk_city: 40,
}


loc_Metro_Sewer_Access = {
}


loc_Metro_Peace = {
        SMOLocationData.a_traditional_festival: 95,
        SMOLocationData.celebrating_in_the_streets: 875,
        SMOLocationData.caught_hopping_on_a_building: 99,
        SMOLocationData.metro_kingdom_timer_challenge_1: 1054,
        SMOLocationData.metro_kingdom_timer_challenge_2: 839,
        SMOLocationData.a_tourist_in_the_metro_kingdom: 881,
}


loc_Snow = {
        SMOLocationData.captain_toad_is_chilly: 694,
        SMOLocationData.shopping_in_shiveria: 868,
}


loc_Snow_Peace = {
        SMOLocationData.caught_hopping_in_the_snow: 1002,
        SMOLocationData.snow_kingdom_timer_challenge_1: 678,
        SMOLocationData.snow_kingdom_timer_challenge_2: 686,
        SMOLocationData.moon_shards_in_the_snow: 2,
        SMOLocationData.taking_notes_snow_path_dash: 3,
        SMOLocationData.fishing_in_the_glacier: 4,
}


loc_Seaside = {
        SMOLocationData.the_stone_pillar_seal: 438,
        SMOLocationData.the_lighthouse_seal: 441,
        SMOLocationData.the_hot_spring_seal: 440,
        SMOLocationData.the_seal_above_the_canyon: 439,
        SMOLocationData.on_the_cliff_overlooking_the_beach: 449,
        SMOLocationData.ride_the_jetstream: 455,
        SMOLocationData.ocean_bottom_maze_treasure: 466,
        SMOLocationData.ocean_bottom_maze_hidden_room: 467,
        SMOLocationData.underwater_highway_tunnel: 450,
        SMOLocationData.shh_its_a_shortcut: 451,
        SMOLocationData.gap_in_the_ocean_trench: 458,
        SMOLocationData.slip_through_the_nesting_spot: 459,
        SMOLocationData.merci_dorrie: 453,
        SMOLocationData.under_a_dangerous_ceiling: 445,
        SMOLocationData.what_the_waves_left_behind: 447,
        SMOLocationData.the_back_canyon_excavate: 444,
        SMOLocationData.bubblaine_northern_reaches: 1151,
        SMOLocationData.glass_palace_treasure_chest: 1057,
        SMOLocationData.treasure_trap_hidden_in_the_inlet: 448,
        SMOLocationData.sea_gardening_inlet_seed: 1103,
        SMOLocationData.sea_gardening_canyon_seed: 1104,
        SMOLocationData.sea_gardening_hot_spring_seed: 1106,
        SMOLocationData.sea_gardening_ocean_trench_seed: 1105,
        SMOLocationData.seaside_kingdom_timer_challenge_1: 468,
        SMOLocationData.moon_shards_in_the_sea: 454,
        SMOLocationData.taking_notes_ocean_surface_dash: 442,
        SMOLocationData.love_by_the_seaside: 446,
        SMOLocationData.good_job_captain_toad: 443,
        SMOLocationData.ocean_quiz_good: 457,
        SMOLocationData.shopping_in_bubblaine: 460,
        SMOLocationData.found_with_seaside_kingdom_art: 1095,
}


loc_Seaside_Peace = {
        SMOLocationData.the_glass_is_half_full: 437,
        SMOLocationData.bonjour_dorrie: 452,
        SMOLocationData.seaside_kingdom_timer_challenge_2: 863,
        SMOLocationData.found_on_the_beach_good_dog: 471,
        SMOLocationData.lighthouse_leaper: 474,
        SMOLocationData.beach_volleyball_champ: 472,
        SMOLocationData.beach_volleyball_hero_of_the_beach: 473,
}


loc_Luncheon = {
        SMOLocationData.the_broodals_are_after_some_cookin: 291,
        SMOLocationData.piled_on_the_salt: 256,
        SMOLocationData.lurking_in_the_pillars_shadow: 250,
        SMOLocationData.overlooking_a_bunch_of_ingredients: 246,
        SMOLocationData.luncheon_kingdom_timer_challenge_1: 264,
        SMOLocationData.love_above_the_lava: 803,
}


loc_Luncheon_Post_Wooded = {
        SMOLocationData.secret_path_to_mount_volbono: 260,
}


loc_Luncheon_Post_Spewart = {
        SMOLocationData.under_the_cheese_rocks: 251,
        SMOLocationData.atop_the_jutting_crag: 253,
        SMOLocationData.is_this_an_ingredient_too: 240,
        SMOLocationData.atop_a_column_in_a_row: 247,
        SMOLocationData.island_of_salt_floating_in_the_lava: 245,
        SMOLocationData.golden_turnip_recipe_1: 242,
        SMOLocationData.golden_turnip_recipe_2: 241,
        SMOLocationData.shopping_in_mount_volbono: 294,
}


loc_Luncheon_Post_Cheese_Rocks = {
        SMOLocationData.big_pot_on_the_volcano_dive_in: 292,
        SMOLocationData.surrounded_by_tall_mountains: 248,
        SMOLocationData.light_the_lantern_on_the_small_island: 254,
        SMOLocationData.golden_turnip_recipe_3: 243,
        SMOLocationData.beneath_the_rolling_vegetables: 263,
        SMOLocationData.all_the_cracks_are_fixed: 970,
        SMOLocationData.taking_notes_swimming_in_magma: 244,
        SMOLocationData.luncheon_kingdom_timer_challenge_2: 249,
        SMOLocationData.treasure_beneath_the_cheese_rocks: 952,
        SMOLocationData.light_the_two_flames: 255,
        SMOLocationData.found_with_luncheon_kingdom_art: 1090,
}


loc_Luncheon_Peace = {
        SMOLocationData.cookatiel_showdown: 290,
        SMOLocationData.luncheon_kingdom_timer_challenge_3: 711,
        SMOLocationData.caught_hopping_at_the_volcano: 289,
        SMOLocationData.light_the_far_off_lanterns: 261,
        SMOLocationData.bon_appetit_captain_toad: 265,
        SMOLocationData.taking_notes_big_pot_swim: 833,
        SMOLocationData.a_tourist_in_the_luncheon_kingdom: 908,
}


loc_Ruined = {
        SMOLocationData.battle_with_the_lord_of_lightning: 795,
        SMOLocationData.in_the_ancient_treasure_chest: 793,
}


loc_Bowser = {
        SMOLocationData.caught_on_the_iron_fence: 345,
        SMOLocationData.stack_up_above_the_wall: 324,
}


loc_Bowser_Infiltrate = {
        SMOLocationData.behind_the_big_wall: 321,
        SMOLocationData.taking_notes_between_spinies: 315,
        SMOLocationData.infiltrate_bowsers_castle: 325,
        SMOLocationData.smart_bombing: 334,
        SMOLocationData.treasure_inside_the_turret: 333,
        SMOLocationData.poking_your_nose_in_the_plaster_wall: 323,
        SMOLocationData.poking_the_turret_wall: 337,
}


loc_Bowser_Post_Bombing = {
        SMOLocationData.big_broodal_battle: 314,
        SMOLocationData.from_the_side_above_the_castle_gate: 335,
        SMOLocationData.exterminate_the_ogres: 320,
        SMOLocationData.jizo_all_in_a_row: 316,
        SMOLocationData.underground_jizo: 317,
        SMOLocationData.shopping_at_bowsers_castle: 360,
}


loc_Bowser_Mecha_Broodal = {
        SMOLocationData.showdown_at_bowsers_castle: 332,
}


loc_Bowser_Peace = {
        SMOLocationData.sunken_treasure_in_the_moat: 327,
        SMOLocationData.on_the_giant_bowser_statues_nose: 339,
        SMOLocationData.inside_a_block_in_the_castle: 319,
        SMOLocationData.hidden_corridor_under_the_floor: 1092,
        SMOLocationData.poking_your_nose_by_the_great_gate: 328,
        SMOLocationData.found_behind_bars: 331,
        SMOLocationData.good_to_see_you_captain_toad: 318,
        SMOLocationData.past_the_moving_wall: 340,
        SMOLocationData.above_the_poison_swamp: 326,
        SMOLocationData.knocking_down_the_nice_frame: 1133,
        SMOLocationData.caught_hopping_at_bowsers_castle: 343,
        SMOLocationData.bowsers_kingdom_timer_challenge_1: 691,
        SMOLocationData.fishing_in_bowsers_castle: 690,
}


loc_Moon = {
        SMOLocationData.shining_above_the_moon: 579,
        SMOLocationData.along_the_cliff_face: 586,
        SMOLocationData.the_tip_of_a_white_spire: 577,
        SMOLocationData.rolling_rock_on_the_moon: 583,
        SMOLocationData.caught_hopping_on_the_moon: 585,
        SMOLocationData.cliffside_treasure_chest: 582,
        SMOLocationData.moon_kingdom_timer_challenge_1: 584,
        SMOLocationData.taking_notes_on_the_moons_surface: 576,
}


loc_Mushroom_Post_Luncheon = {
        SMOLocationData.secret_path_to_peachs_castle: 608,
}


loc_Cap_Postgame = {
        SMOLocationData.the_forgotten_treasure: 228,
        SMOLocationData.taxi_flying_through_bonneton: 1073,
        SMOLocationData.bonnetter_blockade: 1038,
        SMOLocationData.cap_kingdom_regular_cup: 1033,
        SMOLocationData.peach_in_the_cap_kingdom: 229,
        SMOLocationData.found_with_cap_kingdom_art: 1086,
        SMOLocationData.next_to_glasses_bridge: 233,
        SMOLocationData.danger_sign: 816,
        SMOLocationData.under_the_big_ones_brim: 817,
        SMOLocationData.fly_to_the_edge_of_the_fog: 1158,
        SMOLocationData.spin_the_hat_get_a_prize: 1025,
        SMOLocationData.hidden_in_a_sunken_hat: 231,
        SMOLocationData.fog_shrouded_platform: 813,
        SMOLocationData.bird_traveling_in_the_fog: 1156,
        SMOLocationData.caught_hopping_near_the_ship: 232,
        SMOLocationData.taking_notes_in_the_fog: 1018,
        SMOLocationData.cap_kingdom_timer_challenge_2: 981,
        SMOLocationData.cap_kingdom_master_cup: 1034,
}


loc_Cascade_Postgame = {
        SMOLocationData.peach_in_the_cascade_kingdom: 209,
        SMOLocationData.cascade_kingdom_regular_cup: 708,
        SMOLocationData.cascade_kingdom_master_cup: 894,
        SMOLocationData.caveman_cave_fan: 866,
        SMOLocationData.sphynx_traveling_to_the_waterfall: 1041,
        SMOLocationData.bottom_of_the_waterfall_basin: 213,
        SMOLocationData.just_a_hat_skip_and_a_jump: 826,
        SMOLocationData.treasure_under_the_cliff: 214,
        SMOLocationData.next_to_the_stone_arch: 215,
        SMOLocationData.guarded_by_a_colossal_fossil: 825,
        SMOLocationData.under_the_old_electrical_pole: 823,
        SMOLocationData.under_the_ground: 822,
        SMOLocationData.inside_the_busted_fossil: 1167,
        SMOLocationData.caught_hopping_at_the_waterfall: 217,
        SMOLocationData.taking_notes_hurry_upward: 770,
}


loc_Sand_Postgame = {
        SMOLocationData.found_with_sand_kingdom_art: 1096,
        SMOLocationData.jammin_in_the_sand_kingdom: 910,
        SMOLocationData.hat_and_seek_in_the_sand: 924,
        SMOLocationData.sand_kingdom_regular_cup: 1045,
        SMOLocationData.round_the_world_tourist: 535,
        SMOLocationData.peach_in_the_sand_kingdom: 544,
        SMOLocationData.mighty_leap_from_the_palm_tree: 547,
        SMOLocationData.on_the_north_pillar: 546,
        SMOLocationData.into_the_flowing_sands: 799,
        SMOLocationData.in_the_skies_above_the_canyon: 550,
        SMOLocationData.island_in_the_poison_swamp: 521,
        SMOLocationData.an_invisible_gleam: 542,
        SMOLocationData.on_the_eastern_pillar: 540,
        SMOLocationData.caught_hopping_in_the_desert: 553,
        SMOLocationData.poster_cleanup: 545,
        SMOLocationData.taking_notes_running_down: 515,
        SMOLocationData.taking_notes_in_the_wall_painting: 783,
        SMOLocationData.love_at_the_edge_of_the_desert: 965,
        SMOLocationData.more_walking_in_the_desert: 712,
        SMOLocationData.sand_kingdom_master_cup: 1046,
}


loc_Lake_Postgame = {
        SMOLocationData.taxi_flying_through_lake_lamode: 1078,
        SMOLocationData.that_trendy_pirate_look: 870,
        SMOLocationData.space_is_in_right_now: 869,
        SMOLocationData.that_old_west_style: 871,
        SMOLocationData.lake_kingdom_regular_cup: 709,
        SMOLocationData.peach_in_the_lake_kingdom: 408,
        SMOLocationData.behind_the_floodgate: 422,
        SMOLocationData.high_flying_leap: 771,
        SMOLocationData.deep_deep_down: 719,
        SMOLocationData.rooftop_of_the_water_plaza: 1015,
        SMOLocationData.bird_traveling_over_the_lake: 423,
        SMOLocationData.love_by_the_lake: 1017,
        SMOLocationData.lake_kingdom_master_cup: 720,
}


loc_Wooded_Postgame = {
        SMOLocationData.swing_around_secret_flower_field: 1011,
        SMOLocationData.jammin_in_the_wooded_kingdom: 905,
        SMOLocationData.wooded_kingdom_regular_cup: 153,
        SMOLocationData.peach_in_the_wooded_kingdom: 155,
        SMOLocationData.high_up_in_the_cave: 168,
        SMOLocationData.lost_in_the_tall_trees: 892,
        SMOLocationData.looking_down_on_the_goombas: 160,
        SMOLocationData.high_up_on_a_rock_wall: 177,
        SMOLocationData.the_nut_in_the_robot_storeroom: 169,
        SMOLocationData.above_the_iron_mountain_path: 161,
        SMOLocationData.the_nut_under_the_observation_deck: 174,
        SMOLocationData.bird_traveling_the_forest: 166,
        SMOLocationData.invader_in_the_sky_garden: 156,
        SMOLocationData.hot_hot_hot_from_the_campfire: 163,
        SMOLocationData.wooded_kingdom_timer_challenge_3: 1010,
        SMOLocationData.moon_shards_in_the_forest: 152,
        SMOLocationData.taking_notes_on_top_of_the_wall: 170,
        SMOLocationData.taking_notes_stretching: 151,
        SMOLocationData.wooded_kingdom_master_cup: 901,
        SMOLocationData.i_met_an_uproot: 1001,
}


loc_Cloud_Postgame = {
        SMOLocationData.peach_in_the_cloud_kingdom: 1118,
        SMOLocationData.digging_in_the_cloud: 851,
        SMOLocationData.high_high_above_the_clouds: 852,
        SMOLocationData.crossing_the_cloud_sea: 853,
        SMOLocationData.taking_notes_up_and_down: 1160,
}


loc_Lost_Postgame = {
        SMOLocationData.taxi_flying_through_forgotten_isle: 1077,
        SMOLocationData.i_met_a_tropical_wiggler: 943,
        SMOLocationData.lost_kingdom_regular_cup: 832,
        SMOLocationData.peach_in_the_lost_kingdom: 394,
        SMOLocationData.the_shining_fruit: 395,
        SMOLocationData.jump_down_to_the_top_of_a_tree: 396,
        SMOLocationData.line_it_up_blow_it_up: 392,
        SMOLocationData.taking_notes_stretch_and_shrink: 393,
        SMOLocationData.lost_kingdom_master_cup: 897,
        SMOLocationData.lost_kingdom_timer_challenge: 855,
}


loc_Metro_Postgame = {
        SMOLocationData.bird_traveling_in_the_city: 1150,
        SMOLocationData.mario_signs_his_name: 97,
        SMOLocationData.surprise_clown: 874,
        SMOLocationData.a_request_from_the_mayor: 96,
        SMOLocationData.jammin_in_the_metro_kingdom: 904,
        SMOLocationData.sphynx_in_the_city: 1037,
        SMOLocationData.free_parking_leap_of_faith: 979,
        SMOLocationData.metro_kingdom_regular_cup: 939,
        SMOLocationData.hat_and_seek_in_the_city: 81,
        SMOLocationData.peach_in_the_metro_kingdom: 75,
        SMOLocationData.hanging_between_buildings: 84,
        SMOLocationData.crossing_lines: 78,
        SMOLocationData.out_of_a_crate_in_the_city: 74,
        SMOLocationData.bird_traveling_in_the_park: 1155,
        SMOLocationData.metro_kingdom_timer_challenge_3: 938,
        SMOLocationData.found_in_the_park_good_dog: 82,
        SMOLocationData.metro_kingdom_master_cup: 940,
}


loc_Snow_Postgame = {
        SMOLocationData.secret_path_to_shiveria: 937,
        SMOLocationData.snow_kingdom_regular_cup: 695,
        SMOLocationData.hat_and_seek_in_the_snow: 903,
        SMOLocationData.peach_in_the_snow_kingdom: 19,
        SMOLocationData.shining_on_high: 8,
        SMOLocationData.above_the_freezing_fish_pond: 6,
        SMOLocationData.ice_floe_swimming: 7,
        SMOLocationData.forgotten_in_the_holding_room: 843,
        SMOLocationData.it_popped_out_of_the_ice: 10,
        SMOLocationData.deep_in_the_cold_cold_water: 9,
        SMOLocationData.snow_kingdom_timer_challenge_3: 1003,
        SMOLocationData.i_met_a_snow_cheep_cheep: 973,
        SMOLocationData.snow_kingdom_master_cup: 900,
}


loc_Seaside_Postgame = {
        SMOLocationData.secret_path_to_bubblaine: 464,
        SMOLocationData.seaside_kingdom_regular_cup: 1028,
        SMOLocationData.peach_in_the_seaside_kingdom: 477,
        SMOLocationData.above_the_parasol_catch: 780,
        SMOLocationData.what_shines_inside_the_glass: 779,
        SMOLocationData.a_fine_detail_on_the_glass: 920,
        SMOLocationData.underwater_highway_west_explore: 476,
        SMOLocationData.underwater_highway_east_explore: 773,
        SMOLocationData.rapid_ascent_on_hot_spring_island: 1043,
        SMOLocationData.a_light_next_to_the_lighthouse: 776,
        SMOLocationData.the_tall_rock_shell_in_the_deep_ocean: 778,
        SMOLocationData.at_the_base_of_the_lighthouse: 775,
        SMOLocationData.bird_traveling_over_the_ocean: 1120,
        SMOLocationData.caught_hopping_at_glass_palace: 475,
        SMOLocationData.seaside_kingdom_timer_challenge_3: 864,
        SMOLocationData.taking_notes_ocean_bottom_maze: 790,
        SMOLocationData.taking_notes_in_the_sea: 1163,
        SMOLocationData.seaside_kingdom_master_cup: 1029,
}


loc_Luncheon_Postgame = {
        SMOLocationData.the_rooftop_lantern: 269,
        SMOLocationData.jammin_in_the_luncheon_kingdom: 907,
        SMOLocationData.mechanic_repairs_complete: 886,
        SMOLocationData.diving_from_the_big_pot: 1005,
        SMOLocationData.hat_and_seek_among_the_food: 280,
        SMOLocationData.luncheon_kingdom_regular_cup: 266,
        SMOLocationData.peach_in_the_luncheon_kingdom: 268,
        SMOLocationData.from_inside_a_bright_stone: 271,
        SMOLocationData.under_the_meat_plateau: 829,
        SMOLocationData.on_top_of_a_tall_tall_roof: 287,
        SMOLocationData.from_a_crack_in_the_hard_ground: 276,
        SMOLocationData.by_the_cannon_pointed_at_the_big_pot: 277,
        SMOLocationData.luncheon_kingdom_master_cup: 895,
}


loc_Ruined_Postgame = {
        SMOLocationData.peach_in_the_ruined_kingdom: 1117,
        SMOLocationData.caught_in_a_big_horn: 834,
        SMOLocationData.upon_the_broken_arch: 835,
        SMOLocationData.rolling_rock_on_the_battlefield: 909,
}


loc_Bowser_Postgame = {
        SMOLocationData.sphynx_over_bowsers_castle: 1039,
        SMOLocationData.i_met_a_pokio: 941,
        SMOLocationData.bowsers_kingdom_regular_cup: 859,
        SMOLocationData.a_rumble_under_the_arena_floor: 1161,
        SMOLocationData.secret_path_to_bowsers_castle: 322,
        SMOLocationData.peach_in_bowsers_kingdom: 338,
        SMOLocationData.found_with_bowsers_kingdom_art: 1091,
        SMOLocationData.behind_the_tall_wall_poke_poke: 350,
        SMOLocationData.from_crates_in_the_moat: 1032,
        SMOLocationData.caught_on_the_giant_horn: 1016,
        SMOLocationData.inside_a_block_at_the_gate: 356,
        SMOLocationData.small_bird_in_bowsers_castle: 1014,
        SMOLocationData.invader_in_bowsers_castle: 349,
        SMOLocationData.jumping_from_flag_to_flag: 355,
        SMOLocationData.bowsers_kingdom_timer_challenge_2: 963,
        SMOLocationData.taking_notes_on_the_wall: 351,
        SMOLocationData.taking_notes_with_a_spinning_throw: 1102,
        SMOLocationData.third_courtyard_outskirts: 348,
        SMOLocationData.stone_wall_circuit: 1143,
        SMOLocationData.bowsers_kingdom_master_cup: 896,
}


loc_Moon_Postgame = {
        SMOLocationData.sneaking_around_in_the_crater: 693,
        SMOLocationData.found_on_the_moon_good_dog: 672,
        SMOLocationData.moon_shards_on_the_moon: 671,
        SMOLocationData.moon_quiz_amazing: 580,
        SMOLocationData.thanks_captain_toad: 1000,
        SMOLocationData.shopping_in_honeylune_ridge: 1157,
        SMOLocationData.walking_on_the_moon: 578,
        SMOLocationData.moon_kingdom_regular_cup: 707,
        SMOLocationData.doctor_in_the_house: 1164,
        SMOLocationData.a_tourist_in_the_moon_kingdom: 911,
        SMOLocationData.peach_in_the_moon_kingdom: 581,
        SMOLocationData.found_with_moon_kindgom_art: 1165,
        SMOLocationData.mysterious_flying_object: 1049,
        SMOLocationData.hidden_on_the_side_of_the_cliff: 810,
        SMOLocationData.jumping_high_as_a_frog: 811,
        SMOLocationData.moon_kingdom_timer_challenge_2: 798,
        SMOLocationData.walking_on_the_moon_again: 714,
        SMOLocationData.moon_kingdom_master_cup: 899,
        SMOLocationData.taking_notes_in_low_gravity: 828,
}


loc_Mushroom = {
        SMOLocationData.a_tourist_in_the_mushroom_kingdom: 912,
        SMOLocationData.perched_on_the_castle_roof: 1134,
        SMOLocationData.pops_out_of_the_tail: 1027,
        SMOLocationData.caught_hopping_at_peachs_castle: 613,
        SMOLocationData.gardening_for_toad_garden_seed: 1108,
        SMOLocationData.gardening_for_toad_field_seed: 1109,
        SMOLocationData.gardening_for_toad_pasture_seed: 1111,
        SMOLocationData.gardening_for_toad_lake_seed: 1110,
        SMOLocationData.grow_a_flower_garden: 959,
        SMOLocationData.mushroom_kingdom_timer_challenge: 977,
        SMOLocationData.found_at_peachs_castle_good_dog: 840,
        SMOLocationData.taking_notes_around_the_well: 1121,
        SMOLocationData.herding_sheep_at_peachs_castle: 607,
        SMOLocationData.gobbling_fruit_with_yoshi: 856,
        SMOLocationData.yoshis_second_helping: 857,
        SMOLocationData.yoshis_all_filled_up: 858,
        SMOLocationData.love_at_peachs_castle: 606,
        SMOLocationData.toad_defender: 984,
        SMOLocationData.forever_onward_captain_toad: 605,
        SMOLocationData.jammin_in_the_mushroom_kingdom: 913,
        SMOLocationData.shopping_near_peachs_castle: 933,
        SMOLocationData.mushroom_kingdom_regular_cup: 967,
        SMOLocationData.mushroom_kingdom_master_cup: 968,
        SMOLocationData.found_with_mushroom_kingdom_art: 1152,
        SMOLocationData.hat_and_seek_mushroom_kingdom: 978,
        SMOLocationData.princess_peach_home_again: 1119,
}


loc_Dark = {
        SMOLocationData.arrival_at_rabbit_ridge: 1055,
        SMOLocationData.captain_toad_on_the_dark_side: 1122,
        SMOLocationData.found_with_dark_side_art_1: 1132,
        SMOLocationData.found_with_dark_side_art_2: 1130,
        SMOLocationData.found_with_dark_side_art_3: 1131,
        SMOLocationData.found_with_dark_side_art_4: 1124,
        SMOLocationData.found_with_dark_side_art_5: 1129,
        SMOLocationData.found_with_dark_side_art_6: 1127,
        SMOLocationData.found_with_dark_side_art_7: 1126,
        SMOLocationData.found_with_dark_side_art_8: 1123,
        SMOLocationData.found_with_dark_side_art_9: 1128,
        SMOLocationData.found_with_dark_side_art_10: 1125,
}


loc_Darker = {
        SMOLocationData.a_long_journeys_end: 1061,
}


loc_Cap_Shop = {
        SMOLocationData.cap_kingdom_sticker: 2582,
        SMOLocationData.plush_frog: 2599,
        SMOLocationData.bonneton_tower_model: 2600,
        SMOLocationData.black_top_hat: 2501,
        SMOLocationData.black_tuxedo: 2539,
}


loc_Cascade_Shop = {
        SMOLocationData.caveman_headwear: 2502,
        SMOLocationData.caveman_outfit: 2540,
        SMOLocationData.cascade_kingdom_sticker: 2583,
        SMOLocationData.t_rex_model: 2601,
        SMOLocationData.triceratops_trophy: 2602,
}


loc_Sand_Shop = {
        SMOLocationData.sombrero: 2503,
        SMOLocationData.poncho: 2541,
        SMOLocationData.cowboy_hat: 2504,
        SMOLocationData.cowboy_outfit: 2542,
        SMOLocationData.sand_kingdom_sticker: 2584,
        SMOLocationData.jaxi_statue: 2604,
        SMOLocationData.inverted_pyramid_model: 2603,
}


loc_Wooded_Shop = {
        SMOLocationData.explorer_hat: 2506,
        SMOLocationData.explorer_outfit: 2544,
        SMOLocationData.scientist_visor: 2507,
        SMOLocationData.scientist_outfit: 2545,
        SMOLocationData.wooded_kingdom_sticker: 2586,
        SMOLocationData.flowers_from_steam_gardens: 2607,
        SMOLocationData.steam_gardener_watering_can: 2608,
}


loc_Lake_Shop = {
        SMOLocationData.swim_goggles: 2505,
        SMOLocationData.swimwear: 2543,
        SMOLocationData.lake_kingdom_sticker: 2585,
        SMOLocationData.rubber_dorrie: 2606,
        SMOLocationData.underwater_dome: 2605,
}


loc_Lost_Shop = {
        SMOLocationData.aviator_cap: 2508,
        SMOLocationData.aviator_outfit: 2546,
        SMOLocationData.lost_kingdom_sticker: 2587,
        SMOLocationData.potted_palm_tree: 2609,
        SMOLocationData.butterfly_mobile: 2610,
}


loc_Metro_Shop = {
        SMOLocationData.builder_helmet: 2509,
        SMOLocationData.builder_outfit: 2547,
        SMOLocationData.golf_cap: 2510,
        SMOLocationData.golf_outfit: 2548,
        SMOLocationData.metro_kingdom_sticker: 2588,
        SMOLocationData.new_donk_city_hall_model: 2612,
        SMOLocationData.pauline_statue: 2611,
}


loc_Seaside_Shop = {
        SMOLocationData.resort_hat: 2512,
        SMOLocationData.resort_outfit: 2550,
        SMOLocationData.sailor_hat: 2513,
        SMOLocationData.sailor_suit: 2551,
        SMOLocationData.seaside_kingdom_sticker: 2590,
        SMOLocationData.glass_tower_model: 2616,
        SMOLocationData.sand_jar: 2615,
}


loc_Snow_Shop = {
        SMOLocationData.snow_hood: 2511,
        SMOLocationData.snow_suit: 2549,
        SMOLocationData.snow_kingdom_sticker: 2589,
        SMOLocationData.shiverian_rug: 2613,
        SMOLocationData.shiverian_nesting_dolls: 2614,
}


loc_Luncheon_Shop = {
        SMOLocationData.chef_hat: 2514,
        SMOLocationData.chef_suit: 2552,
        SMOLocationData.painters_cap: 2515,
        SMOLocationData.painter_outfit: 2553,
        SMOLocationData.luncheon_kingdom_sticker: 2591,
        SMOLocationData.souvenir_forks: 2617,
        SMOLocationData.vegetable_plate: 2618,
}


loc_Bowser_Shop = {
        SMOLocationData.samurai_helmet: 2516,
        SMOLocationData.samurai_armor: 2554,
        SMOLocationData.happi_headband: 2517,
        SMOLocationData.happi_outfit: 2555,
        SMOLocationData.bowsers_kingdom_sticker: 2592,
        SMOLocationData.paper_lantern: 2619,
        SMOLocationData.jizo_statue: 2620,
}


loc_Moon_Outfit = {
        SMOLocationData.marios_top_hat: 2538,
        SMOLocationData.marios_tuxedo: 2576,
}


loc_Moon_Shop = {
        SMOLocationData.space_helmet: 2518,
        SMOLocationData.space_suit: 2556,
        SMOLocationData.moon_kingdom_sticker: 2593,
        SMOLocationData.moon_rock_fragment: 2621,
        SMOLocationData.moon_lamp: 2622,
}


loc_Mushroom_Shop = {
        SMOLocationData.mario_64_cap: 2519,
        SMOLocationData.mario_64_suit: 2557,
        SMOLocationData.mushroom_cushion_set: 2623,
        SMOLocationData.peachs_castle_model: 2624,
        SMOLocationData.pipe_sticker: 2594,
        SMOLocationData.coin_sticker: 2595,
        SMOLocationData.block_sticker: 2596,
        SMOLocationData.question_block_sticker: 2597,
        SMOLocationData.mushroom_kingdom_sticker: 2598,
}


loc_Postgame_Shop = {
        SMOLocationData.luigi_cap: 2528,
        SMOLocationData.luigi_suit: 2566,
        SMOLocationData.doctor_headwear: 2532,
        SMOLocationData.doctor_outfit: 2570,
        SMOLocationData.waluigi_cap: 2530,
        SMOLocationData.waluigi_suit: 2568,
        SMOLocationData.diddy_kong_hat: 2533,
        SMOLocationData.diddy_kong_suit: 2571,
        SMOLocationData.wario_cap: 2529,
        SMOLocationData.wario_suit: 2567,
        SMOLocationData.hakama: 2579,
        SMOLocationData.bowsers_top_hat: 2534,
        SMOLocationData.bowsers_tuxedo: 2572,
        SMOLocationData.bridal_veil: 2535,
        SMOLocationData.bridal_gown: 2573,
        SMOLocationData.gold_mario_cap: 2531,
        SMOLocationData.gold_mario_suit: 2569,
        SMOLocationData.metal_mario_cap: 2536,
        SMOLocationData.metal_mario_suit: 2574,
}


loc_Dark_Outfit = {
        SMOLocationData.kings_crown: 2537,
        SMOLocationData.kings_outfit: 2575,
}


loc_Darker_Outfit = {
        SMOLocationData.invisibility_hat: 2581,
}


loc_odyssey_outfit = {
        SMOLocationData.captains_hat: 2577,
}


shop_sand_coin = {
        SMOLocationData.employee_cap: 2520,
        SMOLocationData.employee_uniform: 2558,
        SMOLocationData.boxer_shorts: 2578,
}


shop_lake_coin = {
        SMOLocationData.fashionable_cap: 2521,
        SMOLocationData.fashionable_outfit: 2559,
}


shop_wooded_coin = {
        SMOLocationData.mechanic_cap: 2522,
        SMOLocationData.mechanic_outfit: 2560,
}


shop_metro_coin = {
        SMOLocationData.black_fedora: 2523,
        SMOLocationData.black_suit: 2561,
}


shop_seaside_coin = {
        SMOLocationData.pirate_hat: 2524,
        SMOLocationData.pirate_outfit: 2562,
}


shop_luncheon_coin = {
        SMOLocationData.clown_hat: 2525,
        SMOLocationData.clown_suit: 2563,
}


shop_moon_coin = {
        SMOLocationData.football_helmet: 2526,
        SMOLocationData.football_uniform: 2564,
}


shop_post_game_coin = {
        SMOLocationData.classic_cap: 2527,
        SMOLocationData.classic_suit: 2565,
        SMOLocationData.skeleton_suit: 2580,
}


loc_Post_Cloud = {
        SMOLocationData.beat_bowser_in_cloud: 2500,
}

loc_Moon_Post_Moon = {
        SMOLocationData.beat_the_game: 2499,
}

loc_Captures = {
        SMOLocationData.frog: 4025,
        SMOLocationData.spark_pylon: 4026,
        SMOLocationData.paragoomba: 4027,
        SMOLocationData.chain_chomp: 4028,
        SMOLocationData.big_chain_chomp: 4029,
        SMOLocationData.broodes_chain_chomp: 4030,
        SMOLocationData.t_rex: 4031,
        SMOLocationData.binoculars: 4032,
        SMOLocationData.bullet_bill: 4033,
        SMOLocationData.moe_eye: 4034,
        SMOLocationData.cactus: 4035,
        SMOLocationData.goomba: 4036,
        SMOLocationData.knucklotecs_fist: 4037,
        SMOLocationData.mini_rocket: 4038,
        SMOLocationData.glydon: 4039,
        SMOLocationData.lakitu: 4040,
        SMOLocationData.zipper: 4041,
        SMOLocationData.cheep_cheep: 4042,
        SMOLocationData.puzzle_part_lake_kingdom: 4043,
        SMOLocationData.poison_piranha_plant: 4044,
        SMOLocationData.uproot: 4045,
        SMOLocationData.fire_bro: 4046,
        SMOLocationData.sherm: 4047,
        SMOLocationData.coin_coffer: 4048,
        SMOLocationData.tree: 4049,
        SMOLocationData.boulder: 4050,
        SMOLocationData.picture_match_part_goomba: 4051,
        SMOLocationData.tropical_wiggler: 4052,
        SMOLocationData.pole: 4053,
        SMOLocationData.manhole: 4054,
        SMOLocationData.taxi: 4055,
        SMOLocationData.rc_car: 4056,
        SMOLocationData.ty_foo: 4057,
        SMOLocationData.shiverian_racer: 4058,
        SMOLocationData.cheep_cheep_snow_kingdom: 4059,
        SMOLocationData.gushen: 4060,
        SMOLocationData.lava_bubble: 4061,
        SMOLocationData.volbonan: 4062,
        SMOLocationData.hammer_bro: 4063,
        SMOLocationData.meat: 4064,
        SMOLocationData.fire_piranha_plant: 4065,
        SMOLocationData.pokio: 4066,
        SMOLocationData.jizo: 4067,
        SMOLocationData.bowser_statue: 4068,
        SMOLocationData.parabones: 4069,
        SMOLocationData.banzai_bill: 4070,
        SMOLocationData.chargin_chuck: 4071,
        SMOLocationData.bowser: 4072,
        SMOLocationData.letter: 4073,
        SMOLocationData.puzzle_part_metro_kingdom: 4074,
        SMOLocationData.picture_match_part_mario: 4075,
        SMOLocationData.yoshi: 4076,
}

sub_area_frog = {
        SMOLocationData.searching_the_frog_pond: 238,
        SMOLocationData.secrets_of_the_frog_pond: 239,
}

sub_area_poison_tide = {
        SMOLocationData.skimming_the_poison_tide: 236,
        SMOLocationData.slipping_through_the_poison_tide: 237,
}

sub_area_push_block = {
        SMOLocationData.push_block_peril: 234,
        SMOLocationData.hidden_among_the_push_blocks: 235,
}

sub_area_rolling = {
        SMOLocationData.roll_on_and_on: 950,
        SMOLocationData.precision_rolling: 951,
}

sub_area_chain_chomp = {
        SMOLocationData.nice_shot_with_the_chain_chomp: 225,
        SMOLocationData.very_nice_shot_with_the_chain_chomp: 226,
}

sub_area_trex_nest = {
        SMOLocationData.dinosaur_nest_big_cleanup: 1116,
        SMOLocationData.dinosaur_nest_running_wild: 1115,
}

sub_area_cascade_2d = {
        SMOLocationData.past_the_chasm_lifts: 221,
        SMOLocationData.hidden_chasm_passage: 222,
}

sub_area_gusty_bridges = {
        SMOLocationData.across_the_gusty_bridges: 673,
        SMOLocationData.flying_far_away_from_gusty_bridges: 674,
}

sub_area_invisible_maze = {
        SMOLocationData.the_invisible_maze: 562,
        SMOLocationData.skull_sign_in_the_transparent_maze: 561,
}

sub_area_bullet_bill_maze = {
        SMOLocationData.the_bullet_bill_maze_break_through: 555,
        SMOLocationData.the_bullet_bill_maze_side_path: 554,
}

sub_area_jaxi = {
        SMOLocationData.jaxi_driver: 557,
        SMOLocationData.jaxi_stunt_driving: 556,
}

sub_area_strange_neighborhood = {
        SMOLocationData.strange_neighborhood: 570,
        SMOLocationData.above_a_strange_neighborhood: 571,
}

sub_area_sand_outfit = {
        SMOLocationData.dancing_with_new_friends: 569,
}

sub_area_sand_rumbling_floor = {
        SMOLocationData.a_rumble_from_the_sandy_floor: 1136,
}

sub_area_sand_employee = {
        SMOLocationData.employees_only: 564,
}

sub_area_jaxi_ruins = {
        SMOLocationData.ice_cave_treasure: 567,
}

sub_area_sand_sphinx = {
        SMOLocationData.sphynxs_treasure_vault: 566,
}

sub_area_sand_slots = {
        SMOLocationData.sand_kingdom_slots: 1047,
}

sub_area_sand_underground = {
        SMOLocationData.underground_treasure_chest: 953,
        SMOLocationData.goomba_tower_assembly: 558,
}

sub_area_sand_arena = {
        SMOLocationData.the_hole_in_the_desert: 560,
}

sub_area_sand_arena_peace = {
        SMOLocationData.under_the_mummys_curse: 995,
}

sub_area_sand_arena_post = {
        SMOLocationData.binding_band_returned: 887,
}

sub_area_transparent_platform = {
        SMOLocationData.where_the_transparent_platforms_end: 572,
        SMOLocationData.jump_onto_the_transparent_lift: 573,
}

sub_area_colossal_ruins = {
        SMOLocationData.colossal_ruins_dash_jump: 575,
        SMOLocationData.sinking_colossal_ruins_hurry: 574,
}

sub_area_freezing_waterway = {
        SMOLocationData.through_the_freezing_waterway: 35,
        SMOLocationData.freezing_waterway_hidden_room: 36,
}

sub_area_repair = {
        SMOLocationData.a_successful_repair_job: 971,
}

sub_area_zipper = {
        SMOLocationData.unzip_the_chasm: 1008,
        SMOLocationData.super_secret_zipper: 1009,
}

sub_area_jump_grab_climb = {
        SMOLocationData.jump_grab_cling_and_climb: 425,
        SMOLocationData.jump_grab_and_climb_some_more: 426,
}

sub_area_waves_poison = {
        SMOLocationData.waves_of_poison_hoppin_over: 434,
        SMOLocationData.waves_of_poison_hop_to_it: 431,
}

sub_area_woods_treasure_trap = {
        SMOLocationData.deep_woods_treasure_trap: 188,
}

sub_area_explorer = {
        SMOLocationData.exploring_for_treasure: 187,
}

sub_area_flooding_pipe = {
        SMOLocationData.flooding_pipeway: 196,
        SMOLocationData.flooding_pipeway_ceiling_secret: 197,
}

sub_area_flower_road = {
        SMOLocationData.flower_road_run: 191,
        SMOLocationData.flower_road_reach: 192,
}

sub_area_elevator_escalation = {
        SMOLocationData.elevator_escalation: 190,
        SMOLocationData.elevator_blind_spot: 189,
}

sub_area_wooded_fog = {
        SMOLocationData.wandering_in_the_fog: 193,
        SMOLocationData.nut_hidden_in_the_fog: 194,
}

sub_area_wooded_clouds = {
        SMOLocationData.walking_on_clouds: 198,
        SMOLocationData.above_the_clouds: 199,
}

sub_area_flower_field = {
        SMOLocationData.defend_the_secret_flower_field: 181,
}

sub_area_flower_field_peace = {
        SMOLocationData.make_the_secret_flower_field_bloom: 182,
}

sub_area_nut_room = {
        SMOLocationData.spinning_platforms_treasure: 195,
}

sub_area_wooded_invisible_road = {
        SMOLocationData.invisible_road_danger: 202,
        SMOLocationData.invisible_road_hidden_room: 203,
}

sub_area_sheep = {
        SMOLocationData.herding_sheep_above_the_forest_fog: 200,
        SMOLocationData.herding_sheep_on_the_iron_bridge: 201,
}

sub_area_wooded_breakdown_road = {
        SMOLocationData.down_and_back_breakdown_road: 882,
        SMOLocationData.below_breakdown_road: 883,
}

sub_area_cloud_picture = {
        SMOLocationData.picture_match_basically_a_goomba: 982,
}

sub_area_cloud_picture_post = {
        SMOLocationData.picture_match_a_stellar_goomba: 983,
}

sub_area_cube = {
        SMOLocationData.king_of_the_cube: 914,
        SMOLocationData.the_sixth_face: 915,
}

sub_area_jungle = {
        SMOLocationData.stretch_and_traverse_the_jungle: 399,
        SMOLocationData.aglow_in_the_jungle: 400,
}

sub_area_klepto = {
        SMOLocationData.chasing_klepto: 491,
        SMOLocationData.extremely_hot_bath: 492,
}

sub_area_metro_slots = {
        SMOLocationData.metro_kingdom_slots: 1040,
}

sub_area_rc = {
        SMOLocationData.rc_car_pro: 105,
}

sub_area_rc_post = {
        SMOLocationData.rc_car_champ: 106,
}

sub_area_private_room = {
        SMOLocationData.taking_notes_in_the_private_room: 102,
}

sub_area_city_hall = {
        SMOLocationData.city_hall_lost_and_found: 100,
}

sub_area_crowd = {
        SMOLocationData.pushing_through_the_crowd: 1022,
        SMOLocationData.high_over_the_crowd: 1023,
}

sub_area_rewiring = {
        SMOLocationData.rewiring_the_neighborhood: 122,
        SMOLocationData.off_the_beaten_wire: 121,
}

sub_area_siege = {
        SMOLocationData.moon_shards_under_siege: 114,
        SMOLocationData.sharpshooting_under_siege: 113,
}

sub_area_rotating_maze = {
        SMOLocationData.inside_the_rotating_maze: 118,
        SMOLocationData.outside_the_rotating_maze: 119,
}

sub_area_high_rise = {
        SMOLocationData.hanging_from_a_high_rise: 103,
        SMOLocationData.vaulting_up_a_high_rise: 104,
}

sub_area_bullet_billding = {
        SMOLocationData.bullet_billding: 115,
        SMOLocationData.one_mans_trash: 116,
}

sub_area_motor_scooter = {
        SMOLocationData.motor_scooter_escape: 1139,
        SMOLocationData.big_jump_escape: 1140,
}

sub_area_big_screen = {
        SMOLocationData.up_on_the_big_screen: 928,
        SMOLocationData.down_inside_the_big_screen: 929,
}

sub_area_pitch_black = {
        SMOLocationData.scaling_pitchblack_mountain: 949,
        SMOLocationData.reaching_pitchblack_island: 948,
}

sub_area_swinging_scaffolding = {
        SMOLocationData.swinging_scaffolding_jump: 125,
        SMOLocationData.swinging_scaffolding_break: 126,
}

sub_area_motor_daredevil = {
        SMOLocationData.moto_scooter_daredevil: 123,
        SMOLocationData.full_throttle_scooting: 124,
}

sub_area_crowd_post_game = {
        SMOLocationData.hat_and_seek_in_the_crowd: 1021,
}

sub_area_sewer = {
        SMOLocationData.powering_up_the_station: 107,
        SMOLocationData.sewer_treasure: 1100,
}

sub_area_sewer_post_game = {
        SMOLocationData.powering_up_the_power_plant: 848,
}

sub_area_sandy_bottom = {
        SMOLocationData.wriggling_on_the_sandy_bottom: 1024,
}

sub_area_seaside_waterway = {
        SMOLocationData.looking_back_in_the_dark_waterway: 1107,
}

sub_area_seaside_sphynx = {
        SMOLocationData.the_sphynxs_underwater_vault: 483,
}

sub_area_seaside_rumble = {
        SMOLocationData.a_rumble_on_the_seaside_floor: 1135,
}

sub_area_resort = {
        SMOLocationData.a_relaxing_dance: 484,
}

sub_area_cloud_sea = {
        SMOLocationData.wading_in_the_cloud_sea: 485,
        SMOLocationData.sunken_treasure_in_the_cloud_sea: 486,
}

sub_area_valley = {
        SMOLocationData.fly_through_the_narrow_valley: 478,
        SMOLocationData.treasure_chest_in_the_narrow_valley: 479,
}

sub_area_seaside_stretch = {
        SMOLocationData.hurry_and_stretch: 482,
        SMOLocationData.stretch_on_the_side_path: 481,
}

sub_area_seaside_pokio = {
        SMOLocationData.aim_poke: 488,
        SMOLocationData.poke_roll: 487,
}

sub_area_seaside_maze = {
        SMOLocationData.the_spinning_maze_search: 489,
        SMOLocationData.the_spinning_maze_open: 490,
}

sub_area_icicle_post = {
        SMOLocationData.stacked_up_ice_climb: 699,
}

sub_area_ice_wall_post = {
        SMOLocationData.water_pooling_in_the_crevasse: 701,
}

sub_area_gusty_barrier_post = {
        SMOLocationData.icy_jump_challenge: 703,
}

sub_area_snowy_mountain_post = {
        SMOLocationData.squirming_under_the_ice: 704,
}

sub_area_magma_swamp = {
        SMOLocationData.magma_swamp_floating_and_sinking: 302,
        SMOLocationData.corner_of_the_magma_swamp: 303,
}

sub_area_veggies = {
        SMOLocationData.the_treasure_chest_in_the_veggies: 992,
}

sub_area_cook = {
        SMOLocationData.a_strong_simmer: 991,
        SMOLocationData.an_extreme_simmer: 990,
}

sub_area_forks = {
        SMOLocationData.fork_flickin_to_the_summit: 296,
        SMOLocationData.fork_flickin_detour: 297,
}

sub_area_cheese = {
        SMOLocationData.excavate_n_search_the_cheese_rocks: 300,
        SMOLocationData.climb_the_cheese_rocks: 301,
}

sub_area_lava_bubble = {
        SMOLocationData.magma_narrow_path: 299,
        SMOLocationData.crossing_to_the_magma: 298,
}

sub_area_spinning_athletics = {
        SMOLocationData.spinning_athletics_end_goal: 307,
        SMOLocationData.taking_notes_spinning_athletics: 306,
}

sub_area_luncheon_story = {
        SMOLocationData.climb_up_the_cascading_magma: 257,
        SMOLocationData.alcove_behind_the_pillars_of_magma: 259,
}

sub_area_luncheon_slots = {
        SMOLocationData.luncheon_kingdom_slots: 1042,
}

sub_area_gear_steps = {
        SMOLocationData.stepping_over_the_gears_and_lanterns_on_the_gear_steps: 313,
        SMOLocationData.lanterns_on_the_gear_steps: 312,
}

sub_area_volcano_cave = {
        SMOLocationData.volcano_cave_cruisin: 310,
        SMOLocationData.volcano_cave_and_mysterious_clouds: 311,
}

sub_area_lava_islands = {
        SMOLocationData.treasure_of_the_lava_islands: 1101,
        SMOLocationData.flying_over_the_lava_islands: 308,
}

sub_area_roulette_tower = {
        SMOLocationData.roulette_tower_climbed: 888,
        SMOLocationData.roulette_tower_stopped: 889,
}

sub_area_ruined_charging = {
        SMOLocationData.charging_through_an_army: 891,
        SMOLocationData.the_mummys_curse: 890,
}

sub_area_samurai = {
        SMOLocationData.scene_of_crossing_the_poison_swamp: 987,
        SMOLocationData.taking_notes_in_the_folding_screen: 988,
}

sub_area_bowser_vault = {
        SMOLocationData.bowsers_castle_treasure_vault: 999,
}

sub_area_jizo_adventure = {
        SMOLocationData.jizos_big_adventure: 363,
        SMOLocationData.jizo_and_the_hidden_room: 364,
}

sub_area_spinning_tower = {
        SMOLocationData.on_top_of_the_spinning_tower: 368,
        SMOLocationData.down_and_up_the_spinning_tower: 367,
}

sub_area_hexagon_tower = {
        SMOLocationData.searching_hexagon_tower: 801,
        SMOLocationData.center_of_hexagon_tower: 802,
}

sub_area_wooden_tower = {
        SMOLocationData.climb_the_wooden_tower: 370,
        SMOLocationData.poke_the_wooden_tower: 369,
}

sub_area_galaxy = {
        SMOLocationData.edge_of_the_galaxy: 604,
        SMOLocationData.center_of_the_galaxy: 603,
}

sub_area_swings = {
        SMOLocationData.navigating_giant_swings: 601,
        SMOLocationData.a_swing_on_top_of_a_swing: 602,
}

sub_area_sphynx_moon = {
        SMOLocationData.sphynxs_hidden_vault: 599,
}

sub_area_mushroom_picture = {
        SMOLocationData.picture_match_basically_mario: 985,
        SMOLocationData.picture_match_a_stellar_mario: 986,
}

sub_area_64 = {
        SMOLocationData.totally_classic: 934,
        SMOLocationData.courtyard_chest_trap: 1144,
}

sub_area_castle = {
        SMOLocationData.light_from_the_ceiling: 807,
        SMOLocationData.loose_tile_trackdown: 956,
}

sub_area_mushroom_well = {
        SMOLocationData.secret_2d_treasure: 1050,
        SMOLocationData.dot_boost_from_bullet_bill: 1051,
}

sub_area_yoshi_clouds = {
        SMOLocationData.yoshis_feast_in_the_sea_of_clouds: 974,
        SMOLocationData.sunken_star_in_the_sea_of_clouds: 975,
}

sub_area_rematch_tostarena = {
        SMOLocationData.tussle_in_tostarena_rematch: 1148,
}

sub_area_rematch_steam_gardens = {
        SMOLocationData.struggle_in_steam_gardens_rematch: 1149,
}

sub_area_rematch_bubblaine = {
        SMOLocationData.battle_in_bubblaine_rematch: 1147,
}

sub_area_rematch_metro = {
        SMOLocationData.dust_up_in_new_donk_city_rematch: 1141,
}

sub_area_rematch_volbono = {
        SMOLocationData.blowup_at_mount_volbono_rematch: 1142,
}

sub_area_rematch_crumbleden = {
        SMOLocationData.rumble_in_crumbleden_rematch: 1146,
}

sub_area_darker_invisible = {
        SMOLocationData.invisible_road_rush: 1069,
        SMOLocationData.invisible_road_secret: 1068,
}

sub_area_darker_breakdown = {
        SMOLocationData.breakdown_road_hurry: 1062,
        SMOLocationData.breakdown_road_final_challenge: 1063,
}

sub_area_darker_vanishing = {
        SMOLocationData.vanishing_road_rush: 1065,
        SMOLocationData.vanishing_road_challenge: 1064,
}

sub_area_darker_yoshi_siege = {
        SMOLocationData.yoshi_under_siege: 1066,
        SMOLocationData.fruit_feast_under_siege: 1067,
}

sub_area_darker_yoshi_sinking = {
        SMOLocationData.yoshi_on_the_sinking_island: 1070,
        SMOLocationData.fruit_feast_on_the_sinking_island: 1071,
}

sub_area_darker_yoshi_magma = {
        SMOLocationData.yoshis_magma_swamp: 1082,
        SMOLocationData.fruit_feast_in_the_magma_swamp: 1083,
}

sub_area_inverted_pyramid = {
        SMOLocationData.hidden_room_in_the_inverted_pyramid: 563,
}

loc_Sand_Pyramid_Mural = {
        SMOLocationData.secret_of_the_inverted_mural: 504,
}

sub_area_mysterious_clouds = {
        SMOLocationData.across_the_mysterious_clouds: 224,
        SMOLocationData.atop_a_wall_among_the_clouds: 223,
}

sub_area_moon_cave = {
        SMOLocationData.under_the_bowser_statue: 595,
        SMOLocationData.in_a_hole_in_the_magma: 596,
        SMOLocationData.around_the_barrier_wall: 597,
        SMOLocationData.on_top_of_the_cannon: 594,
        SMOLocationData.fly_to_the_treasure_chest_and_back: 598,
}

sub_area_snow_koopa = {
        SMOLocationData.walking_on_ice: 877,
}

sub_area_snow_koopa_post = {
        SMOLocationData.even_more_walking_on_ice: 878,
}

sub_area_snow_outfit = {
        SMOLocationData.moon_shards_in_the_cold_room: 1030,
        SMOLocationData.slip_behind_the_ice: 1031,
}

sub_area_snow_dashing = {
        SMOLocationData.dashing_over_cold_water: 12,
        SMOLocationData.dashing_above_and_beyond: 13,
}

sub_area_snow_freezing_water = {
        SMOLocationData.jump_n_swim_in_the_freezing_water: 14,
        SMOLocationData.freezing_water_near_the_ceiling: 15,
}

sub_area_blowing = {
        SMOLocationData.blowing_and_sliding: 33,
}

sub_area_snow_spinning = {
        SMOLocationData.spinning_above_the_clouds: 830,
        SMOLocationData.high_altitude_spinning: 831,
}

sub_area_snow_flower_road = {
        SMOLocationData.running_the_flower_road: 31,
        SMOLocationData.looking_back_on_the_flower_road: 32,
}

sub_area_iceburn = {
        SMOLocationData.iceburn_circuit_class_a: 998,
        SMOLocationData.iceburn_circuit_class_s: 997,
}

sub_area_bowser_clouds = {
        SMOLocationData.dashing_above_the_clouds: 365,
        SMOLocationData.dashing_through_the_clouds: 366,
}

sub_area_church = {
        SMOLocationData.up_in_the_rafters: 593,
}

sub_area_shiveria = {
        SMOLocationData.entrance_to_shiveria: 1081,
        SMOLocationData.shining_in_the_snow_in_town: 1080,
        SMOLocationData.the_shiverian_treasure_chest: 23,
        SMOLocationData.found_with_snow_kingdom_art: 1087,
        SMOLocationData.the_icicle_barrier: 17,
        SMOLocationData.ice_dodging_goomba_stack: 20,
        SMOLocationData.the_ice_wall_barrier: 22,
        SMOLocationData.treasure_in_the_ice_wall: 24,
        SMOLocationData.the_gusty_barrier: 18,
        SMOLocationData.atop_a_blustery_arch: 16,
        SMOLocationData.the_snowy_mountain_barrier: 25,
        SMOLocationData.behind_the_snowy_mountain: 21,
}

sub_area_shiveria_peace = {
        SMOLocationData.im_not_cold: 873,
}

sub_area_snowline = {
        SMOLocationData.the_bound_bowl_grand_prix: 1020,
        SMOLocationData.snowline_circuit_class_s: 879,
}



base_locations_table = {
    **loc_Cap,
    **loc_Cascade,
    **loc_Cascade_Peace,
    **loc_Cascade_Revisit,
    **loc_Cascade_Post_Metro,
    **loc_Cascade_Post_Snow,
    **loc_Sand,
    **loc_Sand_Pyramid,
    **loc_Night_Sand,
    **loc_Sand_Underground,
    **loc_Sand_Peace,
    **loc_Sand_Pyramid_Peace,
    **loc_Sand_Revisit,
    **loc_Lake,
    **loc_Lake_Post_Seaside,
    **loc_Wooded,
    **loc_Wooded_Post_Metro,
    **loc_Wooded_Post_Story1,
    **loc_Wooded_Peace,
    **loc_Cloud,
    **loc_Lost,
    **loc_Lost_Revisit,
    **loc_Night_Metro,
    **loc_Metro,
    **loc_Metro_Post_Sand,
    **loc_Metro_Sewer_Access,
    **loc_Metro_Peace,
    **loc_Snow,
    **loc_Snow_Peace,
    **loc_Seaside,
    **loc_Seaside_Peace,
    **loc_Luncheon,
    **loc_Luncheon_Post_Wooded,
    **loc_Luncheon_Post_Spewart,
    **loc_Luncheon_Post_Cheese_Rocks,
    **loc_Luncheon_Peace,
    **loc_Ruined,
    **loc_Bowser,
    **loc_Bowser_Infiltrate,
    **loc_Bowser_Post_Bombing,
    **loc_Bowser_Mecha_Broodal,
    **loc_Bowser_Peace,
    **loc_Moon,
    **loc_Mushroom_Post_Luncheon
}

shop_locations_table = {
    **loc_Cap_Shop,
    **loc_Cascade_Shop,
    **loc_Sand_Shop,
    **loc_Wooded_Shop,
    **loc_Lake_Shop,
    **loc_Lost_Shop,
    **loc_Metro_Shop,
    **loc_Seaside_Shop,
    **loc_Snow_Shop,
    **loc_Luncheon_Shop,
    **loc_Bowser_Shop,
    **loc_Moon_Outfit,
    **loc_Moon_Shop,
    **loc_Mushroom_Shop,
    **loc_Postgame_Shop,
    **loc_Dark_Outfit,
    **loc_Darker_Outfit,
    **loc_odyssey_outfit,
    **shop_sand_coin,
    **shop_lake_coin,
    **shop_wooded_coin,
    **shop_metro_coin,
    **shop_seaside_coin,
    **shop_luncheon_coin,
    **shop_moon_coin,
    **shop_post_game_coin
}

post_game_locations_table = {
    **loc_Cap_Postgame,
    **loc_Cascade_Postgame,
    **loc_Sand_Postgame,
    **loc_Lake_Postgame,
    **loc_Wooded_Postgame,
    **loc_Cloud_Postgame,
    **loc_Lost_Postgame,
    **loc_Metro_Postgame,
    **loc_Snow_Postgame,
    **loc_Seaside_Postgame,
    **loc_Luncheon_Postgame,
    **loc_Ruined_Postgame,
    **loc_Bowser_Postgame,
    **loc_Moon_Postgame,
    **loc_Mushroom
}

special_locations_table = {
    **loc_Dark,
    **loc_Darker
}

sub_area_table = {
    **sub_area_frog,
    **sub_area_poison_tide,
    **sub_area_push_block,
    **sub_area_rolling,
    **sub_area_chain_chomp,
    **sub_area_trex_nest,
    **sub_area_cascade_2d,
    **sub_area_gusty_bridges,
    **sub_area_invisible_maze,
    **sub_area_bullet_bill_maze,
    **sub_area_jaxi,
    **sub_area_strange_neighborhood,
    **sub_area_sand_outfit,
    **sub_area_sand_rumbling_floor,
    **sub_area_sand_employee,
    **sub_area_jaxi_ruins,
    **sub_area_sand_sphinx,
    **sub_area_sand_slots,
    **sub_area_sand_underground,
    **sub_area_sand_arena,
    **sub_area_sand_arena_peace,
    **sub_area_sand_arena_post,
    **sub_area_transparent_platform,
    **sub_area_colossal_ruins,
    **sub_area_freezing_waterway,
    **sub_area_repair,
    **sub_area_zipper,
    **sub_area_jump_grab_climb,
    **sub_area_waves_poison,
    **sub_area_woods_treasure_trap,
    **sub_area_explorer,
    **sub_area_flooding_pipe,
    **sub_area_flower_road,
    **sub_area_elevator_escalation,
    **sub_area_wooded_fog,
    **sub_area_wooded_clouds,
    **sub_area_flower_field,
    **sub_area_flower_field_peace,
    **sub_area_nut_room,
    **sub_area_wooded_invisible_road,
    **sub_area_sheep,
    **sub_area_wooded_breakdown_road,
    **sub_area_cloud_picture,
    **sub_area_cloud_picture_post,
    **sub_area_cube,
    **sub_area_jungle,
    **sub_area_klepto,
    **sub_area_metro_slots,
    **sub_area_rc,
    **sub_area_rc_post,
    **sub_area_private_room,
    **sub_area_city_hall,
    **sub_area_crowd,
    **sub_area_rewiring,
    **sub_area_siege,
    **sub_area_rotating_maze,
    **sub_area_high_rise,
    **sub_area_bullet_billding,
    **sub_area_motor_scooter,
    **sub_area_big_screen,
    **sub_area_pitch_black,
    **sub_area_swinging_scaffolding,
    **sub_area_motor_daredevil,
    **sub_area_crowd_post_game,
    **sub_area_sewer,
    **sub_area_sewer_post_game,
    **sub_area_sandy_bottom,
    **sub_area_seaside_waterway,
    **sub_area_seaside_sphynx,
    **sub_area_seaside_rumble,
    **sub_area_resort,
    **sub_area_cloud_sea,
    **sub_area_valley,
    **sub_area_seaside_stretch,
    **sub_area_seaside_pokio,
    **sub_area_seaside_maze,
    **sub_area_icicle_post,
    **sub_area_ice_wall_post,
    **sub_area_gusty_barrier_post,
    **sub_area_snowy_mountain_post,
    **sub_area_magma_swamp,
    **sub_area_veggies,
    **sub_area_cook,
    **sub_area_forks,
    **sub_area_cheese,
    **sub_area_lava_bubble,
    **sub_area_spinning_athletics,
    **sub_area_luncheon_story,
    **sub_area_luncheon_slots,
    **sub_area_gear_steps,
    **sub_area_volcano_cave,
    **sub_area_lava_islands,
    **sub_area_roulette_tower,
    **sub_area_ruined_charging,
    **sub_area_samurai,
    **sub_area_bowser_vault,
    **sub_area_jizo_adventure,
    **sub_area_spinning_tower,
    **sub_area_hexagon_tower,
    **sub_area_wooden_tower,
    **sub_area_galaxy,
    **sub_area_swings,
    **sub_area_sphynx_moon,
    **sub_area_mushroom_picture,
    **sub_area_64,
    **sub_area_castle,
    **sub_area_mushroom_well,
    **sub_area_yoshi_clouds,
    **sub_area_rematch_tostarena,
    **sub_area_rematch_steam_gardens,
    **sub_area_rematch_bubblaine,
    **sub_area_rematch_metro,
    **sub_area_rematch_volbono,
    **sub_area_rematch_crumbleden,
    **sub_area_darker_invisible,
    **sub_area_darker_breakdown,
    **sub_area_darker_vanishing,
    **sub_area_darker_yoshi_siege,
    **sub_area_darker_yoshi_sinking,
    **sub_area_darker_yoshi_magma,
    **sub_area_inverted_pyramid,
    **loc_Sand_Pyramid_Mural,
    **sub_area_mysterious_clouds,
    **sub_area_moon_cave,
    **sub_area_snow_koopa,
    **sub_area_snow_koopa_post,
    **sub_area_snow_outfit,
    **sub_area_snow_dashing,
    **sub_area_snow_freezing_water,
    **sub_area_blowing,
    **sub_area_snow_spinning,
    **sub_area_snow_flower_road,
    **sub_area_iceburn,
    **sub_area_bowser_clouds,
    **sub_area_church,
    **sub_area_shiveria,
    **sub_area_shiveria_peace,
    **sub_area_snowline,
}

#region Regional Coins

cap_kingdom_regional_groups = {
        SMOLocationData.cap_kingdom_regional_coin_group_1: 2700,
        SMOLocationData.cap_kingdom_regional_coin_group_2: 2705,
        SMOLocationData.cap_kingdom_regional_coin_group_3: 2710,
        SMOLocationData.cap_kingdom_regional_coin_group_4: 2715,
        SMOLocationData.cap_kingdom_regional_coin_group_5: 2720,
        SMOLocationData.cap_kingdom_regional_coin_group_6: 2724,
        SMOLocationData.cap_kingdom_regional_coin_group_7: 2728,
        SMOLocationData.cap_kingdom_regional_coin_group_8: 2732,
        SMOLocationData.cap_kingdom_regional_coin_group_9: 2736,
}

top_hat_tower_regional_groups = {
        SMOLocationData.top_hat_tower_regional_coin_group_1: 2740,
        SMOLocationData.top_hat_tower_regional_coin_group_2: 2745,
}

frog_pond_regional_groups = {
        SMOLocationData.frog_pond_regional_coin_group_1: 2751,
}

pushblocks_regional_groups = {
        SMOLocationData.pushblocks_regional_coin_group_1: 2756,
}

poison_tides_regional_groups = {
        SMOLocationData.poison_tides_regional_coin_group_1: 2760,
}

cap_kingdom_regional_coins = {
        SMOLocationData.cap_kingdom_regional_coin_1: 2701,
        SMOLocationData.cap_kingdom_regional_coin_2: 2702,
        SMOLocationData.cap_kingdom_regional_coin_3: 2703,
        SMOLocationData.cap_kingdom_regional_coin_4: 2704,
        SMOLocationData.cap_kingdom_regional_coin_5: 2706,
        SMOLocationData.cap_kingdom_regional_coin_6: 2707,
        SMOLocationData.cap_kingdom_regional_coin_7: 2708,
        SMOLocationData.cap_kingdom_regional_coin_8: 2709,
        SMOLocationData.cap_kingdom_regional_coin_9: 2711,
        SMOLocationData.cap_kingdom_regional_coin_10: 2712,
        SMOLocationData.cap_kingdom_regional_coin_11: 2713,
        SMOLocationData.cap_kingdom_regional_coin_12: 2714,
        SMOLocationData.cap_kingdom_regional_coin_13: 2716,
        SMOLocationData.cap_kingdom_regional_coin_14: 2717,
        SMOLocationData.cap_kingdom_regional_coin_15: 2718,
        SMOLocationData.cap_kingdom_regional_coin_16: 2719,
        SMOLocationData.cap_kingdom_regional_coin_17: 2721,
        SMOLocationData.cap_kingdom_regional_coin_18: 2722,
        SMOLocationData.cap_kingdom_regional_coin_19: 2723,
        SMOLocationData.cap_kingdom_regional_coin_20: 2725,
        SMOLocationData.cap_kingdom_regional_coin_21: 2726,
        SMOLocationData.cap_kingdom_regional_coin_22: 2727,
        SMOLocationData.cap_kingdom_regional_coin_23: 2729,
        SMOLocationData.cap_kingdom_regional_coin_24: 2730,
        SMOLocationData.cap_kingdom_regional_coin_25: 2731,
        SMOLocationData.cap_kingdom_regional_coin_26: 2733,
        SMOLocationData.cap_kingdom_regional_coin_27: 2734,
        SMOLocationData.cap_kingdom_regional_coin_28: 2735,
        SMOLocationData.cap_kingdom_regional_coin_29: 2737,
        SMOLocationData.cap_kingdom_regional_coin_30: 2738,
        SMOLocationData.cap_kingdom_regional_coin_31: 2739,
}

top_hat_tower_regional_coins = {
        SMOLocationData.top_hat_tower_regional_coin_1: 2741,
        SMOLocationData.top_hat_tower_regional_coin_2: 2742,
        SMOLocationData.top_hat_tower_regional_coin_3: 2743,
        SMOLocationData.top_hat_tower_regional_coin_4: 2744,
        SMOLocationData.top_hat_tower_regional_coin_5: 2746,
        SMOLocationData.top_hat_tower_regional_coin_6: 2747,
        SMOLocationData.top_hat_tower_regional_coin_7: 2748,
        SMOLocationData.top_hat_tower_regional_coin_8: 2749,
        SMOLocationData.top_hat_tower_regional_coin_9: 2750,
}

frog_pond_regional_coins = {
        SMOLocationData.frog_pond_regional_coin_1: 2752,
        SMOLocationData.frog_pond_regional_coin_2: 2753,
        SMOLocationData.frog_pond_regional_coin_3: 2754,
        SMOLocationData.frog_pond_regional_coin_4: 2755,
}

pushblocks_regional_coins = {
        SMOLocationData.pushblocks_regional_coin_1: 2757,
        SMOLocationData.pushblocks_regional_coin_2: 2758,
        SMOLocationData.pushblocks_regional_coin_3: 2759,
}

poison_tides_regional_coins = {
        SMOLocationData.poison_tides_regional_coin_1: 2761,
        SMOLocationData.poison_tides_regional_coin_2: 2762,
        SMOLocationData.poison_tides_regional_coin_3: 2763,
}

cascade_kingdom_regional_groups = {
        SMOLocationData.cascade_kingdom_regional_coin_group_1: 2764,
        SMOLocationData.cascade_kingdom_regional_coin_group_2: 2768,
        SMOLocationData.cascade_kingdom_regional_coin_group_3: 2772,
        SMOLocationData.cascade_kingdom_regional_coin_group_4: 2776,
        SMOLocationData.cascade_kingdom_regional_coin_group_5: 2780,
        SMOLocationData.cascade_kingdom_regional_coin_group_6: 2784,
        SMOLocationData.cascade_kingdom_regional_coin_group_7: 2788,
        SMOLocationData.cascade_kingdom_regional_coin_group_8: 2792,
        SMOLocationData.cascade_kingdom_regional_coin_group_9: 2796,
        SMOLocationData.cascade_kingdom_regional_coin_group_10: 2800,
        SMOLocationData.cascade_kingdom_regional_coin_group_11: 2805,
        SMOLocationData.cascade_kingdom_regional_coin_group_12: 2809,
        SMOLocationData.cascade_kingdom_regional_coin_group_13: 2813,
        SMOLocationData.cascade_kingdom_regional_coin_group_15: 2821,
}

cascade_kingdom_peace_regional_groups = {
        SMOLocationData.cascade_kingdom_regional_coin_group_14: 2817,
}

chasm_lifts_regional_groups = {
        SMOLocationData.chasm_lifts_regional_coin_group_1: 2825,
}

cascade_kingdom_regional_coins = {
        SMOLocationData.cascade_kingdom_regional_coin_1: 2765,
        SMOLocationData.cascade_kingdom_regional_coin_2: 2766,
        SMOLocationData.cascade_kingdom_regional_coin_3: 2767,
        SMOLocationData.cascade_kingdom_regional_coin_4: 2769,
        SMOLocationData.cascade_kingdom_regional_coin_5: 2770,
        SMOLocationData.cascade_kingdom_regional_coin_6: 2771,
        SMOLocationData.cascade_kingdom_regional_coin_7: 2773,
        SMOLocationData.cascade_kingdom_regional_coin_8: 2774,
        SMOLocationData.cascade_kingdom_regional_coin_9: 2775,
        SMOLocationData.cascade_kingdom_regional_coin_10: 2777,
        SMOLocationData.cascade_kingdom_regional_coin_11: 2778,
        SMOLocationData.cascade_kingdom_regional_coin_12: 2779,
        SMOLocationData.cascade_kingdom_regional_coin_13: 2781,
        SMOLocationData.cascade_kingdom_regional_coin_14: 2782,
        SMOLocationData.cascade_kingdom_regional_coin_15: 2783,
        SMOLocationData.cascade_kingdom_regional_coin_16: 2785,
        SMOLocationData.cascade_kingdom_regional_coin_17: 2786,
        SMOLocationData.cascade_kingdom_regional_coin_18: 2787,
        SMOLocationData.cascade_kingdom_regional_coin_19: 2789,
        SMOLocationData.cascade_kingdom_regional_coin_20: 2790,
        SMOLocationData.cascade_kingdom_regional_coin_21: 2791,
        SMOLocationData.cascade_kingdom_regional_coin_22: 2793,
        SMOLocationData.cascade_kingdom_regional_coin_23: 2794,
        SMOLocationData.cascade_kingdom_regional_coin_24: 2795,
        SMOLocationData.cascade_kingdom_regional_coin_25: 2797,
        SMOLocationData.cascade_kingdom_regional_coin_26: 2798,
        SMOLocationData.cascade_kingdom_regional_coin_27: 2799,
        SMOLocationData.cascade_kingdom_regional_coin_28: 2801,
        SMOLocationData.cascade_kingdom_regional_coin_29: 2802,
        SMOLocationData.cascade_kingdom_regional_coin_30: 2803,
        SMOLocationData.cascade_kingdom_regional_coin_31: 2804,
        SMOLocationData.cascade_kingdom_regional_coin_32: 2806,
        SMOLocationData.cascade_kingdom_regional_coin_33: 2807,
        SMOLocationData.cascade_kingdom_regional_coin_34: 2808,
        SMOLocationData.cascade_kingdom_regional_coin_35: 2810,
        SMOLocationData.cascade_kingdom_regional_coin_36: 2811,
        SMOLocationData.cascade_kingdom_regional_coin_37: 2812,
        SMOLocationData.cascade_kingdom_regional_coin_38: 2814,
        SMOLocationData.cascade_kingdom_regional_coin_39: 2815,
        SMOLocationData.cascade_kingdom_regional_coin_40: 2816,
        SMOLocationData.cascade_kingdom_regional_coin_41: 2818,
        SMOLocationData.cascade_kingdom_regional_coin_42: 2819,
        SMOLocationData.cascade_kingdom_regional_coin_43: 2820,
        SMOLocationData.cascade_kingdom_regional_coin_44: 2822,
        SMOLocationData.cascade_kingdom_regional_coin_45: 2823,
        SMOLocationData.cascade_kingdom_regional_coin_46: 2824,
}

chasm_lifts_regional_coins = {
        SMOLocationData.chasm_lifts_regional_coin_1: 2826,
        SMOLocationData.chasm_lifts_regional_coin_2: 2827,
        SMOLocationData.chasm_lifts_regional_coin_3: 2828,
        SMOLocationData.chasm_lifts_regional_coin_4: 2829,
}

sand_kingdom_regional_groups = {
        SMOLocationData.sand_kingdom_regional_coin_group_1: 2830,
        SMOLocationData.sand_kingdom_regional_coin_group_2: 2834,
        SMOLocationData.sand_kingdom_regional_coin_group_3: 2838,
        SMOLocationData.sand_kingdom_regional_coin_group_4: 2842,
        SMOLocationData.sand_kingdom_regional_coin_group_5: 2846,
        SMOLocationData.sand_kingdom_regional_coin_group_6: 2850,
        SMOLocationData.sand_kingdom_regional_coin_group_7: 2853,
        SMOLocationData.sand_kingdom_regional_coin_group_8: 2856,
        SMOLocationData.sand_kingdom_regional_coin_group_9: 2860,
        SMOLocationData.sand_kingdom_regional_coin_group_11: 2868,
        SMOLocationData.sand_kingdom_regional_coin_group_12: 2872,
        SMOLocationData.sand_kingdom_regional_coin_group_13: 2876,
        SMOLocationData.sand_kingdom_regional_coin_group_14: 2880,
        SMOLocationData.sand_kingdom_regional_coin_group_15: 2884,
        SMOLocationData.sand_kingdom_regional_coin_group_16: 2887,
        SMOLocationData.sand_kingdom_regional_coin_group_17: 2894,
        SMOLocationData.sand_kingdom_regional_coin_group_20: 2908,
        SMOLocationData.sand_kingdom_regional_coin_group_21: 2911,
}

sand_kingdom_pyramid_over_world_regional_groups = {
        SMOLocationData.sand_kingdom_regional_coin_group_10: 2864,
}

sand_kingdom_peace_regional_groups = {
        SMOLocationData.sand_kingdom_regional_coin_group_18: 2898,
        SMOLocationData.sand_kingdom_regional_coin_group_19: 2903,
}

bullet_bill_maze_regional_groups = {
        SMOLocationData.bullet_bill_maze_regional_coin_group_1: 2914,
}

moeeye_invisible_maze_regional_groups = {
        SMOLocationData.moeeye_invisible_maze_regional_coin_group_1: 2921,
}

ice_cave_regional_groups = {
        SMOLocationData.ice_cave_regional_coin_group_1: 2926,
        SMOLocationData.ice_cave_regional_coin_group_2: 2929,
}

pyramid_upper_interior_regional_groups = {
        SMOLocationData.pyramid_upper_interior_regional_coin_group_1: 2932,
}

strange_neighborhood_regional_groups = {
        SMOLocationData.strange_neighborhood_regional_coin_group_1: 2936,
        SMOLocationData.strange_neighborhood_regional_coin_group_2: 2939,
}

underground_ruins_regional_groups = {
        SMOLocationData.underground_ruins_regional_coin_group_1: 2943,
        SMOLocationData.underground_ruins_regional_coin_group_2: 2947,
}

jaxi_ruins_regional_groups = {
        SMOLocationData.jaxi_ruins_regional_coin_group_1: 2952,
        SMOLocationData.jaxi_ruins_regional_coin_group_2: 2955,
        SMOLocationData.jaxi_ruins_regional_coin_group_3: 2959,
}

sand_kingdom_regional_coins = {
        SMOLocationData.sand_kingdom_regional_coin_1: 2831,
        SMOLocationData.sand_kingdom_regional_coin_2: 2832,
        SMOLocationData.sand_kingdom_regional_coin_3: 2833,
        SMOLocationData.sand_kingdom_regional_coin_4: 2835,
        SMOLocationData.sand_kingdom_regional_coin_5: 2836,
        SMOLocationData.sand_kingdom_regional_coin_6: 2837,
        SMOLocationData.sand_kingdom_regional_coin_7: 2839,
        SMOLocationData.sand_kingdom_regional_coin_8: 2840,
        SMOLocationData.sand_kingdom_regional_coin_9: 2841,
        SMOLocationData.sand_kingdom_regional_coin_10: 2843,
        SMOLocationData.sand_kingdom_regional_coin_11: 2844,
        SMOLocationData.sand_kingdom_regional_coin_12: 2845,
        SMOLocationData.sand_kingdom_regional_coin_13: 2847,
        SMOLocationData.sand_kingdom_regional_coin_14: 2848,
        SMOLocationData.sand_kingdom_regional_coin_15: 2849,
        SMOLocationData.sand_kingdom_regional_coin_16: 2851,
        SMOLocationData.sand_kingdom_regional_coin_17: 2852,
        SMOLocationData.sand_kingdom_regional_coin_18: 2854,
        SMOLocationData.sand_kingdom_regional_coin_19: 2855,
        SMOLocationData.sand_kingdom_regional_coin_20: 2857,
        SMOLocationData.sand_kingdom_regional_coin_21: 2858,
        SMOLocationData.sand_kingdom_regional_coin_22: 2859,
        SMOLocationData.sand_kingdom_regional_coin_23: 2861,
        SMOLocationData.sand_kingdom_regional_coin_24: 2862,
        SMOLocationData.sand_kingdom_regional_coin_25: 2863,
        SMOLocationData.sand_kingdom_regional_coin_26: 2865,
        SMOLocationData.sand_kingdom_regional_coin_27: 2866,
        SMOLocationData.sand_kingdom_regional_coin_28: 2867,
        SMOLocationData.sand_kingdom_regional_coin_29: 2869,
        SMOLocationData.sand_kingdom_regional_coin_30: 2870,
        SMOLocationData.sand_kingdom_regional_coin_31: 2871,
        SMOLocationData.sand_kingdom_regional_coin_32: 2873,
        SMOLocationData.sand_kingdom_regional_coin_33: 2874,
        SMOLocationData.sand_kingdom_regional_coin_34: 2875,
        SMOLocationData.sand_kingdom_regional_coin_35: 2877,
        SMOLocationData.sand_kingdom_regional_coin_36: 2878,
        SMOLocationData.sand_kingdom_regional_coin_37: 2879,
        SMOLocationData.sand_kingdom_regional_coin_38: 2881,
        SMOLocationData.sand_kingdom_regional_coin_39: 2882,
        SMOLocationData.sand_kingdom_regional_coin_40: 2883,
        SMOLocationData.sand_kingdom_regional_coin_41: 2885,
        SMOLocationData.sand_kingdom_regional_coin_42: 2886,
        SMOLocationData.sand_kingdom_regional_coin_43: 2888,
        SMOLocationData.sand_kingdom_regional_coin_44: 2889,
        SMOLocationData.sand_kingdom_regional_coin_45: 2890,
        SMOLocationData.sand_kingdom_regional_coin_46: 2891,
        SMOLocationData.sand_kingdom_regional_coin_47: 2892,
        SMOLocationData.sand_kingdom_regional_coin_48: 2893,
        SMOLocationData.sand_kingdom_regional_coin_49: 2895,
        SMOLocationData.sand_kingdom_regional_coin_50: 2896,
        SMOLocationData.sand_kingdom_regional_coin_51: 2897,
        SMOLocationData.sand_kingdom_regional_coin_52: 2899,
        SMOLocationData.sand_kingdom_regional_coin_53: 2900,
        SMOLocationData.sand_kingdom_regional_coin_54: 2901,
        SMOLocationData.sand_kingdom_regional_coin_55: 2902,
        SMOLocationData.sand_kingdom_regional_coin_56: 2904,
        SMOLocationData.sand_kingdom_regional_coin_57: 2905,
        SMOLocationData.sand_kingdom_regional_coin_58: 2906,
        SMOLocationData.sand_kingdom_regional_coin_59: 2907,
        SMOLocationData.sand_kingdom_regional_coin_60: 2909,
        SMOLocationData.sand_kingdom_regional_coin_61: 2910,
        SMOLocationData.sand_kingdom_regional_coin_62: 2912,
        SMOLocationData.sand_kingdom_regional_coin_63: 2913,
}

bullet_bill_maze_regional_coins = {
        SMOLocationData.bullet_bill_maze_regional_coin_1: 2915,
        SMOLocationData.bullet_bill_maze_regional_coin_2: 2916,
        SMOLocationData.bullet_bill_maze_regional_coin_3: 2917,
        SMOLocationData.bullet_bill_maze_regional_coin_4: 2918,
        SMOLocationData.bullet_bill_maze_regional_coin_5: 2919,
        SMOLocationData.bullet_bill_maze_regional_coin_6: 2920,
}

moeeye_invisible_maze_regional_coins = {
        SMOLocationData.moeeye_invisible_maze_regional_coin_1: 2922,
        SMOLocationData.moeeye_invisible_maze_regional_coin_2: 2923,
        SMOLocationData.moeeye_invisible_maze_regional_coin_3: 2924,
        SMOLocationData.moeeye_invisible_maze_regional_coin_4: 2925,
}

ice_cave_regional_coins = {
        SMOLocationData.ice_cave_regional_coin_1: 2927,
        SMOLocationData.ice_cave_regional_coin_2: 2928,
        SMOLocationData.ice_cave_regional_coin_3: 2930,
        SMOLocationData.ice_cave_regional_coin_4: 2931,
}

pyramid_upper_interior_regional_coins = {
        SMOLocationData.pyramid_upper_interior_regional_coin_1: 2933,
        SMOLocationData.pyramid_upper_interior_regional_coin_2: 2934,
        SMOLocationData.pyramid_upper_interior_regional_coin_3: 2935,
}

strange_neighborhood_regional_coins = {
        SMOLocationData.strange_neighborhood_regional_coin_1: 2937,
        SMOLocationData.strange_neighborhood_regional_coin_2: 2938,
        SMOLocationData.strange_neighborhood_regional_coin_3: 2940,
        SMOLocationData.strange_neighborhood_regional_coin_4: 2941,
        SMOLocationData.strange_neighborhood_regional_coin_5: 2942,
}

underground_ruins_regional_coins = {
        SMOLocationData.underground_ruins_regional_coin_1: 2944,
        SMOLocationData.underground_ruins_regional_coin_2: 2945,
        SMOLocationData.underground_ruins_regional_coin_3: 2946,
        SMOLocationData.underground_ruins_regional_coin_4: 2948,
        SMOLocationData.underground_ruins_regional_coin_5: 2949,
        SMOLocationData.underground_ruins_regional_coin_6: 2950,
        SMOLocationData.underground_ruins_regional_coin_7: 2951,
}

jaxi_ruins_regional_coins = {
        SMOLocationData.jaxi_ruins_regional_coin_1: 2953,
        SMOLocationData.jaxi_ruins_regional_coin_2: 2954,
        SMOLocationData.jaxi_ruins_regional_coin_3: 2956,
        SMOLocationData.jaxi_ruins_regional_coin_4: 2957,
        SMOLocationData.jaxi_ruins_regional_coin_5: 2958,
        SMOLocationData.jaxi_ruins_regional_coin_6: 2960,
        SMOLocationData.jaxi_ruins_regional_coin_7: 2961,
        SMOLocationData.jaxi_ruins_regional_coin_8: 2962,
}

wooded_kingdom_regional_groups = {
        SMOLocationData.wooded_kingdom_regional_coin_group_1: 2963,
        SMOLocationData.wooded_kingdom_regional_coin_group_2: 2967,
        SMOLocationData.wooded_kingdom_regional_coin_group_3: 2971,
        SMOLocationData.wooded_kingdom_regional_coin_group_4: 2975,
        SMOLocationData.wooded_kingdom_regional_coin_group_5: 2978,
        SMOLocationData.wooded_kingdom_regional_coin_group_6: 2983,
        SMOLocationData.wooded_kingdom_regional_coin_group_7: 2988,
        SMOLocationData.wooded_kingdom_regional_coin_group_8: 2992,
        SMOLocationData.wooded_kingdom_regional_coin_group_9: 2996,
        SMOLocationData.wooded_kingdom_regional_coin_group_10: 3001,
        SMOLocationData.wooded_kingdom_regional_coin_group_11: 3006,
        SMOLocationData.wooded_kingdom_regional_coin_group_12: 3011,
        SMOLocationData.wooded_kingdom_regional_coin_group_13: 3015,
        SMOLocationData.wooded_kingdom_regional_coin_group_14: 3019,
        SMOLocationData.wooded_kingdom_regional_coin_group_15: 3024,
        SMOLocationData.wooded_kingdom_regional_coin_group_16: 3028,
        SMOLocationData.wooded_kingdom_regional_coin_group_17: 3032,
        SMOLocationData.wooded_kingdom_regional_coin_group_18: 3036,
        SMOLocationData.wooded_kingdom_regional_coin_group_19: 3039,
        SMOLocationData.wooded_kingdom_regional_coin_group_20: 3044,
        SMOLocationData.wooded_kingdom_regional_coin_group_21: 3047,
        SMOLocationData.wooded_kingdom_regional_coin_group_22: 3051,
        SMOLocationData.wooded_kingdom_regional_coin_group_23: 3055,
        SMOLocationData.wooded_kingdom_regional_coin_group_24: 3059,
}

sky_garden_tower_regional_groups = {
        SMOLocationData.sky_garden_tower_regional_coin_group_1: 3063,
}

flooded_pipes_regional_groups = {
        SMOLocationData.flooded_pipes_regional_coin_group_1: 3067,
}

deep_woods_regional_groups = {
        SMOLocationData.deep_woods_regional_coin_group_1: 3071,
        SMOLocationData.deep_woods_regional_coin_group_2: 3075,
        SMOLocationData.deep_woods_regional_coin_group_3: 3079,
}

walking_on_clouds_regional_groups = {
        SMOLocationData.walking_on_clouds_regional_coin_group_1: 3083,
}

wooded_flower_road_regional_groups = {
        SMOLocationData.wooded_flower_road_regional_coin_group_1: 3087,
}

sherm_elevator_regional_groups = {
        SMOLocationData.sherm_elevator_regional_coin_group_1: 3091,
}

wooded_kingdom_regional_coins = {
        SMOLocationData.wooded_kingdom_regional_coin_1: 2964,
        SMOLocationData.wooded_kingdom_regional_coin_2: 2965,
        SMOLocationData.wooded_kingdom_regional_coin_3: 2966,
        SMOLocationData.wooded_kingdom_regional_coin_4: 2968,
        SMOLocationData.wooded_kingdom_regional_coin_5: 2969,
        SMOLocationData.wooded_kingdom_regional_coin_6: 2970,
        SMOLocationData.wooded_kingdom_regional_coin_7: 2972,
        SMOLocationData.wooded_kingdom_regional_coin_8: 2973,
        SMOLocationData.wooded_kingdom_regional_coin_9: 2974,
        SMOLocationData.wooded_kingdom_regional_coin_10: 2976,
        SMOLocationData.wooded_kingdom_regional_coin_11: 2977,
        SMOLocationData.wooded_kingdom_regional_coin_12: 2979,
        SMOLocationData.wooded_kingdom_regional_coin_13: 2980,
        SMOLocationData.wooded_kingdom_regional_coin_14: 2981,
        SMOLocationData.wooded_kingdom_regional_coin_15: 2982,
        SMOLocationData.wooded_kingdom_regional_coin_16: 2984,
        SMOLocationData.wooded_kingdom_regional_coin_17: 2985,
        SMOLocationData.wooded_kingdom_regional_coin_18: 2986,
        SMOLocationData.wooded_kingdom_regional_coin_19: 2987,
        SMOLocationData.wooded_kingdom_regional_coin_20: 2989,
        SMOLocationData.wooded_kingdom_regional_coin_21: 2990,
        SMOLocationData.wooded_kingdom_regional_coin_22: 2991,
        SMOLocationData.wooded_kingdom_regional_coin_23: 2993,
        SMOLocationData.wooded_kingdom_regional_coin_24: 2994,
        SMOLocationData.wooded_kingdom_regional_coin_25: 2995,
        SMOLocationData.wooded_kingdom_regional_coin_26: 2997,
        SMOLocationData.wooded_kingdom_regional_coin_27: 2998,
        SMOLocationData.wooded_kingdom_regional_coin_28: 2999,
        SMOLocationData.wooded_kingdom_regional_coin_29: 3000,
        SMOLocationData.wooded_kingdom_regional_coin_30: 3002,
        SMOLocationData.wooded_kingdom_regional_coin_31: 3003,
        SMOLocationData.wooded_kingdom_regional_coin_32: 3004,
        SMOLocationData.wooded_kingdom_regional_coin_33: 3005,
        SMOLocationData.wooded_kingdom_regional_coin_34: 3007,
        SMOLocationData.wooded_kingdom_regional_coin_35: 3008,
        SMOLocationData.wooded_kingdom_regional_coin_36: 3009,
        SMOLocationData.wooded_kingdom_regional_coin_37: 3010,
        SMOLocationData.wooded_kingdom_regional_coin_38: 3012,
        SMOLocationData.wooded_kingdom_regional_coin_39: 3013,
        SMOLocationData.wooded_kingdom_regional_coin_40: 3014,
        SMOLocationData.wooded_kingdom_regional_coin_41: 3016,
        SMOLocationData.wooded_kingdom_regional_coin_42: 3017,
        SMOLocationData.wooded_kingdom_regional_coin_43: 3018,
        SMOLocationData.wooded_kingdom_regional_coin_44: 3020,
        SMOLocationData.wooded_kingdom_regional_coin_45: 3021,
        SMOLocationData.wooded_kingdom_regional_coin_46: 3022,
        SMOLocationData.wooded_kingdom_regional_coin_47: 3023,
        SMOLocationData.wooded_kingdom_regional_coin_48: 3025,
        SMOLocationData.wooded_kingdom_regional_coin_49: 3026,
        SMOLocationData.wooded_kingdom_regional_coin_50: 3027,
        SMOLocationData.wooded_kingdom_regional_coin_51: 3029,
        SMOLocationData.wooded_kingdom_regional_coin_52: 3030,
        SMOLocationData.wooded_kingdom_regional_coin_53: 3031,
        SMOLocationData.wooded_kingdom_regional_coin_54: 3033,
        SMOLocationData.wooded_kingdom_regional_coin_55: 3034,
        SMOLocationData.wooded_kingdom_regional_coin_56: 3035,
        SMOLocationData.wooded_kingdom_regional_coin_57: 3037,
        SMOLocationData.wooded_kingdom_regional_coin_58: 3038,
        SMOLocationData.wooded_kingdom_regional_coin_59: 3040,
        SMOLocationData.wooded_kingdom_regional_coin_60: 3041,
        SMOLocationData.wooded_kingdom_regional_coin_61: 3042,
        SMOLocationData.wooded_kingdom_regional_coin_62: 3043,
        SMOLocationData.wooded_kingdom_regional_coin_63: 3045,
        SMOLocationData.wooded_kingdom_regional_coin_64: 3046,
        SMOLocationData.wooded_kingdom_regional_coin_65: 3048,
        SMOLocationData.wooded_kingdom_regional_coin_66: 3049,
        SMOLocationData.wooded_kingdom_regional_coin_67: 3050,
        SMOLocationData.wooded_kingdom_regional_coin_68: 3052,
        SMOLocationData.wooded_kingdom_regional_coin_69: 3053,
        SMOLocationData.wooded_kingdom_regional_coin_70: 3054,
        SMOLocationData.wooded_kingdom_regional_coin_71: 3056,
        SMOLocationData.wooded_kingdom_regional_coin_72: 3057,
        SMOLocationData.wooded_kingdom_regional_coin_73: 3058,
        SMOLocationData.wooded_kingdom_regional_coin_74: 3060,
        SMOLocationData.wooded_kingdom_regional_coin_75: 3061,
        SMOLocationData.wooded_kingdom_regional_coin_76: 3062,
}

sky_garden_tower_regional_coins = {
        SMOLocationData.sky_garden_tower_regional_coin_1: 3064,
        SMOLocationData.sky_garden_tower_regional_coin_2: 3065,
        SMOLocationData.sky_garden_tower_regional_coin_3: 3066,
}

flooded_pipes_regional_coins = {
        SMOLocationData.flooded_pipes_regional_coin_1: 3068,
        SMOLocationData.flooded_pipes_regional_coin_2: 3069,
        SMOLocationData.flooded_pipes_regional_coin_3: 3070,
}

deep_woods_regional_coins = {
        SMOLocationData.deep_woods_regional_coin_1: 3072,
        SMOLocationData.deep_woods_regional_coin_2: 3073,
        SMOLocationData.deep_woods_regional_coin_3: 3074,
        SMOLocationData.deep_woods_regional_coin_4: 3076,
        SMOLocationData.deep_woods_regional_coin_5: 3077,
        SMOLocationData.deep_woods_regional_coin_6: 3078,
        SMOLocationData.deep_woods_regional_coin_7: 3080,
        SMOLocationData.deep_woods_regional_coin_8: 3081,
        SMOLocationData.deep_woods_regional_coin_9: 3082,
}

walking_on_clouds_regional_coins = {
        SMOLocationData.walking_on_clouds_regional_coin_1: 3084,
        SMOLocationData.walking_on_clouds_regional_coin_2: 3085,
        SMOLocationData.walking_on_clouds_regional_coin_3: 3086,
}

wooded_flower_road_regional_coins = {
        SMOLocationData.wooded_flower_road_regional_coin_1: 3088,
        SMOLocationData.wooded_flower_road_regional_coin_2: 3089,
        SMOLocationData.wooded_flower_road_regional_coin_3: 3090,
}

sherm_elevator_regional_coins = {
        SMOLocationData.sherm_elevator_regional_coin_1: 3092,
        SMOLocationData.sherm_elevator_regional_coin_2: 3093,
        SMOLocationData.sherm_elevator_regional_coin_3: 3094,
}

lake_kingdom_regional_groups = {
        SMOLocationData.lake_kingdom_regional_coin_group_1: 3095,
        SMOLocationData.lake_kingdom_regional_coin_group_2: 3100,
        SMOLocationData.lake_kingdom_regional_coin_group_3: 3104,
        SMOLocationData.lake_kingdom_regional_coin_group_4: 3109,
        SMOLocationData.lake_kingdom_regional_coin_group_5: 3113,
        SMOLocationData.lake_kingdom_regional_coin_group_6: 3117,
        SMOLocationData.lake_kingdom_regional_coin_group_7: 3121,
        SMOLocationData.lake_kingdom_regional_coin_group_8: 3125,
        SMOLocationData.lake_kingdom_regional_coin_group_9: 3130,
        SMOLocationData.lake_kingdom_regional_coin_group_10: 3135,
        SMOLocationData.lake_kingdom_regional_coin_group_11: 3139,
        SMOLocationData.lake_kingdom_regional_coin_group_12: 3144,
        SMOLocationData.lake_kingdom_regional_coin_group_13: 3148,
        SMOLocationData.lake_kingdom_regional_coin_group_14: 3152,
}

bouncy_flowers_regional_groups = {
        SMOLocationData.bouncy_flowers_regional_coin_group_1: 3156,
}

lake_kingdom_regional_coins = {
        SMOLocationData.lake_kingdom_regional_coin_1: 3096,
        SMOLocationData.lake_kingdom_regional_coin_2: 3097,
        SMOLocationData.lake_kingdom_regional_coin_3: 3098,
        SMOLocationData.lake_kingdom_regional_coin_4: 3099,
        SMOLocationData.lake_kingdom_regional_coin_5: 3101,
        SMOLocationData.lake_kingdom_regional_coin_6: 3102,
        SMOLocationData.lake_kingdom_regional_coin_7: 3103,
        SMOLocationData.lake_kingdom_regional_coin_8: 3105,
        SMOLocationData.lake_kingdom_regional_coin_9: 3106,
        SMOLocationData.lake_kingdom_regional_coin_10: 3107,
        SMOLocationData.lake_kingdom_regional_coin_11: 3108,
        SMOLocationData.lake_kingdom_regional_coin_12: 3110,
        SMOLocationData.lake_kingdom_regional_coin_13: 3111,
        SMOLocationData.lake_kingdom_regional_coin_14: 3112,
        SMOLocationData.lake_kingdom_regional_coin_15: 3114,
        SMOLocationData.lake_kingdom_regional_coin_16: 3115,
        SMOLocationData.lake_kingdom_regional_coin_17: 3116,
        SMOLocationData.lake_kingdom_regional_coin_18: 3118,
        SMOLocationData.lake_kingdom_regional_coin_19: 3119,
        SMOLocationData.lake_kingdom_regional_coin_20: 3120,
        SMOLocationData.lake_kingdom_regional_coin_21: 3122,
        SMOLocationData.lake_kingdom_regional_coin_22: 3123,
        SMOLocationData.lake_kingdom_regional_coin_23: 3124,
        SMOLocationData.lake_kingdom_regional_coin_24: 3126,
        SMOLocationData.lake_kingdom_regional_coin_25: 3127,
        SMOLocationData.lake_kingdom_regional_coin_26: 3128,
        SMOLocationData.lake_kingdom_regional_coin_27: 3129,
        SMOLocationData.lake_kingdom_regional_coin_28: 3131,
        SMOLocationData.lake_kingdom_regional_coin_29: 3132,
        SMOLocationData.lake_kingdom_regional_coin_30: 3133,
        SMOLocationData.lake_kingdom_regional_coin_31: 3134,
        SMOLocationData.lake_kingdom_regional_coin_32: 3136,
        SMOLocationData.lake_kingdom_regional_coin_33: 3137,
        SMOLocationData.lake_kingdom_regional_coin_34: 3138,
        SMOLocationData.lake_kingdom_regional_coin_35: 3140,
        SMOLocationData.lake_kingdom_regional_coin_36: 3141,
        SMOLocationData.lake_kingdom_regional_coin_37: 3142,
        SMOLocationData.lake_kingdom_regional_coin_38: 3143,
        SMOLocationData.lake_kingdom_regional_coin_39: 3145,
        SMOLocationData.lake_kingdom_regional_coin_40: 3146,
        SMOLocationData.lake_kingdom_regional_coin_41: 3147,
        SMOLocationData.lake_kingdom_regional_coin_42: 3149,
        SMOLocationData.lake_kingdom_regional_coin_43: 3150,
        SMOLocationData.lake_kingdom_regional_coin_44: 3151,
        SMOLocationData.lake_kingdom_regional_coin_45: 3153,
        SMOLocationData.lake_kingdom_regional_coin_46: 3154,
        SMOLocationData.lake_kingdom_regional_coin_47: 3155,
}

bouncy_flowers_regional_coins = {
        SMOLocationData.bouncy_flowers_regional_coin_1: 3157,
        SMOLocationData.bouncy_flowers_regional_coin_2: 3158,
        SMOLocationData.bouncy_flowers_regional_coin_3: 3159,
}

lost_kingdom_regional_groups = {
        SMOLocationData.lost_kingdom_regional_coin_group_1: 3160,
        SMOLocationData.lost_kingdom_regional_coin_group_2: 3164,
        SMOLocationData.lost_kingdom_regional_coin_group_3: 3169,
        SMOLocationData.lost_kingdom_regional_coin_group_4: 3173,
        SMOLocationData.lost_kingdom_regional_coin_group_5: 3177,
        SMOLocationData.lost_kingdom_regional_coin_group_6: 3180,
        SMOLocationData.lost_kingdom_regional_coin_group_7: 3185,
        SMOLocationData.lost_kingdom_regional_coin_group_8: 3189,
        SMOLocationData.lost_kingdom_regional_coin_group_9: 3194,
        SMOLocationData.lost_kingdom_regional_coin_group_10: 3197,
        SMOLocationData.lost_kingdom_regional_coin_group_11: 3200,
        SMOLocationData.lost_kingdom_regional_coin_group_12: 3203,
        SMOLocationData.lost_kingdom_regional_coin_group_13: 3206,
        SMOLocationData.lost_kingdom_regional_coin_group_14: 3210,
        SMOLocationData.lost_kingdom_regional_coin_group_15: 3213,
        SMOLocationData.lost_kingdom_regional_coin_group_16: 3216,
        SMOLocationData.lost_kingdom_regional_coin_group_17: 3220,
        SMOLocationData.lost_kingdom_regional_coin_group_18: 3224,
}

lost_kingdom_regional_coins = {
        SMOLocationData.lost_kingdom_regional_coin_1: 3161,
        SMOLocationData.lost_kingdom_regional_coin_2: 3162,
        SMOLocationData.lost_kingdom_regional_coin_3: 3163,
        SMOLocationData.lost_kingdom_regional_coin_4: 3165,
        SMOLocationData.lost_kingdom_regional_coin_5: 3166,
        SMOLocationData.lost_kingdom_regional_coin_6: 3167,
        SMOLocationData.lost_kingdom_regional_coin_7: 3168,
        SMOLocationData.lost_kingdom_regional_coin_8: 3170,
        SMOLocationData.lost_kingdom_regional_coin_9: 3171,
        SMOLocationData.lost_kingdom_regional_coin_10: 3172,
        SMOLocationData.lost_kingdom_regional_coin_11: 3174,
        SMOLocationData.lost_kingdom_regional_coin_12: 3175,
        SMOLocationData.lost_kingdom_regional_coin_13: 3176,
        SMOLocationData.lost_kingdom_regional_coin_14: 3178,
        SMOLocationData.lost_kingdom_regional_coin_15: 3179,
        SMOLocationData.lost_kingdom_regional_coin_16: 3181,
        SMOLocationData.lost_kingdom_regional_coin_17: 3182,
        SMOLocationData.lost_kingdom_regional_coin_18: 3183,
        SMOLocationData.lost_kingdom_regional_coin_19: 3184,
        SMOLocationData.lost_kingdom_regional_coin_20: 3186,
        SMOLocationData.lost_kingdom_regional_coin_21: 3187,
        SMOLocationData.lost_kingdom_regional_coin_22: 3188,
        SMOLocationData.lost_kingdom_regional_coin_23: 3190,
        SMOLocationData.lost_kingdom_regional_coin_24: 3191,
        SMOLocationData.lost_kingdom_regional_coin_25: 3192,
        SMOLocationData.lost_kingdom_regional_coin_26: 3193,
        SMOLocationData.lost_kingdom_regional_coin_27: 3195,
        SMOLocationData.lost_kingdom_regional_coin_28: 3196,
        SMOLocationData.lost_kingdom_regional_coin_29: 3198,
        SMOLocationData.lost_kingdom_regional_coin_30: 3199,
        SMOLocationData.lost_kingdom_regional_coin_31: 3201,
        SMOLocationData.lost_kingdom_regional_coin_32: 3202,
        SMOLocationData.lost_kingdom_regional_coin_33: 3204,
        SMOLocationData.lost_kingdom_regional_coin_34: 3205,
        SMOLocationData.lost_kingdom_regional_coin_35: 3207,
        SMOLocationData.lost_kingdom_regional_coin_36: 3208,
        SMOLocationData.lost_kingdom_regional_coin_37: 3209,
        SMOLocationData.lost_kingdom_regional_coin_38: 3211,
        SMOLocationData.lost_kingdom_regional_coin_39: 3212,
        SMOLocationData.lost_kingdom_regional_coin_40: 3214,
        SMOLocationData.lost_kingdom_regional_coin_41: 3215,
        SMOLocationData.lost_kingdom_regional_coin_42: 3217,
        SMOLocationData.lost_kingdom_regional_coin_43: 3218,
        SMOLocationData.lost_kingdom_regional_coin_44: 3219,
        SMOLocationData.lost_kingdom_regional_coin_45: 3221,
        SMOLocationData.lost_kingdom_regional_coin_46: 3222,
        SMOLocationData.lost_kingdom_regional_coin_47: 3223,
        SMOLocationData.lost_kingdom_regional_coin_48: 3225,
        SMOLocationData.lost_kingdom_regional_coin_49: 3226,
        SMOLocationData.lost_kingdom_regional_coin_50: 3227,
}

metro_kingdom_regional_groups = {
        SMOLocationData.metro_kingdom_regional_coin_group_1: 3228,
        SMOLocationData.metro_kingdom_regional_coin_group_2: 3232,
        SMOLocationData.metro_kingdom_regional_coin_group_3: 3236,
        SMOLocationData.metro_kingdom_regional_coin_group_4: 3240,
        SMOLocationData.metro_kingdom_regional_coin_group_5: 3244,
        SMOLocationData.metro_kingdom_regional_coin_group_6: 3248,
        SMOLocationData.metro_kingdom_regional_coin_group_7: 3251,
        SMOLocationData.metro_kingdom_regional_coin_group_8: 3255,
        SMOLocationData.metro_kingdom_regional_coin_group_9: 3259,
        SMOLocationData.metro_kingdom_regional_coin_group_10: 3263,
        SMOLocationData.metro_kingdom_regional_coin_group_11: 3267,
        SMOLocationData.metro_kingdom_regional_coin_group_12: 3271,
        SMOLocationData.metro_kingdom_regional_coin_group_13: 3274,
        SMOLocationData.metro_kingdom_regional_coin_group_14: 3278,
        SMOLocationData.metro_kingdom_regional_coin_group_15: 3281,
        SMOLocationData.metro_kingdom_regional_coin_group_16: 3285,
        SMOLocationData.metro_kingdom_regional_coin_group_17: 3289,
        SMOLocationData.metro_kingdom_regional_coin_group_18: 3293,
        SMOLocationData.metro_kingdom_regional_coin_group_19: 3296,
        SMOLocationData.metro_kingdom_regional_coin_group_20: 3301,
        SMOLocationData.metro_kingdom_regional_coin_group_21: 3305,
        SMOLocationData.metro_kingdom_regional_coin_group_22: 3309,
        SMOLocationData.metro_kingdom_regional_coin_group_23: 3312,
        SMOLocationData.metro_kingdom_regional_coin_group_24: 3316,
        SMOLocationData.metro_kingdom_regional_coin_group_25: 3319,
        SMOLocationData.metro_kingdom_regional_coin_group_26: 3322,
}

sewers_regional_groups = {
        SMOLocationData.sewers_regional_coin_group_1: 3325,
        SMOLocationData.sewers_regional_coin_group_2: 3329,
}

city_hall_regional_groups = {
        SMOLocationData.city_hall_regional_coin_group_1: 3334,
        SMOLocationData.city_hall_regional_coin_group_2: 3338,
        SMOLocationData.city_hall_regional_coin_group_3: 3341,
        SMOLocationData.city_hall_regional_coin_group_4: 3345,
}

bullet_billding_regional_groups = {
        SMOLocationData.bullet_billding_regional_coin_group_1: 3348,
}

high_rise_regional_groups = {
        SMOLocationData.high_rise_regional_coin_group_1: 3352,
}

trex_escape_regional_groups = {
        SMOLocationData.trex_escape_regional_coin_group_1: 3356,
        SMOLocationData.trex_escape_regional_coin_group_2: 3360,
}

metro_kingdom_regional_coins = {
        SMOLocationData.metro_kingdom_regional_coin_1: 3229,
        SMOLocationData.metro_kingdom_regional_coin_2: 3230,
        SMOLocationData.metro_kingdom_regional_coin_3: 3231,
        SMOLocationData.metro_kingdom_regional_coin_4: 3233,
        SMOLocationData.metro_kingdom_regional_coin_5: 3234,
        SMOLocationData.metro_kingdom_regional_coin_6: 3235,
        SMOLocationData.metro_kingdom_regional_coin_7: 3237,
        SMOLocationData.metro_kingdom_regional_coin_8: 3238,
        SMOLocationData.metro_kingdom_regional_coin_9: 3239,
        SMOLocationData.metro_kingdom_regional_coin_10: 3241,
        SMOLocationData.metro_kingdom_regional_coin_11: 3242,
        SMOLocationData.metro_kingdom_regional_coin_12: 3243,
        SMOLocationData.metro_kingdom_regional_coin_13: 3245,
        SMOLocationData.metro_kingdom_regional_coin_14: 3246,
        SMOLocationData.metro_kingdom_regional_coin_15: 3247,
        SMOLocationData.metro_kingdom_regional_coin_16: 3249,
        SMOLocationData.metro_kingdom_regional_coin_17: 3250,
        SMOLocationData.metro_kingdom_regional_coin_18: 3252,
        SMOLocationData.metro_kingdom_regional_coin_19: 3253,
        SMOLocationData.metro_kingdom_regional_coin_20: 3254,
        SMOLocationData.metro_kingdom_regional_coin_21: 3256,
        SMOLocationData.metro_kingdom_regional_coin_22: 3257,
        SMOLocationData.metro_kingdom_regional_coin_23: 3258,
        SMOLocationData.metro_kingdom_regional_coin_24: 3260,
        SMOLocationData.metro_kingdom_regional_coin_25: 3261,
        SMOLocationData.metro_kingdom_regional_coin_26: 3262,
        SMOLocationData.metro_kingdom_regional_coin_27: 3264,
        SMOLocationData.metro_kingdom_regional_coin_28: 3265,
        SMOLocationData.metro_kingdom_regional_coin_29: 3266,
        SMOLocationData.metro_kingdom_regional_coin_30: 3268,
        SMOLocationData.metro_kingdom_regional_coin_31: 3269,
        SMOLocationData.metro_kingdom_regional_coin_32: 3270,
        SMOLocationData.metro_kingdom_regional_coin_33: 3272,
        SMOLocationData.metro_kingdom_regional_coin_34: 3273,
        SMOLocationData.metro_kingdom_regional_coin_35: 3275,
        SMOLocationData.metro_kingdom_regional_coin_36: 3276,
        SMOLocationData.metro_kingdom_regional_coin_37: 3277,
        SMOLocationData.metro_kingdom_regional_coin_38: 3279,
        SMOLocationData.metro_kingdom_regional_coin_39: 3280,
        SMOLocationData.metro_kingdom_regional_coin_40: 3282,
        SMOLocationData.metro_kingdom_regional_coin_41: 3283,
        SMOLocationData.metro_kingdom_regional_coin_42: 3284,
        SMOLocationData.metro_kingdom_regional_coin_43: 3286,
        SMOLocationData.metro_kingdom_regional_coin_44: 3287,
        SMOLocationData.metro_kingdom_regional_coin_45: 3288,
        SMOLocationData.metro_kingdom_regional_coin_46: 3290,
        SMOLocationData.metro_kingdom_regional_coin_47: 3291,
        SMOLocationData.metro_kingdom_regional_coin_48: 3292,
        SMOLocationData.metro_kingdom_regional_coin_49: 3294,
        SMOLocationData.metro_kingdom_regional_coin_50: 3295,
        SMOLocationData.metro_kingdom_regional_coin_51: 3297,
        SMOLocationData.metro_kingdom_regional_coin_52: 3298,
        SMOLocationData.metro_kingdom_regional_coin_53: 3299,
        SMOLocationData.metro_kingdom_regional_coin_54: 3300,
        SMOLocationData.metro_kingdom_regional_coin_55: 3302,
        SMOLocationData.metro_kingdom_regional_coin_56: 3303,
        SMOLocationData.metro_kingdom_regional_coin_57: 3304,
        SMOLocationData.metro_kingdom_regional_coin_58: 3306,
        SMOLocationData.metro_kingdom_regional_coin_59: 3307,
        SMOLocationData.metro_kingdom_regional_coin_60: 3308,
        SMOLocationData.metro_kingdom_regional_coin_61: 3310,
        SMOLocationData.metro_kingdom_regional_coin_62: 3311,
        SMOLocationData.metro_kingdom_regional_coin_63: 3313,
        SMOLocationData.metro_kingdom_regional_coin_64: 3314,
        SMOLocationData.metro_kingdom_regional_coin_65: 3315,
        SMOLocationData.metro_kingdom_regional_coin_66: 3317,
        SMOLocationData.metro_kingdom_regional_coin_67: 3318,
        SMOLocationData.metro_kingdom_regional_coin_68: 3320,
        SMOLocationData.metro_kingdom_regional_coin_69: 3321,
        SMOLocationData.metro_kingdom_regional_coin_70: 3323,
        SMOLocationData.metro_kingdom_regional_coin_71: 3324,
}

sewers_regional_coins = {
        SMOLocationData.sewers_regional_coin_1: 3326,
        SMOLocationData.sewers_regional_coin_2: 3327,
        SMOLocationData.sewers_regional_coin_3: 3328,
        SMOLocationData.sewers_regional_coin_4: 3330,
        SMOLocationData.sewers_regional_coin_5: 3331,
        SMOLocationData.sewers_regional_coin_6: 3332,
        SMOLocationData.sewers_regional_coin_7: 3333,
}

city_hall_regional_coins = {
        SMOLocationData.city_hall_regional_coin_1: 3335,
        SMOLocationData.city_hall_regional_coin_2: 3336,
        SMOLocationData.city_hall_regional_coin_3: 3337,
        SMOLocationData.city_hall_regional_coin_4: 3339,
        SMOLocationData.city_hall_regional_coin_5: 3340,
        SMOLocationData.city_hall_regional_coin_6: 3342,
        SMOLocationData.city_hall_regional_coin_7: 3343,
        SMOLocationData.city_hall_regional_coin_8: 3344,
        SMOLocationData.city_hall_regional_coin_9: 3346,
        SMOLocationData.city_hall_regional_coin_10: 3347,
}

bullet_billding_regional_coins = {
        SMOLocationData.bullet_billding_regional_coin_1: 3349,
        SMOLocationData.bullet_billding_regional_coin_2: 3350,
        SMOLocationData.bullet_billding_regional_coin_3: 3351,
}

high_rise_regional_coins = {
        SMOLocationData.high_rise_regional_coin_1: 3353,
        SMOLocationData.high_rise_regional_coin_2: 3354,
        SMOLocationData.high_rise_regional_coin_3: 3355,
}

trex_escape_regional_coins = {
        SMOLocationData.trex_escape_regional_coin_1: 3357,
        SMOLocationData.trex_escape_regional_coin_2: 3358,
        SMOLocationData.trex_escape_regional_coin_3: 3359,
        SMOLocationData.trex_escape_regional_coin_4: 3361,
        SMOLocationData.trex_escape_regional_coin_5: 3362,
        SMOLocationData.trex_escape_regional_coin_6: 3363,
}

seaside_kingdom_regional_groups = {
        SMOLocationData.seaside_kingdom_regional_coin_group_1: 3364,
        SMOLocationData.seaside_kingdom_regional_coin_group_2: 3368,
        SMOLocationData.seaside_kingdom_regional_coin_group_3: 3372,
        SMOLocationData.seaside_kingdom_regional_coin_group_4: 3376,
        SMOLocationData.seaside_kingdom_regional_coin_group_5: 3380,
        SMOLocationData.seaside_kingdom_regional_coin_group_6: 3384,
        SMOLocationData.seaside_kingdom_regional_coin_group_7: 3388,
        SMOLocationData.seaside_kingdom_regional_coin_group_8: 3392,
        SMOLocationData.seaside_kingdom_regional_coin_group_9: 3396,
        SMOLocationData.seaside_kingdom_regional_coin_group_10: 3400,
        SMOLocationData.seaside_kingdom_regional_coin_group_11: 3405,
        SMOLocationData.seaside_kingdom_regional_coin_group_12: 3409,
        SMOLocationData.seaside_kingdom_regional_coin_group_13: 3413,
        SMOLocationData.seaside_kingdom_regional_coin_group_14: 3417,
        SMOLocationData.seaside_kingdom_regional_coin_group_15: 3421,
        SMOLocationData.seaside_kingdom_regional_coin_group_16: 3425,
        SMOLocationData.seaside_kingdom_regional_coin_group_17: 3429,
        SMOLocationData.seaside_kingdom_regional_coin_group_18: 3433,
        SMOLocationData.seaside_kingdom_regional_coin_group_19: 3437,
        SMOLocationData.seaside_kingdom_regional_coin_group_20: 3441,
        SMOLocationData.seaside_kingdom_regional_coin_group_21: 3445,
        SMOLocationData.seaside_kingdom_regional_coin_group_22: 3449,
        SMOLocationData.seaside_kingdom_regional_coin_group_23: 3453,
        SMOLocationData.seaside_kingdom_regional_coin_group_24: 3457,
        SMOLocationData.seaside_kingdom_regional_coin_group_25: 3461,
        SMOLocationData.seaside_kingdom_regional_coin_group_26: 3465,
        SMOLocationData.seaside_kingdom_regional_coin_group_27: 3469,
        SMOLocationData.seaside_kingdom_regional_coin_group_28: 3473,
        SMOLocationData.seaside_kingdom_regional_coin_group_29: 3477,
        SMOLocationData.seaside_kingdom_regional_coin_group_30: 3481,
        SMOLocationData.seaside_kingdom_regional_coin_group_31: 3485,
}

sea_cave_regional_groups = {
        SMOLocationData.sea_cave_regional_coin_group_1: 3489,
        SMOLocationData.sea_cave_regional_coin_group_2: 3493,
}

seaside_kingdom_regional_coins = {
        SMOLocationData.seaside_kingdom_regional_coin_1: 3365,
        SMOLocationData.seaside_kingdom_regional_coin_2: 3366,
        SMOLocationData.seaside_kingdom_regional_coin_3: 3367,
        SMOLocationData.seaside_kingdom_regional_coin_4: 3369,
        SMOLocationData.seaside_kingdom_regional_coin_5: 3370,
        SMOLocationData.seaside_kingdom_regional_coin_6: 3371,
        SMOLocationData.seaside_kingdom_regional_coin_7: 3373,
        SMOLocationData.seaside_kingdom_regional_coin_8: 3374,
        SMOLocationData.seaside_kingdom_regional_coin_9: 3375,
        SMOLocationData.seaside_kingdom_regional_coin_10: 3377,
        SMOLocationData.seaside_kingdom_regional_coin_11: 3378,
        SMOLocationData.seaside_kingdom_regional_coin_12: 3379,
        SMOLocationData.seaside_kingdom_regional_coin_13: 3381,
        SMOLocationData.seaside_kingdom_regional_coin_14: 3382,
        SMOLocationData.seaside_kingdom_regional_coin_15: 3383,
        SMOLocationData.seaside_kingdom_regional_coin_16: 3385,
        SMOLocationData.seaside_kingdom_regional_coin_17: 3386,
        SMOLocationData.seaside_kingdom_regional_coin_18: 3387,
        SMOLocationData.seaside_kingdom_regional_coin_19: 3389,
        SMOLocationData.seaside_kingdom_regional_coin_20: 3390,
        SMOLocationData.seaside_kingdom_regional_coin_21: 3391,
        SMOLocationData.seaside_kingdom_regional_coin_22: 3393,
        SMOLocationData.seaside_kingdom_regional_coin_23: 3394,
        SMOLocationData.seaside_kingdom_regional_coin_24: 3395,
        SMOLocationData.seaside_kingdom_regional_coin_25: 3397,
        SMOLocationData.seaside_kingdom_regional_coin_26: 3398,
        SMOLocationData.seaside_kingdom_regional_coin_27: 3399,
        SMOLocationData.seaside_kingdom_regional_coin_28: 3401,
        SMOLocationData.seaside_kingdom_regional_coin_29: 3402,
        SMOLocationData.seaside_kingdom_regional_coin_30: 3403,
        SMOLocationData.seaside_kingdom_regional_coin_31: 3404,
        SMOLocationData.seaside_kingdom_regional_coin_32: 3406,
        SMOLocationData.seaside_kingdom_regional_coin_33: 3407,
        SMOLocationData.seaside_kingdom_regional_coin_34: 3408,
        SMOLocationData.seaside_kingdom_regional_coin_35: 3410,
        SMOLocationData.seaside_kingdom_regional_coin_36: 3411,
        SMOLocationData.seaside_kingdom_regional_coin_37: 3412,
        SMOLocationData.seaside_kingdom_regional_coin_38: 3414,
        SMOLocationData.seaside_kingdom_regional_coin_39: 3415,
        SMOLocationData.seaside_kingdom_regional_coin_40: 3416,
        SMOLocationData.seaside_kingdom_regional_coin_41: 3418,
        SMOLocationData.seaside_kingdom_regional_coin_42: 3419,
        SMOLocationData.seaside_kingdom_regional_coin_43: 3420,
        SMOLocationData.seaside_kingdom_regional_coin_44: 3422,
        SMOLocationData.seaside_kingdom_regional_coin_45: 3423,
        SMOLocationData.seaside_kingdom_regional_coin_46: 3424,
        SMOLocationData.seaside_kingdom_regional_coin_47: 3426,
        SMOLocationData.seaside_kingdom_regional_coin_48: 3427,
        SMOLocationData.seaside_kingdom_regional_coin_49: 3428,
        SMOLocationData.seaside_kingdom_regional_coin_50: 3430,
        SMOLocationData.seaside_kingdom_regional_coin_51: 3431,
        SMOLocationData.seaside_kingdom_regional_coin_52: 3432,
        SMOLocationData.seaside_kingdom_regional_coin_53: 3434,
        SMOLocationData.seaside_kingdom_regional_coin_54: 3435,
        SMOLocationData.seaside_kingdom_regional_coin_55: 3436,
        SMOLocationData.seaside_kingdom_regional_coin_56: 3438,
        SMOLocationData.seaside_kingdom_regional_coin_57: 3439,
        SMOLocationData.seaside_kingdom_regional_coin_58: 3440,
        SMOLocationData.seaside_kingdom_regional_coin_59: 3442,
        SMOLocationData.seaside_kingdom_regional_coin_60: 3443,
        SMOLocationData.seaside_kingdom_regional_coin_61: 3444,
        SMOLocationData.seaside_kingdom_regional_coin_62: 3446,
        SMOLocationData.seaside_kingdom_regional_coin_63: 3447,
        SMOLocationData.seaside_kingdom_regional_coin_64: 3448,
        SMOLocationData.seaside_kingdom_regional_coin_65: 3450,
        SMOLocationData.seaside_kingdom_regional_coin_66: 3451,
        SMOLocationData.seaside_kingdom_regional_coin_67: 3452,
        SMOLocationData.seaside_kingdom_regional_coin_68: 3454,
        SMOLocationData.seaside_kingdom_regional_coin_69: 3455,
        SMOLocationData.seaside_kingdom_regional_coin_70: 3456,
        SMOLocationData.seaside_kingdom_regional_coin_71: 3458,
        SMOLocationData.seaside_kingdom_regional_coin_72: 3459,
        SMOLocationData.seaside_kingdom_regional_coin_73: 3460,
        SMOLocationData.seaside_kingdom_regional_coin_74: 3462,
        SMOLocationData.seaside_kingdom_regional_coin_75: 3463,
        SMOLocationData.seaside_kingdom_regional_coin_76: 3464,
        SMOLocationData.seaside_kingdom_regional_coin_77: 3466,
        SMOLocationData.seaside_kingdom_regional_coin_78: 3467,
        SMOLocationData.seaside_kingdom_regional_coin_79: 3468,
        SMOLocationData.seaside_kingdom_regional_coin_80: 3470,
        SMOLocationData.seaside_kingdom_regional_coin_81: 3471,
        SMOLocationData.seaside_kingdom_regional_coin_82: 3472,
        SMOLocationData.seaside_kingdom_regional_coin_83: 3474,
        SMOLocationData.seaside_kingdom_regional_coin_84: 3475,
        SMOLocationData.seaside_kingdom_regional_coin_85: 3476,
        SMOLocationData.seaside_kingdom_regional_coin_86: 3478,
        SMOLocationData.seaside_kingdom_regional_coin_87: 3479,
        SMOLocationData.seaside_kingdom_regional_coin_88: 3480,
        SMOLocationData.seaside_kingdom_regional_coin_89: 3482,
        SMOLocationData.seaside_kingdom_regional_coin_90: 3483,
        SMOLocationData.seaside_kingdom_regional_coin_91: 3484,
        SMOLocationData.seaside_kingdom_regional_coin_92: 3486,
        SMOLocationData.seaside_kingdom_regional_coin_93: 3487,
        SMOLocationData.seaside_kingdom_regional_coin_94: 3488,
}

sea_cave_regional_coins = {
        SMOLocationData.sea_cave_regional_coin_1: 3490,
        SMOLocationData.sea_cave_regional_coin_2: 3491,
        SMOLocationData.sea_cave_regional_coin_3: 3492,
        SMOLocationData.sea_cave_regional_coin_4: 3494,
        SMOLocationData.sea_cave_regional_coin_5: 3495,
        SMOLocationData.sea_cave_regional_coin_6: 3496,
}

snow_kingdom_regional_groups = {
        SMOLocationData.snow_kingdom_regional_coin_group_1: 3497,
        SMOLocationData.snow_kingdom_regional_coin_group_2: 3500,
        SMOLocationData.snow_kingdom_regional_coin_group_3: 3503,
        SMOLocationData.snow_kingdom_regional_coin_group_4: 3507,
        SMOLocationData.snow_kingdom_regional_coin_group_5: 3510,
        SMOLocationData.snow_kingdom_regional_coin_group_6: 3513,
}

shiveria_regional_groups = {
        SMOLocationData.shiveria_regional_coin_group_1: 3516,
        SMOLocationData.shiveria_regional_coin_group_2: 3521,
        SMOLocationData.shiveria_regional_coin_group_3: 3525,
        SMOLocationData.shiveria_regional_coin_group_4: 3529,
        SMOLocationData.shiveria_regional_coin_group_5: 3534,
        SMOLocationData.shiveria_regional_coin_group_6: 3538,
        SMOLocationData.shiveria_regional_coin_group_7: 3542,
        SMOLocationData.shiveria_regional_coin_group_8: 3546,
        SMOLocationData.shiveria_regional_coin_group_9: 3551,
}

snowline_regional_groups = {
        SMOLocationData.snowline_regional_coin_group_1: 3555,
        SMOLocationData.snowline_regional_coin_group_2: 3560,
}

snow_kingdom_regional_coins = {
        SMOLocationData.snow_kingdom_regional_coin_1: 3498,
        SMOLocationData.snow_kingdom_regional_coin_2: 3499,
        SMOLocationData.snow_kingdom_regional_coin_3: 3501,
        SMOLocationData.snow_kingdom_regional_coin_4: 3502,
        SMOLocationData.snow_kingdom_regional_coin_5: 3504,
        SMOLocationData.snow_kingdom_regional_coin_6: 3505,
        SMOLocationData.snow_kingdom_regional_coin_7: 3506,
        SMOLocationData.snow_kingdom_regional_coin_8: 3508,
        SMOLocationData.snow_kingdom_regional_coin_9: 3509,
        SMOLocationData.snow_kingdom_regional_coin_10: 3511,
        SMOLocationData.snow_kingdom_regional_coin_11: 3512,
        SMOLocationData.snow_kingdom_regional_coin_12: 3514,
        SMOLocationData.snow_kingdom_regional_coin_13: 3515,
}

shiveria_regional_coins = {
        SMOLocationData.shiveria_regional_coin_1: 3517,
        SMOLocationData.shiveria_regional_coin_2: 3518,
        SMOLocationData.shiveria_regional_coin_3: 3519,
        SMOLocationData.shiveria_regional_coin_4: 3520,
        SMOLocationData.shiveria_regional_coin_5: 3522,
        SMOLocationData.shiveria_regional_coin_6: 3523,
        SMOLocationData.shiveria_regional_coin_7: 3524,
        SMOLocationData.shiveria_regional_coin_8: 3526,
        SMOLocationData.shiveria_regional_coin_9: 3527,
        SMOLocationData.shiveria_regional_coin_10: 3528,
        SMOLocationData.shiveria_regional_coin_11: 3530,
        SMOLocationData.shiveria_regional_coin_12: 3531,
        SMOLocationData.shiveria_regional_coin_13: 3532,
        SMOLocationData.shiveria_regional_coin_14: 3533,
        SMOLocationData.shiveria_regional_coin_15: 3535,
        SMOLocationData.shiveria_regional_coin_16: 3536,
        SMOLocationData.shiveria_regional_coin_17: 3537,
        SMOLocationData.shiveria_regional_coin_18: 3539,
        SMOLocationData.shiveria_regional_coin_19: 3540,
        SMOLocationData.shiveria_regional_coin_20: 3541,
        SMOLocationData.shiveria_regional_coin_21: 3543,
        SMOLocationData.shiveria_regional_coin_22: 3544,
        SMOLocationData.shiveria_regional_coin_23: 3545,
        SMOLocationData.shiveria_regional_coin_24: 3547,
        SMOLocationData.shiveria_regional_coin_25: 3548,
        SMOLocationData.shiveria_regional_coin_26: 3549,
        SMOLocationData.shiveria_regional_coin_27: 3550,
        SMOLocationData.shiveria_regional_coin_28: 3552,
        SMOLocationData.shiveria_regional_coin_29: 3553,
        SMOLocationData.shiveria_regional_coin_30: 3554,

}

snowline_regional_coins = {
        SMOLocationData.snowline_regional_coin_1: 3556,
        SMOLocationData.snowline_regional_coin_2: 3557,
        SMOLocationData.snowline_regional_coin_3: 3558,
        SMOLocationData.snowline_regional_coin_4: 3559,
        SMOLocationData.snowline_regional_coin_5: 3561,
        SMOLocationData.snowline_regional_coin_6: 3562,
        SMOLocationData.snowline_regional_coin_7: 3563,
}

luncheon_kingdom_regional_groups = {
        SMOLocationData.luncheon_kingdom_regional_coin_group_1: 3564,
        SMOLocationData.luncheon_kingdom_regional_coin_group_2: 3568,
        SMOLocationData.luncheon_kingdom_regional_coin_group_3: 3572,
        SMOLocationData.luncheon_kingdom_regional_coin_group_4: 3576,
        SMOLocationData.luncheon_kingdom_regional_coin_group_5: 3580,
        SMOLocationData.luncheon_kingdom_regional_coin_group_6: 3584,
        SMOLocationData.luncheon_kingdom_regional_coin_group_7: 3588,
        SMOLocationData.luncheon_kingdom_regional_coin_group_8: 3591,
        SMOLocationData.luncheon_kingdom_regional_coin_group_9: 3599,
        SMOLocationData.luncheon_kingdom_regional_coin_group_10: 3603,
        SMOLocationData.luncheon_kingdom_regional_coin_group_11: 3607,
        SMOLocationData.luncheon_kingdom_regional_coin_group_12: 3613,
        SMOLocationData.luncheon_kingdom_regional_coin_group_13: 3617,
        SMOLocationData.luncheon_kingdom_regional_coin_group_14: 3622,
        SMOLocationData.luncheon_kingdom_regional_coin_group_15: 3626,
        SMOLocationData.luncheon_kingdom_regional_coin_group_16: 3630,
        SMOLocationData.luncheon_kingdom_regional_coin_group_17: 3634,
        SMOLocationData.luncheon_kingdom_regional_coin_group_18: 3638,
        SMOLocationData.luncheon_kingdom_regional_coin_group_19: 3642,
        SMOLocationData.luncheon_kingdom_regional_coin_group_20: 3646,
        SMOLocationData.luncheon_kingdom_regional_coin_group_21: 3650,
        SMOLocationData.luncheon_kingdom_regional_coin_group_22: 3655,
        SMOLocationData.luncheon_kingdom_regional_coin_group_23: 3659,
        SMOLocationData.luncheon_kingdom_regional_coin_group_24: 3663,
        SMOLocationData.luncheon_kingdom_regional_coin_group_25: 3667,
        SMOLocationData.luncheon_kingdom_regional_coin_group_26: 3671,
}

cascading_magma_regional_groups = {
        SMOLocationData.cascading_magma_regional_coin_group_1: 3675,
        SMOLocationData.cascading_magma_regional_coin_group_2: 3679,
}

magma_narrow_path_regional_groups = {
        SMOLocationData.magma_narrow_path_regional_coin_group_1: 3683,
}

spinning_athletics_regional_groups = {
        SMOLocationData.spinning_athletics_regional_coin_group_1: 3687,
}

fork_flickin_regional_groups = {
        SMOLocationData.fork_flickin_regional_coin_group_1: 3691,
}

luncheon_kingdom_regional_coins = {
        SMOLocationData.luncheon_kingdom_regional_coin_1: 3565,
        SMOLocationData.luncheon_kingdom_regional_coin_2: 3566,
        SMOLocationData.luncheon_kingdom_regional_coin_3: 3567,
        SMOLocationData.luncheon_kingdom_regional_coin_4: 3569,
        SMOLocationData.luncheon_kingdom_regional_coin_5: 3570,
        SMOLocationData.luncheon_kingdom_regional_coin_6: 3571,
        SMOLocationData.luncheon_kingdom_regional_coin_7: 3573,
        SMOLocationData.luncheon_kingdom_regional_coin_8: 3574,
        SMOLocationData.luncheon_kingdom_regional_coin_9: 3575,
        SMOLocationData.luncheon_kingdom_regional_coin_10: 3577,
        SMOLocationData.luncheon_kingdom_regional_coin_11: 3578,
        SMOLocationData.luncheon_kingdom_regional_coin_12: 3579,
        SMOLocationData.luncheon_kingdom_regional_coin_13: 3581,
        SMOLocationData.luncheon_kingdom_regional_coin_14: 3582,
        SMOLocationData.luncheon_kingdom_regional_coin_15: 3583,
        SMOLocationData.luncheon_kingdom_regional_coin_16: 3585,
        SMOLocationData.luncheon_kingdom_regional_coin_17: 3586,
        SMOLocationData.luncheon_kingdom_regional_coin_18: 3587,
        SMOLocationData.luncheon_kingdom_regional_coin_19: 3589,
        SMOLocationData.luncheon_kingdom_regional_coin_20: 3590,
        SMOLocationData.luncheon_kingdom_regional_coin_21: 3592,
        SMOLocationData.luncheon_kingdom_regional_coin_22: 3593,
        SMOLocationData.luncheon_kingdom_regional_coin_23: 3594,
        SMOLocationData.luncheon_kingdom_regional_coin_24: 3595,
        SMOLocationData.luncheon_kingdom_regional_coin_25: 3596,
        SMOLocationData.luncheon_kingdom_regional_coin_26: 3597,
        SMOLocationData.luncheon_kingdom_regional_coin_27: 3598,
        SMOLocationData.luncheon_kingdom_regional_coin_28: 3600,
        SMOLocationData.luncheon_kingdom_regional_coin_29: 3601,
        SMOLocationData.luncheon_kingdom_regional_coin_30: 3602,
        SMOLocationData.luncheon_kingdom_regional_coin_31: 3604,
        SMOLocationData.luncheon_kingdom_regional_coin_32: 3605,
        SMOLocationData.luncheon_kingdom_regional_coin_33: 3606,
        SMOLocationData.luncheon_kingdom_regional_coin_34: 3608,
        SMOLocationData.luncheon_kingdom_regional_coin_35: 3609,
        SMOLocationData.luncheon_kingdom_regional_coin_36: 3610,
        SMOLocationData.luncheon_kingdom_regional_coin_37: 3611,
        SMOLocationData.luncheon_kingdom_regional_coin_38: 3612,
        SMOLocationData.luncheon_kingdom_regional_coin_39: 3614,
        SMOLocationData.luncheon_kingdom_regional_coin_40: 3615,
        SMOLocationData.luncheon_kingdom_regional_coin_41: 3616,
        SMOLocationData.luncheon_kingdom_regional_coin_42: 3618,
        SMOLocationData.luncheon_kingdom_regional_coin_43: 3619,
        SMOLocationData.luncheon_kingdom_regional_coin_44: 3620,
        SMOLocationData.luncheon_kingdom_regional_coin_45: 3621,
        SMOLocationData.luncheon_kingdom_regional_coin_46: 3623,
        SMOLocationData.luncheon_kingdom_regional_coin_47: 3624,
        SMOLocationData.luncheon_kingdom_regional_coin_48: 3625,
        SMOLocationData.luncheon_kingdom_regional_coin_49: 3627,
        SMOLocationData.luncheon_kingdom_regional_coin_50: 3628,
        SMOLocationData.luncheon_kingdom_regional_coin_51: 3629,
        SMOLocationData.luncheon_kingdom_regional_coin_52: 3631,
        SMOLocationData.luncheon_kingdom_regional_coin_53: 3632,
        SMOLocationData.luncheon_kingdom_regional_coin_54: 3633,
        SMOLocationData.luncheon_kingdom_regional_coin_55: 3635,
        SMOLocationData.luncheon_kingdom_regional_coin_56: 3636,
        SMOLocationData.luncheon_kingdom_regional_coin_57: 3637,
        SMOLocationData.luncheon_kingdom_regional_coin_58: 3639,
        SMOLocationData.luncheon_kingdom_regional_coin_59: 3640,
        SMOLocationData.luncheon_kingdom_regional_coin_60: 3641,
        SMOLocationData.luncheon_kingdom_regional_coin_61: 3643,
        SMOLocationData.luncheon_kingdom_regional_coin_62: 3644,
        SMOLocationData.luncheon_kingdom_regional_coin_63: 3645,
        SMOLocationData.luncheon_kingdom_regional_coin_64: 3647,
        SMOLocationData.luncheon_kingdom_regional_coin_65: 3648,
        SMOLocationData.luncheon_kingdom_regional_coin_66: 3649,
        SMOLocationData.luncheon_kingdom_regional_coin_67: 3651,
        SMOLocationData.luncheon_kingdom_regional_coin_68: 3652,
        SMOLocationData.luncheon_kingdom_regional_coin_69: 3653,
        SMOLocationData.luncheon_kingdom_regional_coin_70: 3654,
        SMOLocationData.luncheon_kingdom_regional_coin_71: 3656,
        SMOLocationData.luncheon_kingdom_regional_coin_72: 3657,
        SMOLocationData.luncheon_kingdom_regional_coin_73: 3658,
        SMOLocationData.luncheon_kingdom_regional_coin_74: 3660,
        SMOLocationData.luncheon_kingdom_regional_coin_75: 3661,
        SMOLocationData.luncheon_kingdom_regional_coin_76: 3662,
        SMOLocationData.luncheon_kingdom_regional_coin_77: 3664,
        SMOLocationData.luncheon_kingdom_regional_coin_78: 3665,
        SMOLocationData.luncheon_kingdom_regional_coin_79: 3666,
        SMOLocationData.luncheon_kingdom_regional_coin_80: 3668,
        SMOLocationData.luncheon_kingdom_regional_coin_81: 3669,
        SMOLocationData.luncheon_kingdom_regional_coin_82: 3670,
        SMOLocationData.luncheon_kingdom_regional_coin_83: 3672,
        SMOLocationData.luncheon_kingdom_regional_coin_84: 3673,
        SMOLocationData.luncheon_kingdom_regional_coin_85: 3674,
}

cascading_magma_regional_coins = {
        SMOLocationData.cascading_magma_regional_coin_1: 3676,
        SMOLocationData.cascading_magma_regional_coin_2: 3677,
        SMOLocationData.cascading_magma_regional_coin_3: 3678,
        SMOLocationData.cascading_magma_regional_coin_4: 3680,
        SMOLocationData.cascading_magma_regional_coin_5: 3681,
        SMOLocationData.cascading_magma_regional_coin_6: 3682,
}

magma_narrow_path_regional_coins = {
        SMOLocationData.magma_narrow_path_regional_coin_1: 3684,
        SMOLocationData.magma_narrow_path_regional_coin_2: 3685,
        SMOLocationData.magma_narrow_path_regional_coin_3: 3686,
}

spinning_athletics_regional_coins = {
        SMOLocationData.spinning_athletics_regional_coin_1: 3688,
        SMOLocationData.spinning_athletics_regional_coin_2: 3689,
        SMOLocationData.spinning_athletics_regional_coin_3: 3690,
}

fork_flickin_regional_coins = {
        SMOLocationData.fork_flickin_regional_coin_1: 3692,
        SMOLocationData.fork_flickin_regional_coin_2: 3693,
        SMOLocationData.fork_flickin_regional_coin_3: 3694,
}

bowsers_kingdom_regional_groups = {
        SMOLocationData.bowsers_kingdom_regional_coin_group_1: 3695,
        SMOLocationData.bowsers_kingdom_regional_coin_group_2: 3699,
        SMOLocationData.bowsers_kingdom_regional_coin_group_3: 3703,
        SMOLocationData.bowsers_kingdom_regional_coin_group_4: 3707,
        SMOLocationData.bowsers_kingdom_regional_coin_group_5: 3711,
        SMOLocationData.bowsers_kingdom_regional_coin_group_6: 3715,
        SMOLocationData.bowsers_kingdom_regional_coin_group_7: 3720,
        SMOLocationData.bowsers_kingdom_regional_coin_group_8: 3724,
        SMOLocationData.bowsers_kingdom_regional_coin_group_9: 3728,
        SMOLocationData.bowsers_kingdom_regional_coin_group_10: 3732,
        SMOLocationData.bowsers_kingdom_regional_coin_group_11: 3736,
        SMOLocationData.bowsers_kingdom_regional_coin_group_12: 3740,
        SMOLocationData.bowsers_kingdom_regional_coin_group_20: 3772,
        SMOLocationData.bowsers_kingdom_regional_coin_group_21: 3777,
        SMOLocationData.bowsers_kingdom_regional_coin_group_22: 3782,
        SMOLocationData.bowsers_kingdom_regional_coin_group_23: 3786,
        SMOLocationData.bowsers_kingdom_regional_coin_group_24: 3791,
        SMOLocationData.bowsers_kingdom_regional_coin_group_25: 3794,
        SMOLocationData.bowsers_kingdom_regional_coin_group_26: 3797,
        SMOLocationData.bowsers_kingdom_regional_coin_group_27: 3801,
        SMOLocationData.bowsers_kingdom_regional_coin_group_28: 3805,
        SMOLocationData.bowsers_kingdom_regional_coin_group_29: 3809,
        SMOLocationData.bowsers_kingdom_regional_coin_group_30: 3813,
        SMOLocationData.bowsers_kingdom_regional_coin_group_31: 3818,
        SMOLocationData.bowsers_kingdom_regional_coin_group_32: 3822,
}

bowsers_kingdom_peace_regional_groups = {
        SMOLocationData.bowsers_kingdom_regional_coin_group_13: 3744,
        SMOLocationData.bowsers_kingdom_regional_coin_group_14: 3748,
        SMOLocationData.bowsers_kingdom_regional_coin_group_15: 3752,
        SMOLocationData.bowsers_kingdom_regional_coin_group_16: 3756,
        SMOLocationData.bowsers_kingdom_regional_coin_group_17: 3760,
        SMOLocationData.bowsers_kingdom_regional_coin_group_18: 3764,
        SMOLocationData.bowsers_kingdom_regional_coin_group_19: 3768,
}

bowsers_kingdom_regional_coins = {
        SMOLocationData.bowsers_kingdom_regional_coin_1: 3696,
        SMOLocationData.bowsers_kingdom_regional_coin_2: 3697,
        SMOLocationData.bowsers_kingdom_regional_coin_3: 3698,
        SMOLocationData.bowsers_kingdom_regional_coin_4: 3700,
        SMOLocationData.bowsers_kingdom_regional_coin_5: 3701,
        SMOLocationData.bowsers_kingdom_regional_coin_6: 3702,
        SMOLocationData.bowsers_kingdom_regional_coin_7: 3704,
        SMOLocationData.bowsers_kingdom_regional_coin_8: 3705,
        SMOLocationData.bowsers_kingdom_regional_coin_9: 3706,
        SMOLocationData.bowsers_kingdom_regional_coin_10: 3708,
        SMOLocationData.bowsers_kingdom_regional_coin_11: 3709,
        SMOLocationData.bowsers_kingdom_regional_coin_12: 3710,
        SMOLocationData.bowsers_kingdom_regional_coin_13: 3712,
        SMOLocationData.bowsers_kingdom_regional_coin_14: 3713,
        SMOLocationData.bowsers_kingdom_regional_coin_15: 3714,
        SMOLocationData.bowsers_kingdom_regional_coin_16: 3716,
        SMOLocationData.bowsers_kingdom_regional_coin_17: 3717,
        SMOLocationData.bowsers_kingdom_regional_coin_18: 3718,
        SMOLocationData.bowsers_kingdom_regional_coin_19: 3719,
        SMOLocationData.bowsers_kingdom_regional_coin_20: 3721,
        SMOLocationData.bowsers_kingdom_regional_coin_21: 3722,
        SMOLocationData.bowsers_kingdom_regional_coin_22: 3723,
        SMOLocationData.bowsers_kingdom_regional_coin_23: 3725,
        SMOLocationData.bowsers_kingdom_regional_coin_24: 3726,
        SMOLocationData.bowsers_kingdom_regional_coin_25: 3727,
        SMOLocationData.bowsers_kingdom_regional_coin_26: 3729,
        SMOLocationData.bowsers_kingdom_regional_coin_27: 3730,
        SMOLocationData.bowsers_kingdom_regional_coin_28: 3731,
        SMOLocationData.bowsers_kingdom_regional_coin_29: 3733,
        SMOLocationData.bowsers_kingdom_regional_coin_30: 3734,
        SMOLocationData.bowsers_kingdom_regional_coin_31: 3735,
        SMOLocationData.bowsers_kingdom_regional_coin_32: 3737,
        SMOLocationData.bowsers_kingdom_regional_coin_33: 3738,
        SMOLocationData.bowsers_kingdom_regional_coin_34: 3739,
        SMOLocationData.bowsers_kingdom_regional_coin_35: 3741,
        SMOLocationData.bowsers_kingdom_regional_coin_36: 3742,
        SMOLocationData.bowsers_kingdom_regional_coin_37: 3743,
        SMOLocationData.bowsers_kingdom_regional_coin_38: 3745,
        SMOLocationData.bowsers_kingdom_regional_coin_39: 3746,
        SMOLocationData.bowsers_kingdom_regional_coin_40: 3747,
        SMOLocationData.bowsers_kingdom_regional_coin_41: 3749,
        SMOLocationData.bowsers_kingdom_regional_coin_42: 3750,
        SMOLocationData.bowsers_kingdom_regional_coin_43: 3751,
        SMOLocationData.bowsers_kingdom_regional_coin_44: 3753,
        SMOLocationData.bowsers_kingdom_regional_coin_45: 3754,
        SMOLocationData.bowsers_kingdom_regional_coin_46: 3755,
        SMOLocationData.bowsers_kingdom_regional_coin_47: 3757,
        SMOLocationData.bowsers_kingdom_regional_coin_48: 3758,
        SMOLocationData.bowsers_kingdom_regional_coin_49: 3759,
        SMOLocationData.bowsers_kingdom_regional_coin_50: 3761,
        SMOLocationData.bowsers_kingdom_regional_coin_51: 3762,
        SMOLocationData.bowsers_kingdom_regional_coin_52: 3763,
        SMOLocationData.bowsers_kingdom_regional_coin_53: 3765,
        SMOLocationData.bowsers_kingdom_regional_coin_54: 3766,
        SMOLocationData.bowsers_kingdom_regional_coin_55: 3767,
        SMOLocationData.bowsers_kingdom_regional_coin_56: 3769,
        SMOLocationData.bowsers_kingdom_regional_coin_57: 3770,
        SMOLocationData.bowsers_kingdom_regional_coin_58: 3771,
        SMOLocationData.bowsers_kingdom_regional_coin_59: 3773,
        SMOLocationData.bowsers_kingdom_regional_coin_60: 3774,
        SMOLocationData.bowsers_kingdom_regional_coin_61: 3775,
        SMOLocationData.bowsers_kingdom_regional_coin_62: 3776,
        SMOLocationData.bowsers_kingdom_regional_coin_63: 3778,
        SMOLocationData.bowsers_kingdom_regional_coin_64: 3779,
        SMOLocationData.bowsers_kingdom_regional_coin_65: 3780,
        SMOLocationData.bowsers_kingdom_regional_coin_66: 3781,
        SMOLocationData.bowsers_kingdom_regional_coin_67: 3783,
        SMOLocationData.bowsers_kingdom_regional_coin_68: 3784,
        SMOLocationData.bowsers_kingdom_regional_coin_69: 3785,
        SMOLocationData.bowsers_kingdom_regional_coin_70: 3787,
        SMOLocationData.bowsers_kingdom_regional_coin_71: 3788,
        SMOLocationData.bowsers_kingdom_regional_coin_72: 3789,
        SMOLocationData.bowsers_kingdom_regional_coin_73: 3790,
        SMOLocationData.bowsers_kingdom_regional_coin_74: 3792,
        SMOLocationData.bowsers_kingdom_regional_coin_75: 3793,
        SMOLocationData.bowsers_kingdom_regional_coin_76: 3795,
        SMOLocationData.bowsers_kingdom_regional_coin_77: 3796,
        SMOLocationData.bowsers_kingdom_regional_coin_78: 3798,
        SMOLocationData.bowsers_kingdom_regional_coin_79: 3799,
        SMOLocationData.bowsers_kingdom_regional_coin_80: 3800,
        SMOLocationData.bowsers_kingdom_regional_coin_81: 3802,
        SMOLocationData.bowsers_kingdom_regional_coin_82: 3803,
        SMOLocationData.bowsers_kingdom_regional_coin_83: 3804,
        SMOLocationData.bowsers_kingdom_regional_coin_84: 3806,
        SMOLocationData.bowsers_kingdom_regional_coin_85: 3807,
        SMOLocationData.bowsers_kingdom_regional_coin_86: 3808,
        SMOLocationData.bowsers_kingdom_regional_coin_87: 3810,
        SMOLocationData.bowsers_kingdom_regional_coin_88: 3811,
        SMOLocationData.bowsers_kingdom_regional_coin_89: 3812,
        SMOLocationData.bowsers_kingdom_regional_coin_90: 3814,
        SMOLocationData.bowsers_kingdom_regional_coin_91: 3815,
        SMOLocationData.bowsers_kingdom_regional_coin_92: 3816,
        SMOLocationData.bowsers_kingdom_regional_coin_93: 3817,
        SMOLocationData.bowsers_kingdom_regional_coin_94: 3819,
        SMOLocationData.bowsers_kingdom_regional_coin_95: 3820,
        SMOLocationData.bowsers_kingdom_regional_coin_96: 3821,
        SMOLocationData.bowsers_kingdom_regional_coin_97: 3823,
        SMOLocationData.bowsers_kingdom_regional_coin_98: 3824,
        SMOLocationData.bowsers_kingdom_regional_coin_99: 3825,
        SMOLocationData.bowsers_kingdom_regional_coin_100: 3826,
}

moon_kingdom_regional_groups = {
        SMOLocationData.moon_kingdom_regional_coin_group_1: 3827,
        SMOLocationData.moon_kingdom_regional_coin_group_2: 3831,
        SMOLocationData.moon_kingdom_regional_coin_group_3: 3836,
        SMOLocationData.moon_kingdom_regional_coin_group_4: 3843,
        SMOLocationData.moon_kingdom_regional_coin_group_5: 3847,
        SMOLocationData.moon_kingdom_regional_coin_group_6: 3852,
        SMOLocationData.moon_kingdom_regional_coin_group_7: 3856,
        SMOLocationData.moon_kingdom_regional_coin_group_8: 3860,
        SMOLocationData.moon_kingdom_regional_coin_group_9: 3864,
}

moon_cave_regional_groups = {
        SMOLocationData.moon_cave_regional_coin_group_1: 3868,
        SMOLocationData.moon_cave_regional_coin_group_2: 3872,
        SMOLocationData.moon_cave_regional_coin_group_3: 3876,
        SMOLocationData.moon_cave_regional_coin_group_4: 3880,
        SMOLocationData.moon_cave_regional_coin_group_5: 3884,
        SMOLocationData.moon_cave_regional_coin_group_6: 3888,
}

moon_kingdom_regional_coins = {
        SMOLocationData.moon_kingdom_regional_coin_1: 3828,
        SMOLocationData.moon_kingdom_regional_coin_2: 3829,
        SMOLocationData.moon_kingdom_regional_coin_3: 3830,
        SMOLocationData.moon_kingdom_regional_coin_4: 3832,
        SMOLocationData.moon_kingdom_regional_coin_5: 3833,
        SMOLocationData.moon_kingdom_regional_coin_6: 3834,
        SMOLocationData.moon_kingdom_regional_coin_7: 3835,
        SMOLocationData.moon_kingdom_regional_coin_8: 3837,
        SMOLocationData.moon_kingdom_regional_coin_9: 3838,
        SMOLocationData.moon_kingdom_regional_coin_10: 3839,
        SMOLocationData.moon_kingdom_regional_coin_11: 3840,
        SMOLocationData.moon_kingdom_regional_coin_12: 3841,
        SMOLocationData.moon_kingdom_regional_coin_13: 3842,
        SMOLocationData.moon_kingdom_regional_coin_14: 3844,
        SMOLocationData.moon_kingdom_regional_coin_15: 3845,
        SMOLocationData.moon_kingdom_regional_coin_16: 3846,
        SMOLocationData.moon_kingdom_regional_coin_17: 3848,
        SMOLocationData.moon_kingdom_regional_coin_18: 3849,
        SMOLocationData.moon_kingdom_regional_coin_19: 3850,
        SMOLocationData.moon_kingdom_regional_coin_20: 3851,
        SMOLocationData.moon_kingdom_regional_coin_21: 3853,
        SMOLocationData.moon_kingdom_regional_coin_22: 3854,
        SMOLocationData.moon_kingdom_regional_coin_23: 3855,
        SMOLocationData.moon_kingdom_regional_coin_24: 3857,
        SMOLocationData.moon_kingdom_regional_coin_25: 3858,
        SMOLocationData.moon_kingdom_regional_coin_26: 3859,
        SMOLocationData.moon_kingdom_regional_coin_27: 3861,
        SMOLocationData.moon_kingdom_regional_coin_28: 3862,
        SMOLocationData.moon_kingdom_regional_coin_29: 3863,
        SMOLocationData.moon_kingdom_regional_coin_30: 3865,
        SMOLocationData.moon_kingdom_regional_coin_31: 3866,
        SMOLocationData.moon_kingdom_regional_coin_32: 3867,
}

moon_cave_regional_coins = {
        SMOLocationData.moon_cave_regional_coin_1: 3869,
        SMOLocationData.moon_cave_regional_coin_2: 3870,
        SMOLocationData.moon_cave_regional_coin_3: 3871,
        SMOLocationData.moon_cave_regional_coin_4: 3873,
        SMOLocationData.moon_cave_regional_coin_5: 3874,
        SMOLocationData.moon_cave_regional_coin_6: 3875,
        SMOLocationData.moon_cave_regional_coin_7: 3877,
        SMOLocationData.moon_cave_regional_coin_8: 3878,
        SMOLocationData.moon_cave_regional_coin_9: 3879,
        SMOLocationData.moon_cave_regional_coin_10: 3881,
        SMOLocationData.moon_cave_regional_coin_11: 3882,
        SMOLocationData.moon_cave_regional_coin_12: 3883,
        SMOLocationData.moon_cave_regional_coin_13: 3885,
        SMOLocationData.moon_cave_regional_coin_14: 3886,
        SMOLocationData.moon_cave_regional_coin_15: 3887,
        SMOLocationData.moon_cave_regional_coin_16: 3889,
        SMOLocationData.moon_cave_regional_coin_17: 3890,
        SMOLocationData.moon_cave_regional_coin_18: 3891,
}

mushroom_kingdom_regional_groups = {
        SMOLocationData.mushroom_kingdom_regional_coin_group_1: 3896,
        SMOLocationData.mushroom_kingdom_regional_coin_group_2: 3901,
        SMOLocationData.mushroom_kingdom_regional_coin_group_3: 3905,
        SMOLocationData.mushroom_kingdom_regional_coin_group_4: 3909,
        SMOLocationData.mushroom_kingdom_regional_coin_group_5: 3913,
        SMOLocationData.mushroom_kingdom_regional_coin_group_6: 3918,
        SMOLocationData.mushroom_kingdom_regional_coin_group_7: 3922,
        SMOLocationData.mushroom_kingdom_regional_coin_group_8: 3926,
        SMOLocationData.mushroom_kingdom_regional_coin_group_9: 3930,
        SMOLocationData.mushroom_kingdom_regional_coin_group_10: 3934,
        SMOLocationData.mushroom_kingdom_regional_coin_group_11: 3938,
        SMOLocationData.mushroom_kingdom_regional_coin_group_12: 3942,
        SMOLocationData.mushroom_kingdom_regional_coin_group_13: 3946,
        SMOLocationData.mushroom_kingdom_regional_coin_group_14: 3950,
        SMOLocationData.mushroom_kingdom_regional_coin_group_15: 3954,
        SMOLocationData.mushroom_kingdom_regional_coin_group_16: 3958,
        SMOLocationData.mushroom_kingdom_regional_coin_group_17: 3962,
        SMOLocationData.mushroom_kingdom_regional_coin_group_18: 3966,
        SMOLocationData.mushroom_kingdom_regional_coin_group_19: 3971,
        SMOLocationData.mushroom_kingdom_regional_coin_group_20: 3975,
        SMOLocationData.mushroom_kingdom_regional_coin_group_21: 3978,
        SMOLocationData.mushroom_kingdom_regional_coin_group_22: 3981,
        SMOLocationData.mushroom_kingdom_regional_coin_group_23: 3985,
        SMOLocationData.mushroom_kingdom_regional_coin_group_24: 3989,
        SMOLocationData.mushroom_kingdom_regional_coin_group_25: 3993,
        SMOLocationData.mushroom_kingdom_regional_coin_group_26: 3997,
        SMOLocationData.mushroom_kingdom_regional_coin_group_27: 4001,
        SMOLocationData.mushroom_kingdom_regional_coin_group_28: 4005,
        SMOLocationData.mushroom_kingdom_regional_coin_group_29: 4009,
        SMOLocationData.mushroom_kingdom_regional_coin_group_30: 4013,
        SMOLocationData.mushroom_kingdom_regional_coin_group_31: 4017,
        SMOLocationData.mushroom_kingdom_regional_coin_group_32: 4021,
}

peachs_castle_regional_groups = {
        SMOLocationData.mushroom_kingdom_regional_coin_group_1: 3892,
}

mushroom_kingdom_regional_coins = {
        SMOLocationData.mushroom_kingdom_regional_coin_1: 3897,
        SMOLocationData.mushroom_kingdom_regional_coin_2: 3898,
        SMOLocationData.mushroom_kingdom_regional_coin_3: 3899,
        SMOLocationData.mushroom_kingdom_regional_coin_4: 3900,
        SMOLocationData.mushroom_kingdom_regional_coin_5: 3902,
        SMOLocationData.mushroom_kingdom_regional_coin_6: 3903,
        SMOLocationData.mushroom_kingdom_regional_coin_7: 3904,
        SMOLocationData.mushroom_kingdom_regional_coin_8: 3906,
        SMOLocationData.mushroom_kingdom_regional_coin_9: 3907,
        SMOLocationData.mushroom_kingdom_regional_coin_10: 3908,
        SMOLocationData.mushroom_kingdom_regional_coin_11: 3910,
        SMOLocationData.mushroom_kingdom_regional_coin_12: 3911,
        SMOLocationData.mushroom_kingdom_regional_coin_13: 3912,
        SMOLocationData.mushroom_kingdom_regional_coin_14: 3914,
        SMOLocationData.mushroom_kingdom_regional_coin_15: 3915,
        SMOLocationData.mushroom_kingdom_regional_coin_16: 3916,
        SMOLocationData.mushroom_kingdom_regional_coin_17: 3917,
        SMOLocationData.mushroom_kingdom_regional_coin_18: 3919,
        SMOLocationData.mushroom_kingdom_regional_coin_19: 3920,
        SMOLocationData.mushroom_kingdom_regional_coin_20: 3921,
        SMOLocationData.mushroom_kingdom_regional_coin_21: 3923,
        SMOLocationData.mushroom_kingdom_regional_coin_22: 3924,
        SMOLocationData.mushroom_kingdom_regional_coin_23: 3925,
        SMOLocationData.mushroom_kingdom_regional_coin_24: 3927,
        SMOLocationData.mushroom_kingdom_regional_coin_25: 3928,
        SMOLocationData.mushroom_kingdom_regional_coin_26: 3929,
        SMOLocationData.mushroom_kingdom_regional_coin_27: 3931,
        SMOLocationData.mushroom_kingdom_regional_coin_28: 3932,
        SMOLocationData.mushroom_kingdom_regional_coin_29: 3933,
        SMOLocationData.mushroom_kingdom_regional_coin_30: 3935,
        SMOLocationData.mushroom_kingdom_regional_coin_31: 3936,
        SMOLocationData.mushroom_kingdom_regional_coin_32: 3937,
        SMOLocationData.mushroom_kingdom_regional_coin_33: 3939,
        SMOLocationData.mushroom_kingdom_regional_coin_34: 3940,
        SMOLocationData.mushroom_kingdom_regional_coin_35: 3941,
        SMOLocationData.mushroom_kingdom_regional_coin_36: 3943,
        SMOLocationData.mushroom_kingdom_regional_coin_37: 3944,
        SMOLocationData.mushroom_kingdom_regional_coin_38: 3945,
        SMOLocationData.mushroom_kingdom_regional_coin_39: 3947,
        SMOLocationData.mushroom_kingdom_regional_coin_40: 3948,
        SMOLocationData.mushroom_kingdom_regional_coin_41: 3949,
        SMOLocationData.mushroom_kingdom_regional_coin_42: 3951,
        SMOLocationData.mushroom_kingdom_regional_coin_43: 3952,
        SMOLocationData.mushroom_kingdom_regional_coin_44: 3953,
        SMOLocationData.mushroom_kingdom_regional_coin_45: 3955,
        SMOLocationData.mushroom_kingdom_regional_coin_46: 3956,
        SMOLocationData.mushroom_kingdom_regional_coin_47: 3957,
        SMOLocationData.mushroom_kingdom_regional_coin_48: 3959,
        SMOLocationData.mushroom_kingdom_regional_coin_49: 3960,
        SMOLocationData.mushroom_kingdom_regional_coin_50: 3961,
        SMOLocationData.mushroom_kingdom_regional_coin_51: 3963,
        SMOLocationData.mushroom_kingdom_regional_coin_52: 3964,
        SMOLocationData.mushroom_kingdom_regional_coin_53: 3965,
        SMOLocationData.mushroom_kingdom_regional_coin_54: 3967,
        SMOLocationData.mushroom_kingdom_regional_coin_55: 3968,
        SMOLocationData.mushroom_kingdom_regional_coin_56: 3969,
        SMOLocationData.mushroom_kingdom_regional_coin_57: 3970,
        SMOLocationData.mushroom_kingdom_regional_coin_58: 3972,
        SMOLocationData.mushroom_kingdom_regional_coin_59: 3973,
        SMOLocationData.mushroom_kingdom_regional_coin_60: 3974,
        SMOLocationData.mushroom_kingdom_regional_coin_61: 3976,
        SMOLocationData.mushroom_kingdom_regional_coin_62: 3977,
        SMOLocationData.mushroom_kingdom_regional_coin_63: 3979,
        SMOLocationData.mushroom_kingdom_regional_coin_64: 3980,
        SMOLocationData.mushroom_kingdom_regional_coin_65: 3982,
        SMOLocationData.mushroom_kingdom_regional_coin_66: 3983,
        SMOLocationData.mushroom_kingdom_regional_coin_67: 3984,
        SMOLocationData.mushroom_kingdom_regional_coin_68: 3986,
        SMOLocationData.mushroom_kingdom_regional_coin_69: 3987,
        SMOLocationData.mushroom_kingdom_regional_coin_70: 3988,
        SMOLocationData.mushroom_kingdom_regional_coin_71: 3990,
        SMOLocationData.mushroom_kingdom_regional_coin_72: 3991,
        SMOLocationData.mushroom_kingdom_regional_coin_73: 3992,
        SMOLocationData.mushroom_kingdom_regional_coin_74: 3994,
        SMOLocationData.mushroom_kingdom_regional_coin_75: 3995,
        SMOLocationData.mushroom_kingdom_regional_coin_76: 3996,
        SMOLocationData.mushroom_kingdom_regional_coin_77: 3998,
        SMOLocationData.mushroom_kingdom_regional_coin_78: 3999,
        SMOLocationData.mushroom_kingdom_regional_coin_79: 4000,
        SMOLocationData.mushroom_kingdom_regional_coin_80: 4002,
        SMOLocationData.mushroom_kingdom_regional_coin_81: 4003,
        SMOLocationData.mushroom_kingdom_regional_coin_82: 4004,
        SMOLocationData.mushroom_kingdom_regional_coin_83: 4006,
        SMOLocationData.mushroom_kingdom_regional_coin_84: 4007,
        SMOLocationData.mushroom_kingdom_regional_coin_85: 4008,
        SMOLocationData.mushroom_kingdom_regional_coin_86: 4010,
        SMOLocationData.mushroom_kingdom_regional_coin_87: 4011,
        SMOLocationData.mushroom_kingdom_regional_coin_88: 4012,
        SMOLocationData.mushroom_kingdom_regional_coin_89: 4014,
        SMOLocationData.mushroom_kingdom_regional_coin_90: 4015,
        SMOLocationData.mushroom_kingdom_regional_coin_91: 4016,
        SMOLocationData.mushroom_kingdom_regional_coin_92: 4018,
        SMOLocationData.mushroom_kingdom_regional_coin_93: 4019,
        SMOLocationData.mushroom_kingdom_regional_coin_94: 4020,
        SMOLocationData.mushroom_kingdom_regional_coin_95: 4022,
        SMOLocationData.mushroom_kingdom_regional_coin_96: 4023,
        SMOLocationData.mushroom_kingdom_regional_coin_97: 4024,
}

peachs_castle_regional_coins = {
        SMOLocationData.peachs_castle_regional_coin_1: 3893,
        SMOLocationData.peachs_castle_regional_coin_2: 3894,
        SMOLocationData.peachs_castle_regional_coin_3: 3895,
}

regional_coin_groups_table = {
        **cap_kingdom_regional_groups,
        **cascade_kingdom_regional_groups,
        **sand_kingdom_regional_groups,
        **wooded_kingdom_regional_groups,
        **lake_kingdom_regional_groups,
        **lost_kingdom_regional_groups,
        **metro_kingdom_regional_groups,
        **seaside_kingdom_regional_groups,
        **snow_kingdom_regional_groups,
        **luncheon_kingdom_regional_groups,
        **bowsers_kingdom_regional_groups,
        **mushroom_kingdom_regional_groups,
        **top_hat_tower_regional_groups,
        **frog_pond_regional_groups,
        **pushblocks_regional_groups,
        **poison_tides_regional_groups,
        **chasm_lifts_regional_groups,
        **bullet_bill_maze_regional_groups,
        **jaxi_ruins_regional_groups,
        **strange_neighborhood_regional_groups,
        **moeeye_invisible_maze_regional_groups,
        **ice_cave_regional_groups,
        **pyramid_upper_interior_regional_groups,
        **underground_ruins_regional_groups,
        **sky_garden_tower_regional_groups,
        **flooded_pipes_regional_groups,
        **deep_woods_regional_groups,
        **walking_on_clouds_regional_groups,
        **wooded_flower_road_regional_groups,
        **sherm_elevator_regional_groups,
        **bouncy_flowers_regional_groups,
        **city_hall_regional_groups,
        **sewers_regional_groups,
        **bullet_billding_regional_groups,
        **high_rise_regional_groups,
        **trex_escape_regional_groups,
        **sea_cave_regional_groups,
        **shiveria_regional_groups,
        **snowline_regional_groups,
        **cascading_magma_regional_groups,
        **magma_narrow_path_regional_groups,
        **spinning_athletics_regional_groups,
        **fork_flickin_regional_groups,
        **moon_cave_regional_groups,
        **peachs_castle_regional_groups,
}

regional_coin_table = {
        **cap_kingdom_regional_coins,
        **cascade_kingdom_regional_coins,
        **sand_kingdom_regional_coins,
        **wooded_kingdom_regional_coins,
        **lake_kingdom_regional_coins,
        **lost_kingdom_regional_coins,
        **metro_kingdom_regional_coins,
        **seaside_kingdom_regional_coins,
        **snow_kingdom_regional_coins,
        **luncheon_kingdom_regional_coins,
        **bowsers_kingdom_regional_coins,
        **mushroom_kingdom_regional_coins,
        **top_hat_tower_regional_coins,
        **frog_pond_regional_coins,
        **pushblocks_regional_coins,
        **poison_tides_regional_coins,
        **chasm_lifts_regional_coins,
        **bullet_bill_maze_regional_coins,
        **jaxi_ruins_regional_coins,
        **strange_neighborhood_regional_coins,
        **moeeye_invisible_maze_regional_coins,
        **ice_cave_regional_coins,
        **pyramid_upper_interior_regional_coins,
        **underground_ruins_regional_coins,
        **sky_garden_tower_regional_coins,
        **flooded_pipes_regional_coins,
        **deep_woods_regional_coins,
        **walking_on_clouds_regional_coins,
        **wooded_flower_road_regional_coins,
        **sherm_elevator_regional_coins,
        **bouncy_flowers_regional_coins,
        **city_hall_regional_coins,
        **sewers_regional_coins,
        **bullet_billding_regional_coins,
        **high_rise_regional_coins,
        **trex_escape_regional_coins,
        **sea_cave_regional_coins,
        **shiveria_regional_coins,
        **snowline_regional_coins,
        **cascading_magma_regional_coins,
        **magma_narrow_path_regional_coins,
        **spinning_athletics_regional_coins,
        **fork_flickin_regional_coins,
        **moon_cave_regional_coins,
        **peachs_castle_regional_coins,
}

regional_coin_groups = {
        "CapWorldHomeStage": {
                1: [
                        "obj2103",
                        "obj2105",
                        "obj2108",
                        "obj2104"
                ],
                2: [
                        "obj2109",
                        "obj2110",
                        "obj2111",
                        "obj2112",
                ],
                3: [
                        "obj2117",
                        "obj2118",
                        "obj2119",
                        "obj2120",
                ],
                4: [
                        "obj2139",
                        "obj2140",
                        "obj2141",
                        "obj2142",
                ],
                5: [
                        "obj2143",
                        "obj2144",
                        "obj2145",
                ],
                6: [
                        "obj2147",
                        "obj2148",
                        "obj2149",
                ],
                7: [
                        "obj2166",
                        "obj2167",
                        "obj2168",
                ],
                8: [
                        "obj2169",
                        "obj2170",
                        "obj2171",
                ],
                9: [
                        "obj2233",
                        "obj2234",
                        "obj2235",
                ],
                # Sub Areas
                # Top Hat Tower
                'Top Hat Tower 10': [
                        "obj1348",
                        "obj1349",
                        "obj1350",
                        "obj1351",
                ],
                'Top Hat Tower 11': [
                        "obj1352",
                        "obj1353",
                        "obj1354",
                        "obj1355",
                        "obj1356",
                ],
                # Frog
                'Frog Pond 12': [
                        "obj64",
                        "obj65",
                        "obj66",
                        "obj67",
                ],
                # Push Block
                'Push-Blocks 13': [
                        "obj131",
                        "obj515",
                        "obj516",
                ],
                # Poison
                'Poison Tides 14': [
                        "obj422",
                        "obj423",
                        "obj424",
                ]

        },
        "WaterfallWorldHomeStage": {
                1: [
                        "obj1046",
                        "obj1047",
                        "obj1048",
                ],
                2: [
                        "obj1057",
                        "obj1211",
                        "obj1212",
                ],
                3: [
                        "obj1106",
                        "obj1107",
                        "obj1109",
                ],
                4: [
                        "obj1535",
                        "obj1536",
                        "obj1537",
                ],
                5: [
                        "obj1641",
                        "obj1926",
                        "obj1927",
                ],
                6: [
                        "obj1796",
                        "obj1797",
                        "obj1798",
                ],
                7: [
                        "obj1855",
                        "obj1856",
                        "obj1857",
                ],
                8: [
                        "obj1897",
                        "obj1898",
                        "obj1899",
                ],
                9: [
                        "obj2041",
                        "obj2042",
                        "obj2043",
                ],
                10: [
                        "obj2156",
                        "obj2157",
                        "obj2158",
                        "obj2159",
                ],
                11: [
                        "obj3265",
                        "obj3266",
                        "obj3267",
                ],
                12: [
                        "obj3268",
                        "obj3269",
                        "obj3270",
                ],
                13: [
                        "obj3271",
                        "obj3272",
                        "obj3273",
                ],
                14: [
                        "obj1049",
                        "obj1050",
                        "obj1394",
                ],
                15: [
                        "obj1555",
                        "obj1556",
                        "obj1557",
                ],
                # Sub Areas
                'Chasm Lifts 16': [
                        "obj6460",
                        "obj6461",
                        "obj6462",
                        "obj7621",
                ],
        },
        "SandWorldHomeStage": {
                1: [
                        "obj1438",
                        "obj3024",
                        "obj3025",
                ],
                2: [
                        "obj1831",
                        "obj1832",
                        "obj1833",
                ],
                3: [
                        "obj1967",
                        "obj1969",
                        "obj1970",
                ],
                4: [
                        "obj1999",
                        "obj2000",
                        "obj2399",
                ],
                5: [
                        "obj2018",
                        "obj3737",
                        "obj2019",
                ],
                6: [
                        "obj2021",
                        "obj3726",
                ],
                7: [
                        "obj2022",
                        "obj3727",
                ],
                8: [
                        "obj2392",
                        "obj2393",
                        "obj2394",
                ],
                9: [
                        "obj2396",
                        "obj2397",
                        "obj2398",
                ],
                10: [
                        "obj3404",
                        "obj3405",
                        "obj3406",
                ],
                11: [
                        "obj3479",
                        "obj3480",
                        "obj3481",
                ],
                12: [
                        "obj3720",
                        "obj3721",
                        "obj3722",
                ],
                13: [
                        "obj3723",
                        "obj3724",
                        "obj3725",
                ],
                14: [
                        "obj3855",
                        "obj3856",
                        "obj3857",
                ],
                15: [
                        "obj3879",
                        "obj3880",
                ],
                16: [
                        "obj4864",
                        "obj4865",
                        "obj4866",
                        "obj4867",
                        "obj4868",
                        "obj4869",
                ],
                17: [
                        "obj6862",
                        "obj6863",
                        "obj6864",
                ],
                18: [
                        "obj3671",
                        "obj3673",
                        "obj3676",
                        "obj3677",
                ],
                19: [
                        "obj4871",
                        "obj4873",
                        "obj4875",
                        "obj4876",
                ],
                20: [
                        "obj134",
                        "obj140",
                ],
                21: [
                        "obj135",
                        "obj141",
                ],
                # Sub Areas
                # Bullet Bill
                'Bullet Bill Maze 22': [
                        "obj38",
                        "obj39",
                        "obj40",
                        "obj41",
                        "obj132",
                        "obj133",
                ],
                # Moeye
                'Moe-Eye Invisible Maze 23': [
                        "obj172",
                        "obj203",
                        "obj204",
                        "obj205",
                ],
                # Press
                'Ice Cave 24': [
                        "obj44",
                        "obj46",
                ],
                'Ice Cave 25': [
                        "obj195",
                        "obj196",
                ],
                # Pyramid
                'Pyramid Upper Interior 26': [
                        "obj295",
                        "obj296",
                        "obj297",
                ],
                # Strange Neighborhood
                'Strange Neighborhood 27': [
                        "obj201",
                        "obj202",
                ],
                'Strange Neighborhood 28': [
                        "obj203",
                        "obj225",
                        "obj226",
                ],
                # Underground
                'Underground Ruins 29': [
                        "obj165",
                        "obj166",
                        "obj168",
                ],
                'Underground Ruins 30': [
                        "obj530",
                        "obj531",
                        "obj532",
                        "obj533",
                ],
                # Jaxi
                'Jaxi Ruins 31': [
                        "obj1136",
                        "obj1139",
                ],
                'Jaxi Ruins 32': [
                        "obj1137",
                        "obj1141",
                        "obj1142",
                ],
                'Jaxi Ruins 33': [
                        "obj1138",
                        "obj1143",
                        "obj1144",
                ],
        },
        "LakeWorldHomeStage": {
                1: [
                        "obj20",
                        "obj22",
                        "obj23",
                        "obj21",
                ],
                2: [
                        "obj111",
                        "obj113",
                        "obj112",
                ],
                3: [
                        "obj312",
                        "obj313",
                        "obj314",
                        "obj315",
                ],
                4: [
                        "obj351",
                        "obj353",
                        "obj354",
                ],
                5: [
                        "obj509",
                        "obj511",
                        "obj510",
                ],
                6: [
                        "obj529",
                        "obj530",
                        "obj531",
                ],
                7: [
                        "obj336",
                        "obj337",
                        "obj338",
                ],
                8: [
                        "obj431",
                        "obj432",
                        "obj433",
                        "obj549",
                ],
                9: [
                        "obj448",
                        "obj449",
                        "obj450",
                        "obj746",
                ],
                10: [
                        "obj551",
                        "obj552",
                        "obj554",
                ],
                11: [
                        "obj668",
                        "obj670",
                        "obj671",
                        "obj669",
                ],
                12: [
                        "obj743",
                        "obj744",
                        "obj745",
                ],
                13: [
                        "obj759",
                        "obj760",
                        "obj761",
                ],
                14: [
                        "obj613",
                        "obj615",
                        "obj758",
                ],
                # sub areas
                # bouncy flowers
                'Bouncy Flowers 15': [
                        "obj1095",
                        "obj1096",
                        "obj1137",
                ]
        },
        "ForestWorldHomeStage": {
                2: [
                        "obj1727",
                        "obj1729",
                        "obj1730",
                ],
                3: [
                        "obj1752",
                        "obj1753",
                        "obj1754",
                ],
                4: [
                        "obj1757",
                        "obj1758",
                        "obj1759",
                ],
                5: [
                        "obj1772",
                        "obj5937",
                ],
                6: [
                        "obj1783",
                        "obj1784",
                        "obj1785",
                        "obj1786",
                ],
                7: [
                        "obj2294",
                        "obj2295",
                        "obj4826",
                        "obj6989",
                ],
                8: [
                        "obj2305",
                        "obj2306",
                        "obj2307",
                ],
                9: [
                        "obj4918",
                        "obj4919",
                        "obj4920",
                ],
                10: [
                        "obj5000",
                        "obj5001",
                        "obj5002",
                        "obj6990",
                ],
                11: [
                        "obj5036",
                        "obj5037",
                        "obj5038",
                        "obj5039",
                ],
                12: [
                        "obj5119",
                        "obj5120",
                        "obj5121",
                        "obj5122",
                ],
                13: [
                        "obj5616",
                        "obj5617",
                        "obj5618",
                ],
                14: [
                        "obj5950",
                        "obj5952",
                        "obj5963",
                ],
                15: [
                        "obj5953",
                        "obj5954",
                        "obj5955",
                        "obj6145",
                ],
                16: [
                        "obj5957",
                        "obj5958",
                        "obj6150",
                ],
                17: [
                        "obj5964",
                        "obj5965",
                        "obj5966",
                ],
                18: [
                        "obj5970",
                        "obj5971",
                        "obj5972",
                ],
                19: [
                        "obj6024",
                        "obj6025",
                ],
                20: [
                        "obj6146",
                        "obj6147",
                        "obj6148",
                        "obj6149",
                ],
                21: [
                        "obj6402",
                        "obj6985",
                ],
                22: [
                        "obj7317",
                        "obj7318",
                        "obj7319",
                ],
                23: [
                        "obj7320",
                        "obj7321",
                        "obj7322",
                ],
                24: [
                        "obj7704",
                        "obj7705",
                        "obj7706",
                ],

                25: [
                        "obj1748",
                        "obj1745",
                        "obj1750",
                ],
                # sub areas
                # sky garden tower
                'Sky Garden Tower 26': [
                        "obj216",
                        "obj217",
                        "obj218",
                ],
                # flooded pipes
                'Flooded Pipes 27': [
                        "obj245",
                        "obj246",
                        "obj247",
                ],
                # Deep woods
                'Deep Woods 28': [
                        "obj93",
                        "obj94",
                        "obj95",
                ],
                'Deep Woods 29': [
                        "obj223",
                        "obj224",
                        "obj225",
                ],
                'Deep Woods 30': [
                        "obj321",
                        "obj322",
                        "obj323",
                ],
                # Clouds
                'Walking on Clouds 31': [
                        "obj1546",
                        "obj1547",
                        "obj1548",
                ],
                # flower road
                'Wooded Flower Road 32': [
                        "obj261",
                        "obj262",
                        "obj263",
                ],
                # Sherm
                'Sherm Elevator 33': [
                        "obj253",
                        "obj254",
                        "obj255",
                ],
        },
        "ClashWorldHomeStage": {
                1: [
                        "obj553",
                        "obj554",
                        "obj555",
                ],
                2: [
                        "obj587",
                        "obj1030",
                        "obj1035",
                        "obj1122",
                ],
                3: [
                        "obj588",
                        "obj589",
                        "obj1036",
                ],
                4: [
                        "obj727",
                        "obj979",
                        "obj728",
                ],
                5: [
                        "obj729",
                        "obj1121",
                ],
                6: [
                        "obj851",
                        "obj852",
                        "obj853",
                        "obj854",
                ],
                7: [
                        "obj868",
                        "obj964",
                        "obj870",
                ],
                8: [
                        "obj872",
                        "obj874",
                        "obj875",
                        "obj977",
                ],
                9: [
                        "obj873",
                        "obj998",
                ],
                10: [
                        "obj901",
                        "obj1193",
                ],
                11: [
                        "obj902",
                        "obj904",
                ],
                12: [
                        "obj903",
                        "obj1738",
                ],
                13: [
                        "obj978",
                        "obj1740",
                        "obj1739",
                ],
                14: [
                        "obj997",
                        "obj999",
                ],
                15: [
                        "obj1039",
                        "obj1043",
                ],
                16: [
                        "obj1096",
                        "obj1097",
                        "obj1098",
                ],
                17: [
                        "obj1689",
                        "obj1690",
                        "obj1691",
                ],
                18: [
                        "obj1031",
                        "obj1033",
                        "obj1034",
                ]
        },
        "CityWorldHomeStage": {
                # metro
                1: [
                        "obj4637",
                        "obj4639",
                        "obj4640",
                ],
                2: [
                        "obj7901",
                        "obj7902",
                        "obj7904",
                ],
                3: [
                        "obj8580",
                        "obj8581",
                        "obj8582",
                ],
                4: [
                        "obj9306",
                        "obj9307",
                        "obj9308",
                ],
                5: [
                        "obj9372",
                        "obj9373",
                        "obj9374",
                ],
                6: [
                        "obj10505",
                        "obj11282",
                ],
                7: [
                        "obj4506",
                        "obj4508",
                        "obj4507",
                ],
                8: [
                        "obj4633",
                        "obj10075",
                        "obj10076",
                ],
                9: [
                        "obj4638",
                        "obj13420",
                        "obj13421",
                ],
                10: [
                        "obj5055",
                        "obj5056",
                        "obj9413",
                ],
                11: [
                        "obj5910",
                        "obj5913",
                        "obj5911",
                ],
                12: [
                        "obj7939",
                        "obj11281",
                ],
                13: [
                        "obj8043",
                        "obj13097",
                        "obj13098",
                ],
                14: [
                        "obj8044",
                        "obj8046",
                ],
                15: [
                        "obj8269",
                        "obj9541",
                        "obj9542",
                ],
                16: [
                        "obj8807",
                        "obj8808",
                        "obj8809",
                ],
                17: [
                        "obj10062",
                        "obj10063",
                        "obj10064",
                ],
                18: [
                        "obj10675",
                        "obj10676",
                ],
                19: [
                        "obj10968",
                        "obj10969",
                        "obj10970",
                        "obj10971",
                ],
                20: [
                        "obj10978",
                        "obj10979",
                        "obj10980",
                ],
                21: [
                        "obj11001",
                        "obj11002",
                        "obj11003",
                ],
                22: [
                        "obj11083",
                        "obj11280",
                ],
                23: [
                        "obj12978",
                        "obj12979",
                        "obj12983",
                ],
                24: [
                        "obj13145",
                        "obj13146",
                ],
                25: [
                        "obj15765",
                        "obj15766",
                ],
                26: [
                        "obj15775",
                        "obj15777",
                ],

                # sub areas
                # Sewers
                'Sewers 27': [
                        "obj664",
                        "obj665",
                        "obj666",
                ],
                'Sewers 28': [
                        "obj298",
                        "obj299",
                        "obj301",
                        "obj367",
                ],
                # City Hall
                'City Hall 29': [
                        "obj546",
                        "obj547",
                        "obj1260",
                ],
                'City Hall 30': [
                        "obj874",
                        "obj1041",
                ],
                'City Hall 31': [
                        "obj882",
                        "obj883",
                        "obj884",
                ],
                'City Hall 32': [
                        "obj966",
                        "obj967",
                ],
                # Bullet Billding
                'Bullet Billding 33': [
                        "obj1497",
                        "obj1498",
                        "obj1499",
                ],
                # High Rise
                'High Rise 34': [
                        "obj800",
                        "obj801",
                        "obj802",
                ],
                # Trex Escape
                'T-Rex Escape 35': [
                        "obj5435",
                        "obj5436",
                        "obj5437",
                ],
                'T-Rex Escape 36': [
                        "obj5438",
                        "obj5439",
                        "obj5440",
                ],
        },
        "SeaWorldHomeStage": {
                1: [
                        "obj254",
                        "obj256",
                        "obj371",
                ],
                2: [
                        "obj220",
                        "obj221",
                        "obj223",
                ],
                3: [
                        "obj1149",
                        "obj1150",
                        "obj1151",
                ],
                4: [
                        "obj1152",
                        "obj1154",
                        "obj1153",
                ],
                5: [
                        "obj1403",
                        "obj1404",
                        "obj1405",
                ],
                6: [
                        "obj1566",
                        "obj1567",
                        "obj1568",
                ],
                7: [
                        "obj2064",
                        "obj2065",
                        "obj2066",
                ],
                8: [
                        "obj2204",
                        "obj2205",
                        "obj2206",
                ],
                9: [
                        "obj2385",
                        "obj2386",
                        "obj2387",
                ],
                10: [
                        "obj2398",
                        "obj2399",
                        "obj2400",
                        "obj2445",
                ],
                11: [
                        "obj2409",
                        "obj2411",
                        "obj2410",
                ],
                12: [
                        "obj2413",
                        "obj2415",
                        "obj2414",
                ],
                13: [
                        "obj2455",
                        "obj2456",
                        "obj2457",
                ],
                14: [
                        "obj2458",
                        "obj2459",
                        "obj2460",
                ],
                15: [
                        "obj2552",
                        "obj2553",
                        "obj2554",
                ],
                16: [
                        "obj2686",
                        "obj2687",
                        "obj2688",
                ],
                17: [
                        "obj3078",
                        "obj3079",
                        "obj3080",
                ],
                18: [
                        "obj4312",
                        "obj4313",
                        "obj4314",
                ],
                19: [
                        "obj206",
                        "obj207",
                        "obj208",
                ],
                20: [
                        "obj236",
                        "obj237",
                        "obj238",
                ],
                21: [
                        "obj430",
                        "obj431",
                        "obj432",
                ],
                22: [
                        "obj494",
                        "obj495",
                        "obj496",
                ],
                23: [
                        "obj280",
                        "obj282",
                        "obj281",
                ],
                24: [
                        "obj314",
                        "obj315",
                        "obj316",
                ],
                25: [
                        "obj351",
                        "obj352",
                        "obj353",
                ],
                26: [
                        "obj373",
                        "obj375",
                        "obj374",
                ],
                27: [
                        "obj83",
                        "obj85",
                        "obj84",
                ],
                28: [
                        "obj89",
                        "obj90",
                        "obj103",
                ],
                29: [
                        "obj149",
                        "obj150",
                        "obj151",
                ],
                30: [
                        "obj346",
                        "obj347",
                        "obj348",
                ],
                31: [
                        "obj46",
                        "obj47",
                        "obj48",
                ],
                # sub areas
                # Sea Cave
                'Sea Cave 32': [
                        "obj484",
                        "obj485",
                        "obj486",
                ],
                'Sea Cave 33': [
                        "obj487",
                        "obj488",
                        "obj489",
                ],
        },
        "SnowWorldHomeStage": {
                1: [
                        "obj1150",
                        "obj1151",
                ],
                2: [
                        "obj1348",
                        "obj1350",
                ],
                3: [
                        "obj1426",
                        "obj1427",
                        "obj1428",
                ],
                4: [
                        "obj1432",
                        "obj1433",
                ],
                5: [
                        "obj1533",
                        "obj1534",
                ],
                6: [
                        "obj1535",
                        "obj1536",
                ],
                # sub areas
                # Shiveria
                'Shiveria 7': [
                        "obj1097",
                        "obj1098",
                        "obj1099",
                        "obj1100",
                ],
                # Snowy Mountain
                'Shiveria 8': [
                        "obj169",
                        "obj170",
                        "obj251",
                ],
                'Shiveria 9': [
                        "obj271",
                        "obj272",
                        "obj273",
                ],
                # Ty-foo
                'Shiveria 10': [
                        "obj222",
                        "obj223",
                        "obj224",
                        "obj225",
                ],
                'Shiveria 11': [
                        "obj273",
                        "obj274",
                        "obj275",
                ],
                # Ice Wall
                'Shiveria 12': [
                        "obj273",
                        "obj274",
                        "obj275",
                ],
                'Shiveria 13': [
                        "obj281",
                        "obj282",
                        "obj283",
                ],
                # Icicle
                'Shiveria 14': [
                        "obj380",
                        "obj381",
                        "obj448",
                        "obj449",
                ],
                'Shiveria 15': [
                        "obj421",
                        "obj422",
                        "obj423",
                ],
                'Snowline 16': [
                        "obj923",
                        "obj924",
                        "obj925",
                        "obj926",
                ],
                'Snowline 17': [
                        "obj927",
                        "obj928",
                        "obj929",
                ],

        },
        "LavaWorldHomeStage": {
                1: [
                        "obj2675",
                        "obj2746",
                        "obj2747",
                ],
                2: [
                        "obj2678",
                        "obj2679",
                        "obj2680",
                ],
                3: [
                        "obj2685",
                        "obj2686",
                        "obj2688",
                ],
                4: [
                        "obj2690",
                        "obj2692",
                        "obj2691",
                ],
                5: [
                        "obj2713",
                        "obj2774",
                        "obj2773",
                ],
                6: [
                        "obj2717",
                        "obj2775",
                        "obj4287",
                ],
                7: [
                        "obj2722",
                        "obj2728",
                ],
                8: [
                        "obj2735",
                        "obj2736",
                        "obj2737",
                        "obj2738",
                        "obj2740",
                        "obj2741",
                        "obj2742",
                ],
                9: [
                        "obj2744",
                        "obj5567",
                        "obj5568",
                ],
                10: [
                        "obj2748",
                        "obj2756",
                        "obj2760",
                ],
                11: [
                        "obj2750",
                        "obj2754",
                        "obj2758",
                        "obj2762",
                        "obj2751",
                ],
                12: [
                        "obj2755",
                        "obj2785",
                        "obj2783",
                ],
                13: [
                        "obj2757",
                        "obj2761",
                        "obj3489",
                        "obj3490",
                ],
                14: [
                        "obj2784",
                        "obj2787",
                        "obj3123",
                ],
                15: [
                        "obj3310",
                        "obj3311",
                        "obj3312",
                ],
                16: [
                        "obj3808",
                        "obj3809",
                        "obj3810",
                ],
                17: [
                        "obj3843",
                        "obj3844",
                        "obj3845",
                ],
                18: [
                        "obj5656",
                        "obj5657",
                        "obj5658",
                ],
                19: [
                        "obj6254",
                        "obj6255",
                        "obj6256",
                ],
                20: [
                        "obj6363",
                        "obj6364",
                        "obj6365",
                ],
                21: [
                        "obj2659",
                        "obj2660",
                        "obj2663",
                        "obj2664",
                ],
                22: [
                        "obj2662",
                        "obj3740",
                        "obj3738",
                ],
                23: [
                        "obj2665",
                        "obj2666",
                        "obj3991",
                ],
                24: [
                        "obj3910",
                        "obj3911",
                        "obj3912",
                ],
                25: [
                        "obj6347",
                        "obj6348",
                        "obj6349",
                ],
                26: [
                        "obj6366",
                        "obj6367",
                        "obj6368",
                ],

                # Cascading Magma
                'Cascading Magma 27': [
                        "obj185",
                        "obj208",
                        "obj209",
                ],
                'Cascading Magma 28': [
                        "obj187",
                        "obj206",
                        "obj207",
                ],
                # sub areas
                # Narrow Lava
                'Magma Narrow Path 29': [
                        "obj807",
                        "obj808",
                        "obj809",
                ],
                # Spinning Athletics
                'Spinnning Athletics 30': [
                        "obj431",
                        "obj432",
                        "obj433",
                ],
                # Forks
                'Fork Flickin 31': [
                        "obj5762",
                        "obj5763",
                        "obj5764",
                ]

        },
        "SkyWorldHomeStage": {
                # Castle
                1: [
                        "obj653",
                        "obj4377",
                        "obj6733",
                ],
                2: [
                        "obj1692",
                        "obj1694",
                        "obj1693",
                ],
                3: [
                        "obj1800",
                        "obj1918",
                        "obj2450",
                ],
                4: [
                        "obj1801",
                        "obj1917",
                        "obj2451",
                ],
                5: [
                        "obj1955",
                        "obj1958",
                        "obj1956",
                ],
                6: [
                        "obj2306",
                        "obj2307",
                        "obj2308",
                        "obj2309",
                ],
                7: [
                        "obj2501",
                        "obj2512",
                        "obj2514",
                ],
                8: [
                        "obj2726",
                        "obj2727",
                        "obj2728",
                ],
                9: [
                        "obj3233",
                        "obj3234",
                        "obj3235",
                ],
                10: [
                        "obj5680",
                        "obj5681",
                        "obj8169",
                ],
                11: [
                        "obj6735",
                        "obj6736",
                        "obj6737",
                ],
                12: [
                        "obj7322",
                        "obj7324",
                        "obj7323",
                ],
                # Peace
                13: [
                        "obj650",
                        "obj2132",
                        "obj2133",
                ],
                14: [
                        "obj2714",
                        "obj6734",
                        "obj7583",
                ],
                15: [
                        "obj2715",
                        "obj5705",
                        "obj5682",
                ],
                16: [
                        "obj3634",
                        "obj3635",
                        "obj3636",
                ],
                17: [
                        "obj5706",
                        "obj5708",
                        "obj5707",
                ],
                18: [
                        "obj5735",
                        "obj5736",
                        "obj5737",
                ],
                19: [
                        "obj7580",
                        "obj7581",
                        "obj7582",
                ],
                # end castle peace
                20: [
                        "obj1722",
                        "obj1723",
                        "obj1724",
                        "obj1925",
                ],
                21: [
                        "obj1808",
                        "obj1810",
                        "obj2073",
                        "obj2828",
                ],
                22: [
                        "obj1970",
                        "obj1971",
                        "obj1972",
                ],
                23: [
                        "obj2272",
                        "obj2273",
                        "obj2274",
                        "obj2829",
                ],
                24: [
                        "obj2830",
                        "obj2841",
                ],
                25: [
                        "obj2831",
                        "obj2832",
                ],
                # Wall Zone
                26: [
                        "obj959",
                        "obj960",
                        "obj1227",
                ],
                27: [
                        "obj1503",
                        "obj1504",
                        "obj2159",
                ],
                28: [
                        "obj1612",
                        "obj1832",
                        "obj1613",
                ],
                29: [
                        "obj1872",
                        "obj1873",
                        "obj2192",
                ],
                30: [
                        "obj1964",
                        "obj1965",
                        "obj1967",
                        "obj2238",
                ],
                31: [
                        "obj2097",
                        "obj2098",
                        "obj2099",
                ],
                32: [
                        "obj2218",
                        "obj2219",
                        "obj2220",
                        "obj2237",
                ]
        },
        "MoonWorldHomeStage": {
                1: [
                        "obj71",
                        "obj72",
                        "obj73",
                ],
                2: [
                        "obj94",
                        "obj95",
                        "obj96",
                        "obj97",
                ],
                3: [
                        "obj197",
                        "obj198",
                        "obj199",
                        "obj836",
                        "obj837",
                        "obj838",
                ],
                4: [
                        "obj469",
                        "obj470",
                        "obj471",
                ],
                5: [
                        "obj516",
                        "obj517",
                        "obj518",
                        "obj519",
                ],
                6: [
                        "obj672",
                        "obj673",
                        "obj700",
                ],
                7: [
                        "obj805",
                        "obj806",
                        "obj807",
                ],
                8: [
                        "obj811",
                        "obj812",
                        "obj814",
                ],
                9: [
                        "obj859",
                        "obj860",
                        "obj861",
                ],
                # Moon Cave
                'Moon Cave 10': [
                        "obj6104",
                        "obj6105",
                        "obj6106",
                ],
                'Moon Cave 11': [
                        "obj239",
                        "obj240",
                        "obj412",
                ],
                'Moon Cave 12': [
                        "obj430",
                        "obj461",
                        "obj462",
                ],
                'Moon Cave 13': [
                        "obj405",
                        "obj406",
                        "obj407",
                ],
                'Moon Cave 14': [
                        "obj21",
                        "obj22",
                        "obj23",
                ],
                'Moon Cave 15': [
                        "obj193",
                        "obj194",
                        "obj195",
                ],
        },
        "PeachWorldHomeStage": {
                'peachs castle 1': [
                        "obj92",
                        "obj93",
                        "obj94",
                ],
                2: [
                        "obj740",
                        "obj741",
                        "obj742",
                        "obj847",
                ],
                3: [
                        "obj848",
                        "obj849",
                        "obj850",
                ],
                4: [
                        "obj851",
                        "obj852",
                        "obj853",
                ],
                5: [
                        "obj854",
                        "obj855",
                        "obj856",
                ],
                6: [
                        "obj857",
                        "obj871",
                        "obj872",
                        "obj873",
                ],
                7: [
                        "obj858",
                        "obj859",
                        "obj860",
                ],
                8: [
                        "obj861",
                        "obj862",
                        "obj863",
                ],
                9: [
                        "obj864",
                        "obj865",
                        "obj866",
                ],
                10: [
                        "obj867",
                        "obj877",
                        "obj887",
                ],
                11: [
                        "obj874",
                        "obj875",
                        "obj876",
                ],
                12: [
                        "obj878",
                        "obj879",
                        "obj880",
                ],
                13: [
                        "obj881",
                        "obj882",
                        "obj883",
                ],
                14: [
                        "obj884",
                        "obj885",
                        "obj886",
                ],
                15: [
                        "obj888",
                        "obj889",
                        "obj890",
                ],
                16: [
                        "obj1286",
                        "obj1287",
                        "obj1288",
                ],
                17: [
                        "obj1289",
                        "obj1290",
                        "obj1291",
                ],
                18: [
                        "obj1811",
                        "obj1813",
                        "obj1812",
                ],
                19: [
                        "obj1900",
                        "obj1901",
                        "obj1902",
                        "obj1903",
                ],
                20: [
                        "obj1920",
                        "obj1921",
                        "obj1922",
                ],
                21: [
                        "obj1923",
                        "obj1924",
                ],
                22: [
                        "obj1927",
                        "obj1928",
                ],
                23: [
                        "obj1929",
                        "obj1930",
                        "obj1931",
                ],
                24: [
                        "obj1932",
                        "obj1933",
                        "obj1934",
                ],
                25: [
                        "obj1950",
                        "obj1951",
                        "obj1952",
                ],
                26: [
                        "obj1953",
                        "obj1954",
                        "obj1955",
                ],
                27: [
                        "obj1956",
                        "obj1957",
                        "obj1958",
                ],
                28: [
                        "obj1977",
                        "obj1978",
                        "obj1979",
                ],
                29: [
                        "obj1980",
                        "obj1981",
                        "obj1982",
                ],
                30: [
                        "obj1994",
                        "obj1995",
                        "obj1996",
                ],
                31: [
                        "obj2216",
                        "obj2217",
                        "obj2218",
                ],
                32: [
                        "obj2644",
                        "obj2645",
                        "obj2646",
                ],
                33: [
                        "obj1904",
                        "obj1905",
                        "obj1906",
                ]
        }
}

#endregion

locations_table = {
        **base_locations_table,
        **post_game_locations_table,
        **special_locations_table,
        **shop_locations_table,
        **loc_Post_Cloud,
        **loc_Moon_Post_Moon,
        **loc_Captures,
        **sub_area_table,
        **regional_coin_groups_table,
        **regional_coin_table
}

locations_list = [
    loc_Cap,
    {**loc_Cascade, **loc_Cascade_Peace, **loc_Cascade_Revisit, **loc_Cascade_Post_Snow, **loc_Cascade_Post_Metro},
    {**loc_Sand, **loc_Sand_Peace, **loc_Sand_Revisit, **loc_Sand_Pyramid},
    {**loc_Lake, **loc_Lake_Post_Seaside},
    {**loc_Wooded, **loc_Wooded_Post_Story1, **loc_Wooded_Peace, **loc_Wooded_Post_Metro},
    loc_Cloud,
    {**loc_Lost, **loc_Lost_Revisit},
    {**loc_Night_Metro, **loc_Metro, **loc_Metro_Sewer_Access, **loc_Metro_Peace, **loc_Metro_Post_Sand},
    {**loc_Snow, **loc_Snow_Peace},
    {**loc_Seaside, **loc_Seaside_Peace},
    {**loc_Luncheon, **loc_Luncheon_Post_Spewart, **loc_Luncheon_Post_Cheese_Rocks, **loc_Luncheon_Peace, **loc_Luncheon_Post_Wooded},
    loc_Ruined,
    {**loc_Bowser, **loc_Bowser_Infiltrate, **loc_Bowser_Post_Bombing, **loc_Bowser_Mecha_Broodal, **loc_Bowser_Peace},
    loc_Moon,
    {**loc_Mushroom, **loc_Mushroom_Post_Luncheon},
    loc_Dark,
    loc_Darker
]

full_moon_locations_list = [
    {**loc_Cap, **loc_Cap_Postgame},
    {**loc_Cascade, **loc_Cascade_Peace, **loc_Cascade_Revisit, **loc_Cascade_Post_Snow, **loc_Cascade_Post_Metro, **loc_Cascade_Postgame},
    {**loc_Sand, **loc_Sand_Peace, **loc_Sand_Revisit, **loc_Sand_Pyramid, **loc_Sand_Underground, **loc_Sand_Postgame},
    {**loc_Wooded, **loc_Wooded_Post_Story1, **loc_Wooded_Peace, **loc_Wooded_Post_Metro, **loc_Wooded_Postgame},
    {**loc_Lake, **loc_Lake_Post_Seaside, **loc_Lake_Postgame},
    {**loc_Cloud, **loc_Cloud_Postgame},
    {**loc_Lost, **loc_Lost_Revisit, **loc_Lost_Postgame},
    {**loc_Night_Metro, **loc_Metro, **loc_Metro_Sewer_Access, **loc_Metro_Peace, **loc_Metro_Post_Sand, **loc_Metro_Postgame},
    {**loc_Seaside, **loc_Seaside_Peace, **loc_Seaside_Postgame},
    {**loc_Snow, **loc_Snow_Peace, **loc_Snow_Postgame},
    {**loc_Luncheon, **loc_Luncheon_Post_Spewart, **loc_Luncheon_Post_Cheese_Rocks, **loc_Luncheon_Peace, **loc_Luncheon_Post_Wooded, **loc_Luncheon_Postgame},
    {**loc_Ruined, **loc_Ruined_Postgame},
    {**loc_Bowser, **loc_Bowser_Infiltrate, **loc_Bowser_Post_Bombing, **loc_Bowser_Mecha_Broodal, **loc_Bowser_Peace, **loc_Bowser_Postgame},
    {**loc_Moon, **loc_Moon_Postgame},
    {**loc_Mushroom, **loc_Mushroom_Post_Luncheon},
    loc_Dark,
    loc_Darker
]

post_game_locations_list = [
    loc_Cap_Postgame,
    loc_Cascade_Postgame,
    loc_Sand_Postgame,
    loc_Lake_Postgame,
    loc_Wooded_Postgame,
    loc_Cloud_Postgame,
    loc_Lost_Postgame,
    loc_Metro_Postgame,
    loc_Snow_Postgame,
    loc_Seaside_Postgame,
    loc_Luncheon_Postgame,
    loc_Ruined_Postgame,
    loc_Bowser_Postgame,
    loc_Moon_Postgame
]

multi_moons = {
    "Cascade" : [SMOLocationData.multi_moon_atop_the_falls],
    "Sand" : [SMOLocationData.showdown_on_the_inverted_pyramid,
    SMOLocationData.the_hole_in_the_desert],
    "Lake" : [SMOLocationData.broodals_over_the_lake],
    "Wooded" : [SMOLocationData.flower_thieves_of_sky_garden,
    SMOLocationData.defend_the_secret_flower_field],
    "Metro" : [SMOLocationData.new_donk_citys_pest_problem,
    SMOLocationData.a_traditional_festival],
    "Snow" : [SMOLocationData.the_bound_bowl_grand_prix],
    "Seaside" : [SMOLocationData.the_glass_is_half_full],
    "Luncheon" : [SMOLocationData.big_pot_on_the_volcano_dive_in,
    SMOLocationData.cookatiel_showdown],
    "Ruined" : [SMOLocationData.battle_with_the_lord_of_lightning],
    "Bowser" : [SMOLocationData.showdown_at_bowsers_castle],
    "Mushroom" : [SMOLocationData.tussle_in_tostarena_rematch,
    SMOLocationData.struggle_in_steam_gardens_rematch,
    SMOLocationData.dust_up_in_new_donk_city_rematch,
    SMOLocationData.battle_in_bubblaine_rematch,
    SMOLocationData.blowup_at_mount_volbono_rematch,
    SMOLocationData.rumble_in_crumbleden_rematch],
    "Dark" : [SMOLocationData.arrival_at_rabbit_ridge],
    "Darker" : [SMOLocationData.a_long_journeys_end]
}

story_moons = {
    "Cascade" : [SMOLocationData.our_first_power_moon],
    "Sand" : [SMOLocationData.atop_the_highest_tower,
    SMOLocationData.moon_shards_in_the_sand],
    "Wooded" : [SMOLocationData.road_to_sky_garden,
    SMOLocationData.path_to_the_secret_flower_field],
    "Metro" : [SMOLocationData.drummer_on_board,
    SMOLocationData.guitarist_on_board,
    SMOLocationData.bassist_on_board,
    SMOLocationData.trumpeter_on_board,
    SMOLocationData.powering_up_the_station],
    "Snow" : [SMOLocationData.the_icicle_barrier,
    SMOLocationData.the_ice_wall_barrier,
    SMOLocationData.the_gusty_barrier,
    SMOLocationData.the_snowy_mountain_barrier],
    "Seaside" : [SMOLocationData.the_stone_pillar_seal,
    SMOLocationData.the_lighthouse_seal,
    SMOLocationData.the_hot_spring_seal,
    SMOLocationData.the_seal_above_the_canyon],
    "Luncheon" : [SMOLocationData.the_broodals_are_after_some_cookin,
    SMOLocationData.under_the_cheese_rocks,
    SMOLocationData.climb_up_the_cascading_magma],
    "Bowser" : [SMOLocationData.infiltrate_bowsers_castle,
    SMOLocationData.smart_bombing,
    SMOLocationData.big_broodal_battle]
}

goals_table = {
    Goal.option_sand : SMOLocationData.the_hole_in_the_desert,
    Goal.option_lake : SMOLocationData.broodals_over_the_lake,
    Goal.option_metro : SMOLocationData.a_traditional_festival,
    Goal.option_luncheon : SMOLocationData.cookatiel_showdown,
    Goal.option_moon : SMOLocationData.beat_the_game,
    Goal.option_dark : SMOLocationData.arrival_at_rabbit_ridge,
    Goal.option_darker : SMOLocationData.a_long_journeys_end
}