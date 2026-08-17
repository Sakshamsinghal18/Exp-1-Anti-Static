from PIL import Image, ImageDraw
import os

folder = r"C:\Users\dell premium series\.gemini\antigravity-ide\scratch\antistatic-virtual-lab"

for i in range(1, 31):
    path = os.path.join(folder, f"step{i}.png")
    if not os.path.exists(path):
        print(f"step{i}.png not found, skipping")
        continue

    img = Image.open(path).convert("RGBA")
    w, h = img.size

    # Sample background color from top-left corner (always clean)
    bg_color = img.getpixel((5, 5))

    # The PowerPoint icons sit in the bottom-left corner
    # We cover: left 35% width, bottom 10% height
    patch_w = int(w * 0.35)
    patch_h = int(h * 0.10)
    patch_y = h - patch_h

    draw = ImageDraw.Draw(img)
    draw.rectangle([0, patch_y, patch_w, h], fill=bg_color)

    # Save back as PNG
    img = img.convert("RGB")
    img.save(path)
    print(f"Fixed step{i}.png  (bg={bg_color[:3]}, patch area: 0,{patch_y} to {patch_w},{h})")

print("\nAll done!")
