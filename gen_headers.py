import sys
sys.path.insert(0, '/home/claude/fix')
from measure import text_width

FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"

ICONS = {
    "about": '''<circle cx="32" cy="26" r="7" fill="none" stroke="#FFFFFF" stroke-width="2.5"/>
  <path d="M18 46c0-8 6-13 14-13s14 5 14 13" fill="none" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round"/>''',
    "projects": '''<path d="M16 22h10l3 4h15a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H16a2 2 0 0 1-2-2V24a2 2 0 0 1 2-2Z" fill="none" stroke="#FFFFFF" stroke-width="2.5" stroke-linejoin="round"/>''',
    "skills": '''<rect x="18" y="32" width="6" height="12" rx="2" fill="#FFFFFF"/>
  <rect x="29" y="24" width="6" height="20" rx="2" fill="#FFFFFF"/>
  <rect x="40" y="16" width="6" height="28" rx="2" fill="#FFFFFF"/>''',
    "roadmap": '''<path d="M17 41L28 29L39 41" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="1 5" fill="none" stroke-linecap="round"/>
  <path d="M28 29L45 17" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="1 5" fill="none" stroke-linecap="round"/>
  <circle cx="17" cy="41" r="3" fill="#FFFFFF"/>
  <circle cx="28" cy="29" r="3" fill="#FFFFFF"/>
  <circle cx="45" cy="17" r="3" fill="#FFFFFF"/>''',
    "philosophy": '''<path d="M32 16a10 10 0 0 0-6 18v4h12v-4a10 10 0 0 0-6-18Z" fill="none" stroke="#FFFFFF" stroke-width="2.3" stroke-linejoin="round"/>
  <line x1="27" y1="42" x2="37" y2="42" stroke="#FFFFFF" stroke-width="2.3" stroke-linecap="round"/>''',
    "contact": '''<rect x="16" y="21" width="32" height="22" rx="3" fill="none" stroke="#FFFFFF" stroke-width="2.3"/>
  <path d="M16 23l16 12 16-12" stroke="#FFFFFF" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>''',
}

LABELS = {
    "about": "About Me",
    "projects": "Projects",
    "skills": "Skills",
    "roadmap": "Roadmap",
    "philosophy": "Philosophy",
    "contact": "Contact",
}

def build(key, label):
    tw = text_width(label, 24)
    W = 72 + tw + 28
    H = 64
    svg = f'''<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label} section header">
  <rect x="0" y="0" width="{W}" height="{H}" rx="16" fill="#0F1B33"/>
  <rect x="8" y="8" width="48" height="48" rx="12" fill="#2F5FFF"/>
  {ICONS[key]}
  <text x="72" y="40" font-family="{FONT}" font-size="24" font-weight="700" fill="#FFFFFF">{label}</text>
</svg>
'''
    with open(f'/home/claude/fix/headers/{key}.svg', 'w') as f:
        f.write(svg)
    print(key, W, H)

for k, l in LABELS.items():
    build(k, l)
