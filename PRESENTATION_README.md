# PowerPoint Presentation Generator

This script creates a PowerPoint (.pptx) presentation from images.

## Files

- `create_presentation.py` - Main script to create the PowerPoint presentation
- `create_sample_images.py` - Helper script to create sample images for demonstration
- `images/` - Directory containing images to be added to the presentation
- `presentation.pptx` - Generated PowerPoint presentation

## Requirements

```bash
pip install python-pptx pillow
```

## Usage

### Create presentation from images

Simply run:

```bash
python3 create_presentation.py
```

This will:
1. Look for images in the `images/` directory
2. Create a title slide with "Planning with Files - Image Gallery Presentation"
3. Add each image to a separate slide
4. Save the presentation as `presentation.pptx`

### Create sample images

If you want to generate sample images for testing:

```bash
python3 create_sample_images.py
```

This creates three sample images:
- `images/mit-license.png` - MIT License badge
- `images/star-history.png` - Star History chart visualization
- `images/claude-skill.png` - Claude Code Skill badge

## Customization

You can customize the script by modifying the following parameters in `create_presentation.py`:

```python
create_pptx_from_images(
    output_filename='presentation.pptx',  # Output file name
    images_dir='images'                    # Directory containing images
)
```

## Supported Image Formats

- PNG (.png)
- JPEG (.jpg, .jpeg)
- GIF (.gif)
- BMP (.bmp)

## Output

The generated PowerPoint presentation will have:
- A title slide
- One slide per image with the image name as the slide title
- Images centered and sized to fit the slide while maintaining aspect ratio
- 16:9 aspect ratio (10" x 7.5")

## Example

```bash
# 1. Create sample images (optional)
python3 create_sample_images.py

# 2. Create PowerPoint presentation
python3 create_presentation.py

# Output: presentation.pptx (can be opened with PowerPoint, Google Slides, LibreOffice Impress, etc.)
```

## Notes

- The script automatically sorts images alphabetically by filename
- Each image gets its own slide with a title derived from the filename
- Images are automatically scaled to fit the slide while maintaining aspect ratio
- The presentation uses standard PowerPoint layouts compatible with all major presentation software
