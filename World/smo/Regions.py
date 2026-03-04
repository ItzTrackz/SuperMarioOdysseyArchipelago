from types import NoneType
from typing import Optional, Any
from BaseClasses import Region, Entrance, EntranceType, CollectionState
from . import world_list, capture_items
from .Rules import SMORuleCondition, SMORuleOperation, create_access_rule
from .Data.EntranceData import SMOEntrance
from .Data.ItemData import SMOItemData
from .Entrances import create_entrances, SMORandomizationGroup
from .Locations import SMOLocation, loc_Cap, loc_Cascade, loc_Cascade_Revisit, \
    loc_Sand, loc_Lake, loc_Wooded, loc_Cloud, loc_Lost, loc_Lost_Revisit, loc_Metro, \
    loc_Snow, loc_Seaside, loc_Luncheon, loc_Ruined, loc_Bowser, loc_Moon, \
    locations_table, post_game_locations_table, loc_Dark, loc_Darker, special_locations_table, \
    loc_Cap_Shop, loc_Cascade_Shop, loc_Sand_Shop, loc_Lake_Shop, loc_Wooded_Shop, \
    loc_Lost_Shop, loc_Metro_Shop, loc_Snow_Shop, loc_Seaside_Shop, loc_Luncheon_Shop, \
    loc_Bowser_Shop, loc_Moon_Shop, loc_Mushroom_Shop, loc_Dark_Outfit, loc_Darker_Outfit, \
    loc_Sand_Revisit, loc_Lake_Post_Seaside, loc_Wooded_Post_Metro, loc_Metro_Post_Sand, \
    loc_Cascade_Post_Metro, loc_Cascade_Post_Snow, loc_Post_Cloud, loc_Moon_Post_Moon, \
    loc_Luncheon_Post_Wooded, loc_Mushroom_Post_Luncheon, loc_Sand_Peace, loc_Wooded_Post_Story1, \
    loc_Wooded_Peace, loc_Metro_Peace, loc_Snow_Peace, loc_Seaside_Peace, \
    loc_Luncheon_Post_Spewart, loc_Luncheon_Post_Cheese_Rocks, loc_Luncheon_Peace, \
    loc_Bowser_Infiltrate, loc_Bowser_Post_Bombing, loc_Bowser_Peace, loc_Postgame_Shop, loc_Sand_Pyramid, \
    loc_Sand_Underground, loc_Bowser_Mecha_Broodal, loc_Cascade_Peace, loc_Moon_Outfit, loc_Night_Metro, \
    loc_Mushroom, sub_area_frog, sub_area_poison_tide, sub_area_push_block, \
    sub_area_rolling, sub_area_chain_chomp, sub_area_trex_nest, sub_area_cascade_2d, \
    sub_area_gusty_bridges, sub_area_invisible_maze, sub_area_bullet_bill_maze, sub_area_jaxi, \
    sub_area_strange_neighborhood, sub_area_sand_outfit, sub_area_sand_rumbling_floor, \
    sub_area_sand_employee, sub_area_jaxi_ruins, sub_area_sand_sphinx, sub_area_sand_slots, sub_area_sand_underground, \
    sub_area_sand_arena, sub_area_sand_arena_peace, sub_area_sand_arena_post, sub_area_transparent_platform, \
    sub_area_colossal_ruins, sub_area_freezing_waterway, sub_area_repair, sub_area_zipper, sub_area_jump_grab_climb, \
    sub_area_waves_poison, sub_area_woods_treasure_trap, sub_area_explorer, sub_area_flooding_pipe, \
    sub_area_flower_road, sub_area_elevator_escalation, sub_area_wooded_fog, sub_area_wooded_clouds, \
    sub_area_flower_field, sub_area_flower_field_peace, sub_area_nut_room, sub_area_wooded_invisible_road, \
    sub_area_sheep, sub_area_wooded_breakdown_road, sub_area_cloud_picture, sub_area_cloud_picture_post, sub_area_cube, \
    sub_area_jungle, sub_area_klepto, sub_area_metro_slots, sub_area_rc, sub_area_rc_post, sub_area_private_room, \
    sub_area_city_hall, sub_area_crowd, sub_area_rewiring, sub_area_siege, sub_area_rotating_maze, sub_area_high_rise, \
    sub_area_bullet_billding, sub_area_motor_scooter, sub_area_big_screen, sub_area_pitch_black, \
    sub_area_swinging_scaffolding, sub_area_motor_daredevil, sub_area_crowd_post_game, sub_area_sewer, \
    sub_area_sewer_post_game, sub_area_sandy_bottom, sub_area_seaside_waterway, sub_area_seaside_sphynx, \
    sub_area_seaside_rumble, sub_area_resort, sub_area_cloud_sea, sub_area_valley, sub_area_seaside_stretch, \
    sub_area_seaside_pokio, sub_area_seaside_maze, sub_area_icicle_post, sub_area_ice_wall_post, \
    sub_area_gusty_barrier_post, \
    sub_area_snowy_mountain_post, sub_area_magma_swamp, sub_area_veggies, sub_area_cook, sub_area_forks, \
    sub_area_cheese, sub_area_lava_bubble, sub_area_spinning_athletics, sub_area_luncheon_story, \
    sub_area_luncheon_slots, sub_area_gear_steps, sub_area_volcano_cave, sub_area_lava_islands, sub_area_roulette_tower, \
    sub_area_ruined_charging, sub_area_samurai, sub_area_bowser_vault, sub_area_jizo_adventure, sub_area_spinning_tower, \
    sub_area_hexagon_tower, sub_area_wooden_tower, sub_area_galaxy, sub_area_swings, sub_area_sphynx_moon, \
    sub_area_mushroom_picture, sub_area_64, sub_area_castle, sub_area_mushroom_well, sub_area_yoshi_clouds, \
    sub_area_rematch_tostarena, sub_area_rematch_steam_gardens, sub_area_rematch_bubblaine, sub_area_rematch_metro, \
    sub_area_rematch_volbono, sub_area_rematch_crumbleden, sub_area_darker_invisible, sub_area_darker_breakdown, \
    sub_area_darker_vanishing, sub_area_darker_yoshi_siege, sub_area_darker_yoshi_sinking, sub_area_darker_yoshi_magma, \
    sub_area_inverted_pyramid, loc_odyssey_outfit, sub_area_mysterious_clouds, sub_area_moon_cave, sub_area_snow_outfit, \
    sub_area_snow_koopa, sub_area_snow_dashing, sub_area_snow_freezing_water, sub_area_blowing, sub_area_snow_spinning, \
    sub_area_snow_flower_road, sub_area_iceburn, sub_area_bowser_clouds, shop_sand_coin, shop_wooded_coin, \
    shop_lake_coin, shop_metro_coin, shop_seaside_coin, shop_luncheon_coin, shop_moon_coin, shop_post_game_coin, \
    loc_Cap_Postgame, loc_Cascade_Postgame, loc_Sand_Postgame, loc_Wooded_Postgame, loc_Lake_Postgame, \
    loc_Cloud_Postgame, loc_Lost_Postgame, loc_Metro_Postgame, loc_Seaside_Postgame, loc_Snow_Postgame, \
    loc_Luncheon_Postgame, loc_Ruined_Postgame, loc_Bowser_Postgame, loc_Moon_Postgame, sub_area_church, \
    sub_area_shiveria, sub_area_shiveria_peace, sub_area_snowline, loc_Night_Sand, loc_Sand_Pyramid_Peace, \
    loc_Sand_Pyramid_Mural
from .Data.RegionData import SMORegion
from .Data.LocationData import SMOLocationData
from .Logic import count_moons, total_moons
from entrance_rando import randomize_entrances, disconnect_entrance_for_randomization



def create_region(self, region_data : tuple):
    """ Creates the regions for Super Mario Odyssey.
            Args:
                self: SMOWorld object for this player's world.
                region_data: Tuple containing region information.
    """
    region = Region(region_data[0], self.player, self.multiworld)
    self.multiworld.regions.append(region)
    if len(region_data) > 2:
        if self.options.goal >= region_data[2] or self.options.entrance_randomization > self.options.entrance_randomization.option_off:
            create_locations(region, *region_data[1])
    else:
        if len(region_data) > 1:
            create_locations(region, *region_data[1])
        else:
            print(region.name)
        
def connect_region(self, connection_data : tuple):
    """ Connects Super Mario Odyssey Regions
    :param self: SMOWorld object for this player's world.
    :param connection_data: Tuple containing connection information.
    :return:
    """
    cur_region : Region = self.multiworld.get_region(connection_data[0], self.player)
    if isinstance(connection_data[1], dict):
        for connection in connection_data[1].keys():
            if connection in self.multiworld.regions.region_cache[self.player]:
                connecting_region : Region = self.multiworld.get_region(connection, self.player)
                if callable(connection_data[1][connection]):
                    cur_region.connect(connecting_region, f"{cur_region.name} -> {connecting_region.name}", connection_data[1][connection])
                else:
                    cur_region.connect(connecting_region, f"{cur_region.name} -> {connecting_region.name}")

def create_two_way_entrance_rando_pair(cur_region: Region, enter_name: str, exit_name: str, cur_origin_region: Optional[Region] = None) -> tuple[Entrance, Entrance]:
    """
            :param cur_region: current Region.
            :param enter_name: Name of Entrance pair.
            :param exit_name: Name of Entrance pair.
            :param cur_origin_region: The region the current region descends from.
            :return: Tuple containing the Entrance pair.
    """
    if cur_origin_region:
        region_entry = cur_origin_region.create_er_target(enter_name)
    else:
        region_entry = cur_region.create_er_target(enter_name)
    region_exit = cur_region.create_exit(exit_name)
    region_entry.connected_region = cur_region
    region_exit.parent_region = cur_region
    region_entry.randomization_type = EntranceType.TWO_WAY
    region_exit.randomization_type = EntranceType.TWO_WAY

    return region_entry, region_exit

def create_two_way_entrance_pair(cur_region: Region, enter_name: str, exit_name: str, connecting_region: Region, cur_origin_region: Optional[Region] = None) -> tuple[Entrance, Entrance]:
    """
                :param cur_region: current Region.
                :param enter_name: Name of Entrance pair.
                :param exit_name: Name of Entrance pair.
                :param connecting_region: Region this entrance/exit pair connects to.
                :param cur_origin_region: The region the current region descends from.
                :return: Tuple containing the Entrance pair.
    """
    alternate_entrances = {
        SMOEntrance.top_hat_tower_enter: SMORegion.top_hat_tower,
        SMOEntrance.top_hat_tower_end: SMORegion.top_hat_tower,
        SMOEntrance.deepest_underground_shortcut: SMORegion.deepest_underground,
    }
    region_entry, region_exit = create_two_way_entrance_rando_pair(cur_region, enter_name, exit_name, cur_origin_region)

    region_entry.parent_region = connecting_region
    region_exit.connected_region = connecting_region

    return region_entry, region_exit

def create_one_way_entrance_for_entrance_rando(cur_region: Region, name: str) ->  Entrance:
    """
            :param cur_region: current Region.
            :param name: Name of Entrance pair.
            :return: One-way Entrance.
    """
    region_entry = cur_region.create_er_target(name)
    region_entry.connected_region = cur_region
    region_entry.randomization_type = EntranceType.ONE_WAY

    return region_entry

def create_one_way_exit_for_entrance_rando(cur_region: Region, name: str) ->  Entrance:
    """
            :param cur_region: current Region.
            :param name: Name of Entrance pair.
            :return: One-way Entrance.
    """
    region_exit = cur_region.create_exit(name)
    region_exit.parent_region = cur_region
    region_exit.randomization_type = EntranceType.ONE_WAY

    return region_exit

def create_one_way_entrance(cur_region: Region, name: str, connecting_region: Region) -> Entrance:
    """
                :param cur_region: current Region you are entering.
                :param name: Name of Entrance pair.
                :param connecting_region: Region this entrance/exit pair connects to.
                :return: One-way Entrance.
    """
    alternate_entrances = {
        SMOEntrance.top_hat_tower_enter: SMORegion.top_hat_tower,
        SMOEntrance.top_hat_tower_end: SMORegion.top_hat_tower,
        SMOEntrance.deepest_underground_shortcut: SMORegion.deepest_underground,
    }
    region_entrance = create_one_way_entrance_for_entrance_rando(cur_region, name)

    region_entrance.parent_region = connecting_region

    return region_entrance

def create_one_way_exit(cur_region: Region, name: str, connecting_region: Region) -> Entrance:
    """
                :param cur_region: current Region being exited from.
                :param name: Name of Entrance pair.
                :param connecting_region: Region this entrance/exit pair connects to.
                :return: One-way Entrance.
    """
    alternate_entrances = {
        SMOEntrance.top_hat_tower_enter: SMORegion.top_hat_tower,
        SMOEntrance.top_hat_tower_end: SMORegion.top_hat_tower,
        SMOEntrance.deepest_underground_shortcut: SMORegion.deepest_underground,
    }
    region_exit = create_one_way_exit_for_entrance_rando(cur_region, name)

    region_exit.connected_region = connecting_region

    return region_exit

def create_regions(self):
    """ Creates the regions for Super Mario Odyssey.
            Args:
                self: SMOWorld object for this player's world.
    """

    def connect_coin_shops(region_connections : dict):
        region_connections[SMORegion.shop_sand_coin] = lambda state: state.can_reach(
            self.multiworld.get_region(SMORegion.restored_odyssey, self.player))
        region_connections[SMORegion.shop_lake_coin] = lambda state: state.can_reach(
            self.multiworld.get_region(SMORegion.odyssey_broken_down, self.player))
        region_connections[SMORegion.shop_wooded_coin] = lambda state: state.can_reach(
            self.multiworld.get_region(SMORegion.odyssey_broken_down, self.player))
        region_connections[SMORegion.shop_metro_coin] = lambda state: state.can_reach(
            self.multiworld.get_region(SMORegion.odyssey_repaired_lost, self.player))
        region_connections[SMORegion.shop_seaside_coin] = lambda state: state.can_reach(
            self.multiworld.get_region(SMORegion.odyssey_sails_branch_2, self.player))
        region_connections[SMORegion.shop_luncheon_coin] = lambda state: state.can_reach(
            self.multiworld.get_region(SMORegion.odyssey_sails_branch_2, self.player))
        region_connections[SMORegion.shop_moon_coin] = lambda state: state.can_reach(
            self.multiworld.get_region(SMORegion.odyssey_complete, self.player))
        region_connections[SMORegion.shop_mushroom_coin] = can_reach_mushroom
        region_connections[SMORegion.post_game_coin_outfits] = can_reach_mushroom

    #region Regions

    odyssey_regions = [
        (SMORegion.defunct_odyssey, {}, self.options.goal.option_sand),
        (SMORegion.restored_odyssey, {}, self.options.goal.option_sand),
        (SMORegion.odyssey_interior, {}, self.options.goal.option_sand),
        (SMORegion.odyssey_sail_sand, {}, self.options.goal.option_lake),
        (SMORegion.odyssey_broken_down, {}, self.options.goal.option_metro),
        (SMORegion.odyssey_repaired_lost, {}, self.options.goal.option_metro),
        (SMORegion.odyssey_sail_metro, {}, self.options.goal.option_luncheon),
        (SMORegion.odyssey_sails_branch_2, {}, self.options.goal.option_luncheon),
        (SMORegion.odyssey_sail_luncheon, {}, self.options.goal.option_moon),
        (SMORegion.odyssey_repaired_ruined, {}, self.options.goal.option_moon),
        (SMORegion.odyssey_complete, {}, self.options.goal.option_moon),
        (SMORegion.odyssey_powered_up_dark, {}, self.options.goal.option_dark),
        (SMORegion.odyssey_powered_up_darker, {}, self.options.goal.option_darker),
        #("Odyssey Turns Gold", self.options.goal.option_sand), # For AUM / All achievements goal possibly


    ]

    world_regions = [
        (SMORegion.menu, {}, self.options.goal.option_sand),
        (SMORegion.cap_kingdom_intro, {}, self.options.goal.option_sand),
        (SMORegion.cap_kingdom_topper, {}, self.options.goal.option_sand),
        (SMORegion.cap_kingdom, loc_Cap, self.options.goal.option_sand),
        (SMORegion.cascade_kingdom, loc_Cascade, self.options.goal.option_sand),
        (SMORegion.cascade_kingdom_peace, loc_Cascade_Peace, self.options.goal.option_sand),
        (SMORegion.cascade_kingdom_revisit, loc_Cascade_Revisit, self.options.goal.option_sand),
        (SMORegion.sand_kingdom, loc_Sand, self.options.goal.option_sand),
        (SMORegion.night_sand_kingdom, loc_Night_Sand, self.options.goal.option_sand),
        (SMORegion.top_of_the_inverted_pyramid, loc_Sand_Pyramid, self.options.goal.option_sand),
        (SMORegion.sand_kingdom_peace, loc_Sand_Peace, self.options.goal.option_sand),
        (SMORegion.top_of_the_inverted_pyramid_peace, loc_Sand_Pyramid_Peace, self.options.goal.option_sand),
        (SMORegion.wooded_kingdom, loc_Wooded, self.options.goal.option_lake),
        (SMORegion.wooded_kingdom_post_broodals, loc_Wooded_Post_Story1, self.options.goal.option_lake),
        (SMORegion.wooded_kingdom_peace, loc_Wooded_Peace, self.options.goal.option_lake),
        (SMORegion.lake_kingdom, loc_Lake, self.options.goal.option_lake),
        (SMORegion.cloud_kingdom_boss_fight, loc_Post_Cloud, self.options.goal.option_metro),
        (SMORegion.cloud_kingdom_revisit, loc_Cloud, self.options.goal.option_metro),
        (SMORegion.lost_kingdom, loc_Lost, self.options.goal.option_metro),
        (SMORegion.lost_kingdom_revisit, loc_Lost_Revisit, self.options.goal.option_metro),
        (SMORegion.night_metro_kingdom, loc_Night_Metro, self.options.goal.option_metro),
        (SMORegion.day_metro_kingdom, loc_Metro, self.options.goal.option_metro),
        (SMORegion.metro_kingdom_peace, loc_Metro_Peace, self.options.goal.option_metro),
        (SMORegion.seaside_kingdom, loc_Seaside, self.options.goal.option_luncheon),
        (SMORegion.seaside_kingdom_peace, loc_Seaside_Peace, self.options.goal.option_luncheon),
        (SMORegion.snow_kingdom, loc_Snow, self.options.goal.option_luncheon),
        (SMORegion.snow_kingdom_peace, loc_Snow_Peace, self.options.goal.option_luncheon),
        (SMORegion.luncheon_kingdom, loc_Luncheon, self.options.goal.option_luncheon),
        (SMORegion.luncheon_kingdom_post_broodals, loc_Luncheon_Post_Spewart, self.options.goal.option_luncheon),
        (SMORegion.luncheon_kingdom_meat, loc_Luncheon_Post_Cheese_Rocks, self.options.goal.option_luncheon),
        (SMORegion.luncheon_kingdom_peace, loc_Luncheon_Peace, self.options.goal.option_luncheon),
        (SMORegion.ruined_kingdom, loc_Ruined, self.options.goal.option_moon),
        (SMORegion.bowsers_kingdom, loc_Bowser, self.options.goal.option_moon),
        (SMORegion.infiltrate_bowsers_castle, loc_Bowser_Infiltrate, self.options.goal.option_moon),
        (SMORegion.bowser_kingdom_smart_bombing, loc_Bowser_Post_Bombing, self.options.goal.option_moon),
        (SMORegion.bowser_kingdom_mecha_broodal, loc_Bowser_Mecha_Broodal, self.options.goal.option_moon),
        (SMORegion.bowser_kingdom_peace, loc_Bowser_Peace, self.options.goal.option_moon),
        (SMORegion.moon_kingdom, loc_Moon_Post_Moon, self.options.goal.option_moon),
        (SMORegion.moon_kingdom_peace, loc_Moon, self.options.goal.option_moon),
        (SMORegion.mushroom_kingdom, loc_Mushroom, self.options.goal.option_dark),
        (SMORegion.dark_side, {}, self.options.goal.option_dark),
        (SMORegion.dark_side_2, {}, self.options.goal.option_dark),
        (SMORegion.dark_side_3, {}, self.options.goal.option_dark),
        (SMORegion.dark_side_4, {}, self.options.goal.option_dark),
        (SMORegion.dark_side_5, {}, self.options.goal.option_dark),
        (SMORegion.dark_side_peace, loc_Dark, self.options.goal.option_dark),
        (SMORegion.darker_side, {}, self.options.goal.option_darker),
        (SMORegion.darker_side_tower, loc_Darker, self.options.goal.option_darker),
        (SMORegion.cap_kingdom_moon_rock, loc_Cap_Postgame, self.options.goal.option_dark),
        (SMORegion.cascade_kingdom_moon_rock, loc_Cascade_Postgame, self.options.goal.option_dark),
        (SMORegion.sand_kingdom_moon_rock, loc_Sand_Postgame, self.options.goal.option_dark),
        (SMORegion.wooded_kingdom_moon_rock, loc_Wooded_Postgame, self.options.goal.option_dark),
        (SMORegion.lake_kingdom_moon_rock, loc_Lake_Postgame, self.options.goal.option_dark),
        (SMORegion.cloud_kingdom_moon_rock, loc_Cloud_Postgame, self.options.goal.option_dark),
        (SMORegion.lost_kingdom_moon_rock, loc_Lost_Postgame, self.options.goal.option_dark),
        (SMORegion.metro_kingdom_moon_rock, loc_Metro_Postgame, self.options.goal.option_dark),
        (SMORegion.seaside_kingdom_moon_rock, loc_Seaside_Postgame, self.options.goal.option_dark),
        (SMORegion.snow_kingdom_moon_rock, loc_Snow_Postgame, self.options.goal.option_dark),
        (SMORegion.luncheon_kingdom_moon_rock, loc_Luncheon_Postgame, self.options.goal.option_dark),
        (SMORegion.ruined_kingdom_moon_rock, loc_Ruined_Postgame, self.options.goal.option_dark),
        (SMORegion.bowser_kingdom_moon_rock, loc_Bowser_Postgame, self.options.goal.option_dark),
        (SMORegion.moon_kingdom_moon_rock, loc_Moon_Postgame, self.options.goal.option_dark),

    ]

    capture_regions = [
        (SMORegion.frog, {SMOItemData.frog: 3701}),
        (SMORegion.spark_pylon, {SMOItemData.spark_pylon: 3702}),
        (SMORegion.paragoomba, {SMOItemData.paragoomba: 3703}),
        (SMORegion.chain_chomp, {SMOItemData.chain_chomp: 3704}),
        (SMORegion.big_chain_chomp, {SMOItemData.big_chain_chomp: 3705}),
        (SMORegion.broodes_chain_chomp, {SMOItemData.broodes_chain_chomp: 3706}),
        (SMORegion.t_rex, {SMOItemData.t_rex: 3707}),
        (SMORegion.binoculars, {SMOItemData.binoculars: 3708}),
        (SMORegion.bullet_bill, {SMOItemData.bullet_bill: 3709}),
        (SMORegion.moe_eye, {SMOItemData.moe_eye: 3710}),
        (SMORegion.cactus, {SMOItemData.cactus: 3711}),
        (SMORegion.goomba, {SMOItemData.goomba: 3712}),
        (SMORegion.knucklotecs_fist, {SMOItemData.knucklotecs_fist: 3713}),
        (SMORegion.mini_rocket, {SMOItemData.mini_rocket: 3714}),
        (SMORegion.glydon, {SMOItemData.glydon: 3715}),
        (SMORegion.lakitu, {SMOItemData.lakitu: 3716}),
        (SMORegion.zipper, {SMOItemData.zipper: 3717}),
        (SMORegion.cheep_cheep, {SMOItemData.cheep_cheep: 3718}),
        (SMORegion.puzzle_part_lake_kingdom, {SMOItemData.puzzle_part_lake_kingdom: 3719}),
        (SMORegion.poison_piranha_plant, {SMOItemData.poison_piranha_plant: 3720}),
        (SMORegion.uproot, {SMOItemData.uproot: 3721}),
        (SMORegion.fire_bro, {SMOItemData.fire_bro: 3722}),
        (SMORegion.sherm, {SMOItemData.sherm: 3723}),
        (SMORegion.coin_coffer, {SMOItemData.coin_coffer: 3724}),
        (SMORegion.tree, {SMOItemData.tree: 3725}),
        (SMORegion.boulder, {SMOItemData.boulder: 3726}),
        (SMORegion.picture_match_part_goomba, {SMOItemData.picture_match_part_goomba: 3727}),
        (SMORegion.tropical_wiggler, {SMOItemData.tropical_wiggler: 3728}),
        (SMORegion.pole, {SMOItemData.pole: 3729}),
        (SMORegion.manhole, {SMOItemData.manhole: 3730}),
        (SMORegion.taxi, {SMOItemData.taxi: 3731}),
        (SMORegion.rc_car, {SMOItemData.rc_car: 3732}),
        (SMORegion.ty_foo, {SMOItemData.ty_foo: 3733}),
        (SMORegion.shiverian_racer, {SMOItemData.shiverian_racer: 3734}),
        (SMORegion.cheep_cheep_snow_kingdom, {SMOItemData.cheep_cheep_snow_kingdom: 3735}),
        (SMORegion.gushen, {SMOItemData.gushen: 3736}),
        (SMORegion.lava_bubble, {SMOItemData.lava_bubble: 3737}),
        (SMORegion.volbonan, {SMOItemData.volbonan: 3738}),
        (SMORegion.hammer_bro, {SMOItemData.hammer_bro: 3739}),
        (SMORegion.meat, {SMOItemData.meat: 3740}),
        (SMORegion.fire_piranha_plant, {SMOItemData.fire_piranha_plant: 3741}),
        (SMORegion.pokio, {SMOItemData.pokio: 3742}),
        (SMORegion.jizo, {SMOItemData.jizo: 3743}),
        (SMORegion.bowser_statue, {SMOItemData.bowser_statue: 3744}),
        (SMORegion.parabones, {SMOItemData.parabones: 3745}),
        (SMORegion.banzai_bill, {SMOItemData.banzai_bill: 3746}),
        (SMORegion.chargin_chuck, {SMOItemData.chargin_chuck: 3747}),
        (SMORegion.bowser, { SMOItemData.bowser: 3748}),
        (SMORegion.letter, { SMOItemData.letter: 3749}, self.options.goal.option_dark),
        (SMORegion.puzzle_part_metro_kingdom, {SMOItemData.puzzle_part_metro_kingdom: 3750}, self.options.goal.option_dark),
        (SMORegion.picture_match_part_mario, {SMOItemData.picture_match_part_mario: 3751}, self.options.goal.option_dark),
        (SMORegion.yoshi, { SMOItemData.yoshi: 3752}, self.options.goal.option_dark),
    ]

    sub_area_regions = [
        (SMORegion.top_hat_tower, {}),
        (SMORegion.frog_pond, sub_area_frog),
        (SMORegion.poison_tides, sub_area_poison_tide),
        (SMORegion.push_block, sub_area_push_block),
        (SMORegion.rolling_lane, sub_area_rolling),
        (SMORegion.chain_chomp_cave, sub_area_chain_chomp),
        (SMORegion.t_rex_nest, sub_area_trex_nest),
        (SMORegion.chasm_lifts, sub_area_cascade_2d),
        (SMORegion.gusty_bridges, sub_area_gusty_bridges),
        (SMORegion.mysterious_clouds, sub_area_mysterious_clouds),
        (SMORegion.moe_eye_invisible_maze, sub_area_invisible_maze),
        (SMORegion.bullet_bill_maze, sub_area_bullet_bill_maze),
        (SMORegion.jaxi_ruins, sub_area_jaxi),
        (SMORegion.strange_neighborhood, sub_area_strange_neighborhood),
        (SMORegion.sand_outfit, sub_area_sand_outfit),
        (SMORegion.sand_rumbling_floor_house, sub_area_sand_rumbling_floor),
        (SMORegion.employees_only, sub_area_sand_employee),
        (SMORegion.ice_cave, sub_area_jaxi_ruins),
        (SMORegion.sand_sphynx_vault, sub_area_sand_sphinx),
        (SMORegion.sand_slots, sub_area_sand_slots),
        (SMORegion.inverted_pyramid_lower_interior, {}),
        (SMORegion.inverted_pyramid_mural, loc_Sand_Pyramid_Mural),
        (SMORegion.inverted_pyramid_upper_interior, sub_area_inverted_pyramid),
        (SMORegion.underground_ruins, sub_area_sand_underground),
        (SMORegion.deepest_underground, sub_area_sand_arena),
        (SMORegion.deepest_underground_peace, sub_area_sand_arena_peace),
        (SMORegion.deepest_underground_post_game, sub_area_sand_arena_post),
        (SMORegion.moe_eye_invisible_floor, sub_area_transparent_platform),
        (SMORegion.colossal_ruins, sub_area_colossal_ruins),
        (SMORegion.freezing_waterway, sub_area_freezing_waterway),
        (SMORegion.arch_repair, sub_area_repair),
        (SMORegion.zipper_chasm, sub_area_zipper),
        (SMORegion.bouncy_flowers, sub_area_jump_grab_climb),
        (SMORegion.poison_swamp, sub_area_waves_poison),
        (SMORegion.deep_woods_treasure_trap, sub_area_woods_treasure_trap),
        (SMORegion.explorer_outift, sub_area_explorer),
        (SMORegion.flooding_pipeway, sub_area_flooding_pipe),
        (SMORegion.wooded_flower_road, sub_area_flower_road),
        (SMORegion.sherm_elevator, sub_area_elevator_escalation),
        (SMORegion.fog_wandering, sub_area_wooded_fog),
        (SMORegion.walking_on_clouds, sub_area_wooded_clouds),
        (SMORegion.sky_garden_tower, {}), # Add locations
        (SMORegion.secret_flower_field, sub_area_flower_field),
        (SMORegion.secret_flower_field_peace, sub_area_flower_field_peace),
        (SMORegion.deep_woods, {}), # Add Locations
        (SMORegion.nut_room, sub_area_nut_room),
        (SMORegion.invisible_road, sub_area_wooded_invisible_road),
        (SMORegion.sheep_herding, sub_area_sheep),
        (SMORegion.breakdown_road, sub_area_wooded_breakdown_road),
        (SMORegion.cloud_picture_match, sub_area_cloud_picture),
        (SMORegion.cloud_post_game_picture_match, sub_area_cloud_picture_post),
        (SMORegion.king_of_the_cube, sub_area_cube),
        (SMORegion.tropical_wiggler_swamp, sub_area_jungle),
        (SMORegion.klepto_lava_bath, sub_area_klepto),
        (SMORegion.metro_slots, sub_area_metro_slots),
        (SMORegion.rc_race, sub_area_rc),
        (SMORegion.rc_race_post_game, sub_area_rc_post),
        (SMORegion.private_room, sub_area_private_room),
        (SMORegion.city_hall, sub_area_city_hall),
        (SMORegion.crowded_street, sub_area_crowd),
        (SMORegion.builder_outfit, sub_area_rewiring),
        (SMORegion.metro_siege, sub_area_siege),
        (SMORegion.rotating_maze, sub_area_rotating_maze),
        (SMORegion.high_rise, sub_area_high_rise),
        (SMORegion.bullet_billding, sub_area_bullet_billding),
        (SMORegion.t_rex_escape, sub_area_motor_scooter),
        (SMORegion.projection_room, sub_area_big_screen),
        (SMORegion.pitch_black_island, sub_area_pitch_black),
        (SMORegion.swinging_scaffolding, sub_area_swinging_scaffolding),
        (SMORegion.vanishing_road, sub_area_motor_daredevil),
        (SMORegion.crowded_street_post_game, sub_area_crowd_post_game),
        (SMORegion.sewers, sub_area_sewer),
        (SMORegion.sewers_post_game, sub_area_sewer_post_game),
        (SMORegion.sandy_bottom, sub_area_sandy_bottom),
        (SMORegion.seaside_waterway, sub_area_seaside_waterway),
        (SMORegion.seaside_sphynx_vault, sub_area_seaside_sphynx),
        (SMORegion.seaside_rumbling_room, sub_area_seaside_rumble),
        (SMORegion.resort_outfit, sub_area_resort),
        (SMORegion.wading_in_the_cloud_sea, sub_area_cloud_sea),
        (SMORegion.narrow_valley, sub_area_valley),
        (SMORegion.sinking_island, sub_area_seaside_stretch),
        (SMORegion.pokio_bomb_aiming, sub_area_seaside_pokio),
        (SMORegion.spinning_maze, sub_area_seaside_maze),
        (SMORegion.icicle_barrier_post_game, sub_area_icicle_post),
        (SMORegion.ice_wall_barrier_post_game, sub_area_ice_wall_post),
        (SMORegion.gusty_barrier_post_game, sub_area_gusty_barrier_post),
        (SMORegion.snowy_mountain_barrier_post_game, sub_area_snowy_mountain_post),
        (SMORegion.shiveria, sub_area_shiveria),
        (SMORegion.shiveria_peace, sub_area_shiveria_peace),
        (SMORegion.snowline_circuit, sub_area_snowline),
        (SMORegion.iceburn_circuit, sub_area_iceburn),
        (SMORegion.freezing_room, sub_area_snow_outfit),
        (SMORegion.ice_trace_walking, sub_area_snow_koopa),
        (SMORegion.rocket_flower_dash, sub_area_snow_dashing),
        (SMORegion.freezing_water, sub_area_snow_freezing_water),
        (SMORegion.ty_foo_sliding_puzzle, sub_area_blowing),
        (SMORegion.above_the_clouds, sub_area_snow_spinning),
        (SMORegion.snow_flower_road, sub_area_snow_flower_road),
        (SMORegion.magma_swamp, sub_area_magma_swamp),
        (SMORegion.luncheon_treasure_vault, sub_area_veggies),
        (SMORegion.chef_outfit, sub_area_cook),
        (SMORegion.fork_flickin, sub_area_forks),
        (SMORegion.cheese_excavate, sub_area_cheese),
        (SMORegion.magma_narrow_path, sub_area_lava_bubble),
        (SMORegion.spinning_athletics, sub_area_spinning_athletics),
        (SMORegion.cascading_magma, sub_area_luncheon_story),
        (SMORegion.luncheon_slots, sub_area_luncheon_slots),
        (SMORegion.rotating_gears_with_bitefrost, sub_area_gear_steps),
        (SMORegion.volcano_cave, sub_area_volcano_cave),
        (SMORegion.lava_islands, sub_area_lava_islands),
        (SMORegion.roulette_tower, sub_area_roulette_tower),
        (SMORegion.chargin_chuck_arena, sub_area_ruined_charging),
        (SMORegion.folding_screen, sub_area_samurai),
        (SMORegion.bowsers_treasure_vault, sub_area_bowser_vault),
        (SMORegion.jizos_adventure, sub_area_jizo_adventure),
        (SMORegion.spinning_tower, sub_area_spinning_tower),
        (SMORegion.hexagon_tower, sub_area_hexagon_tower),
        (SMORegion.wooden_tower, sub_area_wooden_tower),
        (SMORegion.dashing_above_the_clouds, sub_area_bowser_clouds),
        (SMORegion.moon_cave, sub_area_moon_cave),
        (SMORegion.inside_the_church, sub_area_church),
        (SMORegion.dot_galaxy, sub_area_galaxy),
        (SMORegion.giant_swings, sub_area_swings),
        (SMORegion.moon_sphynx_vault, sub_area_sphynx_moon),
        (SMORegion.mushroom_picture_match, sub_area_mushroom_picture),
        (SMORegion.peachs_castle, sub_area_castle),
        (SMORegion.castle_courtyard, sub_area_64, self.options.goal.option_dark),
        (SMORegion.mushroom_well, sub_area_mushroom_well, self.options.goal.option_dark),
        (SMORegion.yoshi_in_the_sea_of_clouds, sub_area_yoshi_clouds, self.options.goal.option_dark),
        (SMORegion.knucklotec_rematch, sub_area_rematch_tostarena, self.options.goal.option_dark),
        (SMORegion.torkdrift_rematch, sub_area_rematch_steam_gardens, self.options.goal.option_dark),
        (SMORegion.mollosque_lanceur_rematch, sub_area_rematch_bubblaine, self.options.goal.option_dark),
        (SMORegion.mecha_wiggler_rematch, sub_area_rematch_metro, self.options.goal.option_dark),
        (SMORegion.cookatiel_rematch, sub_area_rematch_volbono, self.options.goal.option_dark),
        (SMORegion.lord_of_lightning_rematch, sub_area_rematch_crumbleden, self.options.goal.option_dark),
        (SMORegion.painting_room_knucklotec, {}),
        (SMORegion.painting_room_torkdrift, {}),
        (SMORegion.painting_room_mollusque_lanceur, {}),
        (SMORegion.painting_room_mecha_wiggler, {}),
        (SMORegion.painting_room_cookatiel, {}),
        (SMORegion.painting_room_lord_of_lightning, {}),
        (SMORegion.dark_side_breakdown_road, sub_area_darker_breakdown, self.options.goal.option_darker),
        (SMORegion.dark_side_invisible_road, sub_area_darker_invisible, self.options.goal.option_darker),
        (SMORegion.dark_side_vanishing_road, sub_area_darker_vanishing, self.options.goal.option_darker),
        (SMORegion.dark_side_under_siege, sub_area_darker_yoshi_siege, self.options.goal.option_darker),
        (SMORegion.dark_side_sinking_island, sub_area_darker_yoshi_sinking, self.options.goal.option_darker),
        (SMORegion.dark_side_magma_swamp, sub_area_darker_yoshi_magma, self.options.goal.option_darker),
        (SMORegion.dark_side_topper, {}),
        (SMORegion.dark_side_harriet, {}),
        (SMORegion.dark_side_rango, {}),
        (SMORegion.dark_side_spewart, {}),
        (SMORegion.darker_side_entrance, {}),
        (SMORegion.darker_side_climb, {}),
        (SMORegion.darker_side_bowser, {}),
        (SMORegion.darker_side_end, {}),
        # (SMORegion.sand_kingdom_shop, loc_Sand_Shop), # Add Shop Room Sub Areas
        # (SMORegion.lake_kingdom_shop, loc_Lake_Shop),
        # (SMORegion.lost_kingdom_shop, loc_Lost_Shop),
        # (SMORegion.metro_kingdom_shop, loc_Metro_Shop),
        # (SMORegion.snow_kingdom_shop, loc_Snow_Shop),
        # (SMORegion.luncheon_kingdom_shop, loc_Luncheon_Shop),
        # (SMORegion.bowser_kingdom_shop, loc_Bowser_Shop),
        # (SMORegion.moon_kingdom_shop, loc_Moon_Shop),
        # (SMORegion.mushroom_kingdom_shop, loc_Mushroom_Shop),
    ]

    shop_regions = [
        (SMORegion.odyssey_outfit, loc_odyssey_outfit),
        (SMORegion.cap_kingdom_shop, loc_Cap_Shop),
        (SMORegion.cascade_kingdom_shop, loc_Cascade_Shop),
        (SMORegion.sand_kingdom_shop, loc_Sand_Shop, self.options.goal.option_sand),
        (SMORegion.wooded_kingdom_shop, loc_Wooded_Shop, self.options.goal.option_lake),
        (SMORegion.lake_kingdom_shop, loc_Lake_Shop, self.options.goal.option_lake),
        (SMORegion.lost_kingdom_shop, loc_Lost_Shop, self.options.goal.option_metro),
        (SMORegion.metro_kingdom_shop, loc_Metro_Shop, self.options.goal.option_metro),
        (SMORegion.seaside_kingdom_shop, loc_Seaside_Shop, self.options.goal.option_luncheon),
        (SMORegion.snow_kingdom_shop, loc_Snow_Shop, self.options.goal.option_luncheon),
        (SMORegion.luncheon_kingdom_shop, loc_Luncheon_Shop, self.options.goal.option_luncheon),
        (SMORegion.bowser_kingdom_shop, loc_Bowser_Shop, self.options.goal.option_moon),
        (SMORegion.moon_kingdom_tuxedo, loc_Moon_Outfit, self.options.goal.option_moon),
        (SMORegion.moon_kingdom_shop, loc_Moon_Shop, self.options.goal.option_moon),
        (SMORegion.mushroom_kingdom_shop, loc_Mushroom_Shop, self.options.goal.option_dark),
        (SMORegion.post_game_coin_outfits, loc_Postgame_Shop, self.options.goal.option_dark),
        (SMORegion.dark_side_outfit, loc_Dark_Outfit, self.options.goal.option_darker),
        (SMORegion.darker_side_outfit, loc_Darker_Outfit, self.options.goal.option_darker),
        (SMORegion.shop_sand_coin, shop_sand_coin, self.options.goal.option_sand),
        (SMORegion.shop_wooded_coin, shop_wooded_coin, self.options.goal.option_metro),
        (SMORegion.shop_lake_coin, shop_lake_coin, self.options.goal.option_metro),
        (SMORegion.shop_metro_coin, shop_metro_coin, self.options.goal.option_metro),
        (SMORegion.shop_seaside_coin, shop_seaside_coin, self.options.goal.option_luncheon),
        (SMORegion.shop_luncheon_coin, shop_luncheon_coin, self.options.goal.option_luncheon),
        (SMORegion.shop_moon_coin, shop_moon_coin, self.options.goal.option_darker),
        (SMORegion.shop_mushroom_coin, shop_post_game_coin, self.options.goal.option_darker),
    ]

    #endregion

    # Sub areas which have two or more over world exits that lead into them
    alternate_entrances = {
        SMOEntrance.deepest_underground_shortcut: SMORegion.deepest_underground,
        SMOEntrance.metro_kingdom_shop: SMORegion.metro_kingdom_shop,
        SMOEntrance.metro_kingdom_shop_regional: SMORegion.metro_kingdom_shop,
        SMOEntrance.inverted_pyramid_upper_interior_reverse: SMORegion.inverted_pyramid_upper_interior,
        #SMOEntrance.sky_garden_tower: SMORegion.metro_kingdom_shop,
    }

    rocket_sub_areas = [
        SMOEntrance.strange_neighborhood,
        SMOEntrance.fog_wandering,
        SMOEntrance.high_rise,
        SMOEntrance.wading_in_the_cloud_sea,
        SMOEntrance.roulette_tower,
        SMOEntrance.mushroom_picture_match,
    ]

    access_requirement_sub_areas = [
        "Sand Costume Bonus (Dancing Room)",
        "Strange Neighborhood",
        "Secret Flower Field",
        "Fog Wandering",
        "Deep Woods: Costume Bonus (Treasure Chest)",
        "Zipper Chasm",
        "RC Race",
        "Rotating Maze",
        "Metro Siege",
        "High Rise",
        "Sewers",
        "Wading in the Cloud Sea",
        "Ty-Foo Sliding Puzzle",
        "Luncheon Costume Bonus (Cooking Pots)",
        "Roulette Tower",
        "Folding Screen",
        "Yoshi in the Sea of Clouds",
        "Painting Room: Lord of Lightning",
        "Mushroom Picture Match",
        "Castle Courtyard",
        "Dark Side Topper",
        "Deepest Underground",
        "Freezing Room",
    ]

    # Cannot go back through entrance or sub area cannot be done in reverse
    one_way_enter_sub_area = [
        SMOEntrance.spinning_platforms_treasure_vault,
        #SMOEntrance.underground_ruins,
        #SMOEntrance.ice_cave,
        SMOEntrance.inverted_pyramid_upper_interior,
        SMOEntrance.darker_side_main,
        SMOEntrance.darker_side_pokio,
        SMOEntrance.darker_side_bowser,
        SMOEntrance.darker_side_end,
        SMOEntrance.secret_flower_field,
        # SMOEntrance.knucklotec_rematch,
        # SMOEntrance.torkdrift_rematch,
        # SMOEntrance.mecha_wiggler_rematch,
        # SMOEntrance.mollusque_lanceur_rematch,
        # SMOEntrance.cookatiel_rematch,
        # SMOEntrance.lord_of_lightning_rematch,
        SMOEntrance.deepest_underground_shortcut,
        SMOEntrance.moe_eye_invisible_floor,
        SMOEntrance.t_rex_escape,

    ]

    # The world entrance this connects to is normally one way
    one_way_exit_sub_area = [
        # SMOEntrance.darker_side_main,
        # SMOEntrance.darker_side_pokio,
        # SMOEntrance.darker_side_bowser,
        # SMOEntrance.darker_side_end,
        SMOEntrance.ice_cave,
        SMOEntrance.inverted_pyramid_mural,
        #SMOEntrance.darker_side_main,
        SMOEntrance.darker_side_pokio,
        SMOEntrance.darker_side_bowser,
        SMOEntrance.darker_side_end,
        #SMOEntrance.secret_flower_field,

        SMOEntrance.deepest_underground_shortcut,
        #SMOEntrance.bullet_bill_maze,
    ]

    locked_sub_area = [
        SMOEntrance.inside_the_church,
        # SMOEntrance.top_hat_tower,
    ]

    unique_exit_sub_area = {
        SMOEntrance.top_hat_tower: SMORegion.cap_kingdom_topper,
        SMOEntrance.inverted_pyramid_lower_interior: SMORegion.inverted_pyramid_mural,
        SMOEntrance.inverted_pyramid_mural: SMORegion.inverted_pyramid_upper_interior,
        SMOEntrance.inverted_pyramid_upper_interior: SMORegion.top_of_the_inverted_pyramid,
        SMOEntrance.deepest_underground_shortcut: SMORegion.sand_kingdom,
        SMOEntrance.bullet_bill_maze: SMORegion.sand_kingdom,
        SMOEntrance.sky_garden_tower: SMORegion.wooded_kingdom,
        #SMOEntrance.secret_flower_field: SMORegion.wooded_kingdom,
        SMOEntrance.ice_cave: SMORegion.sand_kingdom,
        SMOEntrance.moon_cave: SMORegion.moon_kingdom,
        SMOEntrance.painting_room_knucklotec: SMORegion.knucklotec_rematch,
        SMOEntrance.painting_room_torkdrift: SMORegion.torkdrift_rematch,
        SMOEntrance.painting_room_mecha_wiggler: SMORegion.mecha_wiggler_rematch,
        SMOEntrance.painting_room_mollusque_lanceur: SMORegion.mollosque_lanceur_rematch,
        SMOEntrance.painting_room_cookatiel: SMORegion.cookatiel_rematch,
        SMOEntrance.painting_room_lord_of_lightning: SMORegion.lord_of_lightning_rematch,
        SMOEntrance.dark_side_topper: SMORegion.dark_side_2,
        SMOEntrance.dark_side_hariet: SMORegion.dark_side_3,
        SMOEntrance.dark_side_spewart: SMORegion.dark_side_4,
        SMOEntrance.dark_side_rango: SMORegion.dark_side_5,
    }

    can_reach_mushroom = lambda state: state.can_reach(self.get_region(SMORegion.mushroom_kingdom)) and state.can_reach(self.get_region(SMORegion.odyssey_complete))

    #region Connections

    odyssey_connections = [
        (SMORegion.defunct_odyssey, {
            SMORegion.restored_odyssey: lambda state: state.can_reach(self.multiworld.get_region(SMORegion.cascade_kingdom_peace, self.player)) and count_moons(state, "Cascade", self.player) >= self.moon_counts[
                "cascade"],
                                     }),
        (SMORegion.restored_odyssey, {
            SMORegion.odyssey_interior: None,
            SMORegion.cap_kingdom: None,
            SMORegion.cascade_kingdom_revisit: None,
            SMORegion.sand_kingdom: None,
            SMORegion.odyssey_sail_sand: lambda state: count_moons(state, "Sand", self.player) >= self.moon_counts["sand"],
            SMORegion.odyssey_outfit: None,
        }),
        (SMORegion.odyssey_interior, {
            SMORegion.restored_odyssey: None
        }),
        (SMORegion.odyssey_sail_sand, {
            SMORegion.wooded_kingdom: None,
            SMORegion.lake_kingdom: None,
            SMORegion.odyssey_broken_down: lambda state: count_moons(state, "Lake", self.player) >= self.moon_counts["lake"] and
                                   count_moons(state, "Wooded", self.player) >= self.moon_counts["wooded"],
        }),
        (SMORegion.odyssey_broken_down, {
            SMORegion.cloud_kingdom_boss_fight: None,
            SMORegion.lost_kingdom: None,
            SMORegion.cloud_kingdom_revisit: None,
            SMORegion.odyssey_repaired_lost: (lambda state: count_moons(state, "Lost", self.player) >= self.moon_counts["lost"]),
        }),
        (SMORegion.odyssey_repaired_lost, {
            SMORegion.night_metro_kingdom: (lambda state: state.has(SMORegion.spark_pylon, self.player)) if self.options.capture_sanity else None,
            SMORegion.lost_kingdom_revisit: None,
            SMORegion.odyssey_sail_metro: lambda state: count_moons(state, "Metro", self.player) >= self.moon_counts["metro"],
        }),
        (SMORegion.odyssey_sail_metro, {
            SMORegion.seaside_kingdom: None,
            SMORegion.snow_kingdom: None,
            SMORegion.odyssey_sails_branch_2: lambda state: count_moons(state, "Snow", self.player) >= self.moon_counts["snow"] and count_moons(state, "Seaside", self.player) >= self.moon_counts["seaside"],
        }),
        (SMORegion.odyssey_sails_branch_2, {
            SMORegion.luncheon_kingdom: None,
            SMORegion.odyssey_sail_luncheon: lambda state: count_moons(state, "Luncheon", self.player) >= self.moon_counts["luncheon"],
        }),
        (SMORegion.odyssey_sail_luncheon, {
            SMORegion.ruined_kingdom: None,
            SMORegion.odyssey_repaired_ruined: lambda state: count_moons(state, "Ruined", self.player) >= self.moon_counts["ruined"],
        }),
        (SMORegion.odyssey_repaired_ruined, {
            SMORegion.bowsers_kingdom: None,
            SMORegion.odyssey_complete: lambda state: count_moons(state, "Bowser", self.player) >= self.moon_counts["bowser"] and state.can_reach(self.multiworld.get_region(SMORegion.bowser_kingdom_peace, self.player)),
        }),
        (SMORegion.odyssey_complete, {
            SMORegion.moon_kingdom: None,
            SMORegion.moon_kingdom_tuxedo: None,
            SMORegion.mushroom_kingdom: (lambda state: state.has(SMORegion.bowser, self.player)) if self.options.capture_sanity else None,
            SMORegion.odyssey_powered_up_dark: (lambda state: state.has(SMORegion.bowser, self.player) and total_moons(state, self.player) >= self.moon_counts["dark"]) if self.options.capture_sanity else (lambda state: total_moons(state, self.player) >= self.moon_counts["dark"]),
        }),
        (SMORegion.odyssey_powered_up_dark, {
            SMORegion.dark_side : None,
            SMORegion.odyssey_powered_up_darker: lambda state: total_moons(state, self.player) >= self.moon_counts["darker"],
        }),
        (SMORegion.odyssey_powered_up_darker, {
            SMORegion.darker_side : None
        }),
    ]

    world_connections = [
        (SMORegion.menu, {
            SMORegion.cap_kingdom_intro: None,
        }),
        (SMORegion.cap_kingdom_intro, {

        }),
        (SMORegion.cap_kingdom_topper, {
            SMORegion.cascade_kingdom: None,
        }),
        (SMORegion.cap_kingdom, {
            SMORegion.cap_kingdom_moon_rock: can_reach_mushroom,
            SMORegion.cap_kingdom_shop: None,
        }),
        (SMORegion.cascade_kingdom, {
            SMORegion.cascade_kingdom_peace: (lambda state: state.has(SMORegion.broodes_chain_chomp, self.player) and
                state.can_reach(self.multiworld.get_region(SMORegion.broodes_chain_chomp,self.player))) if self.options.capture_sanity else None,
            SMORegion.defunct_odyssey: None,
            SMORegion.t_rex: (lambda state: state.has(SMORegion.chain_chomp, self.player)) if self.options.capture_sanity else None,
            SMORegion.chain_chomp: None,
            SMORegion.big_chain_chomp: (lambda state: state.has(SMORegion.chain_chomp, self.player)) if self.options.capture_sanity else None,
            SMORegion.broodes_chain_chomp: (lambda state: state.has_any([SMORegion.big_chain_chomp, SMORegion.t_rex], self.player)) if self.options.capture_sanity else None,
        }),
        (SMORegion.cascade_kingdom_peace, {
            SMORegion.cascade_kingdom_moon_rock: can_reach_mushroom,
        }),
        (SMORegion.cascade_kingdom_revisit, {
            SMORegion.cascade_kingdom_shop: None,
        }),
        (SMORegion.sand_kingdom, {
            #SMORegion.sand_kingdom_shop: None,
            SMORegion.binoculars: None,
            SMORegion.bullet_bill: None,
            SMORegion.moe_eye: None,
            SMORegion.cactus: None,
            SMORegion.night_sand_kingdom: (lambda state: state.can_reach(SMORegion.top_of_the_inverted_pyramid, player=self.player))
        }),
        (SMORegion.top_of_the_inverted_pyramid, {
        }),
        (SMORegion.night_sand_kingdom, {
            SMORegion.underground_ruins: None,
        }),
        (SMORegion.sand_kingdom_peace, {
            SMORegion.deepest_underground_peace: None,
            SMORegion.mini_rocket: None,
            SMORegion.glydon: None,
            SMORegion.lakitu: None,
            SMORegion.strange_neighborhood: lambda state: state.has(SMORegion.mini_rocket, self.player) if self.options.capture_sanity else None,
            SMORegion.sand_kingdom_moon_rock: can_reach_mushroom,
            SMORegion.top_of_the_inverted_pyramid: (lambda state: state.has(SMORegion.spark_pylon, self.player)) if self.options.capture_sanity else None,
            SMORegion.top_of_the_inverted_pyramid_peace: (lambda state: state.can_reach(SMORegion.top_of_the_inverted_pyramid,player=self.player)),
        }),
        (SMORegion.wooded_kingdom, {
            SMORegion.wooded_kingdom_post_broodals: None,
            SMORegion.wooded_kingdom_shop: None,
        }),
        (SMORegion.wooded_kingdom_post_broodals, {
            SMORegion.wooded_kingdom_peace: (lambda state: state.has_all([SMORegion.uproot, SMORegion.sherm], self.player)) if self.options.capture_sanity else None,
            SMORegion.sherm: None
        }),
        (SMORegion.wooded_kingdom_peace, {
            SMORegion.wooded_kingdom_moon_rock: can_reach_mushroom,
        }),
        (SMORegion.lake_kingdom, {
            SMORegion.cheep_cheep: None,
            SMORegion.zipper: None,
            SMORegion.goomba: None,
            SMORegion.lakitu: None,
            #SMORegion.lake_kingdom_shop: None,
            SMORegion.lake_kingdom_moon_rock: can_reach_mushroom,
        }),
        (SMORegion.cloud_kingdom_boss_fight, {

        }),
        (SMORegion.cloud_kingdom_revisit, {
            SMORegion.cloud_kingdom_moon_rock: can_reach_mushroom,
        }
         ),
        (SMORegion.lost_kingdom, {
            #SMORegion.lost_kingdom_shop: None,
            SMORegion.tropical_wiggler: None,
        }),
        (SMORegion.lost_kingdom_revisit, {
            SMORegion.lost_kingdom_moon_rock: can_reach_mushroom,
        }),
        (SMORegion.night_metro_kingdom, {
            #SMORegion.metro_kingdom_shop: None,
            SMORegion.day_metro_kingdom: (lambda state: state.has_all([SMORegion.sherm, SMORegion.spark_pylon], self.player)) if self.options.capture_sanity else None,
        }),
        (SMORegion.day_metro_kingdom, {
            SMORegion.pole: None,
            SMORegion.manhole: None,
            SMORegion.taxi: None,
        }),
        (SMORegion.metro_kingdom_peace, {
            SMORegion.metro_kingdom_moon_rock: can_reach_mushroom,
        }),
        (SMORegion.seaside_kingdom, {
            SMORegion.gushen: None,
            SMORegion.seaside_kingdom_shop: None,
            SMORegion.seaside_kingdom_peace: (lambda state: state.has(SMORegion.gushen, self.player)) if self.options.capture_sanity else None,
        }),
        (SMORegion.seaside_kingdom_peace, {
            SMORegion.seaside_kingdom_moon_rock: can_reach_mushroom,
        }),
        (SMORegion.snow_kingdom, {
            #SMORegion.snow_kingdom_shop: None,
            SMORegion.snow_kingdom_peace: (lambda state: state.can_reach(self.multiworld.get_region(SMORegion.snowline_circuit, self.player)) and state.has(SMORegion.shiverian_racer, self.player)) if self.options.capture_sanity
                else (lambda state: state.can_reach(self.multiworld.get_region(SMORegion.snowline_circuit, self.player)))
        }),
        (SMORegion.snow_kingdom_peace, {
            SMORegion.ty_foo: None,
            SMORegion.cheep_cheep_snow_kingdom: None,
            SMORegion.snow_kingdom_moon_rock: can_reach_mushroom
        }),
        (SMORegion.luncheon_kingdom, {
            SMORegion.lava_bubble: None,
            SMORegion.luncheon_kingdom_post_broodals: None,
        }),
        (SMORegion.luncheon_kingdom_post_broodals, {
            SMORegion.hammer_bro: None,
            #SMORegion.luncheon_kingdom_shop: None,
            SMORegion.luncheon_kingdom_meat: None,
        }),
        (SMORegion.luncheon_kingdom_meat, {
            SMORegion.meat: None,
            SMORegion.cascading_magma: lambda state: state.can_reach(self.multiworld.get_location("Luncheon Kingdom - Big Pot on the Volcano: Dive In!", self.player)),
        }),
        (SMORegion.cascading_magma, {
            SMORegion.lava_bubble: None,
            SMORegion.luncheon_kingdom_peace: (lambda state: state.has(SMORegion.lava_bubble, self.player)) if self.options.capture_sanity else None,
        }),
        (SMORegion.luncheon_kingdom_peace, {
            SMORegion.fire_piranha_plant: None,
            SMORegion.luncheon_kingdom_moon_rock: can_reach_mushroom
        }),
        (SMORegion.ruined_kingdom, {
            SMORegion.spark_pylon: None,
            SMORegion.ruined_kingdom_moon_rock: can_reach_mushroom,
        }),
        (SMORegion.bowsers_kingdom, {
            SMORegion.infiltrate_bowsers_castle: (lambda state: state.has(SMORegion.spark_pylon, self.player)) if self.options.capture_sanity else None,
        }),
        (SMORegion.infiltrate_bowsers_castle, {
            SMORegion.bowser_kingdom_smart_bombing: None,
        }),
        (SMORegion.bowser_kingdom_smart_bombing, {
            SMORegion.pokio: None,
            SMORegion.jizo: None,
            # SMORegion.bowser_kingdom_shop: None,
            SMORegion.bowser_kingdom_mecha_broodal: None,
        }),
        (SMORegion.bowser_kingdom_mecha_broodal, {
            SMORegion.bowser_kingdom_peace: None,
        }),
        (SMORegion.bowser_kingdom_peace, {
            SMORegion.bowser_kingdom_moon_rock: can_reach_mushroom,
        }),
        (SMORegion.moon_kingdom, {
            #SMORegion.moon_kingdom_shop: None,
            SMORegion.moon_kingdom_peace: can_reach_mushroom,
        }),
        (SMORegion.moon_kingdom_peace, {
            SMORegion.moon_kingdom_moon_rock: can_reach_mushroom,
        }), # Once post moon
        (SMORegion.mushroom_kingdom, {
            SMORegion.yoshi: None,
            #SMORegion.mushroom_kingdom_shop: None,
        }),
        (SMORegion.dark_side, {
        }),
        (SMORegion.dark_side_peace, {
            SMORegion.dark_side_outfit: None,
        }),
        (SMORegion.darker_side, {

        }),
        (SMORegion.darker_side_tower, {
            SMORegion.darker_side_outfit: None
        }),
        (SMORegion.metro_kingdom_moon_rock, {
            SMORegion.letter: None,
        }),
    ]

    sub_area_connections = [
        (SMORegion.top_hat_tower, {
            SMORegion.frog: None,
            #SMORegion.cap_kingdom_topper: (lambda state: state.has(SMORegion.frog, self.player)) if self.options.capture_sanity else None,
        }),
        (SMORegion.frog_pond, {
            SMORegion.frog: None
        }),
        (SMORegion.poison_tides, {
            SMORegion.paragoomba: None
        }),
        (SMORegion.push_block, {
            SMORegion.spark_pylon: None
        }),
        (SMORegion.rolling_lane, {

        }),
        (SMORegion.chain_chomp_cave, {
            SMORegion.chain_chomp: None
        }),
        (SMORegion.t_rex_nest, {
            SMORegion.t_rex: None
        }),
        (SMORegion.chasm_lifts, {

        }),
        (SMORegion.gusty_bridges, {

        }),
        (SMORegion.moe_eye_invisible_maze, {
            SMORegion.moe_eye: None
        }),
        (SMORegion.bullet_bill_maze, {
            SMORegion.bullet_bill: None
        }),
        (SMORegion.jaxi_ruins, {

        }),
        (SMORegion.strange_neighborhood, {
            SMORegion.goomba: None
        }),
        (SMORegion.sand_outfit, {

        }),
        (SMORegion.sand_rumbling_floor_house, {

        }),
        # (SMORegion.employees_only, {
        #
        # }
        #  ),
        (SMORegion.ice_cave, {

        }),
        (SMORegion.sand_sphynx_vault, {

        }),
        (SMORegion.sand_slots, {

        }),
        (SMORegion.inverted_pyramid_lower_interior, {
            #SMORegion.inverted_pyramid_lower_interior: None
        }),
        (SMORegion.inverted_pyramid_upper_interior, {
            #SMORegion.top_of_the_inverted_pyramid: None
        }),
        (SMORegion.underground_ruins, {
            #SMORegion.deepest_underground: (lambda state: state.has(SMORegion.bullet_bill,self.player)) if self.options.capture_sanity else None,
            SMORegion.goomba: None,
            SMORegion.bullet_bill: None,
        }),
        (SMORegion.deepest_underground, {
            SMORegion.sand_kingdom_peace: create_access_rule(self,[(SMORuleCondition.CAPTURE, [SMOItemData.knucklotecs_fist], SMORuleOperation.NONE)]),
            SMORegion.bullet_bill: None,
            SMORegion.knucklotecs_fist: None,
            SMORegion.deepest_underground_post_game: can_reach_mushroom,
        }),
        (SMORegion.deepest_underground_peace, {

        }),
        (SMORegion.deepest_underground_post_game, {

        }),
        (SMORegion.moe_eye_invisible_floor, {
            SMORegion.moe_eye: None
        }),
        (SMORegion.colossal_ruins, {

        }),
        (SMORegion.freezing_waterway, {
            SMORegion.gushen: None
        }),
        (SMORegion.arch_repair, {
            SMORegion.puzzle_part_lake_kingdom: None
        }),
        (SMORegion.zipper_chasm, {
            SMORegion.zipper: None
        }),
        (SMORegion.bouncy_flowers, {

        }),
        (SMORegion.poison_swamp, {
            SMORegion.frog: None
        }),
        (SMORegion.deep_woods_treasure_trap, {

        }),
        (SMORegion.explorer_outift, {

        }),
        (SMORegion.flooding_pipeway, {

        }),
        (SMORegion.wooded_flower_road, {
            SMORegion.goomba: None
        }),
        (SMORegion.sherm_elevator, {
            SMORegion.sherm: None,
            SMORegion.fire_bro: None
        }),
        (SMORegion.fog_wandering, {
            SMORegion.paragoomba: None
        }),
        (SMORegion.walking_on_clouds, {
            SMORegion.uproot: None
        }),
        (SMORegion.secret_flower_field, {
            SMORegion.uproot: None,
            SMORegion.secret_flower_field_peace: lambda state: state.can_reach(self.multiworld.get_region(SMORegion.wooded_kingdom_peace, self.player)),
        }),
        (SMORegion.secret_flower_field_peace, {

        }),
        (SMORegion.deep_woods, {
            SMORegion.t_rex: None,
            SMORegion.coin_coffer: None,
            SMORegion.boulder: None,
            SMORegion.tree: None,
        }),
        (SMORegion.nut_room, {

        }),
        (SMORegion.invisible_road, {
            SMORegion.poison_piranha_plant: None
        }),
        (SMORegion.sheep_herding, {

        }),
        (SMORegion.breakdown_road, {
            SMORegion.bullet_bill: None,
            SMORegion.banzai_bill: None
        }),
        (SMORegion.cloud_picture_match, {
            SMORegion.picture_match_part_goomba: None,
            SMORegion.cloud_post_game_picture_match: can_reach_mushroom
        }),
        (SMORegion.cloud_post_game_picture_match, {
            SMORegion.picture_match_part_goomba: None
        }),
        (SMORegion.king_of_the_cube, {

        }),
        (SMORegion.tropical_wiggler_swamp, {
            SMORegion.tropical_wiggler: None
        }),
        (SMORegion.klepto_lava_bath, {
            SMORegion.lava_bubble: None
        }),
        (SMORegion.metro_slots, {

        }),
        (SMORegion.rc_race, {
            SMORegion.rc_car: None,
            SMORegion.rc_race_post_game: can_reach_mushroom
        }),
        (SMORegion.private_room, {

        }),
        (SMORegion.city_hall, {

        }),
        (SMORegion.crowded_street, {
            SMORegion.crowded_street_post_game: can_reach_mushroom
        }),
        (SMORegion.builder_outfit, {
            SMORegion.spark_pylon: None
        }),
        (SMORegion.metro_siege, {
            SMORegion.sherm: None
        }),
        (SMORegion.rotating_maze, {

        }),
        (SMORegion.high_rise, {

        }),
        (SMORegion.bullet_billding, {
            SMORegion.bullet_bill: None
        }),
        (SMORegion.t_rex_escape, {

        }),
        (SMORegion.projection_room, {

        }),
        (SMORegion.pitch_black_island, {

        }),
        (SMORegion.swinging_scaffolding, {
            SMORegion.hammer_bro: None
        }),
        (SMORegion.vanishing_road, {

        }),
        (SMORegion.sewers, {
            SMORegion.metro_kingdom_peace: lambda state: state.can_reach(self.multiworld.get_region(SMORegion.day_metro_kingdom, self.player)),
            SMORegion.sewers_post_game: lambda state: state.can_reach(self.multiworld.get_region(SMORegion.day_metro_kingdom, self.player))
                                                  and state.can_reach(self.multiworld.get_region(SMORegion.mushroom_kingdom, self.player))
        }),
        (SMORegion.sewers_post_game, {
            SMORegion.puzzle_part_metro_kingdom: None
        }),
        (SMORegion.sandy_bottom, {

        }),
        (SMORegion.seaside_waterway, {
            SMORegion.cheep_cheep: None
        }),
        (SMORegion.seaside_sphynx_vault, {

        }),
        (SMORegion.seaside_rumbling_room, {

        }),
        (SMORegion.resort_outfit, {

        }),
        (SMORegion.wading_in_the_cloud_sea, {

        }),
        (SMORegion.narrow_valley, {
            SMORegion.gushen: None
        }),
        (SMORegion.sinking_island, {
            SMORegion.uproot: None
        }),
        (SMORegion.pokio_bomb_aiming, {
            SMORegion.pokio: None
        }),
        (SMORegion.spinning_maze, {

        }),
        (SMORegion.shiveria, {
            SMORegion.goomba: None,
            SMORegion.ty_foo: None,
            SMORegion.shiveria_peace: lambda state: state.can_reach(self.multiworld.get_region(SMORegion.snow_kingdom_peace, self.player)),
        }),
        (SMORegion.snowline_circuit, {
            SMORegion.shiverian_racer: None,
            SMORegion.snow_kingdom_peace: (lambda state: state.has(SMORegion.shiverian_racer, self.player)) if self.options.capture_sanity else None,
         }),
        (SMORegion.shiveria_peace, {
            SMORegion.icicle_barrier_post_game: can_reach_mushroom,
            SMORegion.ice_wall_barrier_post_game: can_reach_mushroom,
            SMORegion.snowy_mountain_barrier_post_game: can_reach_mushroom,
            SMORegion.gusty_barrier_post_game: can_reach_mushroom,
        }),
        (SMORegion.icicle_barrier_post_game, {
            SMORegion.goomba: None
        }),
        (SMORegion.ice_wall_barrier_post_game, {

        }),
        (SMORegion.gusty_barrier_post_game, {
            SMORegion.ty_foo: None
        }),
        (SMORegion.snowy_mountain_barrier_post_game, {

        }),
        (SMORegion.magma_swamp, {

        }),
        (SMORegion.luncheon_treasure_vault, {

        }),
        (SMORegion.chef_outfit, {
            SMORegion.lava_bubble: None
        }),
        (SMORegion.fork_flickin, {
            SMORegion.volbonan: None
        }),
        (SMORegion.cheese_excavate, {
            SMORegion.hammer_bro: None
        }),
        (SMORegion.magma_narrow_path, {
            SMORegion.lava_bubble: None
        }),
        (SMORegion.spinning_athletics, {

        }),
        (SMORegion.luncheon_slots, {

        }),
        (SMORegion.rotating_gears_with_bitefrost, {
            SMORegion.fire_bro: None
        }),
        (SMORegion.volcano_cave, {

        }),
        (SMORegion.lava_islands, {
            SMORegion.lava_bubble: None
        }),
        (SMORegion.roulette_tower, {

        }),
        (SMORegion.chargin_chuck_arena, {
            SMORegion.chargin_chuck: None
        }),
        (SMORegion.folding_screen, {

        }),
        (SMORegion.bowsers_treasure_vault, {

        }),
        (SMORegion.jizos_adventure, {
            SMORegion.jizo: None
        }),
        (SMORegion.spinning_tower, {

        }),
        (SMORegion.hexagon_tower, {
            SMORegion.parabones: None
        }),
        (SMORegion.wooden_tower, {
            SMORegion.pokio: None
        }),
        (SMORegion.moon_cave, {
            SMORegion.bowser_statue: None,
            SMORegion.parabones: None,
            SMORegion.sherm: (lambda state: state.has(SMORegion.parabones, self.player)) if self.options.capture_sanity else None,
            SMORegion.spark_pylon: (lambda state: state.has(SMORegion.parabones, self.player)) if self.options.capture_sanity else None,
            SMORegion.hammer_bro: (lambda state: state.has_all([SMORegion.parabones, SMORegion.sherm, SMORegion.spark_pylon], self.player)) if self.options.capture_sanity else None,
            SMORegion.tropical_wiggler: (lambda state: state.has_all([SMORegion.parabones, SMORegion.sherm, SMORegion.spark_pylon], self.player)) if self.options.capture_sanity else None,
            SMORegion.banzai_bill: (lambda state: state.has_all([SMORegion.parabones, SMORegion.sherm, SMORegion.spark_pylon], self.player)) if self.options.capture_sanity else None,
            SMORegion.bullet_bill: (lambda state: state.has_all([SMORegion.parabones, SMORegion.sherm, SMORegion.spark_pylon, SMORegion.banzai_bill], self.player)) if self.options.capture_sanity else None,
            SMORegion.moe_eye: (lambda state: state.has_all([SMORegion.parabones, SMORegion.sherm, SMORegion.spark_pylon, SMORegion.banzai_bill], self.player)) if self.options.capture_sanity else None,
            SMORegion.chargin_chuck: (lambda state: state.has_all([SMORegion.parabones, SMORegion.sherm, SMORegion.spark_pylon, SMORegion.banzai_bill], self.player)) if self.options.capture_sanity else None,
            SMORegion.broodes_chain_chomp: (lambda state: state.has_all([SMORegion.parabones, SMORegion.sherm, SMORegion.spark_pylon, SMORegion.banzai_bill], self.player)) if self.options.capture_sanity else None
        }),
        (SMORegion.inside_the_church, {
            SMORegion.bowser: None,
        }),
        (SMORegion.dot_galaxy, {

        }),
        (SMORegion.giant_swings, {

        }),
        (SMORegion.moon_sphynx_vault, {

        }),
        (SMORegion.mushroom_picture_match, {
            SMORegion.picture_match_part_mario: None
        }),
        (SMORegion.peachs_castle, {

        }),
        (SMORegion.castle_courtyard, {

        }),
        (SMORegion.mushroom_well, {

        }),
        (SMORegion.yoshi_in_the_sea_of_clouds, {
            SMORegion.yoshi: None
        }),
        (SMORegion.knucklotec_rematch, {
            SMORegion.knucklotecs_fist: None
        }),
        (SMORegion.torkdrift_rematch, {
            SMORegion.uproot: None
        }),
        (SMORegion.mollosque_lanceur_rematch, {
            SMORegion.gushen: None
        }),
        (SMORegion.mecha_wiggler_rematch, {
            SMORegion.sherm: None
        }),
        (SMORegion.cookatiel_rematch, {
            SMORegion.lava_bubble: None
        }),
        (SMORegion.lord_of_lightning_rematch, {

        }),
        (SMORegion.dark_side_breakdown_road, {

        }),
        (SMORegion.dark_side_invisible_road, {

        }),
        (SMORegion.dark_side_vanishing_road, {

        }),
        (SMORegion.dark_side_under_siege, {
            SMORegion.yoshi: None
        }),
        (SMORegion.dark_side_sinking_island, {
            SMORegion.yoshi: None
        }),
        (SMORegion.dark_side_magma_swamp, {
            SMORegion.yoshi: None
        }),
        (SMORegion.dark_side_topper, {
            SMORegion.dark_side_2: None
        }),
        (SMORegion.dark_side_harriet, {
            SMORegion.dark_side_3: None
        }),
        (SMORegion.dark_side_rango, {
            # Make captain toad region
            SMORegion.dark_side_peace: (lambda state: state.has(SMORegion.hammer_bro,self.player)) if self.options.capture_sanity else None
        }),
        (SMORegion.dark_side_spewart, {
            SMORegion.dark_side_4: None
        }),
        (SMORegion.darker_side_entrance, {
            SMORegion.goomba: None,
            SMORegion.lava_bubble: None,
            SMORegion.uproot: (lambda state: state.has(SMORegion.lava_bubble,self.player)) if self.options.capture_sanity else None,
            SMORegion.yoshi: (lambda state: state.has_all([SMORegion.lava_bubble, SMORegion.uproot],self.player)) if self.options.capture_sanity else None,
            SMORegion.glydon: (lambda state: state.has_all([SMORegion.lava_bubble, SMORegion.uproot, SMORegion.yoshi],self.player)) if self.options.capture_sanity else None,
            SMORegion.volbonan: (lambda state: state.has_all([SMORegion.lava_bubble, SMORegion.uproot, SMORegion.yoshi, SMORegion.glydon],self.player)) if self.options.capture_sanity else None,
        }),
        (SMORegion.darker_side_climb, {
            SMORegion.pokio: None
        }),
        (SMORegion.darker_side_bowser, {
            SMORegion.bowser: None
        }),
        (SMORegion.darker_side_end, {
            SMORegion.spark_pylon: None
        }),
        # Shops
        (SMOEntrance.sand_kingdom_shop, {
            SMORegion.sand_kingdom_shop: None,
        }),
        (SMOEntrance.lake_kingdom_shop, {
            SMORegion.lake_kingdom_shop: None,
        }),
        (SMOEntrance.lost_kingdom_shop, {
            SMORegion.lost_kingdom_shop: None,
        }),
        (SMORegion.metro_kingdom_shop, {
            SMORegion.metro_kingdom_shop: None,
        }),
        (SMOEntrance.snow_kingdom_shop, {
            SMORegion.snow_kingdom_shop: None,
        }),
        (SMOEntrance.luncheon_kingdom_shop, {
            SMORegion.luncheon_kingdom_shop: None,
        }),
        (SMOEntrance.bowsers_kingdom_shop, {
            SMORegion.bowser_kingdom_shop: None,
        }),
        (SMOEntrance.moon_kingdom_shop, {
            SMORegion.moon_kingdom_shop: None,
        }),
        (SMOEntrance.mushroom_kingdom_shop, {
            SMORegion.mushroom_kingdom_shop: None,
        }),
    ]

    # non_entrance_rando_sub_area_connections = [
    #     (SMORegion.inverted_pyramid_lower_interior, {
    #         SMOEntrance.inverted_pyramid_upper_interior: None,
    #     }),
    #     (SMORegion.inverted_pyramid_upper_interior, {
    #         SMORegion.top_of_the_inverted_pyramid: None,
    #     }),
    # ]

#endregion

    # ADD Painting Regions and Connections
    for region in odyssey_regions:
        create_region(self, region)

    for region in world_regions:
        create_region(self, region)

    for region in sub_area_regions:
        create_region(self,region)

    for region in shop_regions:
        create_region(self, region)

    if self.options.capture_sanity:
        for region in capture_regions:
            create_region(self, region)

    for world, connections in world_connections:
        for key in connections.keys():
            if "Kingdom Shop" in key:
                connect_coin_shops(connections)
                break

    for world, connections in sub_area_connections:
        for key in connections.keys():
            if "Kingdom Shop" in key:
                connect_coin_shops(connections)
                break

    for connection in odyssey_connections:
        connect_region(self, connection)

    for connection in world_connections:
        connect_region(self, connection)

    for connection in sub_area_connections:
        connect_region(self, connection)
        # req_caps = []
        # for key in connection[1]:
        #     if key in capture_items:
        #         req_caps.append(key)
        # if len(req_caps) > 0:
        #     reg = self.get_region(connection[0])
        #     req_caps_str = "["
        #     for cap in req_caps:
        #         req_caps_str += f"SMOItemData.{cap.lower().replace("'", "").replace(" ", "_").replace("-", "_").replace(")", "").replace("(", "")}, "
        #     req_caps_str = req_caps_str[:-2] + "]"
        #     for location in reg.locations:
        #         print(f'set_rule(self.get_location(SMOLocationData.{location.name.lower().replace(" ", "_").replace("-", "").replace("!", " ").replace(":", "")
        #             }), create_access_rule(self, '  + "[\n" + "\t\t\t(SMORuleCondition.CAPTURE, " + f"{req_caps_str}, SMORuleOperation.NONE)" + "\n\t\t\t]))")

    self.world_exits, self.world_sub_area_exits, self.non_dead_end_sub_areas = create_entrances(self)

    # One way sub area entrance: one exit no entrance from world region, one entrance no exit to sub area region
    # One way sub area exit: Exit no Entrance from sub area region, Entrance no Exit into world region
    mismatch = 0
    for data in self.world_exits:
        region, exits = data
        for world_exit in exits.keys():
            add_to_er: bool = True
            cur_reg : Region = self.get_region(region)
            origin_region = None
            # if "Kingdom" in region and region != region[:region.index("Kingdom") + 7] and region[:region.index("Kingdom") + 7] in world_regions and "Intro" not in region:
            #     origin_region = self.get_region(region[:region.index("Kingdom") + 7])
            cur_sub_area : Region = self.get_region(alternate_entrances[world_exit] if world_exit in alternate_entrances else world_exit)
            region_entry, region_exit = None, None
            sub_area_entry, sub_area_exit = None, None

            # Over world Region connection
            if origin_region:
                if world_exit in one_way_enter_sub_area:
                    region_exit = create_one_way_exit(cur_reg,f"{region} {world_exit} Entrance",cur_sub_area)
                else:
                    region_entry, region_exit = create_two_way_entrance_pair(cur_reg, f"{region} {world_exit} Entrance", f"{world_exit} Entrance", cur_sub_area, origin_region)
            else:
                if region not in unique_exit_sub_area.keys():
                    if world_exit in one_way_enter_sub_area:
                        region_exit = create_one_way_exit(cur_reg,f"{region} {world_exit} Entrance",cur_sub_area)
                    else:
                        region_entry, region_exit = create_two_way_entrance_pair(cur_reg, f"{region} {world_exit} Entrance",f"{world_exit} Entrance",cur_sub_area)

            # Sub Area
            if world_exit not in unique_exit_sub_area.values():
                if world_exit in one_way_enter_sub_area:
                    sub_area_entry = create_one_way_entrance(cur_sub_area, f"{world_exit} Entrance", cur_reg)
                else:
                    sub_area_entry, sub_area_exit = create_two_way_entrance_pair(cur_sub_area, f"{world_exit} Entrance",f"{region} {world_exit} Entrance", cur_reg)


            if world_exit in locked_sub_area:
                add_to_er = False
            # region_entry, region_exit = create_two_way_entrance_pair(cur_reg, f"{region} {world_exit} Entrance", cur_sub_area)
            # sub_area_entry, sub_area_exit = create_two_way_entrance_pair(cur_sub_area, f"{world_exit}", cur_reg)

            if add_to_er:
                if region_entry:
                    self.sub_area_entrances.append(region_entry)
                if region_exit:
                    self.sub_area_exits.append(region_exit)
                if sub_area_entry:
                    self.sub_area_entrances.append(sub_area_entry)
                if sub_area_exit:
                    self.sub_area_exits.append(sub_area_exit)

            if callable(exits[world_exit]):
                # print(world_exit)
                region_exit.access_rule = exits[world_exit]
                if world_exit in rocket_sub_areas:
                    sub_area_entry.access_rule = exits[world_exit]
                    sub_area_exit.access_rule = exits[world_exit]

            if world_exit in self.non_dead_end_sub_areas:
                unique_exit_region: Region = None
                if world_exit in unique_exit_sub_area:
                    unique_exit_region = self.get_region(unique_exit_sub_area[world_exit])

                    region_entry, region_exit = None, None
                    if world_exit in one_way_exit_sub_area:
                        region_entry = create_one_way_entrance(unique_exit_region,f"{unique_exit_region.name} {world_exit} End", cur_sub_area)
                    else:
                        region_entry, region_exit = create_two_way_entrance_pair(unique_exit_region, f"{unique_exit_region.name} {world_exit} End",f"{world_exit} End", cur_sub_area)

                    if region_entry:
                        self.sub_area_entrances.append(region_entry)
                    if region_exit:
                        self.sub_area_exits.append(region_exit)

                else:
                    # sub area end to over world
                    region_entry, region_exit = None, None
                    if world_exit in one_way_exit_sub_area:
                        region_entry = create_one_way_entrance(cur_reg,
                                                               f"{region} {world_exit} End",
                                                               cur_sub_area)
                    else:
                        region_entry, region_exit = create_two_way_entrance_pair(cur_reg,
                                                                                 f"{region} {world_exit} End",
                                                                                 f"{world_exit} End", cur_sub_area)

                    if region_entry:
                        self.sub_area_entrances.append(region_entry)
                    if region_exit:
                        self.sub_area_exits.append(region_exit)
                sub_area_entry, sub_area_exit = None, None
                if world_exit in one_way_exit_sub_area:
                    sub_area_exit = create_one_way_exit(cur_sub_area, f"{world_exit} End", unique_exit_region if unique_exit_region else cur_reg)
                    sub_area_entry = None
                else:
                    sub_area_entry, sub_area_exit = create_two_way_entrance_pair(cur_sub_area,
                                                                                 f"{world_exit} End",
                                                                                 f"{unique_exit_region.name} {world_exit} End" if unique_exit_region else f"{region} {world_exit} End",
                                                                                 unique_exit_region if unique_exit_region else cur_reg)

                if sub_area_entry and sub_area_entry.connected_region:
                    self.sub_area_entrances.append(sub_area_entry)
                if sub_area_exit:
                    self.sub_area_exits.append(sub_area_exit)


                if callable(exits[world_exit]):
                    if world_exit in rocket_sub_areas:
                        # print(world_exit)
                        sub_area_entry.access_rule = exits[world_exit]
                        sub_area_exit.access_rule = exits[world_exit]


            if len(self.sub_area_entrances) != len(self.sub_area_exits):
                val = len(self.sub_area_entrances) - len(self.sub_area_exits)
                if mismatch != val:
                    mismatch = (len(self.sub_area_entrances) - len(self.sub_area_exits))
                    print("Mismatch. ", f"Entrances: {len(self.sub_area_entrances)} ", f"Exits: {len(self.sub_area_exits)} ", f" {region} {world_exit}")

            if world_exit not in one_way_enter_sub_area and world_exit not in one_way_exit_sub_area and world_exit in self.non_dead_end_sub_areas:
                self.valid_top_hat_replacements.append(world_exit)


def create_locations(region: Region, *locations: str, location_table = locations_table):
    """
    :param region: The Region to add locations too
    :param locations: locations
    :param location_table: name to id dict of world locations
    :return: None
    """
    region.locations += ([SMOLocation(region.player, location_name, location_table[location_name], region) for location_name in locations])
