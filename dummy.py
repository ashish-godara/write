import os

months = ["June", "July", "August", "September", "October", "November", "December"]

for month_no, month in enumerate(months, start=1):
    os.makedirs(month, exist_ok=True)
    filename = f"{month.lower()}.md"
    with open(os.path.join(month, filename), "w") as f:
        f.write(f"---\nlayout: default\ntitle: {month}\nnav_order: {month_no+1}\nhas_children: true\n---")
    print(f"Created file {filename} in {month}")