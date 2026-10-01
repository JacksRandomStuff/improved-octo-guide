import json

OUTPUT_FILE = "music_definitions.json"

DEFAULT_EVENT_NAME = "music.overworld"
DEEP_DARK_EVENT_NAME = "music.deep_dark"

BIOMES = [
    "minecraft:ocean",
    "minecraft:plains",
    "minecraft:desert",
    "minecraft:mountains",
    "minecraft:forest",
    "minecraft:taiga",
    "minecraft:swamp",
    "minecraft:river",
    "minecraft:nether_wastes",
    "minecraft:the_end",
    "minecraft:frozen_ocean",
    "minecraft:frozen_river",
    "minecraft:snowy_tundra",
    "minecraft:snowy_mountains",
    "minecraft:mushroom_fields",
    "minecraft:mushroom_island",
    "minecraft:beach",
    "minecraft:jungle",
    "minecraft:deep_ocean",
    "minecraft:stone_shore",
    "minecraft:snowy_beach",
    "minecraft:birch_forest",
    "minecraft:dark_forest",
    "minecraft:snowy_taiga",
    "minecraft:giant_tree_taiga",
    "minecraft:savanna",
    "minecraft:savanna_plateau",
    "minecraft:badlands",
    "minecraft:end_midlands",
    "minecraft:end_highlands",
    "minecraft:end_barrens",
    "minecraft:warm_ocean",
    "minecraft:lukewarm_ocean",
    "minecraft:cold_ocean",
    "minecraft:deep_warm_ocean",
    "minecraft:deep_lukewarm_ocean",
    "minecraft:deep_cold_ocean",
    "minecraft:deep_frozen_ocean",
    "minecraft:wooded_badlands",
    "minecraft:bamboo_jungle",
    "minecraft:soul_sand_valley",
    "minecraft:crimson_forest",
    "minecraft:warped_forest",
    "minecraft:basalt_deltas",
    "minecraft:dripstone_caves",
    "minecraft:lush_caves",
    "minecraft:meadow",
    "minecraft:grove",
    "minecraft:snowy_slopes",
    "minecraft:jagged_peaks",
    "minecraft:frozen_peaks",
    "minecraft:stony_peaks",
    "minecraft:cherry_grove",
    "minecraft:deep_dark",
    "minecraft:mangrove_swamp",
    "minecraft:eroded_badlands",
    "minecraft:windswept_hills",
    "minecraft:windswept_forest",
    "minecraft:windswept_gravelly_hills",
    "minecraft:windswept_savanna",
    "minecraft:old_growth_birch_forest",
    "minecraft:old_growth_pine_taiga",
    "minecraft:old_growth_spruce_taiga",
    "minecraft:snowy_plains",
    "minecraft:ice_spikes",
    "minecraft:flower_forest",
    "minecraft:stony_shore",
]

music_definitions = {}

for biome in BIOMES:
    event_name = (
        DEEP_DARK_EVENT_NAME
        if biome == "minecraft:deep_dark"
        else DEFAULT_EVENT_NAME
    )

    music_definitions[biome] = {
        "event_name": event_name,
        "min_delay": 0,
        "max_delay": 0
    }

output = {
    "music_definitions": music_definitions
}

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(output, file, indent=2)

print(f"Created {OUTPUT_FILE}")
print(f"Generated {len(BIOMES)} biome definitions.")
