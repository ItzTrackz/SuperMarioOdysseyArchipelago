from collections.abc import Callable
from enum import IntEnum, StrEnum
from typing import Any

from BaseClasses import Location
from worlds.generic.Rules import set_rule, add_rule
from . import regional_coin_table, regional_coin_groups, regional_coin_groups_table
from .Data.RegionData import SMORegion
from .Data.ItemData import SMOItemData
from .Data.EntranceData import SMOEntranceData
from .Data.LocationData import SMOLocationData
from .Data.RuleData import SMORuleCondition, SMORuleOperation, SMOEntranceDataType, SMOKingdoms, rule_data, \
    moon_rule_data
from .Locations import shop_location_costs
from .Items import capture_items
from .Options import SMOOptions
from .Logic import total_moons, count_moons, count_regionals

all_access_rules : set = set()

def create_access_rule(self: "SMOWorld", conditions: list[tuple[SMORuleCondition, Any, SMORuleOperation]]) -> callable:
    """
    Creates an access rule in which all ``conditions`` are met.
    Args:
        self: the current world.
        conditions: a list of conditions and operations that compose the access rule.
    Returns:
        a callable ``access_rule`` function
    """

    def is_active(options: SMOOptions, condition_type:  SMORuleCondition) -> bool:
        """
        Checks if the current condition type is active using the current world options.
        Args:
            options: the ``SMOOptions`` instance of the current world.
            condition_type: the ``SMORuleCondition`` to test.
        Returns:
            ``True`` if the related ``SMOOption`` is enabled. ``False`` otherwise.
        """
        match condition_type:
            case SMORuleCondition.CAPTURE:
                return options.capture_sanity.value == options.capture_sanity.option_true
            #case SMORuleCondition.REGIONAL_COINS:


            # case SMORuleCondition.TRICK_EASY:
            #     return options.trick_logic.value > options.trick_logic.option_off
            #
            # case SMORuleCondition.TRICK_INTERMEDIATE:
            #     return options.trick_logic.value > options.trick_logic.option_easy
            #
            # case SMORuleCondition.TRICK_HARD:
            #     return options.trick_logic.value > options.trick_logic.option_intermediate
            #
            #
            # case SMORuleCondition.GLITCH_EASY:
            #     return options.glitch_logic.value > options.glitch_logic.option_off
            #
            # case SMORuleCondition.GLITCH_INTERMEDIATE:
            #     return options.glitch_logic.value > options.glitch_logic.option_easy
            #
            # case SMORuleCondition.GLITCH_HARD:
            #     return options.glitch_logic.value > options.glitch_logic.option_intermediate
            #

        return True


    access_rule: str = 'lambda state: '
    num_conditions = len(conditions)
    condition_index = 0
    parenthesis_open = False
    rules_list : list[callable] = []
    parenthesis_groups : list[list[int]] = []
    starting_parenthesis : list[int] = []
    in_parenthesis = []
    parenthesis_operators = [SMORuleOperation.PARENTHESIS_NONE, SMORuleOperation.PARENTHESIS_AND, SMORuleOperation.PARENTHESIS_OR]
    for condition, data, operation in conditions:
        if operation in parenthesis_operators:
            if not parenthesis_open and is_active(self.options, condition):
                access_rule += f"("
                parenthesis_groups.append([])
                starting_parenthesis.append(condition_index)
            parenthesis_open = not parenthesis_open
            # if parenthesis_open:
            #     in_parenthesis.append(condition_index)
            #     parenthesis_groups[-1].append(condition_index)

        match condition:
            # case SMORuleCondition.PARENTHESIS_OPEN:
            #     access_rule += " ("
            #
            # case SMORuleCondition.PARENTHESIS_CLOSE:
            #     access_rule += ") "

            case "origin":
                pass
            case SMORuleCondition.REGION:
                access_rule += f'state.can_reach_region("{data}", {self.player})'
                all_access_rules.add(f'state.can_reach_region("{data}", {self.player})')
                rules_list.append(lambda state: state.can_reach_region(data, self.player))

            case SMORuleCondition.ENTRANCE:
                access_rule += f'state.can_reach_entrance("{data[0]} {data[1]} {data[2]}", {self.player})'
                all_access_rules.add(f'state.can_reach_entrance("{data[0]} {data[1]} {data[2]}", {self.player})')
                rules_list.append(lambda state: state.can_reach_entrance(f"{data[0]} {data[1]} {data[2]}", self.player))

            case SMORuleCondition.CAPTURE:
                if is_active(self.options, condition):
                    if isinstance(data, str):
                        access_rule += f'state.has_all(["{data}"], {self.player})'
                        all_access_rules.add(f'state.has_all(["{data}"], {self.player})')
                        rules_list.append(lambda state : state.has_all([data], self.player))

                    else:
                        access_rule += f'state.has_all({data}, {self.player})'
                        all_access_rules.add(f'state.has_all({data}, {self.player})')
                        rules_list.append(lambda state : state.has_all(data, self.player))

            case SMORuleCondition.ITEM:
                if isinstance(data, str):
                    access_rule += f'state.has_all(["{data}"], {self.player})'
                    all_access_rules.add(f'state.has_all(["{data}"], {self.player})')
                    rules_list.append(lambda state: state.has_all([data], self.player))

                else:
                    access_rule += f'state.has_all({data}, {self.player})'
                    all_access_rules.add(f'state.has_all({data}, {self.player})')
                    rules_list.append(lambda state: state.has_all(data, self.player))

            case SMORuleCondition.LOCATION:
                access_rule += f'state.can_reach(state, "{data}", "Location", {self.player})'
                all_access_rules.add(f'state.can_reach(state, "{data}", "Location", {self.player})')

            case SMORuleCondition.MOONS:
                access_rule += f'count_moons(state, "{data[0]}", {self.player}) >= {data[1]}'
                all_access_rules.add(f'count_moons(state, "{data[0]}", {self.player}) >= {data[1]}')
                rules_list.append(lambda state: count_moons(state, data[0], self.player) >= data[1])

            case SMORuleCondition.TOTAL_MOONS:
                access_rule += f'total_moons(state, {self.player}) >= {data}'
                all_access_rules.add(f'total_moons(state, {self.player}) >= {data}')
                rules_list.append(lambda state: total_moons(state, self.player) >= data)

            case SMORuleCondition.REGIONAL_COINS:
                access_rule += f'count_regionals(state, "{data[0]}", {self.player}) >= {data[1]}'
                all_access_rules.add(f'count_regionals(state, "{data[0]}", {self.player}) >= {data[1]}')
                rules_list.append(lambda state: count_regionals(state, data[0], self.player) >= data[1])

            case SMORuleCondition.TRICK_EASY:
                rules_list.append(lambda state: state.multiworld.worlds[self.player].options.trick_logic.value > state.multiworld.worlds[self.player].options.trick_logic.option_off)
                if is_active(self.options, condition):
                    if not data or data and is_active(self.options, data):
                        access_rule += f'state.multiworld.worlds[{self.player}].options.trick_logic.value > state.multiworld.worlds[{self.player}].options.trick_logic.option_off'
                        all_access_rules.add(f'state.multiworld.worlds[{self.player}].options.trick_logic.value > state.multiworld.worlds[{self.player}].options.trick_logic.option_off')

                    else:
                        operation = SMORuleOperation.NONE

            case SMORuleCondition.TRICK_INTERMEDIATE:
                rules_list.append(lambda state: state.multiworld.worlds[self.player].options.trick_logic.value > state.multiworld.worlds[self.player].options.trick_logic.option_easy)
                if is_active(self.options, condition):
                    if not data or data and is_active(self.options, data):
                        access_rule += f'state.multiworld.worlds[{self.player}].options.trick_logic.value > state.multiworld.worlds[{self.player}].options.trick_logic.option_easy'
                        all_access_rules.add(f'state.multiworld.worlds[{self.player}].options.trick_logic.value > state.multiworld.worlds[{self.player}].options.trick_logic.option_easy')
                    else:
                        operation = SMORuleOperation.NONE

            case SMORuleCondition.TRICK_HARD:
                rules_list.append(lambda state: state.multiworld.worlds[self.player].options.trick_logic.value > state.multiworld.worlds[self.player].options.trick_logic.option_intermediate)
                if is_active(self.options, condition):
                    if not data or data and is_active(self.options, data):
                        access_rule += f'state.multiworld.worlds[{self.player}].options.trick_logic.value > state.multiworld.worlds[{self.player}].options.trick_logic.option_intermediate'
                        all_access_rules.add(f'state.multiworld.worlds[{self.player}].options.trick_logic.value > state.multiworld.worlds[{self.player}].options.trick_logic.option_intermediate')

                    else:
                        operation = SMORuleOperation.NONE

            case SMORuleCondition.GLITCH_EASY:
                rules_list.append(
                    lambda state: state.multiworld.worlds[self.player].options.glitch_logic.value > state.multiworld.worlds[
                        self.player].options.glitch_logic.option_off)
                if is_active(self.options, condition):
                    access_rule += f'state.multiworld.worlds[{self.player}].options.glitch_logic.value > state.multiworld.worlds[{self.player}].options.glitch_logic.option_off'
                    all_access_rules.add(f'state.multiworld.worlds[{self.player}].options.glitch_logic.value > state.multiworld.worlds[{self.player}].options.glitch_logic.option_off')

            case SMORuleCondition.GLITCH_INTERMEDIATE:
                rules_list.append(
                    lambda state: state.multiworld.worlds[self.player].options.glitch_logic.value >
                                  state.multiworld.worlds[
                                      self.player].options.glitch_logic.option_easy)
                if is_active(self.options, condition):
                    access_rule += f'state.multiworld.worlds[{self.player}].options.glitch_logic.value > state.multiworld.worlds[{self.player}].options.glitch_logic.option_easy'
                    all_access_rules.add(f'state.multiworld.worlds[{self.player}].options.glitch_logic.value > state.multiworld.worlds[{self.player}].options.glitch_logic.option_easy')

            case SMORuleCondition.GLITCH_HARD:
                rules_list.append(
                    lambda state: state.multiworld.worlds[self.player].options.glitch_logic.value >
                                  state.multiworld.worlds[
                                      self.player].options.glitch_logic.option_intermediate)
                if is_active(self.options, condition):
                    access_rule += f'state.multiworld.worlds[{self.player}].options.glitch_logic.value > state.multiworld.worlds[{self.player}].options.glitch_logic.option_intermediate'
                    all_access_rules.add(f'state.multiworld.worlds[{self.player}].options.glitch_logic.value > state.multiworld.worlds[{self.player}].options.glitch_logic.option_intermediate')


        condition_index += 1
        if operation in parenthesis_operators and (not parenthesis_open or not is_active(self.options, condition)):
            operation = (SMORuleOperation.AND if operation == SMORuleOperation.PARENTHESIS_AND else
            SMORuleOperation.OR if operation == SMORuleOperation.PARENTHESIS_OR else
            SMORuleOperation.NONE)

        if condition_index == num_conditions - 2 and not is_active(self.options, conditions[-1][0]) or not is_active(self.options, condition):
            # Last condition isn't active or current condition isn't active
            # Prevent trailing 'and' or 'or' in access_rule
            operation = SMORuleOperation.NONE if operation not in parenthesis_operators else SMORuleOperation.PARENTHESIS_NONE

        access_rule += "" if operation == SMORuleOperation.NONE else f" {
            "and" if operation == SMORuleOperation.AND else
            "or" if operation == SMORuleOperation.OR else
            ")" if operation == SMORuleOperation.PARENTHESIS_NONE else
            ") and" if operation == SMORuleOperation.PARENTHESIS_AND else
            ") or" if operation == SMORuleOperation.PARENTHESIS_OR else ""} "

    # parenthesis_rules : list[Callable] = []
    # for group in parenthesis_groups:
    #     for condition in group:
    #         if condition == group[0]:
    #             parenthesis_rules.append(rules_list[condition])
    #             continue
    #         if conditions[condition][-1] == SMORuleOperation.AND:
    #             parenthesis_rules[-1] = lambda state: parenthesis_rules[-1](state) and rules_list[condition](state)
    #         if conditions[condition][-1] == SMORuleOperation.OR:
    #             parenthesis_rules[-1] = lambda state: parenthesis_rules[-1](state) or rules_list[condition](state)
    #
    # other_rule = None
    # final_rules = []
    # for condition in range(len(conditions)):
    #     if condition == 0:
    #         final_rules.append(rules_list[condition])
    #         continue
    #     if condition in in_parenthesis:
    #         if condition not in starting_parenthesis:
    #             continue
    #         other_rule = parenthesis_rules[starting_parenthesis.index(condition)]
    #     else:
    #         other_rule = rules_list[condition]
    #
    #
    #     if conditions[condition - 1][2] in [SMORuleOperation.AND, SMORuleOperation.PARENTHESIS_AND]:
    #         final_rules.append(lambda state: final_rules[-1](state) and other_rule(state))
    #     if conditions[condition - 1][2] in [SMORuleOperation.OR, SMORuleOperation.PARENTHESIS_OR]:
    #         final_rules.append(lambda state: final_rules[-1](state) or other_rule(state))
    #
    # for i in rules_list:
    #     all_statics.append(i)
    #
    # for i in parenthesis_rules:
    #     all_statics.append(i)

    if access_rule == 'lambda state: ':
        # No rule generated return default access rule
        return staticmethod(lambda state: True)
    else:
        all_access_rules.add(access_rule)
        return eval(access_rule)
        # all_statics.append(final_rules[-1])
        # return final_rules[-1]


class SMOProgressionSkip:

    def __init__(self):
        self.name = ""
        # Lists of possible item combinations to perform the trick
        self.conditions : list[list[str]] = []
        self.required_options : list[SMORuleCondition] = []


    def make_rule(self):
        rule_conditions : list[tuple[SMORuleCondition, Any, SMORuleOperation]] = []
        for condition in self.conditions:
            rule_conditions.append((SMORuleCondition.ITEM, condition, SMORuleOperation.OR))
        rule_conditions[-1][2] = SMORuleOperation.NONE
        return create_access_rule(self, rule_conditions)

def set_rules(self, options : SMOOptions) -> None:
    """ Sets the placement rules for Super Mario Odyssey.
        Args:
            self: SMOWorld object for this player's world.
            options: The options from this player's yaml.
    """
    # Regional Coin Items
    regional_totals = {}
    for item, option, kingdom, cost in shop_location_costs:
        if kingdom not in regional_totals:
            regional_totals[kingdom] = 0
        if self.options.goal.value >= option or self.options.entrance_randomization > 0:
            regional_totals[kingdom] += cost
            set_rule(self.get_location(item), create_access_rule(self,[
                (SMORuleCondition.REGIONAL_COINS, [kingdom, regional_totals[kingdom]], SMORuleOperation.NONE)
            ]))

    # Outfit Moons
    if self.options.goal > self.options.goal.option_lake:
        set_rule(self.get_location(SMOLocationData.mechanic_cap), create_access_rule(self, [
            (SMORuleCondition.ITEM, SMOItemData.mechanic_cap, SMORuleOperation.OR),
            (SMORuleCondition.REGION, SMORegion.odyssey_broken_down, SMORuleOperation.NONE)
        ]))
        set_rule(self.get_location(SMOLocationData.mechanic_outfit), create_access_rule(self, [
            (SMORuleCondition.ITEM, SMOItemData.mechanic_outfit, SMORuleOperation.OR),
            (SMORuleCondition.REGION, SMORegion.odyssey_broken_down, SMORuleOperation.NONE)
        ]))
        set_rule(self.get_location(SMOLocationData.fashionable_cap), create_access_rule(self, [
            (SMORuleCondition.ITEM, SMOItemData.fashionable_cap, SMORuleOperation.OR),
            (SMORuleCondition.REGION, SMORegion.odyssey_broken_down, SMORuleOperation.NONE)
        ]))
        set_rule(self.get_location(SMOLocationData.fashionable_outfit), create_access_rule(self, [
            (SMORuleCondition.ITEM, SMOItemData.fashionable_outfit, SMORuleOperation.OR),
            (SMORuleCondition.REGION, SMORegion.odyssey_broken_down, SMORuleOperation.NONE)
        ]))

    if self.options.goal > self.options.goal.option_metro:
        set_rule(self.get_location(SMOLocationData.pirate_hat), create_access_rule(self, [
            (SMORuleCondition.ITEM, SMOItemData.pirate_hat, SMORuleOperation.OR),
            (SMORuleCondition.REGION, SMORegion.odyssey_sails_branch_2, SMORuleOperation.NONE)
        ]))
        set_rule(self.get_location(SMOLocationData.pirate_outfit), create_access_rule(self, [
            (SMORuleCondition.ITEM, SMOItemData.pirate_outfit, SMORuleOperation.OR),
            (SMORuleCondition.REGION, SMORegion.odyssey_sails_branch_2, SMORuleOperation.NONE)
        ]))
        # set_rule(self.multiworld.get_location("Clown Hat", self.player),
        #          lambda state: state.has("Clown Hat", self.player) or
        #         (count_moons(self, state, "Snow", self.player) and
        #         count_moons(self, state, "", self.player)))
        # set_rule(self.multiworld.get_location("Clown Suit", self.player),
        #          lambda state: state.has("Clown Suit", self.player) or
        #         (count_moons(self, state, "", self.player) and
        #         count_moons(self, state, "", self.player)))
        # set_rule(self.multiworld.get_location("", self.player),
        #          lambda state: state.has("", self.player) or
        #         (count_moons(self, state, "", self.player) and
        #         count_moons(self, state, "", self.player)))


    if self.options.goal > self.options.goal.option_moon:
        set_rule(self.get_location(SMOLocationData.caveman_cave_fan),
            create_access_rule(self, [
                (SMORuleCondition.ITEM, [SMOItemData.caveman_headwear, SMOItemData.caveman_outfit], SMORuleOperation.NONE)
            ]))
        set_rule(self.get_location(SMOLocationData.that_trendy_pirate_look),
                 create_access_rule(self, [
                     (SMORuleCondition.ITEM, [SMOItemData.pirate_hat, SMOItemData.pirate_outfit],
                      SMORuleOperation.NONE)
                 ]))
        set_rule(self.get_location(SMOLocationData.space_is_in_right_now),
                 create_access_rule(self, [
                     (SMORuleCondition.ITEM, [SMOItemData.space_suit, SMOItemData.space_helmet],
                      SMORuleOperation.NONE)
                 ]))

        set_rule(self.get_location(SMOLocationData.that_old_west_style),
                 create_access_rule(self, [
                     (SMORuleCondition.ITEM, [SMOItemData.cowboy_hat, SMOItemData.cowboy_outfit],
                      SMORuleOperation.NONE)
                 ]))
        set_rule(self.get_location(SMOLocationData.mechanic_repairs_complete),
                 create_access_rule(self, [
                     (SMORuleCondition.ITEM, [SMOItemData.mechanic_cap, SMOItemData.mechanic_outfit],
                      SMORuleOperation.NONE)
                 ]))
        set_rule(self.get_location(SMOLocationData.doctor_in_the_house),
                 create_access_rule(self, [
                     (SMORuleCondition.ITEM, [SMOItemData.doctor_headwear, SMOItemData.doctor_outfit],
                      SMORuleOperation.NONE)
                 ]))

        # set_rule(self.multiworld.get_location("Mushroom Kingdom - Totally Classic", self.player),
        #          lambda state: (state.has("Mario 64 Cap", self.player) and state.has("Mario 64 Suit", self.player)) or (
        #                      state.has("Metal Mario Cap", self.player) and state.has("Metal Mario Clothes", self.player)))
        # set_rule(self.multiworld.get_location("Mushroom Kingdom - Courtyard Chest Trap", self.player),
        #          lambda state: (state.has("Mario 64 Cap", self.player) and state.has("Mario 64 Suit", self.player)) or (
        #                      state.has("Metal Mario Cap", self.player) and state.has("Metal Mario Clothes", self.player)))
        set_rule(self.get_location(SMOLocationData.surprise_clown),
                 create_access_rule(self, [
                     (SMORuleCondition.ITEM, [SMOItemData.clown_hat, SMOItemData.clown_suit],
                      SMORuleOperation.NONE)
                 ]))

    # OBSELETE from new region access rules
    # set_rule(self.get_location(SMOLocationData.dancing_with_new_friends),
    #          create_access_rule(self, [
    #              (SMORuleCondition.ITEM, [SMOItemData.sombrero, SMOItemData.poncho],
    #               SMORuleOperation.OR),
    #              (SMORuleCondition.ITEM, SMOItemData.skeleton_suit, SMORuleOperation.NONE)
    #          ]))

    if self.options.goal > self.options.goal.option_lake:
        pass
        # set_rule(self.multiworld.get_location("Exploring for Treasure", self.player),
        #          lambda state: state.has("Explorer Hat", self.player) and state.has("Explorer Outfit", self.player))


    if self.options.goal > self.options.goal.option_metro:
        # set_rule(self.multiworld.get_location("Rewiring the Neighborhood", self.player),
        #          lambda state: state.has("Builder Helmet", self.player) and state.has("Builder Outfit", self.player))
        # set_rule(self.multiworld.get_location("A Relaxing Dance", self.player),
        #          lambda state: state.has("Resort Hat", self.player) and state.has("Resort Outfit", self.player))
        # set_rule(self.multiworld.get_location("Moon Shards in the Cold Room", self.player),
        #          lambda state: state.has("Snow Hood", self.player) and state.has("Snow Suit", self.player))
        # set_rule(self.multiworld.get_location("Slip Behind the Ice", self.player),
        #          lambda state: state.has("Snow Hood", self.player) and state.has("Snow Suit", self.player))


    # if self.options.goal > self.options.goal.option_metro:
    #     set_rule(self.multiworld.get_location("A Strong Simmer", self.player),
    #              lambda state: state.has("Chef Hat", self.player) and state.has("Chef Suit", self.player))
    #     set_rule(self.multiworld.get_location("An Extreme Simmer", self.player),
    #              lambda state: state.has("Chef Hat", self.player) and state.has("Chef Suit", self.player))
    #
    # if self.options.goal > self.options.goal.option_luncheon:
    #     set_rule(self.multiworld.get_location("Scene of Crossing the Poison Swamp", self.player),
    #              lambda state: state.has("Samurai Helmet", self.player) and state.has("Samurai Armor", self.player))
    #     set_rule(self.multiworld.get_location("Taking Notes: In the Folding Screen", self.player),
    #              lambda state: state.has("Samurai Helmet", self.player) and state.has("Samurai Armor", self.player))

    # Post Game Outfits
    if self.options.goal > self.options.goal.option_moon:
        for outfit in self.outfit_moon_counts.keys():
            if self.options.goal > self.options.goal.option_dark:
                if self.outfit_moon_counts[outfit] < self.moon_counts["dark"]:
                    set_rule(self.get_location(outfit), create_access_rule(self, [
                        (SMORuleCondition.TOTAL_MOONS, self.outfit_moon_counts[outfit], SMORuleOperation.OR),
                        (SMORuleCondition.ITEM, outfit, SMORuleOperation.NONE)
                    ]))
                else:
                    set_rule(self.get_location(outfit), create_access_rule(self, [
                        (SMORuleCondition.ITEM, outfit, SMORuleOperation.NONE)
                    ]))
            elif self.options.goal > self.options.goal.option_darker:
                if self.outfit_moon_counts[outfit] < self.moon_counts["darker"]:
                    set_rule(self.get_location(outfit), create_access_rule(self, [
                        (SMORuleCondition.TOTAL_MOONS, self.outfit_moon_counts[outfit], SMORuleOperation.OR),
                        (SMORuleCondition.ITEM, outfit, SMORuleOperation.NONE)
                    ]))
                else:
                    set_rule(self.get_location(outfit), create_access_rule(self, [
                        (SMORuleCondition.ITEM, outfit, SMORuleOperation.NONE)
                    ]))


    # Completion State
    if options.goal == "sand":
        self.multiworld.completion_condition[self.player] = lambda state: state.count(SMOItemData.sand_multi_moon, self.player) >= 2
    if options.goal == "lake":
        self.multiworld.completion_condition[self.player] = lambda state: state.has(SMOItemData.lake_multi_moon, self.player)
    if options.goal == "metro":
        self.multiworld.completion_condition[self.player] = lambda state: state.count(SMOItemData.metro_multi_moon, self.player) >= 2
    if options.goal == "luncheon":
        self.multiworld.completion_condition[self.player] = lambda state: state.count(SMOItemData.luncheon_multi_moon, self.player) >= 2
    if options.goal == "moon":
        self.multiworld.completion_condition[self.player] = create_access_rule(self, [(SMORuleCondition.ITEM, SMOItemData.beat_the_game, SMORuleOperation.NONE)])
        self.get_location(SMOLocationData.beat_the_game).place_locked_item(self.create_item(SMOItemData.beat_the_game))
    if options.goal == "dark":
        self.multiworld.completion_condition[self.player] = create_access_rule(self, [(SMORuleCondition.ITEM, SMOItemData.dark_side_multi_moon, SMORuleOperation.NONE)])
    if options.goal == "darker":
        self.multiworld.completion_condition[self.player] = create_access_rule(self, [(SMORuleCondition.ITEM, SMOItemData.darker_side_multi_moon, SMORuleOperation.NONE)])

    # Place Goal moon at location
    if options.goal == "sand":
        self.get_location(SMOLocationData.the_hole_in_the_desert).place_locked_item(
            self.create_item(SMOItemData.sand_multi_moon))
    if options.goal == "lake":
        self.get_location(SMOLocationData.broodals_over_the_lake).place_locked_item(
            self.create_item(SMOItemData.lake_multi_moon))
    if options.goal == "metro":
        self.get_location(SMOLocationData.a_traditional_festival).place_locked_item(
            self.create_item(SMOItemData.metro_multi_moon))
    if options.goal == "luncheon":
        self.get_location(SMOLocationData.cookatiel_showdown).place_locked_item(
            self.create_item(SMOItemData.luncheon_multi_moon))
    if options.goal == "dark":
        self.get_location(SMOLocationData.arrival_at_rabbit_ridge).place_locked_item(
            self.create_item(SMOItemData.dark_side_multi_moon))
    if options.goal == "darker":
        self.get_location(SMOLocationData.a_long_journeys_end).place_locked_item(
            self.create_item(SMOItemData.darker_side_multi_moon))


    if options.capture_sanity.value == options.capture_sanity.option_true:
    # Captures
    # Cascade Story

        set_rule(self.get_location(SMOItemData.broodes_chain_chomp),
                 create_access_rule(self, [
                     (SMORuleCondition.CAPTURE, SMOItemData.big_chain_chomp, SMORuleOperation.OR),
                     (SMORuleCondition.CAPTURE, SMOItemData.t_rex, SMORuleOperation.OR),
                     (SMORuleCondition.TRICK_EASY, SMORuleCondition.CAPTURE, SMORuleOperation.NONE),
                 ]))
        #set_rule(self.multiworld.get_location("Our First Power Moon", self.player),
        #         lambda state: state.has("Chain Chomp", self.player) or state.has(SMOItemData.t_rex, self.player))
        #set_rule(self.multiworld.get_location("Multi Moon Atop the Falls", self.player),
        #         lambda state: state.has("Broode's Chain Chomp", self.player))
        # Sand Story
        # TEST CAPTURELESS
        set_rule(self.get_location(SMOLocationData.knucklotecs_fist),
                 create_access_rule(self, [
                     (SMORuleCondition.CAPTURE, [SMOItemData.bullet_bill], SMORuleOperation.NONE),
                 ]))


        # Change when entrance rando implemented
        # set_rule(self.multiworld.get_location("Strange Neighborhood", self.player),
        #          lambda state: state.has("Mini Rocket", self.player))
        # set_rule(self.multiworld.get_location("Above a Strange Neighborhood", self.player),
        #          lambda state: state.has("Mini Rocket", self.player))
        set_rule(self.multiworld.get_location("Inverted Pyramid Model", self.player),
                 lambda state: state.can_reach(self.get_region(SMORegion.sand_kingdom_peace), self.player) and
                 state.can_reach(self.get_region(SMORegion.bullet_bill_maze), self.player) and
                 state.can_reach(self.get_region(SMORegion.moe_eye_invisible_maze), self.player) and
                 state.can_reach(self.get_region(SMORegion.underground_ruins), self.player) and
                 state.can_reach(self.get_region(SMORegion.ice_cave), self.player) and
                 state.can_reach(self.get_region(SMORegion.jaxi_ruins), self.player) and
                 state.can_reach(self.get_region(SMORegion.inverted_pyramid_lower_interior), self.player) and
                 state.can_reach(self.get_region(SMORegion.inverted_pyramid_upper_interior), self.player) and
                 state.can_reach(self.get_region(SMORegion.strange_neighborhood), self.player))

        if self.options.goal > self.options.goal.option_lake:
            # Wooded
            set_rule(self.multiworld.get_location(SMOLocationData.by_the_babbling_brook_in_the_deep_woods, self.player),
                     lambda state: state.has(SMOItemData.coin_coffer, self.player) or state.has(SMOItemData.t_rex, self.player))
            set_rule(self.multiworld.get_location(SMOLocationData.the_hard_rock_in_deep_woods, self.player),
                     lambda state: state.has(SMOItemData.coin_coffer, self.player) or state.has(SMOItemData.t_rex, self.player))
            set_rule(self.multiworld.get_location(SMOLocationData.a_treasure_made_of_coins, self.player),
                     lambda state: state.has(SMOItemData.coin_coffer, self.player))
            set_rule(self.multiworld.get_location(SMOLocationData.beneath_the_roots_of_a_moving_tree, self.player),
                     lambda state: state.has(SMOItemData.tree, self.player))
            set_rule(self.multiworld.get_location(SMOLocationData.love_in_the_forest_ruins, self.player),
                     lambda state: state.has(SMOItemData.goomba, self.player))
            set_rule(self.multiworld.get_location(SMOLocationData.elevator_blind_spot, self.player),
                     lambda state: state.has(SMOItemData.sherm, self.player))
            set_rule(self.multiworld.get_location(SMOLocationData.inside_the_rock_in_the_forest, self.player),
                     lambda state: state.has(SMOItemData.coin_coffer, self.player) or state.has(SMOItemData.sherm, self.player))
            set_rule(self.multiworld.get_location(SMOLocationData.stretching_your_legs, self.player),
                     lambda state: state.has(SMOItemData.uproot, self.player))
            # Add vine sub area uproot req if trick jump not possible
            # Change when entrance rando implemented
            # set_rule(self.multiworld.get_location("Wandering in the Fog", self.player),
            #          lambda state: state.has(SMOItemData.paragoomba, self.player) and state.has("Mini Rocket", self.player))
            set_rule(self.multiworld.get_location(SMOLocationData.wandering_in_the_fog, self.player),
                     lambda state: state.has(SMOItemData.paragoomba, self.player))
            # set_rule(self.multiworld.get_location("Nut Hidden in the Fog", self.player),
            #          lambda state: state.has("Mini Rocket", self.player))
            set_rule(self.multiworld.get_location("Steam Gardener Watering Can", self.player),
                     lambda state: state.has("Boulder", self.player) and
                     state.can_reach(self.get_region(SMORegion.deep_woods), self.player) and
                     state.can_reach(self.get_region(SMORegion.sherm_elevator), self.player)and
                     state.can_reach(self.get_region(SMORegion.wooded_flower_road), self.player))

            # Lake
            set_rule(self.multiworld.get_location("Lake Kingdom - End of the Hidden Passage", self.player),
                     lambda state: state.has("Zipper", self.player))
            set_rule(self.multiworld.get_location("Lake Kingdom - Lake Fishing", self.player),
                     lambda state: state.has("Lakitu", self.player))
            set_rule(self.multiworld.get_location("Lake Kingdom - I Met a Lake Cheep Cheep!", self.player),
                     lambda state: state.has("Cheep Cheep", self.player))
            set_rule(self.multiworld.get_location("A Successful Repair Job", self.player),
                     lambda state: state.has("Puzzle Part (Lake Kingdom)", self.player))
            # Change when entrance rando implemented
            set_rule(self.multiworld.get_location("Unzip the Chasm", self.player),
                     lambda state: state.has("Zipper", self.player))
            # set_rule(self.multiworld.get_location("Super-Secret Zipper", self.player),
            #          lambda state: state.has("Zipper", self.player))
            set_rule(self.multiworld.get_location("Underwater Dome", self.player),
                     lambda state: state.has("Zipper", self.player) and
                     state.can_reach(self.get_region(SMORegion.bouncy_flowers), self.player))


        if self.options.goal > self.options.goal.option_lake:
            # Cloud
            set_rule(self.multiworld.get_location("Picture Match: Basically a Goomba", self.player),
                     lambda state: state.has("Picture Match Part (Goomba)", self.player))

            # Lost
            set_rule(self.multiworld.get_location("Lost Kingdom - Soaring Over the Forgotten Isle!", self.player),
                     lambda state: state.has("Glydon", self.player))
            set_rule(self.multiworld.get_location("Lost Kingdom - Twist ‘n' Turn-Up Treasure", self.player),
                     lambda state: state.has("Tropical Wiggler", self.player))

            # Metro
            set_rule(self.multiworld.get_location("Metro Kingdom - Remotely Captured Car", self.player),
                     lambda state: state.has("RC Car", self.player))
            set_rule(self.multiworld.get_location("RC Car Pro!", self.player),
                     lambda state: state.has("RC Car", self.player))
            set_rule(self.multiworld.get_location("Rewiring the Neighborhood", self.player),
                     lambda state: state.has(SMOItemData.spark_pylon, self.player))
            set_rule(self.multiworld.get_location("Off the Beaten Wire", self.player),
                     lambda state: state.has(SMOItemData.spark_pylon, self.player))
            # Change when entrance rando implemented
            # set_rule(self.multiworld.get_location("Moon Shards Under Siege", self.player),
            #          lambda state: state.has("Taxi", self.player) and state.has(SMOItemData.sherm, self.player))
            # set_rule(self.multiworld.get_location("Sharpshooting Under Siege", self.player),
            #          lambda state: state.has("Taxi", self.player) and state.has(SMOItemData.sherm, self.player))
            set_rule(self.multiworld.get_location("Moon Shards Under Siege", self.player),
                     lambda state: state.has(SMOItemData.sherm, self.player))
            set_rule(self.multiworld.get_location("Sharpshooting Under Siege", self.player),
                     lambda state: state.has(SMOItemData.sherm, self.player))
            # set_rule(self.multiworld.get_location("Inside the Rotating Maze", self.player),
            #          lambda state: state.has("Manhole", self.player))
            # set_rule(self.multiworld.get_location("Outside the Rotating Maze", self.player),
            #          lambda state: state.has("Manhole", self.player))
            # set_rule(self.multiworld.get_location("Vaulting Up a High-Rise", self.player),
            #          lambda state: state.has("Mini Rocket", self.player))
            # set_rule(self.multiworld.get_location("Hanging from a High-Rise", self.player),
            #          lambda state: state.has("Mini Rocket", self.player))
            # set_rule(self.multiworld.get_location("Sewer Treasure", self.player),
            #          lambda state: state.has("Manhole", self.player))
            set_rule(self.multiworld.get_location("Pauline Statue", self.player),
                     lambda state: state.can_reach(self.get_region(SMORegion.sewers), self.player) and
                     state.can_reach(self.get_region(SMORegion.high_rise), self.player) and
                     state.can_reach(self.get_region(SMORegion.city_hall), self.player))

        if self.options.goal > self.options.goal.option_metro:
            # Seaside
            set_rule(self.multiworld.get_location("Seaside Kingdom - Love by the Seaside", self.player),
                     lambda state: state.has(SMOItemData.goomba, self.player))
            set_rule(self.multiworld.get_location("Fly Through the Narrow Valley", self.player),
                     lambda state: state.has("Gushen", self.player))
            set_rule(self.multiworld.get_location("Treasure Chest in the Narrow Valley", self.player),
                     lambda state: state.has("Gushen", self.player))
            set_rule(self.multiworld.get_location("Seaside Kingdom - Lighthouse Leaper", self.player),
                     lambda state: state.has("Glydon", self.player))
            set_rule(self.multiworld.get_location("Sand Jar", self.player),
                     lambda state: state.has("Gushen", self.player) and
                     state.can_reach(self.get_region(SMORegion.seaside_waterway), self.player) and
                     state.can_reach(self.get_region(SMORegion.sinking_island), self.player))
            # Change when entrance rando implemented
            # set_rule(self.multiworld.get_location("Wading in the Cloud Sea", self.player),
            #          lambda state: state.has("Mini Rocket", self.player))
            # set_rule(self.multiworld.get_location("Sunken Treasure in the Cloud Sea", self.player),
            #          lambda state: state.has("Mini Rocket", self.player))

            # Snow
            set_rule(self.multiworld.get_location("Ice-Dodging Goomba Stack", self.player),
                     lambda state: state.has(SMOItemData.goomba, self.player))
            set_rule(self.multiworld.get_location("Snow Kingdom - Fishing in the Glacier!", self.player),
                     lambda state: state.has("Lakitu", self.player))
            set_rule(self.multiworld.get_location("Snowline Circuit Class S", self.player),
                     lambda state: state.has("Shiverian Racer", self.player))
            set_rule(self.multiworld.get_location("Shiverian Nesting Dolls", self.player),
                     lambda state: state.has("Ty-foo", self.player) and
                     state.can_reach(self.get_region(SMORegion.shiveria), self.player) and
                     state.can_reach(self.get_region(SMORegion.snowline_circuit), self.player))
            # Change when entrance rando implemented
            set_rule(self.multiworld.get_location("Blowing and Sliding", self.player),
                     lambda state: state.has("Ty-foo", self.player))

            # Luncheon
            set_rule(self.multiworld.get_location("Luncheon Kingdom - Love Above the Lava", self.player),
                     lambda state: state.has(SMOItemData.goomba, self.player))
            set_rule(self.multiworld.get_location("A Strong Simmer", self.player),
                     lambda state: state.has("Lava Bubble", self.player))
            set_rule(self.multiworld.get_location("An Extreme Simmer", self.player),
                     lambda state: state.has("Lava Bubble", self.player))
            set_rule(self.multiworld.get_location("Excavate ‘n' Search the Cheese Rocks", self.player),
                     lambda state: state.has("Hammer Bro", self.player))
            set_rule(self.multiworld.get_location("Climb the Cheese Rocks", self.player),
                     lambda state: state.has("Hammer Bro", self.player))
            set_rule(self.multiworld.get_location("Luncheon Kingdom - Light the Lantern on the Small Island", self.player),
                     lambda state: state.has("Fire Bro", self.player) or state.has("Lava Bubble", self.player))
            set_rule(self.multiworld.get_location("Luncheon Kingdom - All the Cracks Are Fixed", self.player),
                     lambda state: state.has("Lava Bubble", self.player))
            set_rule(self.multiworld.get_location("Luncheon Kingdom - Taking Notes: Swimming in Magma", self.player),
                     lambda state: state.has("Lava Bubble", self.player))
            set_rule(self.multiworld.get_location("Magma Narrow Path", self.player),
                     lambda state: state.has("Lava Bubble", self.player))
            set_rule(self.multiworld.get_location("Crossing to the Magma", self.player),
                     lambda state: state.has("Lava Bubble", self.player))
            set_rule(self.multiworld.get_location("Luncheon Kingdom - Treasure Beneath the Cheese Rocks", self.player),
                     lambda state: state.has("Hammer Bro", self.player))
            set_rule(self.multiworld.get_location("Alcove Behind the Pillars of Magma", self.player),
                     lambda state: state.has("Lava Bubble", self.player))
            set_rule(self.multiworld.get_location("Luncheon Kingdom - Beneath the Rolling Vegetables", self.player),
                     lambda state: state.has("Lava Bubble", self.player))
            set_rule(self.multiworld.get_location("Luncheon Kingdom - Golden Turnip Recipe 3", self.player),
                     lambda state: state.has("Hammer Bro", self.player))
            # add can_reach for required sub areas
            set_rule(self.multiworld.get_location("Souvenir Forks", self.player),
                     lambda state: state.has("Hammer Bro", self.player) and state.has("Lava Bubble", self.player))
            set_rule(self.multiworld.get_location("Vegetable Plate", self.player),
                     lambda state: state.has("Hammer Bro", self.player) and state.has("Lava Bubble", self.player))
            # Change when entrance rando implemented
            set_rule(self.multiworld.get_location("Fork Flickin' to the Summit", self.player),
                     lambda state: state.has("Volbonan", self.player))
            set_rule(self.multiworld.get_location("Fork Flickin' Detour", self.player),
                     lambda state: state.has("Volbonan", self.player))

        if self.options.goal > self.options.goal.option_luncheon:
            # Bowser
            set_rule(self.multiworld.get_location("Bowser Kingdom - Stack up above the wall", self.player),
                     lambda state: state.has(SMOItemData.goomba, self.player))
            set_rule(self.multiworld.get_location("Bowser Kingdom - Poking Your Nose in the Plaster Wall", self.player),
                     lambda state: state.has("Pokio", self.player))
            set_rule(self.multiworld.get_location("Bowser Kingdom - Poking the Turret Wall", self.player),
                     lambda state: state.has("Pokio", self.player))
            set_rule(self.multiworld.get_location("Bowser Kingdom - Jizo All in a Row", self.player),
                     lambda state: state.has("Jizo", self.player))
            set_rule(self.multiworld.get_location("Bowser Kingdom - Underground Jizo", self.player),
                     lambda state: state.has("Jizo", self.player))
            set_rule(self.multiworld.get_location("Bowser Kingdom - Fishing(?) in Bowser's Castle", self.player),
                     lambda state: state.has("Lakitu", self.player))
            set_rule(self.multiworld.get_location("Jizo's Big Adventure", self.player),
                     lambda state: state.has("Jizo", self.player))
            set_rule(self.multiworld.get_location("Jizo and the Hidden Room", self.player),
                     lambda state: state.has("Jizo", self.player))
            set_rule(self.multiworld.get_location("Bowser Kingdom - Behind the Big Wall", self.player),
                     lambda state: state.has(SMOItemData.spark_pylon, self.player))
            set_rule(self.multiworld.get_location("Bowser Kingdom - Taking notes: Between spinies", self.player),
                     lambda state: state.has(SMOItemData.spark_pylon, self.player))

            # Moon
            #if self.options.goal > self.options.goal.option_moon:
            set_rule(self.multiworld.get_location("Under the Bowser Statue", self.player),
                    lambda state: state.has("Bowser statue", self.player))
            set_rule(self.multiworld.get_location("In a Hole in the Magma", self.player),
                     lambda state: state.has("Parabones", self.player))
            set_rule(self.multiworld.get_location("Around the Barrier Wall", self.player),
                     lambda state: state.has("Banzai Bill", self.player))
            set_rule(self.multiworld.get_location("Fly to the Treasure Chest and Back", self.player),
                 lambda state: state.has("Banzai Bill", self.player))

    # New Rules
    set_rule(self.get_location(SMOLocationData.searching_the_frog_pond), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.secrets_of_the_frog_pond), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.skimming_the_poison_tide), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.slipping_through_the_poison_tide), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.push_block_peril), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.spark_pylon], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.hidden_among_the_push_blocks), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.spark_pylon], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.nice_shot_with_the_chain_chomp), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.chain_chomp], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.very_nice_shot_with_the_chain_chomp), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.chain_chomp], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.dinosaur_nest_big_cleanup), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.t_rex], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.dinosaur_nest_running_wild), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.t_rex], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.the_invisible_maze), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.moe_eye], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.skull_sign_in_the_transparent_maze), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.moe_eye], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.the_bullet_bill_maze_break_through), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.bullet_bill], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.the_bullet_bill_maze_side_path), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.bullet_bill], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))

    set_rule(self.get_location(SMOLocationData.underground_treasure_chest), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.bullet_bill], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.goomba_tower_assembly), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.goomba], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.the_hole_in_the_desert), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.bullet_bill, SMOItemData.knucklotecs_fist], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.where_the_transparent_platforms_end), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.moe_eye], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_HARD, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.jump_onto_the_transparent_lift), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.moe_eye], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.through_the_freezing_waterway), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.gushen], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.freezing_waterway_hidden_room), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.gushen], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.a_successful_repair_job), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.puzzle_part_lake_kingdom], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.unzip_the_chasm), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.zipper], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.super_secret_zipper), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.zipper], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.waves_of_poison_hoppin_over), create_access_rule(self, [
    (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.waves_of_poison_hop_to_it), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.frog], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_INTERMEDIATE, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    # set_rule(self.get_location(SMOLocationData.flower_road_run), create_access_rule(self, [
    #     (SMORuleCondition.CAPTURE, [SMOItemData.goomba], SMORuleOperation.NONE)
    # ]))
    # set_rule(self.get_location(SMOLocationData.flower_road_reach), create_access_rule(self, [
    #     (SMORuleCondition.CAPTURE, [SMOItemData.goomba], SMORuleOperation.NONE)
    # ]))
    set_rule(self.get_location(SMOLocationData.elevator_escalation), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.sherm], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.elevator_blind_spot), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.sherm], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.wandering_in_the_fog), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.nut_hidden_in_the_fog), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.paragoomba], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.walking_on_clouds), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.uproot], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.above_the_clouds), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.uproot], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.defend_the_secret_flower_field), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.uproot], SMORuleOperation.NONE)
    ]))
    # set_rule(self.get_location(SMOLocationData.invisible_road_danger), create_access_rule(self, [
    #     (SMORuleCondition.CAPTURE, [SMOItemData.poison_piranha_plant], SMORuleOperation.NONE)
    # ]))
    # set_rule(self.get_location(SMOLocationData.invisible_road_hidden_room), create_access_rule(self, [
    #     (SMORuleCondition.CAPTURE, [SMOItemData.poison_piranha_plant], SMORuleOperation.NONE)
    # ]))
    # set_rule(self.get_location(SMOLocationData.down_and_back_breakdown_road), create_access_rule(self, [
    #     (SMORuleCondition.CAPTURE, [SMOItemData.banzai_bill], SMORuleOperation.NONE)
    # ]))
    set_rule(self.get_location(SMOLocationData.below_breakdown_road), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.banzai_bill], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.picture_match_basically_a_goomba), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.picture_match_part_goomba], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.picture_match_a_stellar_goomba), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.picture_match_part_goomba], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.stretch_and_traverse_the_jungle), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.tropical_wiggler], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.aglow_in_the_jungle), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.tropical_wiggler], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    # set_rule(self.get_location(SMOLocationData.chasing_klepto), create_access_rule(self, [
    #     (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE)
    # ]))
    # TEST CAPTURELESS
    set_rule(self.get_location(SMOLocationData.extremely_hot_bath), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.rc_car_pro), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.rc_car], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.rewiring_the_neighborhood), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.spark_pylon], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.off_the_beaten_wire), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.spark_pylon], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.moon_shards_under_siege), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.sherm], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.GLITCH_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.sharpshooting_under_siege), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.sherm], SMORuleOperation.NONE)
    ]))
    # set_rule(self.get_location(SMOLocationData.bullet_billding), create_access_rule(self, [
    #     (SMORuleCondition.CAPTURE, [SMOItemData.bullet_bill], SMORuleOperation.NONE)
    # ]))
    set_rule(self.get_location(SMOLocationData.one_mans_trash), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.bullet_bill], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.swinging_scaffolding_jump), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.hammer_bro], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.swinging_scaffolding_break), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.hammer_bro], SMORuleOperation.NONE)
    ]))

    if self.options.goal.value > self.options.goal.option_dark:
        set_rule(self.get_location(SMOLocationData.powering_up_the_power_plant), create_access_rule(self, [
            (SMORuleCondition.CAPTURE, [SMOItemData.puzzle_part_metro_kingdom], SMORuleOperation.NONE)
        ]))
    set_rule(self.get_location(SMOLocationData.looking_back_in_the_dark_waterway), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.cheep_cheep], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.fly_through_the_narrow_valley), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.gushen], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.treasure_chest_in_the_narrow_valley), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.gushen], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.hurry_and_stretch), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.uproot], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.stretch_on_the_side_path), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.uproot], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.aim_poke ), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.poke_roll ), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE)
    ]))
    # set_rule(self.get_location(SMOLocationData.entrance_to_shiveria), create_access_rule(self, [
    #     (SMORuleCondition.CAPTURE, [SMOItemData.goomba, SMOItemData.ty_foo], SMORuleOperation.NONE)
    # ]))
    # set_rule(self.get_location(SMOLocationData.shining_in_the_snow_in_town), create_access_rule(self, [
    #     (SMORuleCondition.CAPTURE, [SMOItemData.goomba, SMOItemData.ty_foo], SMORuleOperation.NONE)
    # ]))
    # set_rule(self.get_location(SMOLocationData.the_shiverian_treasure_chest), create_access_rule(self, [
    #     (SMORuleCondition.CAPTURE, [SMOItemData.goomba, SMOItemData.ty_foo], SMORuleOperation.NONE)
    # ]))
    set_rule(self.get_location(SMOLocationData.found_with_snow_kingdom_art), create_access_rule(self, [
        (SMORuleCondition.REGION, SMORegion.shiveria_peace, SMORuleOperation.NONE)
    ]))
    # set_rule(self.get_location(SMOLocationData.the_icicle_barrier), create_access_rule(self, [
    #     (SMORuleCondition.CAPTURE, [SMOItemData.goomba, SMOItemData.ty_foo], SMORuleOperation.NONE)
    # ]))
    set_rule(self.get_location(SMOLocationData.ice_dodging_goomba_stack), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.goomba], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.GLITCH_HARD, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    # set_rule(self.get_location(SMOLocationData.the_ice_wall_barrier), create_access_rule(self, [
    #     (SMORuleCondition.CAPTURE, [SMOItemData.goomba, SMOItemData.ty_foo], SMORuleOperation.NONE)
    # ]))
    # set_rule(self.get_location(SMOLocationData.treasure_in_the_ice_wall), create_access_rule(self, [
    #     (SMORuleCondition.CAPTURE, [SMOItemData.goomba, SMOItemData.ty_foo], SMORuleOperation.NONE)
    # ]))
    set_rule(self.get_location(SMOLocationData.the_gusty_barrier), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.ty_foo], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.atop_a_blustery_arch), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.ty_foo], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    # set_rule(self.get_location(SMOLocationData.the_snowy_mountain_barrier), create_access_rule(self, [
    #     (SMORuleCondition.CAPTURE, [SMOItemData.goomba, SMOItemData.ty_foo], SMORuleOperation.NONE)
    # ]))
    # set_rule(self.get_location(SMOLocationData.behind_the_snowy_mountain), create_access_rule(self, [
    #     (SMORuleCondition.CAPTURE, [SMOItemData.goomba, SMOItemData.ty_foo], SMORuleOperation.NONE)
    # ]))
    set_rule(self.get_location(SMOLocationData.the_bound_bowl_grand_prix), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.shiverian_racer], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.snowline_circuit_class_s), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.shiverian_racer], SMORuleOperation.AND),
        (SMORuleCondition.REGION, SMORegion.snow_kingdom_peace, SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.stacked_up_ice_climb), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.goomba], SMORuleOperation.AND),
        (SMORuleCondition.REGION, SMORegion.snow_kingdom_moon_rock, SMORuleOperation.AND),
        (SMORuleCondition.REGION, SMORegion.shiveria_peace, SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.icy_jump_challenge), create_access_rule(self, [
        (SMORuleCondition.REGION, SMORegion.snow_kingdom_moon_rock, SMORuleOperation.AND),
        (SMORuleCondition.REGION, SMORegion.shiveria_peace, SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.a_strong_simmer), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.an_extreme_simmer), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.fork_flickin_to_the_summit), create_access_rule(self, [
    (SMORuleCondition.CAPTURE, [SMOItemData.volbonan], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.fork_flickin_detour), create_access_rule(self, [
    (SMORuleCondition.CAPTURE, [SMOItemData.volbonan], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.excavate_n_search_the_cheese_rocks), create_access_rule(self, [
    (SMORuleCondition.CAPTURE, [SMOItemData.hammer_bro], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.climb_the_cheese_rocks), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.hammer_bro], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    # TEST CAPTURELESS
    set_rule(self.get_location(SMOLocationData.magma_narrow_path), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.crossing_to_the_magma), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE)
    ]))
    # TEST CAPTURELESS
    set_rule(self.get_location(SMOLocationData.stepping_over_the_gears_and_lanterns_on_the_gear_steps),
             create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.fire_bro], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.TRICK_EASY, None, SMORuleOperation.PARENTHESIS_NONE)
             ]))
    set_rule(self.get_location(SMOLocationData.lanterns_on_the_gear_steps), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.fire_bro], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.treasure_of_the_lava_islands), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.flying_over_the_lava_islands), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.charging_through_an_army), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.chargin_chuck], SMORuleOperation.NONE)
    ]))
    # set_rule(self.get_location(SMOLocationData.the_mummys_curse), create_access_rule(self, [
    # (SMORuleCondition.CAPTURE, [SMOItemData.chargin_chuck], SMORuleOperation.NONE)
    # ]))
    # TEST CAPTURELESS
    set_rule(self.get_location(SMOLocationData.jizos_big_adventure), create_access_rule(self, [
    (SMORuleCondition.CAPTURE, [SMOItemData.jizo], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.jizo_and_the_hidden_room), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.jizo], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.searching_hexagon_tower), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.parabones], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.center_of_hexagon_tower), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.parabones], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.climb_the_wooden_tower), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.poke_the_wooden_tower), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.pokio], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.under_the_bowser_statue), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.bowser_statue], SMORuleOperation.PARENTHESIS_OR),
        (SMORuleCondition.GLITCH_INTERMEDIATE, None, SMORuleOperation.PARENTHESIS_NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.in_a_hole_in_the_magma), create_access_rule(self, [
        (SMORuleCondition.CAPTURE,
         [SMOItemData.parabones], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.around_the_barrier_wall), create_access_rule(self, [
        (SMORuleCondition.CAPTURE,
         [SMOItemData.sherm, SMOItemData.spark_pylon, SMOItemData.hammer_bro,
          SMOItemData.tropical_wiggler, SMOItemData.banzai_bill, SMOItemData.bullet_bill], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.on_top_of_the_cannon), create_access_rule(self, [
        (SMORuleCondition.CAPTURE,
         [SMOItemData.sherm, SMOItemData.spark_pylon, SMOItemData.hammer_bro,
          SMOItemData.tropical_wiggler, SMOItemData.banzai_bill, SMOItemData.bullet_bill], SMORuleOperation.NONE)
    ]))
    set_rule(self.get_location(SMOLocationData.fly_to_the_treasure_chest_and_back), create_access_rule(self, [
        (SMORuleCondition.CAPTURE,
         [SMOItemData.bowser_statue, SMOItemData.sherm, SMOItemData.spark_pylon, SMOItemData.hammer_bro,
          SMOItemData.tropical_wiggler, SMOItemData.banzai_bill, SMOItemData.bullet_bill], SMORuleOperation.NONE)
    ]))


    # Inverted Mural Unique Sub Area access rule
    set_rule(self.get_location(SMOLocationData.secret_of_the_inverted_mural), create_access_rule(self, [
        (SMORuleCondition.ENTRANCE,
         [SMORegion.sand_kingdom, f"{SMOEntranceData.inverted_pyramid_lower_interior} Unique Exit",
          SMOEntranceDataType.EXIT], SMORuleOperation.OR),
        (SMORuleCondition.ENTRANCE,
         [SMORegion.sand_kingdom, f"{SMOEntranceData.inverted_pyramid_upper_interior} Unique Exit",
          SMOEntranceDataType.EXIT], SMORuleOperation.NONE)
    ]))

    set_rule(self.get_location(SMOLocationData.up_in_the_rafters), create_access_rule(self, [
        (SMORuleCondition.REGION, SMORegion.odyssey_complete, SMORuleOperation.NONE)
    ]))

    set_rule(self.get_location(SMOLocationData.beat_the_game), create_access_rule(self, [
        (SMORuleCondition.CAPTURE, [SMOItemData.bowser], SMORuleOperation.AND),
        (SMORuleCondition.REGION, SMORegion.odyssey_complete, SMORuleOperation.NONE),
    ]))

    if len(self.get_region(SMORegion.mushroom_picture_match).locations) > 0:
        set_rule(self.get_location(SMOLocationData.picture_match_basically_mario), create_access_rule(self, [
            (SMORuleCondition.CAPTURE, [SMOItemData.picture_match_part_mario], SMORuleOperation.NONE)
        ]))
        set_rule(self.get_location(SMOLocationData.picture_match_a_stellar_mario), create_access_rule(self, [
            (SMORuleCondition.CAPTURE, [SMOItemData.picture_match_part_mario], SMORuleOperation.NONE)
        ]))


    for location in self.get_locations():
        if location.name in rule_data:
            if location.access_rule != Location.access_rule:
                print(location.name)
            else:
                if len(rule_data[location.name]) > 0:
                    set_rule(location, create_access_rule(self, rule_data[location.name]))

        if location.name in regional_coin_table:
            for stage in regional_coin_groups:
                for regional_group_id in regional_coin_groups[stage]:
                    if location.address in regional_coin_groups[stage][regional_group_id]:
                        for regional_group_name in regional_coin_groups_table:
                            if regional_coin_groups_table[regional_group_name] == regional_group_id:
                                if regional_group_name in rule_data:
                                    set_rule(location, create_access_rule(self, rule_data[regional_group_name]))
                                else:
                                    break

    # for i in all_access_rules:
    #
    #     print(i)

    # for debugging purposes, you may want to visualize the layout of your world. Uncomment the following code to
# write a PlantUML diagram to the file "my_world.puml" that can help you see whether your regions and locations
# are connected and placed as desired

    # from Utils import visualize_regions
    # visualize_regions(self.get_region("Menu"), "my_world.puml")