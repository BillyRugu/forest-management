rate = 0.3
forest_cover = 1000 
year = 0
while forest_cover > 500:
    forest_cover *= (1-rate) 
    year += 1
print(f"Years to lose half the forest cover:{year}")