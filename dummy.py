import os

months = ["June", "July", "August", "September", "October", "November", "December"]

for month in months:
    os.makedirs(month, exist_ok=True)
    for i in range(1, 32):
        filename = f"{i:02}_{month}.md"
        with open(os.path.join(month, filename), "w") as f:
            f.write(f"---\nlayout: default\ntitle: {i:02} {month}\nparent: {month}\nnav_order: {i}\n---")
        print(f"Created file {filename} in {month}")