#!/usr/bin/env python3
"""
Create sample images for the PowerPoint presentation
"""
from PIL import Image, ImageDraw, ImageFont
import os

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Create MIT License Badge Image
mit_image = Image.new('RGB', (800, 200), color='#ffd700')
draw = ImageDraw.Draw(mit_image)
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
except (OSError, IOError):
    font = ImageFont.load_default()
    font_small = ImageFont.load_default()

draw.text((50, 70), "License: MIT", fill='black', font=font)
mit_image.save('images/mit-license.png')
print("Created: images/mit-license.png")

# Create Star History Chart Image
star_image = Image.new('RGB', (1200, 800), color='white')
draw = ImageDraw.Draw(star_image)

# Draw a simple chart representation
draw.rectangle([100, 100, 1100, 700], outline='black', width=3)
draw.text((400, 50), "Star History Chart", fill='black', font=font)
draw.text((150, 720), "Planning with Files - GitHub Stars", fill='black', font=font_small)

# Draw some sample data points
points = [(150, 650), (300, 600), (450, 500), (600, 350), (750, 250), (900, 200), (1050, 150)]
for i in range(len(points) - 1):
    draw.line([points[i], points[i+1]], fill='blue', width=4)
    draw.ellipse([points[i][0]-8, points[i][1]-8, points[i][0]+8, points[i][1]+8], fill='blue')

# Draw the last point
draw.ellipse([points[-1][0]-8, points[-1][1]-8, points[-1][0]+8, points[-1][1]+8], fill='blue')

star_image.save('images/star-history.png')
print("Created: images/star-history.png")

# Create Claude Code Skill Badge
claude_image = Image.new('RGB', (900, 200), color='#0066cc')
draw = ImageDraw.Draw(claude_image)
draw.text((50, 70), "Claude Code Skill", fill='white', font=font)
claude_image.save('images/claude-skill.png')
print("Created: images/claude-skill.png")

print("\nAll sample images created successfully!")
