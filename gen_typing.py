import sys
sys.path.insert(0, '/home/claude/fix')
from measure import text_width

FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"

def build(text, filename, aria):
    fs = 20
    tw = text_width(text, fs)
    tw_exact = tw  # used for textLength
    W = tw + 40
    H = 40
    cursor_x_end = tw + 6
    svg = f'''<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{aria}">
  <defs>
    <clipPath id="typeClip">
      <rect x="0" y="0" height="{H}" width="0">
        <animate attributeName="width" values="0;{tw_exact};{tw_exact};0;0" keyTimes="0;0.5;0.85;0.92;1" dur="6s" repeatCount="indefinite"/>
      </rect>
    </clipPath>
  </defs>
  <text x="0" y="27" font-family="{FONT}" font-size="{fs}" font-weight="700" fill="#2F5FFF" textLength="{tw_exact}" lengthAdjust="spacingAndGlyphs" clip-path="url(#typeClip)">{text}</text>
  <rect width="3" height="24" y="8" fill="#2F5FFF">
    <animate attributeName="x" values="0;{cursor_x_end};{cursor_x_end};0;0" keyTimes="0;0.5;0.85;0.92;1" dur="6s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite"/>
  </rect>
</svg>
'''
    with open(f'/home/claude/fix/headers/{filename}', 'w') as f:
        f.write(svg)
    print(filename, W, H)

build("Software Quality Assurance Engineer", "typing-intro-en.svg", "Typing headline: Software Quality Assurance Engineer")
build("Engenheiro de Qualidade de Software", "typing-intro-pt.svg", "Frase animada: Engenheiro de Qualidade de Software")
