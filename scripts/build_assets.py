"""Build the profile's small, self-contained SVG assets (no remote dependencies)."""

from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"
ASSETS.mkdir(exist_ok=True)

for theme, colors in {
    "light": ("#fbf7ee", "#202f4b", "#62718a", "#365d8d", "#c89651", "#e8e1d4"),
    "dark": ("#171f2c", "#f1eadc", "#a8b5ca", "#8dafdc", "#dcaf72", "#354155"),
}.items():
    bg, ink, muted, blue, gold, line = colors
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="256" viewBox="0 0 960 256" role="img" aria-labelledby="title desc">
  <title id="title">Hi, I’m Jiang Wu.</title>
  <desc id="desc">Personalized intelligence, from models to agents. An abstract constellation connects ideas and experience.</desc>
  <rect width="960" height="256" rx="16" fill="{bg}"/>
  <path d="M36 33h30" stroke="{gold}" stroke-width="3"/>
  <text x="80" y="38" font-family="Arial,Helvetica,sans-serif" font-size="12" font-weight="600" letter-spacing="3" fill="{muted}">A PERSONAL RESEARCH SPACE</text>
  <text x="36" y="119" font-family="Georgia,'Times New Roman',serif" font-size="59" letter-spacing="-1.8" fill="{ink}">Hi, I’m Jiang Wu.</text>
  <text x="39" y="159" font-family="Arial,Helvetica,sans-serif" font-size="22" fill="{muted}">Personalized intelligence,</text>
  <text x="39" y="190" font-family="Arial,Helvetica,sans-serif" font-size="22" fill="{muted}">from models to agents.</text>
  <path d="M38 221h475" stroke="{line}"/>
  <g fill="none" stroke="{line}" stroke-width="1">
    <circle cx="773" cy="130" r="91"/>
    <ellipse cx="773" cy="130" rx="135" ry="53" transform="rotate(-35 773 130)"/>
    <ellipse cx="773" cy="130" rx="113" ry="62" transform="rotate(40 773 130)"/>
  </g>
  <path d="M651 190C665 100 701 74 755 105S824 201 887 68" fill="none" stroke="{blue}" stroke-width="2.5"/>
  <path d="M668 62C700 182 776 168 863 196" fill="none" stroke="{gold}" stroke-width="2"/>
  <path d="M708 98L756 106L808 156L847 127" fill="none" stroke="{blue}" stroke-width="1" opacity=".55"/>
  <g fill="{bg}" stroke="{blue}" stroke-width="2">
    <circle cx="708" cy="98" r="5"/>
    <circle cx="808" cy="156" r="5"/>
    <circle cx="847" cy="127" r="5"/>
  </g>
  <circle cx="756" cy="106" r="9" fill="{blue}"/>
  <circle cx="756" cy="106" r="18" fill="none" stroke="{blue}" opacity=".22"/>
  <circle cx="668" cy="62" r="5" fill="{gold}"/>
  <circle cx="863" cy="196" r="5" fill="{gold}"/>
  <circle cx="887" cy="68" r="4" fill="{blue}"/>
  <circle cx="651" cy="190" r="4" fill="{blue}"/>
  <path d="M899 219h19m-9.5-9.5v19" stroke="{gold}" stroke-width="1.5"/>
</svg>
'''
    (ASSETS / f"header-{theme}.svg").write_text(svg)
    (ASSETS / f"header-mobile-{theme}.svg").write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="232" viewBox="0 0 480 232" role="img" aria-labelledby="title desc">
  <title id="title">Hi, I’m Jiang Wu.</title>
  <desc id="desc">Personalized intelligence, from models to agents.</desc>
  <rect width="480" height="232" rx="16" fill="{bg}"/>
  <path d="M28 31h22" stroke="{gold}" stroke-width="3"/>
  <text x="63" y="35" font-family="Arial,Helvetica,sans-serif" font-size="10" font-weight="600" letter-spacing="2" fill="{muted}">A PERSONAL RESEARCH SPACE</text>
  <text x="27" y="104" font-family="Georgia,'Times New Roman',serif" font-size="46" letter-spacing="-1.4" fill="{ink}">Hi, I’m Jiang Wu.</text>
  <text x="29" y="148" font-family="Arial,Helvetica,sans-serif" font-size="20" fill="{muted}">Personalized intelligence,</text>
  <text x="29" y="178" font-family="Arial,Helvetica,sans-serif" font-size="20" fill="{muted}">from models to agents.</text>
  <path d="M29 207h259" stroke="{line}"/>
  <g fill="none" stroke="{line}">
    <circle cx="396" cy="168" r="40"/>
    <ellipse cx="396" cy="168" rx="59" ry="25" transform="rotate(-35 396 168)"/>
    <ellipse cx="396" cy="168" rx="48" ry="28" transform="rotate(40 396 168)"/>
  </g>
  <path d="M343 194C351 144 371 143 389 161S421 203 449 132" fill="none" stroke="{blue}" stroke-width="2"/>
  <path d="M352 135C370 189 400 181 434 200" fill="none" stroke="{gold}" stroke-width="1.5"/>
  <circle cx="389" cy="161" r="5" fill="{blue}"/>
  <circle cx="352" cy="135" r="3" fill="{gold}"/>
  <circle cx="434" cy="200" r="3" fill="{gold}"/>
</svg>
''')

for slug, label, width in [
    ("website", "Website", 100),
    ("scholar", "Google Scholar", 148),
    ("email", "Say hello", 112),
]:
    (ASSETS / f"link-{slug}.svg").write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="34" viewBox="0 0 {width} 34">
  <rect x=".5" y=".5" width="{width-1}" height="33" rx="8" fill="#f8f5ed" stroke="#e3dccf"/>
  <text x="16" y="22" font-family="Arial,Helvetica,sans-serif" font-size="13" font-weight="600" fill="#28496e">{label}</text>
  <path d="M{width-26} 21l9-9m-8 0h8v8" stroke="#8e744e" stroke-width="1.4" fill="none"/>
</svg>
''')

(ASSETS / "oral.svg").write_text('''<svg xmlns="http://www.w3.org/2000/svg" width="54" height="20" viewBox="0 0 54 20">
  <rect width="54" height="20" rx="5" fill="#823d4e"/>
  <circle cx="10" cy="10" r="2.3" fill="#f2d9b5"/>
  <text x="18" y="14" font-family="Arial,Helvetica,sans-serif" font-size="10" font-weight="700" letter-spacing=".6" fill="#fff8ee">ORAL</text>
</svg>
''')
