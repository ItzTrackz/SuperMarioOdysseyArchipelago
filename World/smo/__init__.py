import random
from math import floor
from typing import Mapping, Any, TextIO

from .Data.EntranceData import SMOEntrance
from .Data.RegionData import SMORegion
from .Items import item_table, SMOItem, filler_item_table, outfits, shop_items, \
    moon_item_table, moon_types, world_list, stickers, souvenirs, capture_items, \
    location_hint_list
from .Locations import locations_table, SMOLocation, locations_list, post_game_locations_list, \
    special_locations_table, full_moon_locations_list, story_moons, multi_moons, goals_table
from .Options import SMOOptions
from .Rules import set_rules
from .Regions import create_regions
from .Entrances import display_name_to_internal_name, display_name_alias, stage_id_to_name, SMORandomizationGroup, \
                        internal_name_to_entrance, stage_names, stage_ids
from BaseClasses import Item, ItemClassification, Entrance, Region, EntranceType, MultiWorld
from worlds.AutoWorld import World
from worlds.LauncherComponents import (Component, components, Type as component_type, SuffixIdentifier, launch as launch_component)
from entrance_rando import ERPlacementState, randomize_entrances, disconnect_entrance_for_randomization


def launch_client(*args: str):
    from .Connector.Client import launch
    print(len(args))
    launch_component(launch, name="SMOClient", args=args)

component = Component("Super Mario Odyssey Client", component_type=component_type.CLIENT,
                      game_name="Super Mario Odyssey", func=launch_client)
components.append(component)

class SMOWorld(World):
    """Super Mario Odyssey is a 3-D Platformer where Mario sets off across the world with his companion Cappy to save Princess Peach and Cappy's sister Tiara from Bowser's wedding plans."""
    game = "Super Mario Odyssey"

    #settings_key = "smo_settings"
    #settings : SMOSettings

    options_dataclass = SMOOptions
    options: SMOOptions

    topology_present = True  # show path to required location checks in spoiler

    # ID of first item and location, could be hard-coded but code may be easier
    # to read with this as a property.
    # instead of dynamic numbering, IDs could be part of data
    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = {**item_table, **moon_types}

    location_name_to_id = locations_table
    # Number of Power Moons required to leave each kingdom
    default_moon_counts = {
        "cascade": 5,
        "sand": 16,
        "lake": 8,
        "wooded": 16,
        "lost": 10,
        "metro": 20,
        "snow": 10,
        "seaside": 10,
        "luncheon": 18,
        "ruined": 3,
        "bowser": 8,
        "dark": 250,
        "darker": 500
    }

    # Number of Power Moons required to unlock post game outfits.
    outfit_moon_counts = {
        "Luigi Cap" : 160,
        "Luigi Suit" : 180,
        "Doctor Headwear" : 220,
        "Doctor Outfit" : 240,
        "Waluigi Cap" : 260,
        "Waluigi Suit" : 280,
        "Diddy Kong Hat" : 300,
        "Diddy Kong Suit" : 320,
        "Wario Cap" : 340,
        "Wario Suit" : 360,
        "Hakama" : 380,
        "Bowser's Top Hat" : 420,
        "Bowser's Tuxedo" : 440,
        "Bridal Veil" : 460,
        "Bridal Gown" : 480,
        "Gold Mario Cap" : 500,
        "Gold Mario Suit" : 500,
        "Metal Mario Cap" : 500,
        "Metal Mario Suit" : 500
    }

    # Maximum number of Power Moons for any given kingdom's progression
    max_counts = {
        "cascade": 19,
        "sand": 65,
        "lake": 28,
        "wooded": 53,
        "lost": 20,
        "metro": 57,
        "snow": 35,
        "seaside": 51,
        "luncheon": 53,
        "ruined": 6,
        "bowser": 40,
        "dark": 375,
        "darker": 750
    }
    # Number of Power Moon checks in each kingdom
    max_checks = {
        "cap": 31,
        "cascade": 42,
        "sand": 93,
        "lake": 44,
        "wooded": 80,
        "cloud": 9,
        "lost": 35,
        "metro": 85,
        "snow": 57,
        "seaside": 73,
        "luncheon": 72,
        "ruined": 12,
        "bowser": 64,
        "moon": 38,
        "mushroom": 55,
        "dark": 26,
        "darker": 3
    }

    placed_counts = {
        "cascade": 0,
        "sand": 0,
        "lake": 0,
        "wooded": 0,
        "lost": 0,
        "metro": 0,
        "snow": 0,
        "seaside": 0,
        "luncheon": 0,
        "ruined": 0,
        "bowser": 0,
        "dark": 0,
        "darker": 0
    }

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    item_name_groups = {
        "Cap": ["Cap Power Moon"],
        "Cascade": ["Cascade Power Moon","Cascade Story Moon", "Cascade Multi-Moon"],
        "Sand": ["Sand Power Moon","Sand Story Moon", "Sand Multi-Moon"],
        "Lake": ["Lake Power Moon", "Lake Multi-Moon"],
        "Wooded": ["Wooded Power Moon","Wooded Story Moon", "Wooded Multi-Moon"],
        "Cloud": ["Cloud Power Moon"],
        "Lost": ["Lost Power Moon"],
        "Metro": ["Metro Power Moon","Metro Story Moon", "Metro Multi-Moon"],
        "Snow": ["Snow Power Moon","Snow Story Moon", "Snow Multi-Moon"],
        "Seaside": ["Seaside Power Moon","Seaside Story Moon", "Seaside Multi-Moon"],
        "Luncheon": ["Luncheon Power Moon","Luncheon Story Moon", "Luncheon Multi-Moon"],
        "Ruined": ["Ruined Power Moon", "Ruined Multi-Moon"],
        "Bowser": ["Bowser Power Moon","Bowser Story Moon", "Bowser Multi-Moon"],
        "Moon": ["Moon Power Moon"],
        "Mushroom": ["Power Star", "Mushroom Multi-Moon"],
        "Dark": ["Dark Side Power Moon", "Dark Side Multi-Moon"],
        "Darker": ["Darker Side Multi-Moon"]
    }



    def __init__(self, multiworld: "MultiWorld", player: int):
        # Number of Power Moons required to leave each kingdom
        self.moon_counts = {
            "cascade": 5,
            "sand": 16,
            "lake": 8,
            "wooded": 16,
            "lost": 10,
            "metro": 20,
            "snow": 10,
            "seaside": 10,
            "luncheon": 18,
            "ruined": 3,
            "bowser": 8,
            "dark": 250,
            "darker": 500
        }
        self.shine_items: dict[int, list[str]] = {}
        self.shine_replace_data = {}
        self.shine_colors: dict[int, int] = {}
        self.color_list: list[int] = []
        self.shop_games: list[str] = []
        self.shop_players: list[str] = []
        self.shop_ap_items: list[str] = []
        self.shop_replace_data = {}
        self.coin_values = {}
        self.world_exits: list[tuple[str, dict]] = []
        self.world_sub_area_exits = []
        self.non_dead_end_sub_areas = []
        # Sub Area Entrances allowed for randomization
        self.sub_area_entrances: list[Entrance] = []
        # Sub area Exits allowed for randomization.
        self.sub_area_exits: list[Entrance] = []
        self.valid_top_hat_replacements: list[str] = []
        self.top_hat_tower_bind: str = ""
        self.randomized_entrances: ERPlacementState = None
        self.entrance_data: list[tuple[int,int, int, bool]] = []
        super().__init__(multiworld, player)


    def generate_early(self):
        pass
        # self.multiworld.early_items[self.player]["Cascade Multi-Moon"] = 1
        # self.multiworld.early_items[self.player]["Cascade Story Moon"] = 1
        # self.multiworld.early_items[self.player]["Cascade Power Moon"] = self.moon_counts["cascade"]-4
        # if self.options.capture_sanity.value == self.options.capture_sanity.option_true:
        #     self.multiworld.early_items[self.player]["Broode's Chain Chomp"] = 1
        #     self.multiworld.early_items[self.player]["Chain Chomp"] = 1
        #     self.multiworld.early_items[self.player]["T-Rex"] = 1

    def create_regions(self):
        if self.options.counts > 0:
            self.randomize_moon_amounts()

        create_regions(self)
        sub_area_index = random.randint(0, len(self.valid_top_hat_replacements) - 1)
        self.top_hat_tower_bind = self.valid_top_hat_replacements[sub_area_index]
        print(self.top_hat_tower_bind)

    def create_item(self, name: str) -> Item:
        item_id = self.item_name_to_id[name]
        classification: ItemClassification = ItemClassification.filler
        if name in filler_item_table.keys():
            classification = ItemClassification.filler
        else:
            if name == "Beat the Game" and self.options.goal == "moon":
                classification = ItemClassification.progression_skip_balancing
            elif name in outfits:
                if outfits.index(name) <= 33:
                    classification = ItemClassification.progression_skip_balancing
            elif name in shop_items:
                # Until achievements implemented if possible
                # some outfits for dark and darker goals not handled correctly
                classification = ItemClassification.filler
            elif name in capture_items:
                if self.options.goal < self.options.goal.option_dark and capture_items.index(name) >= 48 and self.options.entrance_randomization == 0:
                    classification = ItemClassification.filler
                else:
                    classification = ItemClassification.progression
            elif name in moon_types:
                classification = ItemClassification.progression

        item: SMOItem

        # if classification == ItemClassification.progression_skip_balancing and name in self.item_name_groups["Cascade"]:
        #     print(name)
        item = SMOItem(name, classification, self.player, item_id)
        return item

    def create_items(self):
        pool : list = []

        # Additively build pool
        #region Moons
        locations: list = []
        for location in self.get_locations():
            if location.name in [*outfits, *shop_items, *capture_items]:
                continue
            else:
                locations += [location.name]
        #print(locations)

        placement_counts = [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ]

        revised_counts = [
            0,
            min(floor(self.moon_counts["cascade"] * self.options.extra_moons.value / 100.0), self.max_counts["cascade"]),
            min(floor(self.moon_counts["sand"] * self.options.extra_moons.value / 100.0), self.max_counts["sand"]),
            min(floor(self.moon_counts["wooded"] * self.options.extra_moons.value / 100.0), self.max_counts["wooded"]),
            min(floor(self.moon_counts["lake"] * self.options.extra_moons.value / 100.0), self.max_counts["lake"]),
            0,
            min(floor(self.moon_counts["lost"] * self.options.extra_moons.value / 100.0), self.max_counts["lost"]),
            min(floor(self.moon_counts["metro"] * self.options.extra_moons.value / 100.0), self.max_counts["metro"]),
            min(floor(self.moon_counts["seaside"] * self.options.extra_moons.value / 100.0), self.max_counts["seaside"]),
            min(floor(self.moon_counts["snow"] * self.options.extra_moons.value / 100.0), self.max_counts["snow"]),
            min(floor(self.moon_counts["luncheon"] * self.options.extra_moons.value / 100.0), self.max_counts["luncheon"]),
            min(floor(self.moon_counts["ruined"] * self.options.extra_moons.value / 100.0), self.max_counts["ruined"]),
            min(floor(self.moon_counts["bowser"] * self.options.extra_moons.value / 100.0), self.max_counts["bowser"]),
            0,
            0,
            0,
            0,
        ]
        if self.options.goal == self.options.goal.option_dark:
            kingdoms : list = list(range(15))
            while sum(revised_counts[0:15]) < self.moon_counts["dark"]:
                index = kingdoms[random.randint(0, len(kingdoms) - 1)]
                revised_counts[index] += 1
                if revised_counts[index] == self.max_checks[world_list[index].lower()]:
                    kingdoms.remove(index)
        elif self.options.goal == self.options.goal.option_darker:
            kingdoms: list = list(range(16))
            while sum(revised_counts[0:16]) < self.moon_counts["darker"]:
                index = kingdoms[random.randint(0, len(kingdoms) - 1)]
                revised_counts[index] += 1
                if revised_counts[index] == self.max_checks[world_list[index].lower()]:
                    kingdoms.remove(index)

        for kingdom in story_moons.keys():
            for i in range(len(story_moons[kingdom])):
                if story_moons[kingdom][i] in locations:
                    pool.append(f"{kingdom} Story Moon")
                    placement_counts[world_list.index(kingdom.capitalize())] += 1
                    placement_counts[15] += 1
                    placement_counts[16] += 1
        for kingdom in multi_moons.keys():
            for i in range(len(multi_moons[kingdom])):
                if multi_moons[kingdom][i] in locations:
                    pool.append(f"{kingdom + (' Side' if 'Dark' in kingdom else '')} Multi-Moon")
                    placement_counts[world_list.index(kingdom.capitalize())] += 3
                    placement_counts[15] += 3
                    placement_counts[16] += 3

        for index in range(len(world_list)):
            while placement_counts[index] < revised_counts[index]:
                pool.append(f"{world_list[index] + (' Side' if 'Dark' in world_list[index] else '')} Power Moon")
                placement_counts[index] += 1
                placement_counts[15] += 1
                placement_counts[16] += 1


        # for location in locations:
        #     # found : bool = False
        #     for index in range(len(world_list)):
        #         if location in full_moon_locations_list[index]:
        #             item = ""
        #             if (placement_counts[index] < revised_counts[index]
        #                 or (world_list[index] in story_moons and location in story_moons[world_list[index]])
        #                 or (index < 14 and world_list[index] in multi_moons and location in multi_moons[world_list[index]])):
        #                 # found = True
        #                 item: str = world_list[index]
        #                 place : bool = False
        #
        #                 if "Dark" in item:
        #                     item += " Side"
        #                 # Multi
        #                 if world_list[index] in multi_moons and location in multi_moons[world_list[index]]:
        #                     item += " Multi-Moon"
        #                     # Prevent placement of duplicate goal Multi-Moon
        #                     if location == goals_table[self.options.goal.value]:
        #                         break
        #                     place = not self.options.story >= 2
        #                 elif world_list[index] in story_moons and location in story_moons[world_list[index]]:
        #                     item += " Story Moon"
        #                     place = not (self.options.story == 1 or self.options.story == 3)
        #                 else:
        #                     if world_list[index] == "Mushroom":
        #                         item = "Power Star"
        #                     else:
        #                         item += " Power Moon"
        #
        #                 placement_counts[index] += 3 if "Multi" in item else 1
        #
        #                 if place:
        #                     self.get_location(location).place_locked_item(self.create_item(item))
        #                     break
        #             else:
        #                 pass
        #                 #print(location)
        #             if item != "":
        #                 if "Snow" in item:
        #                     pass
        #                     #print (item)
        #                 pool.append(item)
        #             break
        #     # if not found:
        #     #     print(location)
        for index in range(len(world_list)):
            while placement_counts[index] > revised_counts[index]:
                if world_list[index] + " Power Moon" in pool:
                    pool.remove(world_list[index] + " Power Moon")
                    placement_counts[index] -= 1
                else:
                    break

        #endregion Moons

        for item in self.multiworld.early_items[self.player]:
            while item in pool:
                pool.remove(item)

        locations : list = []

        for location in self.get_locations():
            if location.name in outfits or location.name in shop_items:
                locations += [location.name]

        #region Shops
        item_names : list = []
        # Outfits
        for location in outfits:
            if location in locations:
                if self.options.shop_sanity == "outfits" or self.options.shop_sanity == "all":
                    pool.append(location)
                elif self.options.shop_sanity == "shuffle":
                    item_names.append(location)
                else:
                    self.get_location(location).place_locked_item(self.create_item(location))

        # Souvenirs and stickers
        for location in shop_items:
            if location in locations:
                if self.options.shop_sanity == "non_outfits" or self.options.shop_sanity == "all":
                    pool.append(location)
                else:
                    self.get_location(location).place_locked_item(self.create_item(location))

        # Shop sanity shuffle
        if self.options.shop_sanity == "shuffle":
            while len(item_names) > 0:
                item = item_names.pop(random.randint(0, len(item_names) - 1))
                self.get_location(item).place_locked_item(self.create_item(item))

        #endregion Shops

        #region Captures
        locations: list = []
        for location in self.get_locations():
            if location.name in capture_items and not location.item:
                locations += [location.name]
            # else:
            #      print(location.name)

        if self.options.capture_sanity.value == self.options.capture_sanity.option_true:
            for location in locations:
                if location in capture_items and not location in self.multiworld.early_items[self.player]:
                    pool.append(location)

        #endregion Captures

        #region Regional Coins



        #endregion Regional Coins


        # Remove start_inventory items from pool
        for start_item in self.options.start_inventory:
            for num in range(self.options.start_inventory[start_item]):
                pool.remove(start_item)

        needed_items = len(list(self.multiworld.get_unfilled_locations(self.player))) - 1
        print(len(pool), needed_items)
        if len(pool) < needed_items:
            while len(pool) - 1 < needed_items:
                pool.append(self.get_filler_item_name())
        # else:
        #     while len(pool) > needed_items:
        #         pool.remove(self.get_filler_item_name())


        for i in pool:
            self.multiworld.itempool += [self.create_item(i)]
        # Reset placed counts so multi worlds support more than one SMO instance
        for key in self.placed_counts.keys():
            self.placed_counts[key] = 0

    def set_rules(self):
        set_rules(self, self.options)

    def connect_entrances(self) -> None:
            # SOMEWHERE in reassigning of top hat, exits and entrances become unequal
        if self.options.entrance_randomization > 0:

            intro = self.get_region(SMORegion.cap_kingdom_intro)
            topper = self.get_region(SMORegion.cap_kingdom_topper)
            bind_region = self.get_region(self.top_hat_tower_bind)
            top_hat = self.get_region(SMORegion.top_hat_tower)

            if len(self.sub_area_entrances) != len(self.sub_area_exits):
               raise("Mismatch. ", f"Entrances: {len(self.sub_area_entrances)} Exits: {len(self.sub_area_exits)}")

            for entrance in self.sub_area_entrances:
                if entrance.randomization_type == EntranceType.ONE_WAY:
                    disconnect_entrance_for_randomization(entrance, SMORandomizationGroup.DOOR,
                                                          f"{entrance.name}")
                else:
                    # if " Entrance" in entrance.name and entrance.parent_region == bind_region:
                    #     disconnect_entrance_for_randomization(entrance,  SMORandomizationGroup.TOP_HAT_ENTER)
                    #
                    # elif " End" in entrance.name and entrance.parent_region == bind_region:
                    #     disconnect_entrance_for_randomization(entrance,  SMORandomizationGroup.TOP_HAT_ENTER)
                    #
                    #
                    # elif entrance.parent_region == intro:
                    #     disconnect_entrance_for_randomization(entrance, SMORandomizationGroup.TOP_HAT_EXIT)
                    #
                    # elif entrance.parent_region == topper:
                    #     disconnect_entrance_for_randomization(entrance, SMORandomizationGroup.TOP_HAT_EXIT)
                    #
                    # else:
                        disconnect_entrance_for_randomization(entrance, SMORandomizationGroup.DOOR)

            for possible_exit in self.sub_area_exits:
                # if f"{self.top_hat_tower_bind} Entrance" in possible_exit.name and possible_exit.parent_region == bind_region:
                #     possible_exit.randomization_group = SMORandomizationGroup.TOP_HAT_EXIT
                #
                # elif f"{self.top_hat_tower_bind} End" in possible_exit.name and possible_exit.parent_region == bind_region :
                #     possible_exit.randomization_group = SMORandomizationGroup.TOP_HAT_EXIT
                #
                # elif possible_exit.parent_region == intro:
                #     possible_exit.randomization_group = SMORandomizationGroup.TOP_HAT_ENTER
                #
                # elif possible_exit.parent_region == topper:
                #     possible_exit.randomization_group = SMORandomizationGroup.TOP_HAT_ENTER

                possible_exit.connected_region = None

            no_target_group = {
            SMORandomizationGroup.DOOR: [SMORandomizationGroup.DOOR, SMORandomizationGroup.PIPE],
                SMORandomizationGroup.TOP_HAT_ENTER: [SMORandomizationGroup.TOP_HAT_EXIT],
                SMORandomizationGroup.TOP_HAT_EXIT: [SMORandomizationGroup.TOP_HAT_ENTER],
                # SMORandomizationGroup.TOP_HAT_SUB_AREA_ENTER: [SMORandomizationGroup.TOP_HAT_ENTER],
                # SMORandomizationGroup.TOP_HAT_SUB_AREA_EXIT: [SMORandomizationGroup.TOP_HAT_EXIT],
            }

            self.randomized_entrances = randomize_entrances(self, coupled=True, target_group_lookup=no_target_group, exits=self.sub_area_exits)

        # Finish Regional Coin Rules in Rules.py
        # Fix some exits not having a corresponding entrance

    def get_filler_item_name(self) -> str:
        #print ("why no filler")
        return "Coins"

    def generate_basic(self) -> None:
        pass

    def randomize_moon_amounts(self):
        """ Randomizes the moon requirements for progressing to each kingdom."""
        if self.options.counts == 1:
            for key in self.moon_counts.keys():
                if key != "dark" and key != "darker":
                    self.moon_counts[key] = 1
            kingdoms = list(self.moon_counts.keys())
            kingdoms.remove("dark")
            kingdoms.remove("darker")
            count = 0
            for kingdom in kingdoms:
                count += self.moon_counts[kingdom]
            while count != 124 and len(kingdoms) > 0:
                selected = kingdoms[random.randint(0, len(kingdoms)-1)]
                self.moon_counts[selected] += 1
                count += 1
                if self.moon_counts[selected] == self.max_counts[selected]:
                    kingdoms.remove(selected)
        elif self.options.counts == 2:
            for key in self.moon_counts.keys():
                if key != "dark" and key != "darker":
                    self.moon_counts[key] = 1
            self.moon_counts["ruined"] = 3
            kingdoms = list(self.moon_counts.keys())
            kingdoms.remove("dark")
            kingdoms.remove("darker")
            kingdoms.remove("ruined")
            count = 3
            for kingdom in kingdoms:
                count += self.moon_counts[kingdom]
            while count != 124:
                selected = kingdoms[random.randint(0, len(kingdoms)-1)]
                self.moon_counts[selected] += 1
                count += 1
                if self.moon_counts[selected] == self.max_counts[selected]:
                    kingdoms.remove(selected)
        elif self.options.counts == 3:
            for key in self.moon_counts.keys():
                self.moon_counts[key] = random.randint(int(self.moon_counts[key] * 0.8), int(self.moon_counts[key] * 1.25))

        elif self.options.counts == 4:
            for key in self.moon_counts.keys():
                self.moon_counts[key] = random.randint(int(self.moon_counts[key] * 1.0), int(self.moon_counts[key] * 2.0))
        if self.moon_counts["dark"] > self.moon_counts["darker"]:
            temp = self.moon_counts["darker"]
            self.moon_counts["darker"] = self.moon_counts["dark"]
            self.moon_counts["dark"] = temp
        for key in self.moon_counts.keys():
            if self.moon_counts[key] > self.max_counts[key]:
                self.moon_counts[key] = self.max_counts[key]
        if self.options.counts == 1 or self.options.counts == 2:
            kingdoms = list(self.moon_counts.keys())
            kingdoms.remove("dark")
            kingdoms.remove("darker")
            count = 0
            for kingdom in kingdoms:
                count += self.moon_counts[kingdom]
            if count != 124:
                raise Exception("Moon count exception! Moons required to beat the game is not 124, was " + str(count))
        # Change all outfit moon requirements to a proportion based on random Dark Side count
        # for key in self.outfit_moon_counts.keys():
        #     self.outfit_moon_counts[key] = int(self.outfit_moon_counts[key] * (self.moon_counts["dark"]/250))
            # if self.outfit_moon_counts[key] > self.moon_counts["dark"]:
            #     self.outfit_moon_counts[key] = self.moon_counts["dark"] - 1


    def bind_game_entrances(self) -> None:
        entry : Entrance
        missing_bindings = []
        for entry in self.randomized_entrances.placements:
            if entry.name == "Top Hat Tower Entrance":
                print(entry.name, entry.connected_region)
            if entry.connected_region.name == SMORegion.cap_kingdom_topper:
                print(entry.name, entry.connected_region)
            if entry.parent_region.name not in display_name_to_internal_name.keys():
                if entry.parent_region.name not in missing_bindings and entry.parent_region.name not in display_name_alias.keys():
                    missing_bindings.append(entry.parent_region.name)
            if entry.connected_region.name not in display_name_to_internal_name.keys():
                if entry.connected_region.name not in missing_bindings and entry.connected_region.name not in display_name_alias.keys():
                    missing_bindings.append(entry.connected_region.name)

        for unique_entry in missing_bindings:
            pass
            #print(f'"{unique_entry}",')

        for key in display_name_to_internal_name.keys():
            if display_name_to_internal_name[key] not in list(stage_id_to_name.values()):
                pass
                #print(key)

        #set_stage_ids = set(stage_ids)

        for i in range(len(stage_ids)):
            if stage_ids.index(stage_ids[i]) != i:
                print(i, stage_ids[i])

        # for i in set_stage_ids:
        #     print(f"'{i}',")

        missing_maps = []
        missing_stage_ids = []

        for i in internal_name_to_entrance:
            if i not in stage_names:
                missing_maps.append(i)


            for j in internal_name_to_entrance[i]:
                if isinstance(internal_name_to_entrance[i][j], dict):
                    for k in internal_name_to_entrance[i][j]:
                        if internal_name_to_entrance[i][j][k] not in stage_ids and internal_name_to_entrance[i][j][k] not in missing_stage_ids:
                            missing_stage_ids.append(internal_name_to_entrance[i][j][k])
                else:
                    if internal_name_to_entrance[i][j] not in stage_ids and internal_name_to_entrance[i][j] not in missing_stage_ids:
                        missing_stage_ids.append(internal_name_to_entrance[i][j])

        for i in missing_maps:
            print(f"'{i}',")

        for i in missing_stage_ids:
            print(f"'{i}',")

        pass_through_areas = [*world_list, "Inverted", "Underground", "Rematch"]
        for entrance, binding in self.randomized_entrances.pairings:
            if entrance in self.multiworld.regions.entrance_cache[self.player]:
                _exit = self.get_entrance(entrance)
            else:
                print(entrance)
            if binding in self.multiworld.regions.entrance_cache[self.player]:
                entry = self.get_entrance(binding)
            else:
                print(binding)
            # add proper support for _rev entrances and exits (ex. Shiveria/SnowWorldTownStage)
            exit_name = (display_name_to_internal_name[_exit.parent_region.name
                if (_exit.name.split(' ')[0] in pass_through_areas or _exit.name.split(' ')[1] in pass_through_areas)
                else _exit.name[0:_exit.name.index(" Entrance")]
                if " Entrance" in _exit.name else _exit.name[0:_exit.name.index(" End")]])
            entry_name = (display_name_to_internal_name[entry.parent_region.name
                if (entry.name.split(' ')[0] in pass_through_areas or entry.name.split(' ')[1] in pass_through_areas)
                else entry.name[0:entry.name.index(" Entrance")]
                if " Entrance" in entry.name else entry.name[0:entry.name.index(" End")]])
            exit_stage_name = exit_name if 'WorldHomeStage' not in exit_name else display_name_to_internal_name[_exit.name[0:-9 if " Entrance" in _exit.name else -4]]
            entry_stage_name = entry_name if 'WorldHomeStage' not in entry_name else display_name_to_internal_name[entry.name[0:entry.name.index(" Entrance" if " Entrance" in entry.name else " End")]]
            if 'entrance' in internal_name_to_entrance[exit_name] or 'exit' in internal_name_to_entrance[exit_name]:
                exit_stage_id = (internal_name_to_entrance[exit_name]
                    ['entrance' if ' entrance' in _exit.name.lower()
                        else 'exit' if  ' end' in _exit.name.lower()
                        else ''])
            else:
                if isinstance(internal_name_to_entrance[exit_name][exit_stage_name], dict):
                    exit_stage_id = (internal_name_to_entrance[exit_name][exit_stage_name]
                    ['entrance' if ' entrance' in _exit.name.lower()
                    else 'exit' if  ' end' in _exit.name.lower() else ''])
                else:
                    exit_stage_id = internal_name_to_entrance[exit_name][exit_stage_name]
            if 'entrance' in internal_name_to_entrance[entry_name] or 'exit' in internal_name_to_entrance[entry_name]:
                enter_stage_id = (internal_name_to_entrance[entry_name]
                ['entrance' if ' entrance' in entry.name.lower()
                    else 'exit' if  ' end' in entry.name.lower() else ''])
            else:
                if isinstance(internal_name_to_entrance[entry_name][entry_stage_name], dict):
                    enter_stage_id = (internal_name_to_entrance[entry_name][entry_stage_name]
                    ['entrance' if ' entrance' in entry.name.lower()
                    else 'exit' if  ' end' in entry.name.lower() else ''])
                else:
                    enter_stage_id = internal_name_to_entrance[entry_name][entry_stage_name]
            exit_stage_id_index = stage_ids.index(exit_stage_id)
            enter_stage_id_index = stage_ids.index(enter_stage_id)
            entry_index = stage_names.index(entry_name)
            self.entrance_data.append((exit_stage_id_index, enter_stage_id_index, entry_index, entry_stage_name == entry_name))



    # Change regionals to be dependent on the option
    def fill_slot_data(self) -> Mapping[str, Any]:
        # Entrance Rando
        if self.options.entrance_randomization:
            self.bind_game_entrances()
            print("test")


        for player in range(1, self.multiworld.players + 1):
            if not player in self.coin_values:
                self.coin_values[player] = {}
            for location in self.multiworld.get_locations(player):
                if location.item.player == self.player:
                    if location.item.game == self.game and location.item.name == "Coins":
                        rand_num = self.random.randint(0,99)
                        if rand_num < 44:
                            coin_amount = self.random.randint(50, 100)
                            location.item.name = f"{str(coin_amount)} " + location.item.name
                            self.coin_values[location.player][location.address] = coin_amount
                        elif rand_num < 74:
                            coin_amount = self.random.randint(101, 250)
                            location.item.name = f"{str(coin_amount)} " + location.item.name
                            self.coin_values[location.player][location.address] = coin_amount
                        elif rand_num < 89:
                            coin_amount = self.random.randint(251, 500)
                            location.item.name = f"{str(coin_amount)} " + location.item.name
                            self.coin_values[location.player][location.address] = coin_amount
                        elif rand_num < 96:
                            coin_amount = self.random.randint(501, 750)
                            location.item.name = f"{str(coin_amount)} " + location.item.name
                            self.coin_values[location.player][location.address] = coin_amount
                        elif rand_num < 100:
                            coin_amount = self.random.randint(751, 1000)
                            location.item.name = f"{str(coin_amount)} " + location.item.name
                            self.coin_values[location.player][location.address] = coin_amount



        for world_id in range(len(location_hint_list)):
            self.shine_replace_data[world_id] = {}
            self.shine_items[world_id] = []

        for location in self.multiworld.get_locations(self.player):
            for world_id in range(len(location_hint_list)):
                if self.location_name_to_id[location.name] in location_hint_list[world_id]:
                    if not location.item.name in self.shine_items[world_id]:
                        self.shine_items[world_id].append(f"{self.multiworld.get_player_name(location.item.player)}'s {location.item.name.replace('_', ' ')}")

        # Sort shine item lists
        for world_id in range(len(location_hint_list)):
            self.shine_items[world_id] = sorted(self.shine_items[world_id])

        for world_id in range(len(location_hint_list)):
            for hint_id in range(len(location_hint_list[world_id])):
                for key in list(location_hint_list[world_id].keys()):
                    if location_hint_list[world_id][key] == hint_id:
                        loc_name = self.location_id_to_name[key]
                        if loc_name in self.multiworld.regions.location_cache[self.player]:
                            location = self.multiworld.get_location(loc_name, self.player)
                            name_index : int = self.shine_items[world_id].index(f"{self.multiworld.get_player_name(location.item.player)}'s {location.item.name.replace('_', ' ')}")
                            self.shine_replace_data[world_id][hint_id] = [-1, name_index]
                        else:
                            self.shine_replace_data[world_id][hint_id] = [-1, 255]

        match self.options.colors.value:
            case self.options.colors.option_off:
                self.color_list = [0, 0, 5, 7, 2, 0, 0, 1, 4, 8, 6, 0, 3, 9, -1, 9, 9, 27]
                for location in self.get_locations():
                    for kingdom in range(17):
                        if location.name in full_moon_locations_list[kingdom]:
                            self.shine_colors[self.location_name_to_id[location.name]] = self.color_list[kingdom]

            case self.options.colors.option_kingdom_random:
                colors = list(range(30))
                for i in range(17):
                    self.color_list.append(colors.pop(self.random.randint(0, len(colors) - 1)))
                for location in self.get_locations():
                    for kingdom in range(17):
                        if location.name in full_moon_locations_list[kingdom]:
                            self.shine_colors[self.location_name_to_id[location.name]] = self.color_list[kingdom]

            case self.options.colors.option_item:
                self.color_list = [0, 15, 5, 2, 7, 11, 14, 1, 8, 4, 6, 13, 17, 9, -1, 9, 9, 10, 12, 16, 18, 19]
                for location in self.get_locations():
                    for kingdom in range(17):
                        if self.location_name_to_id[location.name] < 1168:
                            if location.item.game == self.game:
                                if location.item.name in capture_items:
                                    self.shine_colors[self.location_name_to_id[location.name]] = self.color_list[18]
                                elif location.item.name in stickers or location.item.name in souvenirs:
                                    self.shine_colors[self.location_name_to_id[location.name]] = self.color_list[19]
                                elif location.item.name in outfits:
                                    self.shine_colors[self.location_name_to_id[location.name]] = self.color_list[20]
                                elif world_list[kingdom] in location.item.name:
                                    self.shine_colors[self.location_name_to_id[location.name]] = self.color_list[kingdom]
                                    break

                            else:
                                self.shine_colors[self.location_name_to_id[location.name]] = self.color_list[21]
                                break

            case self.options.colors.option_classification:
                pass

            case self.options.colors.option_item_random:
                colors = list(range(30))
                for i in range(22):
                    self.color_list.append(colors.pop(self.random.randint(0, len(colors) - 1)))
                for location in self.get_locations():
                    for kingdom in range(17):
                        if self.location_name_to_id[location.name] < 1168:
                            if location.item.game == self.game:
                                if location.item.name in capture_items:
                                    self.shine_colors[self.location_name_to_id[location.name]] = self.color_list[18]
                                elif location.item.name in stickers or location.item.name in souvenirs:
                                    self.shine_colors[self.location_name_to_id[location.name]] = self.color_list[19]
                                elif location.item.name in outfits:
                                    self.shine_colors[self.location_name_to_id[location.name]] = self.color_list[20]
                                elif world_list[kingdom] in location.item.name:
                                    self.shine_colors[self.location_name_to_id[location.name]] = self.color_list[
                                        kingdom]
                                    break

                            else:
                                self.shine_colors[self.location_name_to_id[location.name]] = self.color_list[21]
                                break

            case self.options.colors.option_classification_random:
                pass

            case self.options.colors.option_chaos:
                for location in self.get_locations():
                    if self.location_name_to_id[location.name] < 1168:
                        self.shine_colors[self.location_name_to_id[location.name]] = self.random.randint(0,30)

        self.shop_replace_data["caps"] = {}
        self.shop_replace_data["clothes"] = {}
        self.shop_replace_data["stickers"] = {}
        self.shop_replace_data["souvenirs"] = {}
        self.shop_replace_data["moons"] = {}
        self.shop_games = []
        self.shop_players = []
        self.shop_ap_items = []
        for location in self.multiworld.get_locations(self.player):
            if location.name in shop_items or location.name in outfits or "Shopping" in location.name:
                if not self.multiworld.get_player_name(location.item.player) in self.shop_players:
                    self.shop_players.append(self.multiworld.get_player_name(location.item.player))
                if not location.item.name in self.shop_ap_items:
                    self.shop_ap_items.append(location.item.name.replace("_", " "))
                if not location.item.game in self.shop_games:
                    self.shop_games.append(location.item.game.replace("_", " "))
        self.shop_games = sorted(self.shop_games)
        self.shop_players = sorted(self.shop_players)
        self.shop_ap_items = sorted(self.shop_ap_items)
        for location in self.multiworld.get_locations(self.player):
                if self.location_name_to_id[location.name] < 2582 :
                    if "Shopping" in location.name:
                        self.shop_replace_data["moons"][self.location_name_to_id[location.name]] = [self.shop_games.index(location.item.game.replace("_", " ")),
                        self.shop_players.index(self.multiworld.get_player_name(location.item.player)),
                        self.shop_ap_items.index(location.item.name.replace("_", " ")), location.item.classification.value]
                    else:
                        if 2539 > self.location_name_to_id[location.name] > 2500 or 2582 > self.location_name_to_id[location.name] > 2576:
                            self.shop_replace_data["caps"][self.location_name_to_id[location.name]] = [self.shop_games.index(location.item.game.replace("_", " ")),
                            self.shop_players.index(self.multiworld.get_player_name(location.item.player)),
                            self.shop_ap_items.index( location.item.name.replace("_", " ")), location.item.classification.value]
                        if self.location_name_to_id[location.name] > 2538:
                            self.shop_replace_data["clothes"][self.location_name_to_id[location.name]] = [self.shop_games.index(location.item.game.replace("_", " ")),
                            self.shop_players.index(self.multiworld.get_player_name(location.item.player)),
                            self.shop_ap_items.index(location.item.name.replace("_", " ")), location.item.classification.value]
                if location.name in stickers:
                    self.shop_replace_data["stickers"][self.location_name_to_id[location.name]] = [self.shop_games.index(location.item.game.replace("_", " ")),
                    self.shop_players.index(self.multiworld.get_player_name(location.item.player)),
                    self.shop_ap_items.index(location.item.name.replace("_", " ")), location.item.classification.value]
                if location.name in souvenirs:
                    self.shop_replace_data["souvenirs"][self.location_name_to_id[location.name]] = [self.shop_games.index(location.item.game.replace("_", " ")),
                    self.shop_players.index(self.multiworld.get_player_name(location.item.player)),
                    self.shop_ap_items.index(location.item.name.replace("_", " ")), location.item.classification.value]

        return {**(self.options.as_dict("goal", "colors", "capture_sanity", "entrance_randomization", "death_link")), "counts" : self.moon_counts,
                "shine_items" : self.shine_items, "shine_replace_data" : self.shine_replace_data, "shine_colors" : self.shine_colors,
                "shop_games" : self.shop_games, "shop_players" : self.shop_players, "shop_ap_items" : self.shop_ap_items,
                "shop_replace_data" : self.shop_replace_data, "coin_values" : self.coin_values,
                "regionals" : False,
                "entrances" : ""}


    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        if self.options.counts > 0:
            text = f"{'Moon Requirements:':33}"
            for key in self.moon_counts.keys():
                if world_list.index(key.capitalize()) <= self.options.goal:
                    text += f"\n{'':33}{(key.capitalize() + (' Kingdom: ' if world_list.index(key.capitalize()) < self.options.goal.option_dark else ' Side: '))}{str(self.moon_counts[key])}"
            spoiler_handle.write(text)

    def generate_output(self, output_directory: str):
        pass
        # if self.options.colors.value or self.options.counts.value > 0 or self.options.shop_sanity.value > 0:
        #     out_base = output_path(output_directory, self.multiworld.get_out_file_name_base(self.player))
        #     patch = SMOProcedurePatch(player=self.player, player_name=self.multiworld.get_player_name(self.player))
        #     write_patch(self, patch)
        #     patch.write(os.path.join(output_directory, f"{out_base}{patch.patch_file_ending}"))

    def interpret_slot_data(self, slot_data: dict[str, any]) -> dict[str, any]:
        """Parse slot data for Universal Tracker to properly validate logic and track progression."""
        relevant_data = {}

        # Parse moon count requirements for each kingdom
        relevant_data["MoonCounts"] = slot_data["counts"]

        # Parse game options
        relevant_data["Goal"] = slot_data["goal"]
        relevant_data["Colors"] = slot_data["colors"]
        relevant_data["CaptureSanity"] = slot_data["capture_sanity"]

        # Parse shine data structures (for hint system)
        relevant_data["ShineItems"] = slot_data["shine_items"]
        relevant_data["ShineReplaceData"] = slot_data["shine_replace_data"]
        relevant_data["ShineColors"] = slot_data["shine_colors"]

        # Parse shop data structures
        relevant_data["ShopGames"] = slot_data["shop_games"]
        relevant_data["ShopPlayers"] = slot_data["shop_players"]
        relevant_data["ShopAPItems"] = slot_data["shop_ap_items"]
        relevant_data["ShopReplaceData"] = slot_data["shop_replace_data"]

        # Parse coin values
        relevant_data["CoinValues"] = slot_data["coin_values"]

        return relevant_data