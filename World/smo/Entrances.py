from enum import IntEnum
from typing import Any
from BaseClasses import Entrance, EntranceType
from .Data.ItemData import SMOItemData
from.Rules import SMORuleCondition, SMORuleOperation, create_access_rule
from .Data.EntranceData import SMOEntrance
from .Data.RegionData import SMORegion


class SMORandomizationGroup(IntEnum):
        """
        Enumeration of Super Mario Odyssey Entrance Types
        """
        DOOR = 0
        PIPE = 1
        MOON_PIPE = 2
        HIT_BOX = 3
        PAINTING = 4
        ROCKET = 5
        TOP_HAT_ENTER = 6
        TOP_HAT_EXIT = 7
        TOP_HAT_SUB_AREA_ENTER = 8
        TOP_HAT_SUB_AREA_EXIT = 9

display_name_alias = {
    SMORegion.cap_kingdom_intro: SMOEntrance.cap_kingdom,
    "Moon Kingdom Peace": SMOEntrance.moon_kingdom,
    "Day Metro Kingdom": SMOEntrance.metro_kingdom,
    "Sand Kingdom Peace": SMOEntrance.sand_kingdom,
    "Luncheon Kingdom Post Broodals": SMOEntrance.luncheon_kingdom,
    "Sand Kingdom Moon Rock": SMOEntrance.sand_kingdom,
    "Luncheon Kingdom Meat": SMOEntrance.luncheon_kingdom,
    SMORegion.infiltrate_bowsers_castle: SMOEntrance.bowsers_kingdom,
    "Bowser Kingdom Moon Rock": SMOEntrance.bowsers_kingdom,
    "Lake Kingdom Moon Rock": SMOEntrance.lake_kingdom,
    "Wooded Kingdom Moon Rock": SMOEntrance.wooded_kingdom,
    "Metro Kingdom Moon Rock": SMOEntrance.metro_kingdom,
    "Snow Kingdom Peace": SMOEntrance.snow_kingdom,
    "Bowser Kingdom Peace": SMOEntrance.bowsers_kingdom,
    SMORegion.night_metro_kingdom: "CityWorldHomeStage",
    "Bowser Kingdom Smart Bombing": SMOEntrance.bowsers_kingdom,
    "Moon Kingdom Moon Rock": SMOEntrance.moon_kingdom,
    "Dark Side Peace": SMOEntrance.dark_side,
    "Cascade Kingdom Moon Rock": SMOEntrance.cascade_kingdom,
    "Wooded Kingdom Post Broodals": SMOEntrance.wooded_kingdom,
    "Cascade Kingdom Peace": SMOEntrance.cascade_kingdom,
    "Snow Kingdom Moon Rock": SMOEntrance.snow_kingdom,
    "Lost Kingdom Moon Rock": SMOEntrance.lost_kingdom,
    "Cap Kingdom Topper": SMOEntrance.cap_kingdom,
    "Luncheon Kingdom Moon Rock": SMOEntrance.luncheon_kingdom,
    "Cloud Kingdom Revisit": SMOEntrance.cloud_kingdom,
    "Cap Kingdom Moon Rock": SMOEntrance.cap_kingdom,
    "Wooded Kingdom Peace": SMOEntrance.wooded_kingdom,
    "Cloud Kingdom Moon Rock": SMOEntrance.cloud_kingdom,
    "Sand Kingdom Shop Employee Entrance": SMOEntrance.sand_kingdom_shop,
    "Bowser Kingdom Mecha Broodal": SMOEntrance.bowsers_kingdom,
    "Ruined Kingdom Moon Rock": SMOEntrance.ruined_kingdom,
    "Seaside Kingdom Moon Rock": SMOEntrance.seaside_kingdom,
    "Dark Side 4th Floor": "Special1WorldHomeStage",
    "Dark Side 3rd Floor": "Special1WorldHomeStage",
    "Dark Side 2nd Floor": "Special1WorldHomeStage",
}

display_name_to_internal_name = {
    SMOEntrance.cap_kingdom:"CapWorldHomeStage",
    SMOEntrance.top_hat_tower:"CapWorldTowerStage",
    SMOEntrance.poison_tides:"PoisonWaveExStage",
    SMOEntrance.push_blocks:"PushBlockExStage",
    SMOEntrance.frog_pond:"FrogSearchExStage",
    SMOEntrance.rolling_lane:"RollingExStage",
    SMOEntrance.cascade_kingdom:"WaterfallWorldHomeStage",
    SMOEntrance.t_rex_nest:"TrexPoppunExStage",
    SMOEntrance.chain_chomp_cave:"WanwanClashExStage",
    SMOEntrance.chasm_lifts:"Lift2DExStage",
    SMOEntrance.mysterious_clouds:"CapAppearExStage",
    SMOEntrance.gusty_bridges:"WindBlowExStage",
    SMOEntrance.sand_kingdom:"SandWorldHomeStage",
    SMOEntrance.sand_kingdom_shop:"SandWorldShopStage",
    SMOEntrance.sand_slots:"SandWorldSlotStage",
    SMOEntrance.sand_costume_bonus_dancing_room:"SandWorldCostumeStage",
    SMOEntrance.sand_sphynx_vault:"SandWorldSecretStage",
    SMOEntrance.sand_rumbling_floor_house:"SandWorldVibrationStage",
    SMOEntrance.inverted_pyramid_lower_interior:"SandWorldPyramid000Stage",
    SMOEntrance.inverted_pyramid_mural:"SandWorldHomeStage",
    SMOEntrance.inverted_pyramid_upper_interior:"SandWorldPyramid001Stage",
    SMOEntrance.top_of_the_inverted_pyramid: "SandWorldHomeStage",
    SMOEntrance.underground_ruins:"SandWorldUnderground000Stage",
    SMOEntrance.deepest_underground:"SandWorldUnderground001Stage",
    SMOEntrance.ice_cave:"SandWorldPressExStage",
    SMOEntrance.moe_eye_invisible_maze:"SandWorldMeganeExStage",
    SMOEntrance.bullet_bill_maze:"SandWorldKillerExStage",
    SMOEntrance.jaxi_ruins:"SandWorldSphinxExStage",
    SMOEntrance.strange_neighborhood:"SandWorldRotateExStage",
    SMOEntrance.moe_eye_invisible_floor:"MeganeLiftExStage",
    SMOEntrance.colossal_ruins:"RocketFlowerExStage",
    SMOEntrance.freezing_waterway:"WaterTubeExStage",
    SMOEntrance.lake_kingdom:"LakeWorldHomeStage",
    SMOEntrance.lake_kingdom_shop:"LakeWorldShopStage",
    SMOEntrance.arch_repair:"GotogotonExStage",
    SMOEntrance.zipper_chasm:"FastenerExStage",
    SMOEntrance.bouncy_flowers:"TrampolineWallCatchExStage",
    SMOEntrance.poison_swamp:"FrogPoisonExStage",
    SMOEntrance.wooded_kingdom:"ForestWorldHomeStage",
    SMOEntrance.sky_garden_tower:"ForestWorldTowerStage",
    SMOEntrance.secret_flower_field:"ForestWorldBossStage",
    SMOEntrance.deep_woods:"ForestWorldWoodsStage",
    SMOEntrance.deep_woods_costume_bonus_treasure_chest:"ForestWorldWoodsCostumeStage",
    SMOEntrance.deep_woods_treasure_trap:"ForestWorldWoodsTreasureStage",
    SMOEntrance.spinning_platforms_treasure_vault:"ForestWorldBonusStage", # Unsure
    SMOEntrance.flooding_pipeway:"ForestWorldWaterExStage",
    SMOEntrance.fog_wandering:"FogMountainExStage",
    SMOEntrance.wooded_flower_road:"RailCollisionExStage",
    SMOEntrance.sherm_elevator:"ShootingElevatorExStage",
    SMOEntrance.walking_on_clouds:"ForestWorldCloudBonusExStage",
    SMOEntrance.invisible_road:"PackunPoisonExStage",
    SMOEntrance.sheep_herding:"AnimalChaseExStage",
    SMOEntrance.breakdown_road:"KillerRoadExStage",
    SMOEntrance.cloud_kingdom:"CloudWorldHomeStage",
    SMOEntrance.cloud_picture_match:"FukuwaraiKuriboStage",
    SMOEntrance.king_of_the_cube:"Cube2DExStage",
    SMOEntrance.lost_kingdom:"ClashWorldHomeStage",
    SMOEntrance.lost_kingdom_shop:"ClashWorldShopStage",
    SMOEntrance.tropical_wiggler_swamp:"ImomuPoisonExStage",
    SMOEntrance.klepto_lava_bath:"JangoExStage",
    SMOEntrance.metro_kingdom:"CityWorldHomeStage",
    SMOEntrance.metro_kingdom_shop:"CityWorldShop01Stage",
    SMOEntrance.metro_kingdom_shop_regional:"CityWorldShop01Stage", # Might Change
    SMOEntrance.metro_slots:"CityWorldSandSlotStage",
    SMOEntrance.city_hall:"CityWorldMainTowerStage",
    SMOEntrance.sewers:"CityWorldFactoryStage",
    SMOEntrance.rc_race:"RadioControlExStage",
    SMOEntrance.private_room:"Note2D3DRoomExStage",
    SMOEntrance.projection_room:"Theater2DExStage",
    SMOEntrance.crowded_street:"CityPeopleRoadStage",
    SMOEntrance.builder_outfit:"ElectricWireExStage",
    SMOEntrance.metro_siege:"ShootingCityExStage",
    SMOEntrance.rotating_maze:"CapRotatePackunExStage",
    SMOEntrance.high_rise:"PoleGrabCeilExStage",
    SMOEntrance.bullet_building:"PoleKillerExStage",
    SMOEntrance.t_rex_escape:"TrexBikeExStage",
    SMOEntrance.pitch_black_island:"DonsukeExStage",
    SMOEntrance.swinging_scaffolding:"SwingSteelExStage",
    SMOEntrance.vanishing_road:"BikeSteelExStage",
    SMOEntrance.snow_kingdom:"SnowWorldHomeStage",
    SMOEntrance.snow_kingdom_shop:"SnowWorldShopStage",
    SMOEntrance.freezing_room:"SnowWorldCostumeStage",
    SMOEntrance.ice_trace_walking:"IceWalkerExStage",
    SMOEntrance.shiveria:"SnowWorldTownStage",
    SMOEntrance.snowline_circuit_lobby:"SnowWorldLobby000Stage",
    "Snowline Circuit: Class S Lobby":"SnowWorldLobby001Stage",
    "Snowline Circuit: Class A":"SnowWorldRace000Stage",
    "Snowline Circuit: Class S":"SnowWorldRace001Stage",
    "Snowline Circuit: Tutorial":"SnowWorldRaceTutorialStage",
    SMOEntrance.iceburn_circuit_class_a_lobby:"SnowWorldLobbyExStage",
    "Iceburn Circuit: Class A":"SnowWorldRaceExStage",
    "Iceburn Circuit: Class S":"SnowWorldRaceHardExStage",
    SMOEntrance.rocket_flower_dash:"IceWaterDashExStage",
    SMOEntrance.freezing_water:"IceWaterBlockExStage",
    SMOEntrance.ty_foo_sliding_puzzle:"ByugoPuzzleExStage",
    SMOEntrance.above_the_clouds:"SnowWorldCloudBonusExStage",
    SMOEntrance.snow_flower_road:"KillerRailCollisionExStage",
    SMOEntrance.seaside_kingdom:"SeaWorldHomeStage",
    SMOEntrance.seaside_costume_bonus_dancing_room:"SeaWorldCostumeStage",
    SMOEntrance.seaside_sphynx_treasure_vault:"SeaWorldSecretStage",
    SMOEntrance.seaside_rumbling_floor_cave:"SeaWorldVibrationStage",
    SMOEntrance.underwater_tunnel:"SeaWorldUtsuboCaveStage",
    SMOEntrance.sandy_bottom:"SeaWorldSneakingManStage",
    SMOEntrance.wading_in_the_cloud_sea:"CloudExStage",
    SMOEntrance.narrow_valley:"WaterValleyExStage",
    SMOEntrance.sinking_island:"SenobiTowerExStage",
    SMOEntrance.pokio_bomb_aiming:"ReflectBombExStage",
    SMOEntrance.spinning_maze:"TogezoRotateExStage",
    SMOEntrance.luncheon_kingdom:"LavaWorldHomeStage",
    SMOEntrance.luncheon_kingdom_shop:"LavaWorldShopStage",
    SMOEntrance.luncheon_costume_bonus_cooking_pots:"LavaWorldCostumeStage",
    SMOEntrance.luncheon_slots:"LavaBonus1Zone",
    SMOEntrance.luncheon_treasure_vault:"LavaWorldTreasureStage",
    SMOEntrance.magma_swamp:"LavaWorldUpDownExStage",
    SMOEntrance.magma_narrow_path:"LavaWorldBubbleLaneExStage",
    SMOEntrance.fork_flickin:"ForkExStage",
    SMOEntrance.cheese_excavate:"LavaWorldExcavationExStage",
    SMOEntrance.spinning_athletics:"LavaWorldClockExStage",
    SMOEntrance.rotating_gears_with_bitefrost:"GabuzouClockExStage",
    SMOEntrance.volcano_cave:"CapAppearLavaLiftExStage",
    SMOEntrance.lava_islands:"LavaWorldFenceLiftExStage",
    SMOEntrance.ruined_kingdom:"BossRaidWorldHomeStage",
    SMOEntrance.roulette_tower:"DotTowerExStage",
    SMOEntrance.chargin_chuck_arena:"BullRunExStage",
    SMOEntrance.bowsers_kingdom:"SkyWorldHomeStage",
    SMOEntrance.bowsers_kingdom_shop:"SkyWorldShopStage",
    SMOEntrance.folding_screen:"SkyWorldCostumeStage",
    SMOEntrance.bowsers_treasure_vault:"SkyWorldTreasureStage",
    SMOEntrance.spinning_tower:"TsukkunRotateExStage",
    SMOEntrance.jizos_adventure:"JizoSwitchExStage",
    SMOEntrance.dashing_above_the_clouds:"SkyWorldCloudBonusExStage",
    SMOEntrance.hexagon_tower:"KaronWingTowerStage",
    SMOEntrance.wooden_tower:"TsukkunClimbExStage",
    SMOEntrance.moon_kingdom:"MoonWorldHomeStage",
    SMOEntrance.moon_kingdom_shop:"MoonWorldShopRoom",
    SMOEntrance.moon_sphynx_vault:"MoonWorldSphinxRoom",
    SMOEntrance.moon_cave:"MoonWorldCaptureParadeStage",
    SMOEntrance.inside_the_church:"MoonWorldWeddingRoomStage",
    "Inside the Church 2 (possibly unused)":"MoonWorldWeddingRoom2Stage",
    "Moon":"MoonWorldKoopa1Stage",
    #"Moon":"MoonWorldKoopa2Stage",
    "Bowser Caverns:":"MoonWorldBasementStage",
    SMOEntrance.dot_galaxy:"Galaxy2DExStage",
    SMOEntrance.giant_swings:"MoonAthleticExStage",
    SMOEntrance.dark_side:"Special1WorldHomeStage",
    SMOEntrance.dark_side_topper:"Special1WorldTowerStackerStage",
    SMOEntrance.dark_side_hariet:"Special1WorldTowerBombTailStage",
    SMOEntrance.dark_side_spewart:"Special1WorldTowerFireBlowerStage",
    SMOEntrance.dark_side_rango:"Special1WorldTowerCapThrowerStage",
    SMOEntrance.dark_side_breakdown_road:"KillerRoadNoCapExStage",
    SMOEntrance.dark_side_invisible_road:"PackunPoisonNoCapExStage",
    SMOEntrance.dark_side_vanishing_road:"BikeSteelNoCapExStage",
    SMOEntrance.dark_side_siege:"ShootingCityYoshiExStage",
    SMOEntrance.dark_side_sinking_island:"SenobiTowerYoshiExStage",
    SMOEntrance.dark_side_magma_swamp:"LavaWorldUpDownYoshiExStage",
    SMOEntrance.darker_side:"Special2WorldHomeStage",
    "Darker Side: Main":"Special2WorldLavaStage",
    "Darker Side: Pokio":"Special2WorldCloudStage",
    "Darker Side: Bowser":"Special2WorldKoopaStage",
    "Mushroom Kingdom":"PeachWorldHomeStage",
    SMOEntrance.peachs_castle:"PeachWorldCastleStage",
    SMOEntrance.mushroom_kingdom_shop:"PeachWorldShopStage",
    SMOEntrance.castle_courtyard:"PeachWorldCostumeStage",
    SMOEntrance.mushroom_picture_match:"FukuwaraiMarioStage",
    SMOEntrance.painting_room_knucklotec:"PeachWorldPictureBossKnuckleStage",
    SMOEntrance.painting_room_torkdrift:"PeachWorldPictureBossForestStage",
    SMOEntrance.painting_room_mecha_wiggler:"PeachWorldPictureMofumofuStage",
    SMOEntrance.painting_room_mollusque_lanceur:"PeachWorldPictureGiantWanderBossStage",
    SMOEntrance.painting_room_cookatiel:"PeachWorldPictureBossMagmaStage",
    SMOEntrance.painting_room_lord_of_lightning:"PeachWorldPictureBossRaidStage",
    SMOEntrance.knucklotec_rematch:"RevengeBossKnuckleStage",
    SMOEntrance.torkdrift_rematch:"RevengeForestBossStage",
    SMOEntrance.mecha_wiggler_rematch:"RevengeMofumofuStage",
    SMOEntrance.mollusque_lanceur_rematch:"RevengeGiantWanderBossStage",
    SMOEntrance.cookatiel_rematch:"RevengeBossMagmaStage",
    SMOEntrance.lord_of_lightning_rematch:"RevengeBossRaidStage",
    SMOEntrance.yoshi_in_the_sea_of_clouds:"YoshiCloudExStage",
    SMOEntrance.mushroom_well:"DotHardExStage",
    **display_name_alias,
}



stage_id_to_name = {
    # "bikereturn": "BikeSteelExStage",
    # "bike": "BikeSteelExStage",
    "bike": "BikeSteelExStage",
    "bikereturn": "BikeSteelExStage",
    "BossRaidWorldMoonEx02_Exit": "BullRunExStage",
    "BossRaidWorldMoonEx02_Enter": "BullRunExStage",
    "CapAppearExEnt": "CapAppearExStage",
    "CapAppearExExit": "CapAppearExStage",
    "LavaLiftExdokan": "CapAppearLavaLiftExStage",
    "LavaLiftEx": "CapAppearLavaLiftExStage",
    "Goal": "CapWorldTowerStage",
    "Ex": "CapWorldTowerStage",
    "gunsyudokan": "CityPeopleRoadStage",
    "gunsyu": "CityPeopleRoadStage",
    "main_enter": "CityWorldMainTowerStage",
    "main_exit": "CityWorldMainTowerStage",
    "shop_corect": "CityWorldShop01Stage",
    "shop_coin": "CityWorldShop01Stage",
    "densendokan": "ElectricWireExStage",
    "densen": "ElectricWireExStage",
    "bonus2": "ForestWorldBonusStage",
    "bonus": "ForestWorldBonusStage",
    "boss001": "ForestWorldBossStage",
    # "boss001": "ForestWorldBossStage",
    "Tower001": "ForestWorldTowerStage",
    "Tower002": "ForestWorldTowerStage",
    "EX_Water": "ForestWorldWaterExStage",
    "EX_Water_Exit": "ForestWorldWaterExStage",
    "Jyukai001v": "ForestWorldWoodsStage",
    "Jyukai002": "ForestWorldWoodsStage",
    "Jyukai003v": "ForestWorldWoodsStage",
    "Jyukai004": "ForestWorldWoodsStage",
    # "Jyukai001v": "ForestWorldWoodsStage",
    # "Jyukai001v": "ForestWorldWoodsStage",
    "ForkEX": "ForkExStage",
    # "ForkEX": "ForkExStage",
    "LakeWorldMoonEX1b": "FrogPoisonExStage",
    "LakeWorldMoonEX1a": "FrogPoisonExStage",
    "GabuzouClockEx": "GabuzouClockExStage",
    "GabuzouClockExdokan": "GabuzouClockExStage",
    "dot00": "Galaxy2DExStage",
    "dot01": "Galaxy2DExStage",
    "EX_IceWater_Exit": "IceWaterBlockExStage",
    "EX_IceWater": "IceWaterBlockExStage",
    "EX_IceWaterDash_Exit": "IceWaterDashExStage",
    "EX_IceWaterDash": "IceWaterDashExStage",
    "imomu_02": "ImomuPoisonExStage",
    "imomu_01": "ImomuPoisonExStage",
    "jizo02": "JizoSwitchExStage",
    "jizo01": "JizoSwitchExStage",
    "EX_RailCol2_Exit": "KillerRailCollisionExStage",
    "EX_RailCol2": "KillerRailCollisionExStage",
    "PechoBubbleExDokan": "LavaWorldBubbleLaneExStage",
    "PechoBubbleEx": "LavaWorldBubbleLaneExStage",
    "BBQExDokan": "LavaWorldClockExStage",
    "BBQEx": "LavaWorldClockExStage",
    "CostumeOut": "LavaWorldCostumeStage",
    "CostumeEventWorldLava": "LavaWorldCostumeStage",
    "FenceLiftEx": "LavaWorldFenceLiftExStage",
    "FenceLiftExdokan": "LavaWorldFenceLiftExStage",
    "KeyMoveExDokan": "LavaWorldUpDownExStage",
    "KeyMoveEx": "LavaWorldUpDownExStage",
    "Lift2DExit": "Lift2DExStage",
    "Lift2D": "Lift2DExStage",
    "meganelift02": "MeganeLiftExStage",
    "meganelift01": "MeganeLiftExStage",
    "moon_exit": "MoonAthleticExStage",
    "moon": "MoonAthleticExStage",
    "vvv": "MoonWorldCaptureParadeStage",
    "bbb": "MoonWorldCaptureParadeStage",
    "PoisonEx_Exit": "PackunPoisonExStage",
    "PoisonEx": "PackunPoisonExStage",
    "BossRaidA": "PeachWorldPictureBossRaidStage",
    "BossRaidB": "PeachWorldPictureBossRaidStage",
    "GiantWanderBossA": "PeachWorldPictureGiantWanderBossStage",
    "GiantWanderBossB": "PeachWorldPictureGiantWanderBossStage",
    "PoisonWaveExExit": "PoisonWaveExStage",
    "PoisonWaveExEnt": "PoisonWaveExStage",
    "boureturn": "PoleKillerExStage",
    "bou": "PoleKillerExStage",
    "PushBlockExStageEntDokan": "PushBlockExStage",
    "PushBlockExStageEnt": "PushBlockExStage",
    "EX_RailCollision_Exit": "RailCollisionExStage",
    "EX_RailCollision": "RailCollisionExStage",
    "SeaWorldMoonEX1a": "ReflectBombExStage",
    "SeaWorldMoonEX1b": "ReflectBombExStage",
    "rollinggoal": "RollingExStage",
    "rollingstart": "RollingExStage",
    "doukutu2": "SandWorldKillerExStage",
    "doukutu1": "SandWorldKillerExStage",
    "anki2": "SandWorldMeganeExStage",
    "wall": "SandWorldMeganeExStage",
    "arijigoku1": "SandWorldPressExStage",
    "arijigoku2": "SandWorldPressExStage",
    "run00return": "SandWorldSphinxExStage",
    "run00": "SandWorldSphinxExStage",
    "PukupukuCaveGoal": "SeaWorldUtsuboCaveStage",
    "PukupukuCaveStart": "SeaWorldUtsuboCaveStage",
    "SeaWorldEX3b": "SenobiTowerExStage",
    "SeaWorldEX3a": "SenobiTowerExStage",
    "taxi": "ShootingCityExStage",
    "taxireturn": "ShootingCityExStage",
    "EX_Tankuro_Exit": "ShootingElevatorExStage",
    "EX_Tankuro": "ShootingElevatorExStage",
    "sora001": "SkyWorldCloudBonusExStage",
    # "sora001": "SkyWorldCloudBonusExStage",
    # "sora001": "SkyWorldCloudBonusExStage",
    # "sora001": "SkyWorldCloudBonusExStage",
    # "sora001": "SkyWorldCloudBonusExStage",
    # "sora001": "SkyWorldCloudBonusExStage",
    # "sora001": "SkyWorldCloudBonusExStage",
    # "sora001": "SkyWorldCloudBonusExStage",
    # "sora001": "SkyWorldCloudBonusExStage",
    # "sora001": "SkyWorldCloudBonusExStage",
    # "sora001": "SkyWorldCloudBonusExStage",
    # "sora001": "SkyWorldCloudBonusExStage",
    "BombTailRoomStart": "Special1WorldTowerBombTailStage",
    "BombTailRoomGoal": "Special1WorldTowerBombTailStage",
    "CapThrowerRoomGoal": "Special1WorldTowerCapThrowerStage",
    "CapThrowerRoomStart": "Special1WorldTowerCapThrowerStage",
    "FireBlowerRoomStart": "Special1WorldTowerFireBlowerStage",
    "FireBlowerRoomGoal": "Special1WorldTowerFireBlowerStage",
    "StackerRoomStart": "Special1WorldTowerStackerStage",
    "StackerRoomGoal": "Special1WorldTowerStackerStage",
    "MoonGoal": "Special2WorldLavaStage",
    "CP_Entrance": "Special2WorldLavaStage",
    "gragrareturn": "SwingSteelExStage",
    "gragra": "SwingSteelExStage",
    "CapTrampolineB": "TrampolineWallCatchExStage",
    "CapTrampolineA": "TrampolineWallCatchExStage",
    "bike02return": "TrexBikeExStage",
    "bike02": "TrexBikeExStage",
    "tukkun001_exit": "TsukkunClimbExStage",
    "tukkun001_enter": "TsukkunClimbExStage",
    "tukkun000_exit": "TsukkunRotateExStage",
    "tukkun000_enter": "TsukkunRotateExStage",
    "WanwanExGoal": "WanwanClashExStage",
    "WanwanExStart": "WanwanClashExStage",
    "EX_2DHosui_Exit": "WaterTubeExStage",
    "EX_2DHosui": "WaterTubeExStage",
    "SeaWorldEX1b": "WaterValleyExStage",
    "SeaWorldEX1a": "WaterValleyExStage",
    "WindBlowExGoal": "WindBlowExStage",
    "WindBlowExStart": "WindBlowExStage",

    # Dead Ends
    "EX_AnimalChase": "AnimalChaseExStage",
    "ByugoPuzzle": "ByugoPuzzleExStage",
    "kaitendokan": "CapRotatePackunExStage",
    "under001enter": "CityWorldFactoryStage",
    "Bonus": "CityWorldSandSlotStage",
    "Kinopio": "ClashWorldShopStage",
    "cube": "Cube2DExStage",
    "donsuke": "DonsukeExStage",
    "PeachWorldEx2a": "DotHardExStage",
    "FastenerEx": "FastenerExStage",
    "EXCloud": "ForestWorldCloudBonusExStage",
    "Explorer_Bonus": "ForestWorldWoodsCostumeStage",
    "TreasureTree": "ForestWorldWoodsTreasureStage",
    "FrogSearchExStageEnt": "FrogSearchExStage",
    "Fukuwarai": "FukuwaraiKuriboStage",
    "Goton": "GotogotonExStage",
    "HomeEntrance": "HomeShipInsideStage",
    "FigureWalker": "IceWalkerExStage",
    "ClashWorldMoonEX2": "JangoExStage",
    "Patakaron02": "KaronWingTowerStage",
    "KillerRoad": "KillerRoadExStage",
    "LakeWorldShop": "LakeWorldShopStage",
    "MartinCubeEx": "LavaWorldExcavationExStage",
    "shop(lava)": "LavaWorldShopStage", # "shop"
    "TreasureEventWorldLava": "LavaWorldTreasureStage",
    # "None": "MoonWorldKoopa1Stage",
    # "None": "MoonWorldKoopa2Stage",
    "ddd": "MoonWorldShopRoom",
    "ggg": "MoonWorldSphinxRoom",
    "aaa": "MoonWorldWeddingRoomStage",
    "onpu": "Note2D3DRoomExStage",
    "PeachCastleGate": "PeachWorldCastleStage",
    "BossForestA": "PeachWorldPictureBossForestStage",
    "BossKnuckleA": "PeachWorldPictureBossKnuckleStage",
    "BossMagmaA": "PeachWorldPictureBossMagmaStage",
    "MofumofuA": "PeachWorldPictureMofumofuStage",
    "PeachWorldShopA": "PeachWorldShopStage",
    "car": "RadioControlExStage",
    "rocket": "RocketFlowerExStage",
    "abc": "SandWorldCostumeStage",
    "pyramid01": "SandWorldPyramid000Stage",
    "pyramid04": "SandWorldPyramid001Stage",
    "hide": "SandWorldSecretStage",
    "bar1": "SandWorldShopStage",
    "town(sand)": "SandWorldSlotStage", # "town"
    "Yadokari00": "SandWorldUnderground001Stage",
    "shindo": "SandWorldVibrationStage",
    "CostumeEventSeaWorld": "SeaWorldCostumeStage",
    "TreasureEventWorldSea": "SeaWorldSecretStage",
    "RoomEventWorldSea": "SeaWorldSneakingManStage",
    "shindo_Lv2": "SeaWorldVibrationStage",
    "byoubu": "SkyWorldCostumeStage",
    "shop(sky)": "SkyWorldShopStage", # "shop"
    "shop_dress": "SkyWorldTreasureStage",
    "EX_SkyBonus": "SnowWorldCloudBonusExStage",
    "SnowCostumeEx": "SnowWorldCostumeStage",
    "RaceTrackExit": "SnowWorldLobby000Stage",
    "MoonRace": "SnowWorldLobbyExStage",
    "ShopDoor": "SnowWorldShopStage",
    "room2_start": "Special2WorldCloudStage",
    "room3_goal": "Special2WorldKoopaStage",
    "theater": "Theater2DExStage",
    "SeaWorldMoonEX2": "TogezoRotateExStage",
    "RexPoppunEx": "TrexPoppunExStage",
    "PeachWorldEx1a": "YoshiCloudExStage",
    "SnowUGEnt": "SnowWorldTownStage",
    "icestart": "SandWorldUnderground000Stage",
    "biru": "SandWorldRotateExStage",
    "EX_Mist": "FogMountainExStage",
    "tenjo": "PoleGrabCeilExStage",
    "SeaWorldEX2": "CloudExStage",
    "town(lava)": "LavaBonus1Zone", # "town"
    "BossRaidWorldEx01_Eixt": "DotTowerExStage",
    "BikeSteelNoCapEx_Exit": "BikeSteelNoCapExStage",
    "PackunPoisonNoCapEx_Exit": "PackunPoisonNoCapExStage",
    "ShootingCityYoshiEx": "ShootingCityYoshiExStage",
    "SenobiTowerYoshiEx": "SenobiTowerYoshiExStage",
    "LavaWorldUpDownYoshiEx": "LavaWorldUpDownYoshiExStage",
    "SenobiTowerYoshiEx_Exit": "SenobiTowerYoshiExStage",
    "LavaWorldUpDownYoshiEx_Exit": "LavaWorldUpDownYoshiExStage",
    "ShootingCityYoshiEx_Exit": "ShootingCityYoshiExStage",
    "KillerRoadNoCapEx": "KillerRoadNoCapExStage",
    "BikeSteelNoCapEx": "BikeSteelNoCapExStage",
    "PackunPoisonNoCapEx": "PackunPoisonNoCapExStage",
    "PictureBossMagma": "PeachWorldPictureBossMagmaStage",
    "PictureMofumofu": "PeachWorldPictureMofumofuStage",
    "PictureBossRaid": "PeachWorldPictureBossRaidStage",
    # "BossRaidA": "PeachWorldPictureBossRaidStage",
    # "BossRaidB": "PeachWorldPictureBossRaidStage",
    "PictureBossForest": "PeachWorldPictureBossForestStage",
    "PictureBossKnuckle": "PeachWorldPictureBossKnuckleStage",
    "PictureGiantWanderBoss": "PeachWorldPictureGiantWanderBossStage",

    "start(cookatiel)": "RevengeBossMagmaStage",
    "start(wiggler)": "RevengeMofumofuStage",
    "start(dragon)": "RevengeBossRaidStage",
    "start(torkdrift)": "RevengeForestBossStage",
    "start(knucklotec)": "RevengeBossKnuckleStage",
    "start(mollusque)": "RevengeGiantWanderBossStage",

    "Fukuwarai2": "FukuwaraiMarioStage",
    "CostumeEventWorldPeach": "PeachWorldCostumeStage",

}

internal_name_to_entrance = {
    "BikeSteelExStage": {
        "entrance": "bike",
        "exit": "bikereturn",
    },
    "BullRunExStage": {
        "exit": "BossRaidWorldMoonEx02_Exit",
        "entrance": "BossRaidWorldMoonEx02_Enter",
    },
    "CapAppearExStage": {
        "entrance": "CapAppearExEnt",
        "exit": "CapAppearExExit",
    },
    "CapAppearLavaLiftExStage": {
        "exit": "LavaLiftExdokan",
        "entrance": "LavaLiftEx",
    },
    "CapWorldTowerStage": {
        "exit": "Goal",
        "entrance": "Ex",
    },
    "CityPeopleRoadStage": {
        "exit": "gunsyudokan",
        "entrance": "gunsyu",
    },
    "CityWorldMainTowerStage": {
        "entrance": "main_enter",
        "exit": "main_exit",
    },
    "CityWorldShop01Stage": {
        "exit": "shop_corect",
        "entrance": "shop_coin",
    },
    "ElectricWireExStage": {
        "exit": "densendokan",
        "entrance": "densen",
    },
    "ForestWorldBonusStage": {
        "exit": "bonus2",
        "entrance": "bonus",
    },
    "ForestWorldBossStage": {
        "entrance": "boss001",
    },
    "ForestWorldTowerStage": {
        "entrance": "Tower001",
        "exit": "Tower002",
    },
    "ForestWorldWaterExStage": {
        "entrance": "EX_Water",
        "exit": "EX_Water_Exit",
    },
    "ForestWorldWoodsStage": {
        "exit1": "Jyukai001v",
        "exit2": "Jyukai002",
        "exit3": "Jyukai003v",
        "exit4": "Jyukai004",
    },
    "ForkExStage": {
        "entrance": "ForkEX",
        "exit": "ForkEX2",
    },
    "FrogPoisonExStage": {
        "exit": "LakeWorldMoonEX1b",
        "entrance": "LakeWorldMoonEX1a",
    },
    "GabuzouClockExStage": {
        "entrance": "GabuzouClockEx",
        "exit": "GabuzouClockExdokan",
    },
    "Galaxy2DExStage": {
        "entrance": "dot00",
        "exit": "dot01",
    }, # Check
    "IceWaterBlockExStage": {
        "exit": "EX_IceWater_Exit",
        "entrance": "EX_IceWater",
    },
    "IceWaterDashExStage": {
        "exit": "EX_IceWaterDash_Exit",
        "entrance": "EX_IceWaterDash",
    },
    "ImomuPoisonExStage": {
        "exit": "imomu_02",
        "entrance": "imomu_01",
    },
    "JizoSwitchExStage": {
        "exit": "jizo02",
        "entrance": "jizo01",
    },
    "KillerRailCollisionExStage": {
        "exit": "EX_RailCol2_Exit",
        "entrance": "EX_RailCol2",
    },
    "LavaWorldBubbleLaneExStage": {
        "exit": "PechoBubbleExDokan",
        "entrance": "PechoBubbleEx",
    },
    "LavaWorldClockExStage": {
        "exit": "BBQExDokan",
        "entrance": "BBQEx",
    },
    "LavaWorldCostumeStage": {
        "exit": "CostumeOut",
        "entrance": "CostumeEventWorldLava",
    },
    "LavaWorldFenceLiftExStage": {
        "entrance": "FenceLiftEx",
        "exit": "FenceLiftExdokan",
    },
    "LavaWorldUpDownExStage": {
        "exit": "KeyMoveExDokan",
        "entrance": "KeyMoveEx",
    },
    "Lift2DExStage": {
        "exit": "Lift2DExit",
        "entrance": "Lift2D",
    },
    "MeganeLiftExStage": {
        "exit": "meganelift02",
        "entrance": "meganelift01",
    },
    "MoonAthleticExStage": {
        "exit": "moon_exit",
        "entrance": "moon",
    },
    "MoonWorldCaptureParadeStage": {
        "exit": "vvv",
        "entrance": "bbb",
    },
    "PackunPoisonExStage": {
        "exit": "PoisonEx_Exit",
        "entrance": "PoisonEx",
    },
    "PeachWorldPictureBossRaidStage": {
        "entrance": "BossRaidA",
        #"entrance": "BossRaidB",
        "exit": "PictureBossRaid",
    },
    "PeachWorldPictureGiantWanderBossStage": {
        "entrance": "GiantWanderBossA",
        #"exit": "GiantWanderBossB",
        "exit": "PictureGiantWanderBoss",
    },
    "PoisonWaveExStage": {
        "exit": "PoisonWaveExExit",
        "entrance": "PoisonWaveExEnt",
    },
    "PoleKillerExStage": {
        "exit": "boureturn",
        "entrance": "bou",
    },
    "PushBlockExStage": {
        "exit": "PushBlockExStageEntDokan",
        "entrance": "PushBlockExStageEnt",
    },
    "RailCollisionExStage": {
        "exit": "EX_RailCollision_Exit",
        "entrance": "EX_RailCollision",
    },
    "ReflectBombExStage": {
        "entrance": "SeaWorldMoonEX1a",
        "exit": "SeaWorldMoonEX1b",
    },
    "RollingExStage": {
        "exit": "rollinggoal",
        "entrance": "rollingstart",
    },
    "SandWorldKillerExStage": {
        "exit": "doukutu2",
        "entrance": "doukutu1",
    },
    "SandWorldMeganeExStage": {
        "exit": "anki2",
        "entrance": "wall",
    },
    "SandWorldPressExStage": {
        "entrance": "arijigoku1",
        "exit": "arijigoku2",
    },
    "SandWorldSphinxExStage": {
        "exit": "run00return",
        "entrance": "run00",
    },
    "SeaWorldUtsuboCaveStage": {
        "exit": "PukupukuCaveGoal",
        "entrance": "PukupukuCaveStart",
    },
    "SenobiTowerExStage": {
        "exit": "SeaWorldEX3b",
        "entrance": "SeaWorldEX3a",
    },
    "ShootingCityExStage": {
        "entrance": "taxi",
        "exit": "taxireturn",
    },
    "ShootingElevatorExStage": {
        "exit": "EX_Tankuro_Exit",
        "entrance": "EX_Tankuro",
    },
    "SkyWorldCloudBonusExStage": {
        "entrance": "sora001",
    },
    "Special1WorldTowerBombTailStage": {
        "entrance": "BombTailRoomStart",
        "exit": "BombTailRoomGoal",
    },
    "Special1WorldTowerCapThrowerStage": {
        "exit": "CapThrowerRoomGoal",
        "entrance": "CapThrowerRoomStart",
    },
    "Special1WorldTowerFireBlowerStage": {
        "entrance": "FireBlowerRoomStart",
        "exit": "FireBlowerRoomGoal",
    },
    "Special1WorldTowerStackerStage": {
        "entrance": "StackerRoomStart",
        "exit": "StackerRoomGoal",
    },
    "Special2WorldLavaStage": {
        "exit": "MoonGoal",
        "entrance": "CP_Entrance",
    },
    "SwingSteelExStage": {
        "exit": "gragrareturn",
        "entrance": "gragra",
    },
    "TrampolineWallCatchExStage": {
        "exit": "CapTrampolineB",
        "entrance": "CapTrampolineA",
    },
    "TrexBikeExStage": {
        "exit": "bike02return",
        "entrance": "bike02",
    },
    "TsukkunClimbExStage": {
        "exit": "tukkun001_exit",
        "entrance": "tukkun001_enter",
    },
    "TsukkunRotateExStage": {
        "exit": "tukkun000_exit",
        "entrance": "tukkun000_enter",
    },
    "WanwanClashExStage": {
        "exit": "WanwanExGoal",
        "entrance": "WanwanExStart",
    },
    "WaterTubeExStage": {
        "exit": "EX_2DHosui_Exit",
        "entrance": "EX_2DHosui",
    },
    "WaterValleyExStage": {
        "exit": "SeaWorldEX1b",
        "entrance": "SeaWorldEX1a",
    },
    "WindBlowExStage": {
        "exit": "WindBlowExGoal",
        "entrance": "WindBlowExStart",
    },
    "AnimalChaseExStage": {
        "entrance": "EX_AnimalChase",
    },
    "ByugoPuzzleExStage": {
        "entrance": "ByugoPuzzle",
    },
    "CapRotatePackunExStage": {
        "entrance": "kaitendokan",
    },
    "CityWorldFactoryStage": {
        "entrance": "under001enter",
    },
    "CityWorldSandSlotStage": {
        "entrance": "Bonus",
    },
    "ClashWorldShopStage": {
        "entrance": "Kinopio",
    },
    "Cube2DExStage": {
        "entrance": "cube",
    },
    "DonsukeExStage": {
        "entrance": "donsuke",
    },
    "DotHardExStage": {
        "entrance": "PeachWorldEx2a",
    },
    "FastenerExStage": {
        "entrance": "FastenerEx",
    },
    "ForestWorldCloudBonusExStage": {
        "entrance": "EXCloud",
    },
    "ForestWorldWoodsCostumeStage": {
        "entrance": "Explorer_Bonus",
    },
    "ForestWorldWoodsTreasureStage": {
        "entrance": "TreasureTree",
    },
    "FrogSearchExStage": {
        "entrance": "FrogSearchExStageEnt",
    },
    "FukuwaraiKuriboStage": {
        "entrance": "Fukuwarai",
    },
    "GotogotonExStage": {
        "entrance": "Goton",
    },
    "HomeShipInsideStage": {
        "entrance": "HomeEntrance",
    },
    "IceWalkerExStage": {
        "entrance": "FigureWalker",
    },
    "JangoExStage": {
        "entrance": "ClashWorldMoonEX2",
    },
    "KaronWingTowerStage": {
        "entrance": "Patakaron02",
    },
    "KillerRoadExStage": {
        "entrance": "KillerRoad",
    },
    "LakeWorldShopStage": {
        "entrance": "LakeWorldShop",
    },
    "LavaWorldExcavationExStage": {
        "entrance": "MartinCubeEx",
    },
    "LavaWorldShopStage": {
    },
    "LavaWorldTreasureStage": {
        "entrance": "TreasureEventWorldLava",
    },
    "MoonWorldShopRoom": {
        "entrance": "ddd",
    },
    "MoonWorldSphinxRoom": {
        "entrance": "ggg",
    },
    "MoonWorldWeddingRoomStage": {
        "entrance": "aaa",
    },
    "Note2D3DRoomExStage": {
        "entrance": "onpu",
    },
    "PeachWorldCastleStage": {
        "entrance": "PeachCastleGate",
    },
    "PeachWorldPictureBossForestStage": {
        "entrance": "BossForestA",
        "exit": "PictureBossForest",
    },
    "PeachWorldPictureBossKnuckleStage": {
        "entrance": "BossKnuckleA",
        "exit": "PictureBossKnuckle",
    },
    "PeachWorldPictureBossMagmaStage": {
        "entrance": "BossMagmaA",
        "exit": "PictureBossMagma",
    },
    "PeachWorldPictureMofumofuStage": {
        "entrance": "MofumofuA",
        "exit": "PictureMofumofu",
    },
    "PeachWorldShopStage": {
        "entrance": "PeachWorldShopA",
    },
    "RadioControlExStage": {
        "entrance": "car",
    },
    "RocketFlowerExStage": {
        "entrance": "rocket",
    },
    "SandWorldCostumeStage": {
        "entrance": "abc",
    },
    "SandWorldPyramid000Stage": {
        "entrance": "pyramid01",
    },
    "SandWorldPyramid001Stage": {
        "entrance": "pyramid04",
    },
    "SandWorldSecretStage": {
        "entrance": "hide",
    },
    "SandWorldShopStage": {
        "entrance": "bar1",
    },
    "SandWorldSlotStage": {
        "entrance": "town"
    },
    "SandWorldUnderground001Stage": {
        "entrance": "Yadokari00",
    },
    "SandWorldVibrationStage": {
        "entrance": "shindo",
    },
    "SeaWorldCostumeStage": {
        "entrance": "CostumeEventSeaWorld",
    },
    "SeaWorldSecretStage": {
        "entrance": "TreasureEventWorldSea",
    },
    "SeaWorldSneakingManStage": {
        "entrance": "RoomEventWorldSea",
    },
    "SeaWorldVibrationStage": {
        "entrance": "shindo_Lv2",
    },
    "SkyWorldCostumeStage": {
        "entrance": "byoubu",
    },
    "SkyWorldShopStage": {
        "entrance": "shop"
    },
    "SkyWorldTreasureStage": {
        "entrance": "shop_dress",
    },
    "SnowWorldCloudBonusExStage": {
        "entrance": "EX_SkyBonus",
    },
    "SnowWorldCostumeStage": {
        "entrance": "SnowCostumeEx",
    },
    "SnowWorldLobby000Stage": {
        "entrance": "RaceTrackExit",
    },
    "SnowWorldLobbyExStage": {
        "entrance": "MoonRace",
    },
    "SnowWorldShopStage": {
        "entrance": "ShopDoor",
    },
    "Special2WorldCloudStage": {
        "entrance": "room2_start",
    },
    "Special2WorldKoopaStage": {
        "entrance": "room3_goal",
    },
    "Theater2DExStage": {
        "entrance": "theater",
    },
    "TogezoRotateExStage": {
        "entrance": "SeaWorldMoonEX2",
    },
    "TrexPoppunExStage": {
        "entrance": "RexPoppunEx",
    },
    "YoshiCloudExStage": {
        "entrance": "PeachWorldEx1a",
    },
    "SnowWorldTownStage": {
        "entrance": "SnowUGEnt",
        "entrance_rev": "SnowUGExit",
        "exit": "RaceEntrance",
        "exit_rev": "RaceTrackExit"
    },
    "SandWorldUnderground000Stage": {
    },
    "SandWorldRotateExStage": {
        "entrance": "biru",
        "exit": "birureturn",
    },
    "FogMountainExStage": {
        "entrance": "EX_Mist",
    },
    "PoleGrabCeilExStage": {
        "entrance": "tenjo",
        "exit": "tenjo2",
    },
    "CloudExStage": {
        "entrance": "SeaWorldEX2",
    },
    # "LavaBonus1Zone": {
    #     "entrance": "town",
    # },
    "DotTowerExStage": {
        "entrance": "BossRaidWorldEx01_Eixt",
        "exit": "BossRaidWorldEx01_Eixt2"
    },
    "BikeSteelNoCapExStage": {
        "exit": "BikeSteelNoCapEx_Exit",
        "entrance": "BikeSteelNoCapEx",
    },
    "PackunPoisonNoCapExStage": {
        "exit": "PackunPoisonNoCapEx_Exit",
        "entrance": "PackunPoisonNoCapEx",
    },
    "ShootingCityYoshiExStage": {
        "entrance": "ShootingCityYoshiEx",
        "exit": "ShootingCityYoshiEx_Exit",
    },
    "SenobiTowerYoshiExStage": {
        "entrance": "SenobiTowerYoshiEx",
        "exit": "SenobiTowerYoshiEx_Exit",
    },
    "LavaWorldUpDownYoshiExStage": {
        "entrance": "LavaWorldUpDownYoshiEx",
        "exit": "LavaWorldUpDownYoshiEx_Exit",
    },
    "KillerRoadNoCapExStage": {
        "entrance": "KillerRoadNoCapEx",
    },
    "RevengeBossMagmaStage": {
        "entrance": "PictureBossMagma",
    },
    "RevengeMofumofuStage": {
        "entrance": "PictureMofumofu",
    },
    "RevengeBossRaidStage": {
        "entrance": "PictureBossRaid",
    },
    "RevengeForestBossStage": {
        "entrance": "PictureBossForest",
    },
    "RevengeBossKnuckleStage": {
        "entrance": "PictureBossKnuckle",
    },
    "RevengeGiantWanderBossStage": {
        "entrance": "PictureGiantWanderBoss",
    },
    "FukuwaraiMarioStage": {
        "entrance": "Fukuwarai2",
    },
    "PeachWorldCostumeStage": {
        "entrance": "CostumeEventWorldPeach",
    },

    # Over worlds
    # replace with SMOEntrance.name : id
    'CapWorldHomeStage': {
        'CapWorldTowerStage':
            {
                'exit' : 'Ex',
                'entrance': 'Goal'
            },
        'PoisonWaveExStage': 'PoisonWaveExExit',
        'FrogSearchExStage': 'FrogSearchExStageEnt',
        'PushBlockExStage': 'PushBlockExStageEntDokan',
        'RollingExStage': 'rollinggoal',
        # 'rollingstart': 'RollingExStage', # don't come out of entrance if exit pipe is available
        },

    'WaterfallWorldHomeStage': {
        'TrexPoppunExStage': 'RexPoppunEx',
        'WanwanClashExStage': 'WanwanExGoal',
        'Lift2DExStage': 'Lift2DExit',
        'CapAppearExStage': 'CapAppearExExit',
        'WindBlowExStage': 'WindBlowExGoal',
        },

    'SandWorldHomeStage': {
        'SandWorldPyramid000Stage': 'pyramid01',
        'SandWorldPyramid001Stage': 'pyramid04',
        'SandWorldShopStage': 'bar2',
        'SandWorldSecretStage': 'hide',
        'SandWorldUnderground001Stage': 'Out',
        'SandWorldMeganeExStage': 'anki2',
        'SandWorldPressExStage': {
            'entrance': 'arijigoku1',
            'exit': 'arijigoku2',
        },
        'SandWorldSphinxExStage': 'run00',
        'SandWorldKillerExStage': 'doukutu2',
        'SandWorldVibrationStage': 'shindo',
        'SandWorldUnderground000Stage': 'Under01',
        'MeganeLiftExStage': 'meganelift02',
        'RocketFlowerExStage': 'rocket',
        'WaterTubeExStage': 'EX_2DHosui_Exit',
        'SandWorldCostumeStage': 'abc',
        'SandWorldSlotStage': 'town',
        'SandWorldRotateExStage': 'birureturn',
        },

    'ForestWorldHomeStage': {
        'ForestWorldTowerStage': {
            'entrance': 'Tower001',
            'exit': 'Tower002'
            },
        'ForestWorldBossStage': 'boss002',
        'ForestWorldWoodsStage':{
            'entrance1': 'Jyukai001',
            'entrance2': 'Jyukai003',
        },


        'ForestWorldCloudBonusExStage': 'EXCloud',
        'ForestWorldWaterExStage': 'EX_Water_Exit',
        'ForestWorldBonusStage': 'bonus2',
        'RailCollisionExStage': 'EX_RailCollision_Exit',
        'ShootingElevatorExStage': 'EX_Tankuro_Exit',
        'AnimalChaseExStage': 'EX_AnimalChase',
        'PackunPoisonExStage': 'PoisonEx_Exit',
        'KillerRoadExStage': 'KillerRoad', # Might need a new exit pipe for coming out of this exit in wrong scenario
        },

    'LakeWorldHomeStage': {
        'FrogPoisonExStage': 'LakeWorldMoonEX1b',
        'TrampolineWallCatchExStage': 'CapTrampolineB',
        'LakeWorldShopStage': 'LakeWorldShop',
        'FastenerExStage' : 'FastenerEx'
        },

    'CloudWorldHomeStage': {
        'FukuwaraiKuriboStage': 'Fukuwarai',
        'Cube2DExStage': 'cube',
        },

    'ClashWorldHomeStage': {
        'ClashWorldShopStage': 'Kinopio',
        'JangoExStage': 'ClashWorldMoonEX2',
        'ImomuPoisonExStage': 'imomu_02',
    },

    'CityWorldHomeStage': {
        'CityWorldMainTowerStage': {
            "entrance": 'main_enter',
            'exit': 'main_exit',
        },
        'CityWorldShop01Stage': {
            'regional': 'shop_corect',
            'coin': 'shop_coin',
        },
        'Note2D3DRoomExStage': 'onpu',
        'RadioControlExStage': 'car',
        'CityWorldSandSlotStage': 'Bonus',
        'CapRotatePackunExStage': 'kaitendokan',
        'CityPeopleRoadStage': {
            'entrance': 'gunsyu',
            'exit': 'gunsyudokan',
        },
        'ShootingCityExStage': 'taxi',
        'Theater2DExStage': 'theater',
        'CityWorldFactoryStage': 'under001enter',
        'PoleKillerExStage': 'boureturn',
        'ElectricWireExStage': 'densendokan',
        'TrexBikeExStage': 'bike02return',
        'SwingSteelExStage': 'gragrareturn',
        'DonsukeExStage': 'donsuke',
        'BikeSteelExStage': 'bikereturn',
        'PoleGrabCeilExStage': 'tenjo',
        },

    'SeaWorldHomeStage': {
        'SeaWorldVibrationStage': 'shindo_Lv2',
        'TogezoRotateExStage': 'SeaWorldMoonEX2',
        'ReflectBombExStage': 'SeaWorldMoonEX1b',
        'SeaWorldCostumeStage': 'CostumeEventSeaWorld',
        'WaterValleyExStage': 'SeaWorldEX1b',
        'SenobiTowerExStage': 'SeaWorldEX3b',
        'SeaWorldSneakingManStage': 'RoomEventWorldSea',
        'SeaWorldUtsuboCaveStage': {
            'entrance': 'PukupukuCaveStart',
            'exit': 'PukupukuCaveGoal',
        },
        'SeaWorldSecretStage': 'TreasureEventWorldSea',
        'CloudExStage': 'SeaWorldEX2Return'
        },

    'SnowWorldHomeStage': {
        'IceWaterDashExStage': 'EX_IceWaterDash_Exit',
        'ByugoPuzzleExStage': 'ByugoPuzzle',
        'IceWalkerExStage': 'FigureWalker',
        'SnowWorldCloudBonusExStage': 'EX_SkyBonus',
        'SnowWorldLobbyExStage': 'MoonRace',
        'SnowWorldTownStage': 'SnowUGExit',
        'IceWaterBlockExStage': 'EX_IceWater_Exit',
        'TestShirai011Stage': 'EX_IceWaterDash_Exit',
        'KillerRailCollisionExStage': 'EX_RailCol2_Exit',
        },

    'LavaWorldHomeStage': {
        'ForkExStage': 'ForkEX',
        'LavaWorldExcavationExStage': 'MartinCubeEx',
        'LavaWorldUpDownExStage': 'KeyMoveExDokan',
        'LavaWorldBubbleLaneExStage': 'PechoBubbleExDokan',
        'LavaWorldClockExStage': 'BBQExDokan',
        'LavaWorldCostumeStage': 'CostumeOut',
        'LavaWorldFenceLiftExStage': 'FenceLiftExdokan',
        'CapAppearLavaLiftExStage': 'LavaLiftExdokan',
        'GabuzouClockExStage': 'GabuzouClockExdokan',
        'LavaBonus1Zone': 'town',
        'LavaWorldShopStage': 'shop',
        'LavaWorldTreasureStage': 'TreasureEventWorldLava',
        },

    'BossRaidWorldHomeStage': {
        'DotTowerExStage': 'BossRaidWorldEx01_Eixt',
        'BullRunExStage': 'BossRaidWorldMoonEx02_Exit',
        },

    'SkyWorldHomeStage': {
        'SkyWorldShopStage': 'shop',
        'SkyWorldCostumeStage':'byoubu',
        'SkyWorldCloudBonusExStage':'sora001',
        'SkyWorldTreasureStage':'shop_dress',
        'TsukkunRotateExStage':'tukkun000_exit',
        'JizoSwitchExStage':'jizo02',
        'TsukkunClimbExStage':'tukkun001_exit',
        'KaronWingTowerStage':'Patakaron02',
        },

    'MoonWorldHomeStage': {
        'MoonWorldWeddingRoomStage': {
            'entrance':'aaa',
            'secret': 'fff',
        },
        'MoonWorldCaptureParadeStage': {
            'exit':'bbb',
            'entrance': 'vvv',
        },
        'MoonWorldSphinxRoom': 'ggg',
        'MoonWorldShopRoom': 'ddd',
        'Galaxy2DExStage': 'dot01',
        'MoonAthleticExStage': 'moon_exit',
        },

    'PeachWorldHomeStage': {
        'PeachWorldCastleStage': 'PeachCastleGate',
        'PeachWorldShopStage': 'PeachWorldShopA',
        'PeachWorldPictureBossMagmaStage': 'BossMagmaA',
        'PeachWorldPictureMofumofuStage': 'MofumofuA',
        'PeachWorldPictureBossKnuckleStage': 'BossKnuckleA',
        'PeachWorldPictureBossForestStage': 'BossForestA',
        'YoshiCloudExStage': 'PeachWorldEx1a',
        'PeachWorldPictureGiantWanderBossStage': 'GiantWanderBossB',
        'PeachWorldPictureBossRaidStage': 'BossRaidB',
        'DotHardExStage': 'PeachWorldEx2a',
        'PeachWorldCostumeStage': 'CostumeEventWorldPeach',
        'FukuwaraiMarioStage': 'Fukuwarai2',
        },

    'Special1WorldHomeStage': {

        'Special1WorldTowerCapThrowerStage': {
            'entrance': 'CapThrowerRoomStart',
            'exit': 'CapThrowerRoomGoal',
        },
        'Special1WorldTowerBombTailStage': {
            'entrance': 'BombTailRoomStart',
            'exit': 'BombTailRoomGoal',
        },
        'Special1WorldTowerFireBlowerStage': {
            'entrance': 'FireBlowerRoomStart',
            'exit': 'FireBlowerRoomGoal',
        },
        'Special1WorldTowerStackerStage': {
            'entrance': 'StackerRoomStart',
            'exit': 'StackerRoomGoal',
        },
        'BikeSteelNoCapExStage': 'BikeSteelNoCapEx_Exit',
        'PackunPoisonNoCapExStage': 'PackunPoisonNoCapEx_Exit',
        'SenobiTowerYoshiExStage': 'SenobiTowerYoshiEx_Exit',
        'LavaWorldUpDownYoshiExStage': 'LavaWorldUpDownYoshiEx_Exit',
        'ShootingCityYoshiExStage': 'ShootingCityYoshiEx_Exit',
        'KillerRoadNoCapExStage': 'KillerRoadNoCapEx',
        },

    'Special2WorldHomeStage': {
        'Special2WorldLavaStage': {
            'entrance':'CP_Entrance',
            'exit': 'MoonGoal',
            }
        },
}

stage_names = [
    "AnimalChaseExStage",
    "BikeSteelExStage",
    "BossRaidWorldHomeStage",
    "BullRunExStage",
    "ByugoPuzzleExStage",
    "CapAppearExStage",
    "CapAppearLavaLiftExStage",
    "CapRotatePackunExStage",
    "CapWorldHomeStage",
    "CapWorldTowerStage",
    "CityPeopleRoadStage",
    "CityWorldFactoryStage",
    "CityWorldHomeStage",
    "CityWorldMainTowerStage",
    "CityWorldSandSlotStage",
    "CityWorldShop01Stage",
    "ClashWorldHomeStage",
    "ClashWorldShopStage",
    "CloudWorldHomeStage",
    "Cube2DExStage",
    "DonsukeExStage",
    "DotHardExStage",
    "ElectricWireExStage",
    "FastenerExStage",
    "ForestWorldBonusStage",
    "ForestWorldBossStage",
    "ForestWorldCloudBonusExStage",
    "ForestWorldHomeStage",
    "ForestWorldTowerStage",
    "ForestWorldWaterExStage",
    "ForestWorldWoodsCostumeStage",
    "ForestWorldWoodsStage",
    "ForestWorldWoodsTreasureStage",
    "ForkExStage",
    "FrogPoisonExStage",
    "FrogSearchExStage",
    "FukuwaraiKuriboStage",
    "GabuzouClockExStage",
    "Galaxy2DExStage",
    "GotogotonExStage",
    "HomeShipInsideStage",
    "IceWalkerExStage",
    "IceWaterBlockExStage",
    "IceWaterDashExStage",
    "ImomuPoisonExStage",
    "JangoExStage",
    "JizoSwitchExStage",
    "KaronWingTowerStage",
    "KillerRailCollisionExStage",
    "KillerRoadExStage",
    "LakeWorldHomeStage",
    "LakeWorldShopStage",
    "LavaWorldBubbleLaneExStage",
    "LavaWorldClockExStage",
    "LavaWorldCostumeStage",
    "LavaWorldExcavationExStage",
    "LavaWorldFenceLiftExStage",
    "LavaWorldHomeStage",
    "LavaWorldShopStage",
    "LavaWorldTreasureStage",
    "LavaWorldUpDownExStage",
    "Lift2DExStage",
    "MeganeLiftExStage",
    "MoonAthleticExStage",
    "MoonWorldCaptureParadeStage",
    "MoonWorldHomeStage",
    "MoonWorldKoopa1Stage",
    "MoonWorldKoopa2Stage",
    "MoonWorldShopRoom",
    "MoonWorldSphinxRoom",
    "MoonWorldWeddingRoomStage",
    "Note2D3DRoomExStage",
    "PackunPoisonExStage",
    "PeachWorldCastleStage",
    "PeachWorldHomeStage",
    "PeachWorldPictureBossForestStage",
    "PeachWorldPictureBossKnuckleStage",
    "PeachWorldPictureBossMagmaStage",
    "PeachWorldPictureBossRaidStage",
    "PeachWorldPictureGiantWanderBossStage",
    "PeachWorldPictureMofumofuStage",
    "PeachWorldShopStage",
    "PoisonWaveExStage",
    "PoleKillerExStage",
    "PushBlockExStage",
    "RadioControlExStage",
    "RailCollisionExStage",
    "ReflectBombExStage",
    "RocketFlowerExStage",
    "RollingExStage",
    "SandWorldCostumeStage",
    "SandWorldHomeStage",
    "SandWorldKillerExStage",
    "SandWorldMeganeExStage",
    "SandWorldPressExStage",
    "SandWorldPyramid000Stage",
    "SandWorldPyramid001Stage",
    "SandWorldSecretStage",
    "SandWorldShopStage",
    "SandWorldSlotStage",
    "SandWorldSphinxExStage",
    "SandWorldUnderground000Stage",
    "SandWorldUnderground001Stage",
    "SandWorldVibrationStage",
    "SeaWorldCostumeStage",
    "SeaWorldHomeStage",
    "SeaWorldSecretStage",
    "SeaWorldSneakingManStage",
    "SeaWorldUtsuboCaveStage",
    "SeaWorldVibrationStage",
    "SenobiTowerExStage",
    "ShootingCityExStage",
    "ShootingElevatorExStage",
    "SkyWorldCloudBonusExStage",
    "SkyWorldCostumeStage",
    "SkyWorldHomeStage",
    "SkyWorldShopStage",
    "SkyWorldTreasureStage",
    "SnowWorldCloudBonusExStage",
    "SnowWorldCostumeStage",
    "SnowWorldHomeStage",
    "SnowWorldLobby000Stage",
    "SnowWorldLobbyExStage",
    "SnowWorldShopStage",
    "SnowWorldTownStage",
    "Special1WorldHomeStage",
    "Special1WorldTowerBombTailStage",
    "Special1WorldTowerCapThrowerStage",
    "Special1WorldTowerFireBlowerStage",
    "Special1WorldTowerStackerStage",
    "Special2WorldCloudStage",
    "Special2WorldHomeStage",
    "Special2WorldKoopaStage",
    "Special2WorldLavaStage",
    "SwingSteelExStage",
    "Theater2DExStage",
    "TogezoRotateExStage",
    "TrampolineWallCatchExStage",
    "TrexBikeExStage",
    "TrexPoppunExStage",
    "TsukkunClimbExStage",
    "TsukkunRotateExStage",
    "WanwanClashExStage",
    "WaterfallWorldHomeStage",
    "WaterTubeExStage",
    "WaterValleyExStage",
    "WindBlowExStage",
    "YoshiCloudExStage",
    'SandWorldRotateExStage',
    'FogMountainExStage',
    'PoleGrabCeilExStage',
    'CloudExStage',
    'LavaBonus1Zone',
    'DotTowerExStage',
    'BikeSteelNoCapExStage',
    'PackunPoisonNoCapExStage',
    'ShootingCityYoshiExStage',
    'SenobiTowerYoshiExStage',
    'LavaWorldUpDownYoshiExStage',
    'KillerRoadNoCapExStage',
    'RevengeBossMagmaStage',
    'RevengeMofumofuStage',
    'RevengeBossRaidStage',
    'RevengeForestBossStage',
    'RevengeBossKnuckleStage',
    'RevengeGiantWanderBossStage',
    'FukuwaraiMarioStage',
    'PeachWorldCostumeStage',
]

stage_ids = [
    'jizo01',
    'dot00',
    'start',
    'LavaWorldUpDownYoshiEx_Exit',
    'CapTrampolineB',
    'PoisonWaveExEnt',
    'arijigoku',
    'SeaWorldEX1a',
    'BossRaidWorldMoonEx02_Exit',
    'SeaWorldEX1b',
    'under001enter',
    'Tower002',
    'SeaWorldMoonEX1b',
    'Bonus',
    'None',
    'KeyMoveEx',
    'ShootingCityYoshiEx_Exit',
    'CP_Entrance',
    'PoisonEx_Exit',
    'donsuke',
    'cube',
    'pyramid03',
    'vvv',
    'EX_RailCollision_Exit',
    'main_enter',
    'boureturn',
    'moon',
    'pyramid02',
    'bar1',
    'FrogSearchExStageEnt',
    'FireBlowerRoomGoal',
    'MoonRace',
    'gunsyu',
    'Jyukai002',
    'LakeWorldMoonEX1b',
    'BBQExDokan',
    'BossKnuckleA',
    'Kinopio',
    'StackerRoomStart',
    'Tower001',
    'bbb',
    'aaa',
    'KeyMoveExDokan',
    'run00',
    'CostumeEventSeaWorld',
    'dot01',
    'bike02',
    'tukkun000_enter',
    'RaceEntrance',
    'SnowCostumeEx',
    'wall',
    'tukkun001_exit',
    'FenceLiftEx',
    'CostumeOut',
    'FenceLiftExdokan',
    'MofumofuA',
    'BBQEx',
    'WindBlowExStart',
    'Lift2D',
    'Fukuwarai',
    'LakeWorldMoonEX1a',
    'EXCloud',
    'SeaWorldMoonEX1a',
    'SenobiTowerYoshiEx_Exit',
    'Jyukai003',
    'BombTailRoomGoal',
    'EX_AnimalChase',
    'ForkEX',
    'town',
    'PeachWorldEx2a',
    'main_exit',
    'Goton',
    'CapAppearExEnt',
    'WanwanExStart',
    'bou',
    'Explorer_Bonus',
    'ddd',
    'EX_IceWaterDash',
    'abc',
    'CapAppearExExit',
    'BossRaidB',
    'jizo02',
    'LavaLiftEx',
    'EX_SkyBonus',
    'BikeSteelNoCapEx_Exit',
    'imomu_02',
    'meganelift02',
    'Jyukai001v',
    'ggg',
    'taxireturn',
    'shop_dress',
    'room2_start',
    'sora001',
    'TreasureEventWorldSea',
    'arijigoku2',
    'rocket',
    'CapTrampolineA',
    'EX_IceWater_Exit',
    'Jyukai001',
    'LakeWorldShop',
    'EX_RailCollision',
    'bonus',
    'kaitendokan',
    'shindo',
    'PushBlockExStageEnt',
    'pyramid01',
    'densendokan',
    'EX_RailCol2',
    'StackerRoomGoal',
    'Ex',
    'icestart',
    'PechoBubbleExDokan',
    'PechoBubbleEx',
    'onpu',
    'PeachWorldEx1a',
    'SeaWorldEX3b',
    'EX_Tankuro_Exit',
    'PackunPoisonNoCapEx_Exit',
    'SeaWorldMoonEX2',
    'meganelift01',
    'PushBlockExStageEntDokan',
    'GiantWanderBossA',
    'moon_exit',
    'Goal',
    'car',
    'bar2',
    'RaceTrackExit',
    'ShootingCityYoshiEx',
    'bike02return',
    'shindo_Lv2',
    'room2_goal',
    'EX_IceWater',
    'ShopDoor',
    'ByugoPuzzle',
    'EX_Water_Exit',
    'BombTailRoomStart',
    'taxi',
    'densen',
    'ClashWorldMoonEX2',
    'GabuzouClockEx',
    'MartinCubeEx',
    'FireBlowerRoomStart',
    'ccc',
    'PeachCastleGate',
    'SenobiTowerYoshiEx',
    'RexPoppunEx',
    'PukupukuCaveGoal',
    'tukkun001_enter',
    'gragrareturn',
    'EX_Water',
    'WanwanExGoal',
    'Lift2DExit',
    'theater',
    'Yadokari00',
    'BossForestA',
    'imomu_01',
    'PeachWorldShopA',
    'rollinggoal',
    'EX_2DHosui_Exit',
    'LavaLiftExdokan',
    'GabuzouClockExdokan',
    'anki2',
    'boss001',
    'FastenerEx',
    'FigureWalker',
    'shop',
    'CapThrowerRoomStart',
    'ForkEX2',
    'arijigoku1',
    'CapThrowerRoomGoal',
    'Jyukai003v',
    'HomeEntrance',
    'pyramid04',
    'doukutu2',
    'PoisonWaveExExit',
    'SnowUGEnt',
    'BossMagmaA',
    'KillerRoad',
    'PoisonEx',
    'BossRaidWorldMoonEx02_Enter',
    'bonus2',
    'SnowUGExit',
    'BossRaidA',
    'Jyukai004',
    'Out',
    'EX_IceWaterDash_Exit',
    'hide',
    'byoubu',
    'shop_coin',
    'fff',
    'bike',
    'PukupukuCaveStart',
    'boss002',
    'GiantWanderBossB',
    'MoonGoal',
    'Patakaron02',
    'doukutu1',
    'gunsyudokan',
    'room3_goal',
    'EX_2DHosui',
    'run00return',
    'WindBlowExGoal',
    'EX_Tankuro',
    'RoomEventWorldSea',
    'LavaWorldUpDownYoshiEx',
    'rollingstart',
    'bikereturn',
    'shop_corect',
    'EX_RailCol2_Exit',
    'Under01',
    'SeaWorldEX3a',
    'TreasureEventWorldLava',
    'TreasureTree',
    'CostumeEventWorldLava',
    'tukkun000_exit',
    'gragra',
    'PictureBossRaid',
    'PictureGiantWanderBoss',
    'biru',
    'birureturn',
    'EX_Mist',
    'tenjo',
    'tenjo2',
    'SeaWorldEX2',
    'BossRaidWorldEx01_Eixt',
    'BossRaidWorldEx01_Eixt2',
    'BikeSteelNoCapEx',
    'PackunPoisonNoCapEx',
    'KillerRoadNoCapEx',
    'PictureBossMagma',
    'PictureMofumofu',
    'PictureBossForest',
    'PictureBossKnuckle',
    'Fukuwarai2',
    'CostumeEventWorldPeach',
    'SeaWorldEX2Return',
]

def create_entrances(self):
    world_sub_area_exits = [
        (SMORegion.cap_kingdom_intro, {
            SMOEntrance.top_hat_tower: None,
        }),
        # (SMORegion.cap_kingdom_topper, {
        #     SMOEntrance.top_hat_tower_end: None,
        # }),
        (SMORegion.cap_kingdom, {
            SMOEntrance.push_blocks: None,
            SMOEntrance.poison_tides: None,
            SMOEntrance.frog_pond: None,
            SMOEntrance.rolling_lane: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.cap_kingdom_moon_rock, SMORuleOperation.NONE)
            ])),
        }),
        # (SMORegion.cap_kingdom_moon_rock, {}
        #
        # , SMORuleOperation.NONE)
        (SMORegion.cascade_kingdom_peace, {
            SMOEntrance.chasm_lifts: None,
            SMOEntrance.t_rex_nest: None,
            SMOEntrance.chain_chomp_cave: None,
            SMOEntrance.gusty_bridges: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.cascade_kingdom_moon_rock, SMORuleOperation.NONE)
                ])),
            SMOEntrance.mysterious_clouds: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.cascade_kingdom_moon_rock, SMORuleOperation.NONE)
                ])),
        }),
        # (SMORegion.cascade_kingdom_moon_rock, {
        #
        # }),
        (SMORegion.sand_kingdom, {
            SMOEntrance.ice_cave: None,
            SMOEntrance.bullet_bill_maze: None,
            SMOEntrance.jaxi_ruins: None,
            SMOEntrance.inverted_pyramid_lower_interior: None,
            SMOEntrance.moe_eye_invisible_maze: None,
            SMOEntrance.sand_kingdom_shop: None,
            SMOEntrance.sand_sphynx_vault: None,
            SMOEntrance.underground_ruins: None,
            SMOEntrance.sand_costume_bonus_dancing_room : (create_access_rule(self, [
                (SMORuleCondition.ITEM ,[SMOItemData.sombrero, SMOItemData.poncho], SMORuleOperation.OR),
                (SMORuleCondition.ITEM, [SMOItemData.skeleton_suit], SMORuleOperation.NONE)
            ])),
            SMOEntrance.sand_slots: None,
            SMOEntrance.sand_kingdom_employee: None,
            SMOEntrance.sand_rumbling_floor_house: None,
            SMOEntrance.deepest_underground_shortcut: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.sand_kingdom_peace, SMORuleOperation.NONE)
                ])),
            SMOEntrance.strange_neighborhood: (create_access_rule(self, [
                (SMORuleCondition.CAPTURE, [SMOItemData.mini_rocket], SMORuleOperation.AND),
                (SMORuleCondition.REGION, SMORegion.sand_kingdom_peace, SMORuleOperation.NONE)
                 ])),
            SMOEntrance.colossal_ruins: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.sand_kingdom_moon_rock, SMORuleOperation.NONE)
                ])),
            SMOEntrance.freezing_waterway: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.sand_kingdom_moon_rock, SMORuleOperation.NONE)
                ])),
            SMOEntrance.moe_eye_invisible_floor: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.sand_kingdom_moon_rock, SMORuleOperation.NONE)
                ])),
        }),
        # (SMORegion.sand_kingdom_peace, {
        #
        # }),
        (SMORegion.top_of_the_inverted_pyramid, {
            #SMOEntrance.inverted_pyramid_upper_interior_reverse: None,
        }),
        # (SMORegion.sand_kingdom_moon_rock, {
        #
        # }),
        (SMORegion.wooded_kingdom, {
            SMOEntrance.sky_garden_tower: None,
            SMOEntrance.deep_woods: None,
            SMOEntrance.flooding_pipeway: None,
            SMOEntrance.sherm_elevator: None,
            SMOEntrance.wooded_flower_road: None,
            SMOEntrance.secret_flower_field: (create_access_rule(self, [
                (SMORuleCondition.CAPTURE, SMOItemData.sherm, SMORuleOperation.AND),
                (SMORuleCondition.REGION, SMORegion.wooded_kingdom_post_broodals, SMORuleOperation.NONE)
            ])),
            SMOEntrance.spinning_platforms_treasure_vault: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.wooded_kingdom_post_broodals, SMORuleOperation.NONE)
                ])),
            SMOEntrance.walking_on_clouds: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.cascade_kingdom_moon_rock, SMORuleOperation.NONE)
                ])),
            SMOEntrance.fog_wandering: (create_access_rule(self, [
                (SMORuleCondition.CAPTURE, SMOItemData.mini_rocket, SMORuleOperation.AND),
                (SMORuleCondition.REGION, SMORegion.wooded_kingdom_peace, SMORuleOperation.NONE)
                ])),
            SMOEntrance.sheep_herding: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.wooded_kingdom_moon_rock, SMORuleOperation.NONE)
            ])),
            SMOEntrance.invisible_road: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.wooded_kingdom_moon_rock, SMORuleOperation.NONE)
                ])),
            SMOEntrance.breakdown_road: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.wooded_kingdom_moon_rock, SMORuleOperation.NONE)
                ])),
        }),
        # (SMORegion.wooded_kingdom_post_broodals, {
        #
        # }),
        # (SMORegion.wooded_kingdom_peace, {
        #     }),
        # (SMORegion.wooded_kingdom_moon_rock, {
        #
        # }),
        (SMORegion.deep_woods, {
            SMOEntrance.deep_woods_costume_bonus_treasure_chest: (create_access_rule( self, [
                (SMORuleCondition.ITEM, [SMOItemData.explorer_hat, SMOItemData.explorer_outfit], SMORuleOperation.NONE)
            ])),
            SMOEntrance.deep_woods_treasure_trap: None,
        }),
        (SMORegion.lake_kingdom, {
            SMOEntrance.arch_repair: None,
            SMOEntrance.zipper_chasm: (create_access_rule(self, [
                (SMORuleCondition.CAPTURE, [SMOItemData.zipper], SMORuleOperation.NONE)
            ])),
            SMOEntrance.bouncy_flowers: None,
            SMOEntrance.lake_kingdom_shop: None,
            SMOEntrance.poison_swamp: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.lake_kingdom_moon_rock, SMORuleOperation.NONE)
                ])),
        }),
        # (SMORegion.lake_kingdom_moon_rock, {
        #
        # }),
        (SMORegion.cloud_kingdom_revisit, {
            SMOEntrance.cloud_picture_match: None,
            SMOEntrance.king_of_the_cube: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.cloud_kingdom_moon_rock, SMORuleOperation.NONE)
                ])),
        }),
        # (SMORegion.cloud_kingdom_moon_rock, {
        #
        # }),
        (SMORegion.lost_kingdom, {
            SMOEntrance.lost_kingdom_shop: None,
            SMOEntrance.klepto_lava_bath: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.lost_kingdom_moon_rock, SMORuleOperation.NONE)
                ])),
            SMOEntrance.tropical_wiggler_swamp: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.lost_kingdom_moon_rock, SMORuleOperation.NONE)
                ])),
        }),
        # (SMORegion.lost_kingdom_moon_rock, {
        #
        # }),
        (SMORegion.night_metro_kingdom, {
            SMOEntrance.city_hall: None,
            SMOEntrance.metro_kingdom_shop: None,
            SMOEntrance.metro_kingdom_shop_regional: None,
            SMOEntrance.private_room: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.day_metro_kingdom, SMORuleOperation.NONE)
                ])),
            SMOEntrance.bullet_building: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.day_metro_kingdom, SMORuleOperation.NONE)
                ])),
            SMOEntrance.rc_race: (create_access_rule(self, [
                    (SMORuleCondition.CAPTURE, SMOItemData.rc_car, SMORuleOperation.AND),
                    (SMORuleCondition.REGION, SMORegion.day_metro_kingdom, SMORuleOperation.NONE)
                ])),
            SMOEntrance.builder_outfit: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.day_metro_kingdom, SMORuleOperation.AND),
                (SMORuleCondition.ITEM, [SMOItemData.builder_helmet, SMOItemData.builder_outfit], SMORuleOperation.NONE)
            ])),
            SMOEntrance.metro_slots: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.day_metro_kingdom, SMORuleOperation.NONE)
                ])),
            SMOEntrance.rotating_maze: (create_access_rule(self, [
                (SMORuleCondition.CAPTURE, SMOItemData.manhole, SMORuleOperation.AND),
                (SMORuleCondition.REGION, SMORegion.day_metro_kingdom, SMORuleOperation.NONE)
                ])),
            SMOEntrance.t_rex_escape: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.day_metro_kingdom, SMORuleOperation.NONE)
                ])),
            SMOEntrance.crowded_street: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.day_metro_kingdom, SMORuleOperation.NONE)
                ])),
            SMOEntrance.metro_siege: (create_access_rule(self, [
                (SMORuleCondition.CAPTURE, SMOItemData.taxi, SMORuleOperation.AND),
                (SMORuleCondition.REGION, SMORegion.day_metro_kingdom, SMORuleOperation.NONE)
                ])),
            SMOEntrance.high_rise: (create_access_rule(self, [
                (SMORuleCondition.CAPTURE, SMOItemData.mini_rocket, SMORuleOperation.AND),
                (SMORuleCondition.REGION, SMORegion.day_metro_kingdom, SMORuleOperation.NONE)
                ])),
            SMOEntrance.sewers: (create_access_rule(self, [
                    (SMORuleCondition.CAPTURE, SMOItemData.manhole, SMORuleOperation.AND),
                    (SMORuleCondition.REGION, SMORegion.day_metro_kingdom, SMORuleOperation.NONE)
                ])),
            SMOEntrance.projection_room: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.metro_kingdom_moon_rock, SMORuleOperation.NONE)
                ])),
            SMOEntrance.swinging_scaffolding: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.metro_kingdom_moon_rock, SMORuleOperation.NONE)
                ])),
            SMOEntrance.vanishing_road: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.metro_kingdom_moon_rock, SMORuleOperation.NONE)
                ])),
            SMOEntrance.pitch_black_island: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.metro_kingdom_moon_rock, SMORuleOperation.NONE)
                ])),
        }),
        # (SMORegion.day_metro_kingdom, {
        #     }),
        # (SMORegion.metro_kingdom_sewers, {
        #     SMOEntrance.sewers: None,
        # }),
        # (SMORegion.metro_kingdom_moon_rock, {
        #
        # }),
        (SMORegion.seaside_kingdom, {
            SMOEntrance.seaside_rumbling_floor_cave: None,
            SMOEntrance.spinning_maze: None,
            SMOEntrance.wading_in_the_cloud_sea: (create_access_rule(self, [
                (SMORuleCondition.CAPTURE, SMOItemData.mini_rocket, SMORuleOperation.NONE)
            ])),
            SMOEntrance.sandy_bottom: None,
            SMOEntrance.narrow_valley: None,
            SMOEntrance.sinking_island: None,
            SMOEntrance.seaside_costume_bonus_dancing_room: None,
            SMOEntrance.seaside_sphynx_treasure_vault: None,
            SMOEntrance.underwater_tunnel: None,
            SMOEntrance.pokio_bomb_aiming: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.seaside_kingdom_moon_rock, SMORuleOperation.NONE)
                ])),
        }),
        # (SMORegion.seaside_kingdom_moon_rock, {
        #
        # }),
        (SMORegion.snow_kingdom, {
            SMOEntrance.shiveria: None,
            SMOEntrance.rocket_flower_dash: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.snow_kingdom_peace, SMORuleOperation.NONE)
                ])),
            SMOEntrance.ty_foo_sliding_puzzle: (create_access_rule(self, [
                    (SMORuleCondition.CAPTURE, SMOItemData.ty_foo, SMORuleOperation.AND),
                    (SMORuleCondition.REGION ,SMORegion.snow_kingdom_peace, SMORuleOperation.NONE)
                ])),
            SMOEntrance.ice_trace_walking: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.snow_kingdom_peace, SMORuleOperation.NONE)
                ])),
            SMOEntrance.above_the_clouds: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.snow_kingdom_peace, SMORuleOperation.NONE)
                ])),
            SMOEntrance.freezing_water: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.snow_kingdom_peace, SMORuleOperation.NONE)
                ])),
            SMOEntrance.snow_flower_road: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.snow_kingdom_moon_rock, SMORuleOperation.NONE)
                ])),
            SMOEntrance.iceburn_circuit_class_a_lobby: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.snow_kingdom_moon_rock, SMORuleOperation.NONE)
                ])),
        }),
        # (SMORegion.snow_kingdom_peace, {
        #
        # }),
        # (SMORegion.snow_kingdom_moon_rock, {
        #
        # }),
        (SMORegion.luncheon_kingdom, {
            SMOEntrance.magma_swamp: None,
            SMOEntrance.fork_flickin: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.luncheon_kingdom_post_broodals, SMORuleOperation.NONE)
            ])),
            SMOEntrance.luncheon_kingdom_shop: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.luncheon_kingdom_post_broodals, SMORuleOperation.NONE)
            ])),
            SMOEntrance.luncheon_costume_bonus_cooking_pots: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.luncheon_kingdom_post_broodals, SMORuleOperation.AND),
                (SMORuleCondition.ITEM,[SMOItemData.chef_hat, SMOItemData.chef_suit], SMORuleOperation.NONE)
            ])),
            SMOEntrance.luncheon_slots: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.luncheon_kingdom_post_broodals, SMORuleOperation.NONE)
            ])),
            SMOEntrance.cheese_excavate: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.luncheon_kingdom_meat, SMORuleOperation.NONE)
            ])),
            SMOEntrance.spinning_athletics: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.luncheon_kingdom_meat, SMORuleOperation.NONE)
            ])),
            SMOEntrance.magma_narrow_path: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.luncheon_kingdom_meat, SMORuleOperation.NONE)
            ])),
            SMOEntrance.luncheon_treasure_vault: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.luncheon_kingdom_meat, SMORuleOperation.NONE)
            ])),
            SMOEntrance.volcano_cave: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.luncheon_kingdom_moon_rock, SMORuleOperation.NONE)
            ])),
            SMOEntrance.rotating_gears_with_bitefrost: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.luncheon_kingdom_moon_rock, SMORuleOperation.NONE)
            ])),
            SMOEntrance.lava_islands: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.luncheon_kingdom_moon_rock, SMORuleOperation.NONE)
            ])),
        }),
        # (SMORegion.luncheon_kingdom_post_broodals, {
        #
        # }),

        # (SMORegion.luncheon_kingdom_meat, {
        #
        # }),
        # (SMORegion.luncheon_kingdom_moon_rock, {
        #
        # }),
        (SMORegion.ruined_kingdom, {
            SMOEntrance.roulette_tower: (create_access_rule(self, [
                (SMORuleCondition.CAPTURE,[SMORegion.mini_rocket], SMORuleOperation.NONE)
            ])),
            SMOEntrance.chargin_chuck_arena: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.ruined_kingdom_moon_rock, SMORuleOperation.NONE)
            ])),
        }),
        # (SMORegion.ruined_kingdom_moon_rock, {
        #
        # }),
        (SMORegion.infiltrate_bowsers_castle, {
            SMOEntrance.bowsers_kingdom_shop: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.bowser_kingdom_smart_bombing, SMORuleOperation.NONE)
            ])),
            SMOEntrance.folding_screen: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.bowser_kingdom_smart_bombing, SMORuleOperation.AND),
                (SMORuleCondition.ITEM,[SMOItemData.samurai_helmet, SMOItemData.samurai_armor], SMORuleOperation.NONE)
            ])),
            SMOEntrance.dashing_above_the_clouds: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.bowser_kingdom_mecha_broodal, SMORuleOperation.NONE)
            ])),
            SMOEntrance.spinning_tower: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.bowser_kingdom_peace, SMORuleOperation.NONE)
            ])),
            SMOEntrance.jizos_adventure: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.bowser_kingdom_peace, SMORuleOperation.NONE)
            ])),
            SMOEntrance.bowsers_treasure_vault: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.bowser_kingdom_peace, SMORuleOperation.NONE)
            ])),
            SMOEntrance.hexagon_tower: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.bowser_kingdom_moon_rock, SMORuleOperation.NONE)
            ])),
            SMOEntrance.wooden_tower: (create_access_rule(self, [
                (SMORuleCondition.REGION, SMORegion.bowser_kingdom_moon_rock, SMORuleOperation.NONE)
            ])),
        }),
        # (SMORegion.bowser_kingdom_smart_bombing, {
        #     }),
        # (SMORegion.bowser_kingdom_mecha_broodal, {
        #
        # }),
        # (SMORegion.bowser_kingdom_peace, {
        #
        # }),
        # (SMORegion.bowser_kingdom_moon_rock, {
        #
        # }),
        (SMORegion.moon_kingdom, {
            SMOEntrance.inside_the_church: None,
            SMOEntrance.moon_cave: None,
        }),
        (SMORegion.moon_kingdom_peace, {
            SMOEntrance.moon_sphynx_vault: None,
            SMOEntrance.moon_kingdom_shop: None,
        }),
        (SMORegion.moon_kingdom_moon_rock, {
            SMOEntrance.giant_swings: None,
            SMOEntrance.dot_galaxy: None,
        }),
        (SMORegion.mushroom_kingdom, {
            SMOEntrance.peachs_castle: None,
            SMOEntrance.mushroom_kingdom_shop: None,
            SMOEntrance.painting_room_cookatiel: None,
            SMOEntrance.painting_room_mecha_wiggler: None,
            SMOEntrance.painting_room_knucklotec: None,
            SMOEntrance.painting_room_torkdrift: None,
            SMOEntrance.mushroom_well: None,
            SMOEntrance.yoshi_in_the_sea_of_clouds: (create_access_rule(self, [
                (SMORuleCondition.CAPTURE, SMOItemData.yoshi, SMORuleOperation.NONE)
            ])),
            SMOEntrance.painting_room_mollusque_lanceur: None,
            SMOEntrance.painting_room_lord_of_lightning: (create_access_rule(self, [
                (SMORuleCondition.CAPTURE, SMOItemData.yoshi, SMORuleOperation.NONE)
            ])),
            SMOEntrance.mushroom_picture_match : (create_access_rule(self, [
                (SMORuleCondition.CAPTURE, SMOItemData.mini_rocket, SMORuleOperation.NONE)
            ])),
            SMOEntrance.castle_courtyard : (create_access_rule(self, [
                (SMORuleCondition.ITEM, [SMOItemData.mario_64_cap, SMOItemData.mario_64_suit], SMORuleOperation.OR),
                (SMORuleCondition.ITEM, [SMOItemData.metal_mario_cap, SMOItemData.metal_mario_suit], SMORuleOperation.NONE)
            ])),
        }),
        (SMORegion.dark_side, {
            SMOEntrance.dark_side_topper: (create_access_rule(self, [
                (SMORuleCondition.CAPTURE, SMOItemData.spark_pylon, SMORuleOperation.NONE)
            ])),
            SMOEntrance.dark_side_vanishing_road: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.dark_side_peace, SMORuleOperation.NONE)
                ])),
            SMOEntrance.dark_side_invisible_road: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.dark_side_peace, SMORuleOperation.NONE)
                ])),
            SMOEntrance.dark_side_breakdown_road: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.dark_side_peace, SMORuleOperation.NONE)
                ])),
            SMOEntrance.dark_side_siege: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.dark_side_peace, SMORuleOperation.NONE)
                ])),
            SMOEntrance.dark_side_sinking_island: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.dark_side_peace, SMORuleOperation.NONE)
                ])),
            SMOEntrance.dark_side_magma_swamp: (create_access_rule(self, [
                (SMORuleCondition.REGION,SMORegion.dark_side_peace, SMORuleOperation.NONE)
                ])),
        }),
        (SMORegion.dark_side_2 , {
            SMOEntrance.dark_side_hariet: None,
        }),
        (SMORegion.dark_side_3 , {
            SMOEntrance.dark_side_spewart: None,
        }),
        (SMORegion.dark_side_4 , {
            SMOEntrance.dark_side_rango: None,
        }),

        # (SMORegion.dark_side_peace, {
        #
        # }),
        (SMORegion.darker_side, {
            SMOEntrance.darker_side_main: (create_access_rule(self, [
                (SMORuleCondition.CAPTURE, SMOItemData.frog, SMORuleOperation.NONE)
            ])),
        }),
        (SMORegion.darker_side_entrance, {
            SMOEntrance.darker_side_pokio: (create_access_rule(self, [
                (SMORuleCondition.CAPTURE, [SMOItemData.lava_bubble, SMOItemData.uproot, SMOItemData.yoshi, SMOItemData.glydon, SMOItemData.volbonan], SMORuleOperation.NONE)
            ])),
        }),
        (SMORegion.darker_side_climb, {
            SMOEntrance.darker_side_bowser: (create_access_rule(self, [
                (SMORuleCondition.CAPTURE, SMOItemData.pokio, SMORuleOperation.NONE)
            ])),
        }),
        (SMORegion.darker_side_bowser, {
            SMOEntrance.darker_side_end: (create_access_rule(self, [
                (SMORuleCondition.CAPTURE, SMOItemData.bowser, SMORuleOperation.NONE)
            ])),
        }),
        (SMORegion.darker_side_end, {
            SMOEntrance.darker_side_tower: (create_access_rule(self, [
                (SMORuleCondition.CAPTURE, SMOItemData.spark_pylon, SMORuleOperation.NONE)
            ])),
        }),

        # sub_areas
        # (SMORegion.top_hat_tower, {
        #     SMOEntrance.top_hat_tower_end: (create_access_rule(self, [
        #         (SMORuleCondition.CAPTURE, SMOItemData.frog , SMORuleOperation.NONE)
        #     ])),
        # }),

        (SMORegion.inverted_pyramid_lower_interior, {
            SMOEntrance.inverted_pyramid_mural: None,
        }),
        (SMORegion.inverted_pyramid_mural, {
            SMOEntrance.inverted_pyramid_upper_interior: None,
        }),
        (SMORegion.inverted_pyramid_upper_interior, {
            SMOEntrance.top_of_the_inverted_pyramid: None,
        }),
        (SMORegion.underground_ruins, {
            SMOEntrance.deepest_underground: (create_access_rule(self, [
                (SMORuleCondition.CAPTURE, [SMOItemData.bullet_bill, SMOItemData.knucklotecs_fist], SMORuleOperation.NONE)
            ])),
        }),


        (SMORegion.shiveria, {
            SMOEntrance.snowline_circuit_lobby: None,
            SMOEntrance.freezing_room: (create_access_rule(self, [
                (SMORuleCondition.ITEM, [SMOItemData.snow_hood, SMOItemData.snow_suit], SMORuleOperation.NONE)
            ])),
            SMOEntrance.snow_kingdom_shop: None,
        }),






        (SMORegion.painting_room_knucklotec, {
            SMOEntrance.knucklotec_rematch: None,
        }),
        (SMORegion.painting_room_torkdrift, {
            SMOEntrance.torkdrift_rematch: None,
        }),
        (SMORegion.painting_room_mecha_wiggler, {
            SMOEntrance.mecha_wiggler_rematch: None,
        }),
        (SMORegion.painting_room_mollusque_lanceur, {
            SMOEntrance.mollusque_lanceur_rematch: None,
        }),
        (SMORegion.painting_room_cookatiel, {
            SMOEntrance.cookatiel_rematch: None,
        }),
        (SMORegion.painting_room_lord_of_lightning, {
            SMOEntrance.lord_of_lightning_rematch: None,
        }),


        # (, {}),
        # (, {}),
        # (, {}),
        # (, {}),
    ]

    sub_area_coupled_entrances = [
        SMOEntrance.top_hat_tower,
        SMOEntrance.push_blocks,
        SMOEntrance.poison_tides,
        SMOEntrance.frog_pond,
        SMOEntrance.rolling_lane,
        SMOEntrance.chasm_lifts,
        SMOEntrance.t_rex_nest,
        SMOEntrance.chain_chomp_cave,
        SMOEntrance.gusty_bridges,
        SMOEntrance.mysterious_clouds,
        SMOEntrance.ice_cave,
        SMOEntrance.bullet_bill_maze,
        SMOEntrance.jaxi_ruins,
        SMOEntrance.inverted_pyramid_lower_interior,
        SMOEntrance.inverted_pyramid_mural,
        SMOEntrance.moe_eye_invisible_maze,
        SMOEntrance.sand_kingdom_shop,
        SMOEntrance.sand_sphynx_vault,
        SMOEntrance.underground_ruins,
        SMOEntrance.inverted_pyramid_upper_interior,
        SMOEntrance.deepest_underground,
        SMOEntrance.sand_rumbling_floor_house,
        SMOEntrance.strange_neighborhood,
        SMOEntrance.colossal_ruins,
        SMOEntrance.freezing_waterway,
        SMOEntrance.moe_eye_invisible_floor,
        SMOEntrance.sky_garden_tower,
        SMOEntrance.deep_woods,
        SMOEntrance.flooding_pipeway,
        SMOEntrance.sherm_elevator,
        SMOEntrance.wooded_flower_road,
        SMOEntrance.secret_flower_field,
        SMOEntrance.walking_on_clouds,
        SMOEntrance.fog_wandering,
        SMOEntrance.sheep_herding,
        SMOEntrance.invisible_road,
        SMOEntrance.breakdown_road,
        SMOEntrance.poison_swamp,
        SMOEntrance.cloud_picture_match,
        SMOEntrance.king_of_the_cube,
        SMOEntrance.lost_kingdom_shop,
        SMOEntrance.klepto_lava_bath,
        SMOEntrance.tropical_wiggler_swamp,
        SMOEntrance.city_hall,
        SMOEntrance.metro_kingdom_shop,
        SMOEntrance.metro_kingdom_shop_regional,
        SMOEntrance.private_room,
        SMOEntrance.bullet_building,
        SMOEntrance.rc_race,
        SMOEntrance.builder_outfit,
        SMOEntrance.metro_slots,
        SMOEntrance.rotating_maze,
        SMOEntrance.t_rex_escape,
        SMOEntrance.crowded_street,
        SMOEntrance.metro_siege,
        SMOEntrance.high_rise,
        SMOEntrance.sewers,
        SMOEntrance.projection_room,
        SMOEntrance.swinging_scaffolding,
        SMOEntrance.vanishing_road,
        SMOEntrance.pitch_black_island,
        SMOEntrance.seaside_rumbling_floor_cave,
        SMOEntrance.spinning_maze,
        SMOEntrance.wading_in_the_cloud_sea,
        SMOEntrance.pokio_bomb_aiming,
        SMOEntrance.rocket_flower_dash,
        SMOEntrance.shiveria,
        SMOEntrance.ty_foo_sliding_puzzle,
        SMOEntrance.ice_trace_walking,
        SMOEntrance.above_the_clouds,
        SMOEntrance.freezing_water,
        SMOEntrance.snow_flower_road,
        SMOEntrance.iceburn_circuit_class_a_lobby,
        SMOEntrance.fork_flickin,
        SMOEntrance.magma_swamp,
        SMOEntrance.cheese_excavate,
        SMOEntrance.spinning_athletics,
        SMOEntrance.magma_narrow_path,
        SMOEntrance.volcano_cave,
        SMOEntrance.rotating_gears_with_bitefrost,
        SMOEntrance.lava_islands,
        SMOEntrance.roulette_tower,
        SMOEntrance.chargin_chuck_arena,
        SMOEntrance.bowsers_kingdom_shop,
        SMOEntrance.inside_the_church,
        SMOEntrance.moon_cave,
        SMOEntrance.moon_sphynx_vault,
        SMOEntrance.moon_kingdom_shop,
        SMOEntrance.giant_swings,
        SMOEntrance.dot_galaxy,
        SMOEntrance.peachs_castle,
        SMOEntrance.mushroom_kingdom_shop,
        SMOEntrance.painting_room_cookatiel,
        SMOEntrance.painting_room_mecha_wiggler,
        SMOEntrance.painting_room_knucklotec,
        SMOEntrance.painting_room_torkdrift,
        SMOEntrance.mushroom_well,
        SMOEntrance.yoshi_in_the_sea_of_clouds,
        SMOEntrance.painting_room_mollusque_lanceur,
        SMOEntrance.painting_room_lord_of_lightning,
        SMOEntrance.mushroom_picture_match,
        SMOEntrance.dark_side_topper,
        SMOEntrance.dark_side_hariet,
        SMOEntrance.dark_side_spewart,
        SMOEntrance.dark_side_rango,
        SMOEntrance.dark_side_vanishing_road,
        SMOEntrance.dark_side_invisible_road,
        SMOEntrance.dark_side_siege,
        SMOEntrance.dark_side_sinking_island,
        SMOEntrance.dark_side_magma_swamp,
        SMOEntrance.darker_side_main,
        SMOEntrance.darker_side_pokio,
        SMOEntrance.darker_side_bowser,
        SMOEntrance.darker_side_end,
        SMOEntrance.darker_side_tower,
        SMOEntrance.luncheon_treasure_vault,
        SMOEntrance.snowline_circuit_lobby,
        SMOEntrance.sandy_bottom,
        SMOEntrance.sand_slots,
        SMOEntrance.sand_costume_bonus_dancing_room,
        SMOEntrance.sand_kingdom_employee,
        SMOEntrance.arch_repair,
        SMOEntrance.zipper_chasm,
        SMOEntrance.bouncy_flowers,
        SMOEntrance.seaside_costume_bonus_dancing_room,
        SMOEntrance.sinking_island,
        SMOEntrance.deep_woods_costume_bonus_treasure_chest,
        SMOEntrance.deep_woods_treasure_trap,
        SMOEntrance.spinning_platforms_treasure_vault,
        SMOEntrance.underwater_tunnel,
        SMOEntrance.seaside_sphynx_treasure_vault,
        SMOEntrance.narrow_valley,
        SMOEntrance.luncheon_costume_bonus_cooking_pots,
        SMOEntrance.luncheon_slots,
        SMOEntrance.folding_screen,
        SMOEntrance.dashing_above_the_clouds,
        SMOEntrance.bowsers_treasure_vault,
        SMOEntrance.jizos_adventure,
        SMOEntrance.spinning_tower,
        SMOEntrance.hexagon_tower,
        SMOEntrance.wooden_tower,
        SMOEntrance.castle_courtyard,
        SMOEntrance.knucklotec_rematch,
        SMOEntrance.torkdrift_rematch,
        SMOEntrance.mecha_wiggler_rematch,
        SMOEntrance.mollusque_lanceur_rematch,
        SMOEntrance.cookatiel_rematch,
        SMOEntrance.lord_of_lightning_rematch,
        SMOEntrance.freezing_room,
        SMOEntrance.dark_side_breakdown_road,
        SMOEntrance.deepest_underground_shortcut,
        SMOEntrance.lake_kingdom_shop,
        SMOEntrance.snow_kingdom_shop,
        SMOEntrance.luncheon_kingdom_shop,
        ]

    sub_area_unique_exits = [
        SMOEntrance.top_hat_tower,
        SMOEntrance.push_blocks,
        SMOEntrance.poison_tides,
        SMOEntrance.rolling_lane,
        SMOEntrance.chasm_lifts,
        SMOEntrance.chain_chomp_cave,
        SMOEntrance.gusty_bridges,
        SMOEntrance.mysterious_clouds,
        SMOEntrance.ice_cave,
        SMOEntrance.bullet_bill_maze,
        SMOEntrance.jaxi_ruins,
        SMOEntrance.inverted_pyramid_lower_interior,
        SMOEntrance.inverted_pyramid_mural,
        SMOEntrance.moe_eye_invisible_maze,
        SMOEntrance.underground_ruins,
        SMOEntrance.inverted_pyramid_upper_interior,
        SMOEntrance.strange_neighborhood,
        SMOEntrance.colossal_ruins,
        SMOEntrance.freezing_waterway,
        SMOEntrance.moe_eye_invisible_floor,
        SMOEntrance.sky_garden_tower,
        SMOEntrance.deep_woods,
        SMOEntrance.flooding_pipeway,
        SMOEntrance.sherm_elevator,
        SMOEntrance.wooded_flower_road,
        SMOEntrance.secret_flower_field,
        SMOEntrance.invisible_road,
        SMOEntrance.poison_swamp,
        SMOEntrance.tropical_wiggler_swamp,
        SMOEntrance.city_hall,
        # SMOEntrance.metro_kingdom_shop,
        SMOEntrance.bullet_building,
        SMOEntrance.builder_outfit,
        SMOEntrance.t_rex_escape,
        SMOEntrance.crowded_street,
        SMOEntrance.metro_siege,
        SMOEntrance.high_rise,
        SMOEntrance.swinging_scaffolding,
        SMOEntrance.vanishing_road,
       # SMOEntrance.spinning_maze # ?,
        SMOEntrance.wading_in_the_cloud_sea,
        SMOEntrance.pokio_bomb_aiming,
        SMOEntrance.rocket_flower_dash,
        SMOEntrance.shiveria,
        SMOEntrance.freezing_water,
        SMOEntrance.snow_flower_road,
        SMOEntrance.fork_flickin,
        SMOEntrance.magma_swamp,
        SMOEntrance.spinning_athletics,
        SMOEntrance.magma_narrow_path,
        SMOEntrance.volcano_cave,
        SMOEntrance.rotating_gears_with_bitefrost,
        SMOEntrance.lava_islands,
        SMOEntrance.roulette_tower,
        SMOEntrance.chargin_chuck_arena,
        SMOEntrance.moon_cave,
        SMOEntrance.giant_swings,
        SMOEntrance.dot_galaxy,
        SMOEntrance.painting_room_cookatiel,
        SMOEntrance.painting_room_mecha_wiggler,
        SMOEntrance.painting_room_knucklotec,
        SMOEntrance.painting_room_torkdrift,
        SMOEntrance.painting_room_mollusque_lanceur,
        SMOEntrance.painting_room_lord_of_lightning,
        SMOEntrance.dark_side_topper,
        SMOEntrance.dark_side_hariet,
        SMOEntrance.dark_side_spewart,
        SMOEntrance.dark_side_rango,
        SMOEntrance.dark_side_vanishing_road,
        SMOEntrance.dark_side_invisible_road,
        SMOEntrance.dark_side_siege,
        SMOEntrance.dark_side_sinking_island,
        SMOEntrance.dark_side_magma_swamp,
        SMOEntrance.darker_side_main,
        SMOEntrance.bouncy_flowers,
        SMOEntrance.sinking_island,
        SMOEntrance.spinning_platforms_treasure_vault, # ? oneway?,
        SMOEntrance.underwater_tunnel,
        SMOEntrance.narrow_valley,
        SMOEntrance.luncheon_costume_bonus_cooking_pots,
        SMOEntrance.jizos_adventure,
        SMOEntrance.spinning_tower,
        SMOEntrance.wooden_tower,
        SMOEntrance.deepest_underground_shortcut,
        # SMOEntrance.darker_side_pokio,
        # SMOEntrance.darker_side_bowser,
        # SMOEntrance.darker_side_end,
    ]

    return world_sub_area_exits, sub_area_coupled_entrances, sub_area_unique_exits