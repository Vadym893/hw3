washing_product = "jacket"
rinse = True
spin = False

washing_times = {
    "jacket": 40,
    "underwear": 70,
    "shoes": 20
}

rinse_time = 15
spin_time = 9

total_washing_time = washing_times.get(washing_product, 0)

if rinse:
    total_washing_time += rinse_time

if spin:
    total_washing_time += spin_time
print(f"Total washing time: {total_washing_time} minutes")