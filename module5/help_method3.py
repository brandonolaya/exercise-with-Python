# Check if the sets below form isolated sets
# (that is, they have no elements in common),
# using the isdisjoint() method. Store said result
# in the isolated_sets variable:

smartphone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
tv_brands = {"Sony", "Philips", "Samsung", "LG"}
isolated_sets = smartphone_brands.isdisjoint(tv_brands)
print(isolated_sets)