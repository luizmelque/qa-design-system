from PIL import ImageFont

def text_width(text, size, bold=True):
    path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    font = ImageFont.truetype(path, size)
    bbox = font.getbbox(text)
    return bbox[2] - bbox[0]

if __name__ == "__main__":
    for label in ["About Me","Projects","Skills","Roadmap","Philosophy","Contact"]:
        print(label, text_width(label, 24))
