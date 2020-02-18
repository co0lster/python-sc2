# THIS FILE WAS AUTOMATICALLY GENERATED BY "generate_dicts_from_data_json.py" DO NOT CHANGE MANUALLY!
# ANY CHANGE WILL BE OVERWRITTEN

from ..ids.unit_typeid import UnitTypeId
from ..ids.ability_id import AbilityId
from ..ids.upgrade_id import UpgradeId

# from ..ids.buff_id import BuffId
# from ..ids.effect_id import EffectId

from typing import Dict, Set, Union

RESEARCH_INFO: Dict[
    UnitTypeId, Dict[UpgradeId, Dict[str, Union[AbilityId, bool, UnitTypeId]]]
] = {
    UnitTypeId.ARMORY: {
        UpgradeId.TERRANSHIPWEAPONSLEVEL1: {
            "ability": AbilityId.ARMORYRESEARCH_TERRANSHIPWEAPONSLEVEL1
        },
        UpgradeId.TERRANSHIPWEAPONSLEVEL2: {
            "ability": AbilityId.ARMORYRESEARCH_TERRANSHIPWEAPONSLEVEL2,
            "required_upgrade": UpgradeId.TERRANSHIPWEAPONSLEVEL1,
        },
        UpgradeId.TERRANSHIPWEAPONSLEVEL3: {
            "ability": AbilityId.ARMORYRESEARCH_TERRANSHIPWEAPONSLEVEL3,
            "required_upgrade": UpgradeId.TERRANSHIPWEAPONSLEVEL2,
        },
        UpgradeId.TERRANVEHICLEANDSHIPARMORSLEVEL1: {
            "ability": AbilityId.ARMORYRESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL1
        },
        UpgradeId.TERRANVEHICLEANDSHIPARMORSLEVEL2: {
            "ability": AbilityId.ARMORYRESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL2,
            "required_upgrade": UpgradeId.TERRANVEHICLEANDSHIPARMORSLEVEL1,
        },
        UpgradeId.TERRANVEHICLEANDSHIPARMORSLEVEL3: {
            "ability": AbilityId.ARMORYRESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL3,
            "required_upgrade": UpgradeId.TERRANVEHICLEANDSHIPARMORSLEVEL2,
        },
        UpgradeId.TERRANVEHICLEWEAPONSLEVEL1: {
            "ability": AbilityId.ARMORYRESEARCH_TERRANVEHICLEWEAPONSLEVEL1
        },
        UpgradeId.TERRANVEHICLEWEAPONSLEVEL2: {
            "ability": AbilityId.ARMORYRESEARCH_TERRANVEHICLEWEAPONSLEVEL2,
            "required_upgrade": UpgradeId.TERRANVEHICLEWEAPONSLEVEL1,
        },
        UpgradeId.TERRANVEHICLEWEAPONSLEVEL3: {
            "ability": AbilityId.ARMORYRESEARCH_TERRANVEHICLEWEAPONSLEVEL3,
            "required_upgrade": UpgradeId.TERRANVEHICLEWEAPONSLEVEL2,
        },
    },
    UnitTypeId.BANELINGNEST: {
        UpgradeId.CENTRIFICALHOOKS: {
            "ability": AbilityId.RESEARCH_CENTRIFUGALHOOKS,
            "required_building": UnitTypeId.LAIR,
        }
    },
    UnitTypeId.BARRACKSTECHLAB: {
        UpgradeId.PUNISHERGRENADES: {"ability": AbilityId.RESEARCH_CONCUSSIVESHELLS},
        UpgradeId.SHIELDWALL: {"ability": AbilityId.RESEARCH_COMBATSHIELD},
        UpgradeId.STIMPACK: {"ability": AbilityId.BARRACKSTECHLABRESEARCH_STIMPACK},
    },
    UnitTypeId.CYBERNETICSCORE: {
        UpgradeId.PROTOSSAIRARMORSLEVEL1: {
            "ability": AbilityId.CYBERNETICSCORERESEARCH_PROTOSSAIRARMORLEVEL1,
            "requires_power": True,
        },
        UpgradeId.PROTOSSAIRARMORSLEVEL2: {
            "ability": AbilityId.CYBERNETICSCORERESEARCH_PROTOSSAIRARMORLEVEL2,
            "required_building": UnitTypeId.FLEETBEACON,
            "required_upgrade": UpgradeId.PROTOSSAIRARMORSLEVEL1,
            "requires_power": True,
        },
        UpgradeId.PROTOSSAIRARMORSLEVEL3: {
            "ability": AbilityId.CYBERNETICSCORERESEARCH_PROTOSSAIRARMORLEVEL3,
            "required_building": UnitTypeId.FLEETBEACON,
            "required_upgrade": UpgradeId.PROTOSSAIRARMORSLEVEL2,
            "requires_power": True,
        },
        UpgradeId.PROTOSSAIRWEAPONSLEVEL1: {
            "ability": AbilityId.CYBERNETICSCORERESEARCH_PROTOSSAIRWEAPONSLEVEL1,
            "requires_power": True,
        },
        UpgradeId.PROTOSSAIRWEAPONSLEVEL2: {
            "ability": AbilityId.CYBERNETICSCORERESEARCH_PROTOSSAIRWEAPONSLEVEL2,
            "required_building": UnitTypeId.FLEETBEACON,
            "required_upgrade": UpgradeId.PROTOSSAIRWEAPONSLEVEL1,
            "requires_power": True,
        },
        UpgradeId.PROTOSSAIRWEAPONSLEVEL3: {
            "ability": AbilityId.CYBERNETICSCORERESEARCH_PROTOSSAIRWEAPONSLEVEL3,
            "required_building": UnitTypeId.FLEETBEACON,
            "required_upgrade": UpgradeId.PROTOSSAIRWEAPONSLEVEL2,
            "requires_power": True,
        },
        UpgradeId.WARPGATERESEARCH: {
            "ability": AbilityId.RESEARCH_WARPGATE,
            "requires_power": True,
        },
    },
    UnitTypeId.DARKSHRINE: {
        UpgradeId.DARKTEMPLARBLINKUPGRADE: {
            "ability": AbilityId.RESEARCH_SHADOWSTRIKE,
            "requires_power": True,
        }
    },
    UnitTypeId.ENGINEERINGBAY: {
        UpgradeId.HISECAUTOTRACKING: {"ability": AbilityId.RESEARCH_HISECAUTOTRACKING},
        UpgradeId.TERRANBUILDINGARMOR: {
            "ability": AbilityId.RESEARCH_TERRANSTRUCTUREARMORUPGRADE
        },
        UpgradeId.TERRANINFANTRYARMORSLEVEL1: {
            "ability": AbilityId.ENGINEERINGBAYRESEARCH_TERRANINFANTRYARMORLEVEL1
        },
        UpgradeId.TERRANINFANTRYARMORSLEVEL2: {
            "ability": AbilityId.ENGINEERINGBAYRESEARCH_TERRANINFANTRYARMORLEVEL2,
            "required_building": UnitTypeId.ARMORY,
            "required_upgrade": UpgradeId.TERRANINFANTRYARMORSLEVEL1,
        },
        UpgradeId.TERRANINFANTRYARMORSLEVEL3: {
            "ability": AbilityId.ENGINEERINGBAYRESEARCH_TERRANINFANTRYARMORLEVEL3,
            "required_building": UnitTypeId.ARMORY,
            "required_upgrade": UpgradeId.TERRANINFANTRYARMORSLEVEL2,
        },
        UpgradeId.TERRANINFANTRYWEAPONSLEVEL1: {
            "ability": AbilityId.ENGINEERINGBAYRESEARCH_TERRANINFANTRYWEAPONSLEVEL1
        },
        UpgradeId.TERRANINFANTRYWEAPONSLEVEL2: {
            "ability": AbilityId.ENGINEERINGBAYRESEARCH_TERRANINFANTRYWEAPONSLEVEL2,
            "required_building": UnitTypeId.ARMORY,
            "required_upgrade": UpgradeId.TERRANINFANTRYWEAPONSLEVEL1,
        },
        UpgradeId.TERRANINFANTRYWEAPONSLEVEL3: {
            "ability": AbilityId.ENGINEERINGBAYRESEARCH_TERRANINFANTRYWEAPONSLEVEL3,
            "required_building": UnitTypeId.ARMORY,
            "required_upgrade": UpgradeId.TERRANINFANTRYWEAPONSLEVEL2,
        },
    },
    UnitTypeId.EVOLUTIONCHAMBER: {
        UpgradeId.ZERGGROUNDARMORSLEVEL1: {
            "ability": AbilityId.RESEARCH_ZERGGROUNDARMORLEVEL1
        },
        UpgradeId.ZERGGROUNDARMORSLEVEL2: {
            "ability": AbilityId.RESEARCH_ZERGGROUNDARMORLEVEL2,
            "required_building": UnitTypeId.LAIR,
            "required_upgrade": UpgradeId.ZERGGROUNDARMORSLEVEL1,
        },
        UpgradeId.ZERGGROUNDARMORSLEVEL3: {
            "ability": AbilityId.RESEARCH_ZERGGROUNDARMORLEVEL3,
            "required_building": UnitTypeId.HIVE,
            "required_upgrade": UpgradeId.ZERGGROUNDARMORSLEVEL2,
        },
        UpgradeId.ZERGMELEEWEAPONSLEVEL1: {
            "ability": AbilityId.RESEARCH_ZERGMELEEWEAPONSLEVEL1
        },
        UpgradeId.ZERGMELEEWEAPONSLEVEL2: {
            "ability": AbilityId.RESEARCH_ZERGMELEEWEAPONSLEVEL2,
            "required_building": UnitTypeId.LAIR,
            "required_upgrade": UpgradeId.ZERGMELEEWEAPONSLEVEL1,
        },
        UpgradeId.ZERGMELEEWEAPONSLEVEL3: {
            "ability": AbilityId.RESEARCH_ZERGMELEEWEAPONSLEVEL3,
            "required_building": UnitTypeId.HIVE,
            "required_upgrade": UpgradeId.ZERGMELEEWEAPONSLEVEL2,
        },
        UpgradeId.ZERGMISSILEWEAPONSLEVEL1: {
            "ability": AbilityId.RESEARCH_ZERGMISSILEWEAPONSLEVEL1
        },
        UpgradeId.ZERGMISSILEWEAPONSLEVEL2: {
            "ability": AbilityId.RESEARCH_ZERGMISSILEWEAPONSLEVEL2,
            "required_building": UnitTypeId.LAIR,
            "required_upgrade": UpgradeId.ZERGMISSILEWEAPONSLEVEL1,
        },
        UpgradeId.ZERGMISSILEWEAPONSLEVEL3: {
            "ability": AbilityId.RESEARCH_ZERGMISSILEWEAPONSLEVEL3,
            "required_building": UnitTypeId.HIVE,
            "required_upgrade": UpgradeId.ZERGMISSILEWEAPONSLEVEL2,
        },
    },
    UnitTypeId.FACTORYTECHLAB: {
        UpgradeId.CYCLONELOCKONDAMAGEUPGRADE: {
            "ability": AbilityId.RESEARCH_CYCLONELOCKONDAMAGE
        },
        UpgradeId.DRILLCLAWS: {
            "ability": AbilityId.RESEARCH_DRILLINGCLAWS,
            "required_building": UnitTypeId.ARMORY,
        },
        UpgradeId.HIGHCAPACITYBARRELS: {
            "ability": AbilityId.RESEARCH_INFERNALPREIGNITER
        },
        UpgradeId.SMARTSERVOS: {
            "ability": AbilityId.RESEARCH_SMARTSERVOS,
            "required_building": UnitTypeId.ARMORY,
        },
    },
    UnitTypeId.FLEETBEACON: {
        UpgradeId.PHOENIXRANGEUPGRADE: {
            "ability": AbilityId.RESEARCH_PHOENIXANIONPULSECRYSTALS,
            "requires_power": True,
        },
        UpgradeId.VOIDRAYSPEEDUPGRADE: {
            "ability": AbilityId.FLEETBEACONRESEARCH_RESEARCHVOIDRAYSPEEDUPGRADE,
            "requires_power": True,
        },
    },
    UnitTypeId.FORGE: {
        UpgradeId.PROTOSSGROUNDARMORSLEVEL1: {
            "ability": AbilityId.FORGERESEARCH_PROTOSSGROUNDARMORLEVEL1,
            "requires_power": True,
        },
        UpgradeId.PROTOSSGROUNDARMORSLEVEL2: {
            "ability": AbilityId.FORGERESEARCH_PROTOSSGROUNDARMORLEVEL2,
            "required_building": UnitTypeId.TWILIGHTCOUNCIL,
            "required_upgrade": UpgradeId.PROTOSSGROUNDARMORSLEVEL1,
            "requires_power": True,
        },
        UpgradeId.PROTOSSGROUNDARMORSLEVEL3: {
            "ability": AbilityId.FORGERESEARCH_PROTOSSGROUNDARMORLEVEL3,
            "required_building": UnitTypeId.TWILIGHTCOUNCIL,
            "required_upgrade": UpgradeId.PROTOSSGROUNDARMORSLEVEL2,
            "requires_power": True,
        },
        UpgradeId.PROTOSSGROUNDWEAPONSLEVEL1: {
            "ability": AbilityId.FORGERESEARCH_PROTOSSGROUNDWEAPONSLEVEL1,
            "requires_power": True,
        },
        UpgradeId.PROTOSSGROUNDWEAPONSLEVEL2: {
            "ability": AbilityId.FORGERESEARCH_PROTOSSGROUNDWEAPONSLEVEL2,
            "required_building": UnitTypeId.TWILIGHTCOUNCIL,
            "required_upgrade": UpgradeId.PROTOSSGROUNDWEAPONSLEVEL1,
            "requires_power": True,
        },
        UpgradeId.PROTOSSGROUNDWEAPONSLEVEL3: {
            "ability": AbilityId.FORGERESEARCH_PROTOSSGROUNDWEAPONSLEVEL3,
            "required_building": UnitTypeId.TWILIGHTCOUNCIL,
            "required_upgrade": UpgradeId.PROTOSSGROUNDWEAPONSLEVEL2,
            "requires_power": True,
        },
        UpgradeId.PROTOSSSHIELDSLEVEL1: {
            "ability": AbilityId.FORGERESEARCH_PROTOSSSHIELDSLEVEL1,
            "requires_power": True,
        },
        UpgradeId.PROTOSSSHIELDSLEVEL2: {
            "ability": AbilityId.FORGERESEARCH_PROTOSSSHIELDSLEVEL2,
            "required_building": UnitTypeId.TWILIGHTCOUNCIL,
            "required_upgrade": UpgradeId.PROTOSSSHIELDSLEVEL1,
            "requires_power": True,
        },
        UpgradeId.PROTOSSSHIELDSLEVEL3: {
            "ability": AbilityId.FORGERESEARCH_PROTOSSSHIELDSLEVEL3,
            "required_building": UnitTypeId.TWILIGHTCOUNCIL,
            "required_upgrade": UpgradeId.PROTOSSSHIELDSLEVEL2,
            "requires_power": True,
        },
    },
    UnitTypeId.FUSIONCORE: {
        UpgradeId.BATTLECRUISERENABLESPECIALIZATIONS: {
            "ability": AbilityId.RESEARCH_BATTLECRUISERWEAPONREFIT
        },
        UpgradeId.LIBERATORAGRANGEUPGRADE: {
            "ability": AbilityId.FUSIONCORERESEARCH_RESEARCHBALLISTICRANGE
        },
        UpgradeId.MEDIVACINCREASESPEEDBOOST: {
            "ability": AbilityId.FUSIONCORERESEARCH_RESEARCHRAPIDREIGNITIONSYSTEM
        },
    },
    UnitTypeId.GHOSTACADEMY: {
        UpgradeId.ENHANCEDSHOCKWAVES: {
            "ability": AbilityId.GHOSTACADEMYRESEARCH_RESEARCHENHANCEDSHOCKWAVES
        },
        UpgradeId.PERSONALCLOAKING: {"ability": AbilityId.RESEARCH_PERSONALCLOAKING},
    },
    UnitTypeId.GREATERSPIRE: {
        UpgradeId.ZERGFLYERARMORSLEVEL1: {
            "ability": AbilityId.RESEARCH_ZERGFLYERARMORLEVEL1
        },
        UpgradeId.ZERGFLYERARMORSLEVEL2: {
            "ability": AbilityId.RESEARCH_ZERGFLYERARMORLEVEL2,
            "required_building": UnitTypeId.LAIR,
            "required_upgrade": UpgradeId.ZERGFLYERARMORSLEVEL1,
        },
        UpgradeId.ZERGFLYERARMORSLEVEL3: {
            "ability": AbilityId.RESEARCH_ZERGFLYERARMORLEVEL3,
            "required_building": UnitTypeId.HIVE,
            "required_upgrade": UpgradeId.ZERGFLYERARMORSLEVEL2,
        },
        UpgradeId.ZERGFLYERWEAPONSLEVEL1: {
            "ability": AbilityId.RESEARCH_ZERGFLYERATTACKLEVEL1
        },
        UpgradeId.ZERGFLYERWEAPONSLEVEL2: {
            "ability": AbilityId.RESEARCH_ZERGFLYERATTACKLEVEL2,
            "required_building": UnitTypeId.LAIR,
            "required_upgrade": UpgradeId.ZERGFLYERWEAPONSLEVEL1,
        },
        UpgradeId.ZERGFLYERWEAPONSLEVEL3: {
            "ability": AbilityId.RESEARCH_ZERGFLYERATTACKLEVEL3,
            "required_building": UnitTypeId.HIVE,
            "required_upgrade": UpgradeId.ZERGFLYERWEAPONSLEVEL2,
        },
    },
    UnitTypeId.HATCHERY: {
        UpgradeId.BURROW: {"ability": AbilityId.RESEARCH_BURROW},
        UpgradeId.OVERLORDSPEED: {"ability": AbilityId.RESEARCH_PNEUMATIZEDCARAPACE},
    },
    UnitTypeId.HIVE: {
        UpgradeId.BURROW: {"ability": AbilityId.RESEARCH_BURROW},
        UpgradeId.OVERLORDSPEED: {"ability": AbilityId.RESEARCH_PNEUMATIZEDCARAPACE},
    },
    UnitTypeId.HYDRALISKDEN: {
        UpgradeId.EVOLVEGROOVEDSPINES: {"ability": AbilityId.RESEARCH_GROOVEDSPINES},
        UpgradeId.EVOLVEMUSCULARAUGMENTS: {
            "ability": AbilityId.RESEARCH_MUSCULARAUGMENTS
        },
    },
    UnitTypeId.INFESTATIONPIT: {
        UpgradeId.INFESTORENERGYUPGRADE: {"ability": AbilityId.RESEARCH_PATHOGENGLANDS},
        UpgradeId.MICROBIALSHROUD: {
            "ability": AbilityId.INFESTATIONPITRESEARCH_EVOLVEAMORPHOUSARMORCLOUD
        },
        UpgradeId.NEURALPARASITE: {"ability": AbilityId.RESEARCH_NEURALPARASITE},
    },
    UnitTypeId.LAIR: {
        UpgradeId.BURROW: {"ability": AbilityId.RESEARCH_BURROW},
        UpgradeId.OVERLORDSPEED: {"ability": AbilityId.RESEARCH_PNEUMATIZEDCARAPACE},
    },
    UnitTypeId.LURKERDENMP: {
        UpgradeId.DIGGINGCLAWS: {
            "ability": AbilityId.RESEARCH_ADAPTIVETALONS,
            "required_building": UnitTypeId.HIVE,
        },
        UpgradeId.LURKERRANGE: {
            "ability": AbilityId.LURKERDENRESEARCH_RESEARCHLURKERRANGE,
            "required_building": UnitTypeId.HIVE,
        },
    },
    UnitTypeId.ROACHWARREN: {
        UpgradeId.GLIALRECONSTITUTION: {
            "ability": AbilityId.RESEARCH_GLIALREGENERATION,
            "required_building": UnitTypeId.LAIR,
        },
        UpgradeId.TUNNELINGCLAWS: {
            "ability": AbilityId.RESEARCH_TUNNELINGCLAWS,
            "required_building": UnitTypeId.LAIR,
        },
    },
    UnitTypeId.ROBOTICSBAY: {
        UpgradeId.EXTENDEDTHERMALLANCE: {
            "ability": AbilityId.RESEARCH_EXTENDEDTHERMALLANCE,
            "requires_power": True,
        },
        UpgradeId.GRAVITICDRIVE: {
            "ability": AbilityId.RESEARCH_GRAVITICDRIVE,
            "requires_power": True,
        },
        UpgradeId.OBSERVERGRAVITICBOOSTER: {
            "ability": AbilityId.RESEARCH_GRAVITICBOOSTER,
            "requires_power": True,
        },
    },
    UnitTypeId.SPAWNINGPOOL: {
        UpgradeId.ZERGLINGATTACKSPEED: {
            "ability": AbilityId.RESEARCH_ZERGLINGADRENALGLANDS,
            "required_building": UnitTypeId.HIVE,
        },
        UpgradeId.ZERGLINGMOVEMENTSPEED: {
            "ability": AbilityId.RESEARCH_ZERGLINGMETABOLICBOOST
        },
    },
    UnitTypeId.SPIRE: {
        UpgradeId.ZERGFLYERARMORSLEVEL1: {
            "ability": AbilityId.RESEARCH_ZERGFLYERARMORLEVEL1
        },
        UpgradeId.ZERGFLYERARMORSLEVEL2: {
            "ability": AbilityId.RESEARCH_ZERGFLYERARMORLEVEL2,
            "required_building": UnitTypeId.LAIR,
            "required_upgrade": UpgradeId.ZERGFLYERARMORSLEVEL1,
        },
        UpgradeId.ZERGFLYERARMORSLEVEL3: {
            "ability": AbilityId.RESEARCH_ZERGFLYERARMORLEVEL3,
            "required_building": UnitTypeId.HIVE,
            "required_upgrade": UpgradeId.ZERGFLYERARMORSLEVEL2,
        },
        UpgradeId.ZERGFLYERWEAPONSLEVEL1: {
            "ability": AbilityId.RESEARCH_ZERGFLYERATTACKLEVEL1
        },
        UpgradeId.ZERGFLYERWEAPONSLEVEL2: {
            "ability": AbilityId.RESEARCH_ZERGFLYERATTACKLEVEL2,
            "required_building": UnitTypeId.LAIR,
            "required_upgrade": UpgradeId.ZERGFLYERWEAPONSLEVEL1,
        },
        UpgradeId.ZERGFLYERWEAPONSLEVEL3: {
            "ability": AbilityId.RESEARCH_ZERGFLYERATTACKLEVEL3,
            "required_building": UnitTypeId.HIVE,
            "required_upgrade": UpgradeId.ZERGFLYERWEAPONSLEVEL2,
        },
    },
    UnitTypeId.STARPORTTECHLAB: {
        UpgradeId.BANSHEECLOAK: {"ability": AbilityId.RESEARCH_BANSHEECLOAKINGFIELD},
        UpgradeId.BANSHEESPEED: {
            "ability": AbilityId.RESEARCH_BANSHEEHYPERFLIGHTROTORS
        },
        UpgradeId.RAVENCORVIDREACTOR: {
            "ability": AbilityId.RESEARCH_RAVENCORVIDREACTOR
        },
    },
    UnitTypeId.TEMPLARARCHIVE: {
        UpgradeId.PSISTORMTECH: {
            "ability": AbilityId.RESEARCH_PSISTORM,
            "requires_power": True,
        }
    },
    UnitTypeId.TWILIGHTCOUNCIL: {
        UpgradeId.ADEPTPIERCINGATTACK: {
            "ability": AbilityId.RESEARCH_ADEPTRESONATINGGLAIVES,
            "requires_power": True,
        },
        UpgradeId.BLINKTECH: {
            "ability": AbilityId.RESEARCH_BLINK,
            "requires_power": True,
        },
        UpgradeId.CHARGE: {
            "ability": AbilityId.RESEARCH_CHARGE,
            "requires_power": True,
        },
    },
    UnitTypeId.ULTRALISKCAVERN: {
        UpgradeId.ANABOLICSYNTHESIS: {"ability": AbilityId.RESEARCH_ANABOLICSYNTHESIS},
        UpgradeId.CHITINOUSPLATING: {"ability": AbilityId.RESEARCH_CHITINOUSPLATING},
    },
}
