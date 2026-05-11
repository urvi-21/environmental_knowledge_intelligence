import re


# ----------------------------------------
# ENVIRONMENTAL / DOMAIN KEYWORDS
# ----------------------------------------

ENVIRONMENTAL_KEYWORDS = [

    # ----------------------------------------
    # CLIMATE & ATMOSPHERE
    # ----------------------------------------

    "climate",
    "temperature",
    "global warming",
    "warming",
    "greenhouse",
    "greenhouse gases",
    "carbon",
    "carbon dioxide",
    "co2",
    "methane",
    "nitrous oxide",
    "emissions",
    "atmosphere",
    "aerosol",
    "radiation",
    "heatwave",
    "air quality",
    "ozone",
    "precipitation",
    "rainfall",
    "drought",
    "flood",

    # ----------------------------------------
    # HYDROLOGY & WATER SYSTEMS
    # ----------------------------------------

    "hydrology",
    "watershed",
    "water",
    "surface water",
    "groundwater",
    "streamflow",
    "runoff",
    "river basin",
    "catchment",
    "evapotranspiration",
    "water quality",
    "soil moisture",

    # ----------------------------------------
    # REMOTE SENSING & GEOSPATIAL
    # ----------------------------------------

    "remote sensing",
    "satellite",
    "earth observation",
    "gis",
    "gee",
    "landsat",
    "sentinel",
    "modis",
    "spatial",
    "raster",
    "pixel",
    "time series",

    # ----------------------------------------
    # LAND & ECOLOGY
    # ----------------------------------------

    "vegetation",
    "ndvi",
    "forest",
    "ecosystem",
    "biodiversity",
    "land degradation",
    "land cover",
    "land use",
    "soil erosion",
    "desertification",
    "deforestation",
    "urbanization",
    "ecological",
    "habitat",
    "sustainability",
    "pollution"
]


# ----------------------------------------
# DOMAIN RELEVANCE SCORE
# ----------------------------------------

def environmental_score(chunk):

    chunk_lower = chunk.lower()

    score = 0

    matched_keywords = []

    for keyword in ENVIRONMENTAL_KEYWORDS:

        if keyword in chunk_lower:

            score += 1

            matched_keywords.append(keyword)

    # ----------------------------------------
    # NORMALIZE SCORE
    # ----------------------------------------

    score = min(score, 5)

    return score


# ----------------------------------------
# SCIENTIFIC DENSITY SCORE
# ----------------------------------------

def scientific_density_score(chunk):

    # ----------------------------------------
    # NUMERICAL VALUES
    # ----------------------------------------

    numbers = re.findall(
        r'\d+\.?\d*',
        chunk
    )

    # ----------------------------------------
    # SCIENTIFIC TERMS
    # ----------------------------------------

    scientific_terms = [

        "increase",
        "decrease",
        "percentage",
        "temperature",
        "co2",
        "warming",
        "emissions",
        "measurement",
        "satellite",
        "observation",
        "trend",
        "model",
        "simulation",
        "analysis",
        "scientific",
        "dataset",
        "climate",
        "greenhouse",
        "carbon",
        "methane",
        "hydrology",
        "remote sensing",
        "spatial",
        "environmental",
        "monitoring",
        "prediction",
        "forecasting"
    ]

    score = len(numbers)

    chunk_lower = chunk.lower()

    for term in scientific_terms:

        if term in chunk_lower:

            score += 1

    # ----------------------------------------
    # NORMALIZE SCORE
    # ----------------------------------------

    score = min(score, 5)

    return score