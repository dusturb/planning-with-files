#!/usr/bin/env python3
"""
Create a PowerPoint presentation from images in the images directory
"""
from pptx import Presentation
from pptx.util import Inches
import os
import glob

def create_pptx_from_images(output_filename='presentation.pptx', images_dir='images'):
    """
    Create a PowerPoint presentation with each image on a separate slide
    
    Args:
        output_filename: Name of the output .pptx file
        images_dir: Directory containing the images
    """
    # Create a presentation object
    prs = Presentation()
    
    # Set slide dimensions (16:9 aspect ratio)
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)
    
    # Add a title slide
    title_slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(title_slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    
    title.text = "Planning with Files"
    subtitle.text = "Image Gallery Presentation"
    
    # Get all image files from the images directory
    image_extensions = ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.bmp']
    image_files = []
    
    for ext in image_extensions:
        image_files.extend(glob.glob(os.path.join(images_dir, ext)))
    
    image_files.sort()
    
    if not image_files:
        print(f"Warning: No images found in {images_dir} directory")
        return
    
    print(f"Found {len(image_files)} image(s) to add to presentation")
    
    # Add a slide for each image
    for img_path in image_files:
        # Use a blank slide layout
        blank_slide_layout = prs.slide_layouts[6]
        slide = prs.slides.add_slide(blank_slide_layout)
        
        # Get image filename without extension for the title
        img_name = os.path.splitext(os.path.basename(img_path))[0]
        
        # Add a text box at the top for the image title
        left = Inches(0.5)
        top = Inches(0.3)
        width = Inches(9)
        height = Inches(0.5)
        
        txBox = slide.shapes.add_textbox(left, top, width, height)
        tf = txBox.text_frame
        tf.text = img_name.replace('-', ' ').replace('_', ' ').title()
        
        # Format the title
        p = tf.paragraphs[0]
        p.font.size = Inches(0.4)
        p.font.bold = True
        
        # Calculate image position and size to fit on slide
        # Leave space at top for title
        left = Inches(1)
        top = Inches(1.2)
        max_width = Inches(8)
        max_height = Inches(5.8)
        
        # Add the image
        try:
            pic = slide.shapes.add_picture(img_path, left, top, width=max_width)
            
            # If image height exceeds max, scale it down
            if pic.height > max_height:
                aspect_ratio = pic.width / pic.height
                pic.height = max_height
                pic.width = int(max_height * aspect_ratio)
                
            # Center the image horizontally
            pic.left = int((prs.slide_width - pic.width) / 2)
            
            print(f"Added slide for: {img_name}")
        except Exception as e:
            print(f"Error adding image {img_path}: {e}")
    
    # Save the presentation
    prs.save(output_filename)
    print(f"\n✓ PowerPoint presentation saved as: {output_filename}")
    print(f"  Total slides: {len(prs.slides)}")
    return output_filename

if __name__ == '__main__':
    create_pptx_from_images()
