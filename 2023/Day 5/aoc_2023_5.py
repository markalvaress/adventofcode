import numpy as np

almanac_file = open("input.txt", "r")
almanac = almanac_file.read()
almanac_file.close()

almanac_split = almanac.splitlines()

def create_mapping_function(domain, image):
    """
    Given a set of subdomains and a set of images (i.e. lists of ranges), returns a function of x that 
    matches everything in domain with image, and everything outside the domain with itself.
    """

    def f(x):
        x_in_domain = [x in domain[i] for i in range(len(domain))]

        # index() returns an error if True is not present, so this is essentially an if(*no error*)
        # if the number is nowhere in the stated domains then we return itself
        try:
            location_of_dom_and_image = x_in_domain.index(True)
        except:
            return(x)
        
        domain_subset = domain[location_of_dom_and_image]
        #print(f"Input was found in the following subdomain: {domain_subset}")
        image_subset = image[location_of_dom_and_image]        

        value = (x - domain_subset.start) + image_subset.start
        return(value)

    return(f)

def create_domain_and_image(almanac_subsection):
    domain = []
    image = []

    for line in almanac_subsection:
        img_start, domain_start, img_length = [int(i) for i in line.split(" ")]

        domain.append(range(domain_start, domain_start + img_length))
        image.append(range(img_start, img_start + img_length))

    return(domain, image)

# Given the small amount of separate funs, I think easiest to just manually state the location of each almanac subsection
seed_to_soil_almanac = almanac_split[3:40]
soil_to_fert_almanac = almanac_split[42:52]
fert_to_water_almanac = almanac_split[54:90]
water_to_light_almanac = almanac_split[92:138]
light_to_temp_almanac = almanac_split[140:168]
temp_to_hum_almanac = almanac_split[170:210]
hum_to_loc_almanac = almanac_split[212:254]

seed_to_soil = create_mapping_function(*create_domain_and_image(seed_to_soil_almanac)) # i could incorporate create_domain... into create_mapping_function, but I think it's clearer this way 
soil_to_fert = create_mapping_function(*create_domain_and_image(soil_to_fert_almanac))
fert_to_water = create_mapping_function(*create_domain_and_image(fert_to_water_almanac))
water_to_light = create_mapping_function(*create_domain_and_image(water_to_light_almanac))
light_to_temp = create_mapping_function(*create_domain_and_image(light_to_temp_almanac))
temp_to_hum = create_mapping_function(*create_domain_and_image(temp_to_hum_almanac))
hum_to_loc = create_mapping_function(*create_domain_and_image(hum_to_loc_almanac))

def seed_to_loc(seed):
    soil = seed_to_soil(seed)
    fert = soil_to_fert(soil)
    water = fert_to_water(fert)
    light = water_to_light(water)
    temp = light_to_temp(light)
    hum = temp_to_hum(temp)
    loc = hum_to_loc(hum)

    return(loc)

seeds = almanac_split[0].split( )[1:]
locs = [seed_to_loc(int(seed)) for seed in seeds]

print(f"Lowest location number: {min(locs)}")

# parte 2 --------------------------------------------------------------------------------------------------------

def range_intersection(range1, range2):
    intersect_start = max(range1.start, range2.start)
    intersect_stop = min(range1.stop, range2.stop)

    if intersect_start >= intersect_stop:
        raise ValueError("Ranges do not intersect")
    else:
        intersection = range(intersect_start, intersect_stop)
        return(intersection)
    
def do_ranges_intersect(range1, range2):
    intersect_start = max(range1.start, range2.start)
    intersect_stop = min(range1.stop, range2.stop)

    if intersect_start >= intersect_stop:
        return False
    else: 
        return True

seed_ranges = [range(int(seeds[2*i]), int(seeds[2*i]) + int(seeds[2*i + 1])) for i in range(int(len(seeds)/2))]

# need to compare the seed ranges to the domain of seed_to_soil
domain_seed_to_soil, img_seed_to_soil = create_domain_and_image(seed_to_soil_almanac)

# So all seed ranges intersect with exactly two subdomains
for i in range(len(seed_ranges)):
    num_intersections = sum([do_ranges_intersect(seed_ranges[0], subdomain) for subdomain in domain_seed_to_soil])
    print(f"Seed range {i} intersects with {num_intersections} subdomains of the seed to soil domain.")


# This results in memory error (there are like 18 billion numbers to check):
# locs_from_seedranges = []
# for seed_range in seed_ranges:
#     locs_from_seedranges.append(*[seed_to_loc(seed) for seed in seed_range])
