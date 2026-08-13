skills = [
    ("Software Testing", 85),
    ("Test Analysis", 80),
    ("Requirement Analysis", 75),
    ("API Testing", 70),
    ("SQL", 65),
    ("Playwright", 60),
    ("Cypress", 55),
    ("CI/CD", 30),
    ("Performance Testing", 20),
    ("Accessibility Testing", 15),
]

pad = 24
row_h = 38
top_pad = 14
content_w = 640
track_x = pad + 190
track_w = 360
track_h = 12
content_h = top_pad*2 + row_h*len(skills)
W = content_w + pad*2
H = content_h

FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"

def build(animated):
    svg = []
    label = "Learning roadmap, animated" if animated else "Learning roadmap"
    svg.append(f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">')
    svg.append(f'  <rect x="0" y="0" width="{W}" height="{H}" rx="16" fill="#0F1B33"/>')
    for i, (skill_label, pct) in enumerate(skills):
        y = pad + top_pad + i*row_h
        label_y = y + track_h + 1
        bar_w = track_w * pct / 100
        svg.append(f'  <text x="{pad}" y="{label_y}" font-family="{FONT}" font-size="13" font-weight="600" fill="#FFFFFF">{skill_label}</text>')
        svg.append(f'  <rect x="{track_x}" y="{y}" width="{track_w}" height="{track_h}" rx="6" fill="#1E2C4A"/>')
        if animated:
            delay = i * 0.08
            svg.append(f'  <rect x="{track_x}" y="{y}" width="0" height="{track_h}" rx="6" fill="#2F5FFF"><animate attributeName="width" from="0" to="{bar_w:.1f}" dur="1s" begin="{delay:.2f}s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/></rect>')
        else:
            svg.append(f'  <rect x="{track_x}" y="{y}" width="{bar_w:.1f}" height="{track_h}" rx="6" fill="#2F5FFF"/>')
        svg.append(f'  <text x="{W-pad}" y="{label_y}" text-anchor="end" font-family="{FONT}" font-size="12" font-weight="600" fill="#94A3B8">{pct}%</text>')
    svg.append('</svg>')
    fname = 'roadmap-animated.svg' if animated else 'roadmap.svg'
    with open(f'/home/claude/fix/roadmap/{fname}', 'w') as f:
        f.write('\n'.join(svg) + '\n')
    print(fname, W, H)

build(False)
build(True)
