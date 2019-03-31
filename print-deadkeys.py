#! python3

# hint: use set PYTHONIOENCODING=UTF-8 to control encoding of stdout

import sys
import unicodedata

latin = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# mapping of latin letters in the Symbol font
greek = "ΑΒΧΔΕΦΓΗΙϑΚΛΜΝΟΠΘΡΣΤΥςΩΞΨΖαβχδεφγηιϕκλμνοπθρστυϖωξψζ"

class DeadKey:
    def __init__(self, name, keypress, deadkey, combining_accent, extras):
        self.name = name
        self.keypress = keypress
        self.deadkey = deadkey
        self.combining_accent = combining_accent
        self.extras = extras

    def isaccent(self):
        return unicodedata.combining(self.combining_accent) != 0
        
    def all(self):
        """ all combinations"""
        yield from self.extras
        if self.isaccent():
            for l in latin:
                a = l + self.combining_accent
                b = unicodedata.normalize("NFC", a)
                if len(b) == 1:
                    yield (l, b)
        yield (" ", self.deadkey)
        
# Note that not all characters work as dead keys. En-dash doesn't work.
# luckily all our combining diacritics work.
dk = [
    DeadKey("Backtick",  "`", "`", "\u0300", []), 
    DeadKey("Quote",      "'", "´", "\u0301", [
        (",", "‚")  # ← that's a low quotation mark
    ]),
    DeadKey("Circumflex", "6", "^", "\u0302", []), 
    DeadKey("Tilde",      "Shift + `", "~", "\u0303", []), 
    DeadKey("Dash",     "-", "¯", "\u0304", [
        (">", "→"),
        ("<", "←"),
        ("v", "↓"),
        ("^", "↑"),
        ("-", "–"),
        ("_", "—"),
        (":", "÷"),
        ("+", "±"),
    ]), 
    DeadKey("Dot",  ".", "˙", "\u0307", [
        (".", "…"),
        ("-", "·"),
        ("=", "•"),
    ]), 
    DeadKey("Double quote",  "Shift + '", "¨", "\u0308", [
        (",", "„")
        ]), 
    DeadKey("Ring above", "o", "˚", "\u030a", []), 
    DeadKey("Caron",      "Shift + 6", "ˇ", "\u030c", []),
    DeadKey("Cedilla",    ",", "¸", "\u0327", []),
    DeadKey("Mathematical characters",          "+", "×", "×",      [
        ("-", "−"), # minus sign (subtly different from en dash)
        ("<", "≤"),
        (">", "≥"),
        ("/", "≠"),
        ("~", "≈"),
        ("v", "√"),
        ("o", "°"),
        ("'", "′"),
        ('"', "″"),
        ("8", "∞"),
        ("D", "∆"),
        ("d", "∂"),
        ("s", "∫"),
        ("S", "∑"),
        ("P", "∏"),
    ]),
    DeadKey("Greek", "g", "γ", "γ", list(zip(latin, greek))),
]

what = sys.argv[1] if len(sys.argv) == 2 else ""

if what == "klc":
    for d in dk:
        print("DEADKEY\t{:04x} ".format(ord(d.deadkey)))
        print()
        for a, b in d.all():
            print("{:04x}\t{:04x}\t// {} -> {}".format(ord(a), ord(b), a, b))
        print()
elif what == "md":
    for d in dk:
        if not d.extras: continue
        print("### {}: <kbd>{}</kbd>".format(d.name, d.keypress))
        print("| base | char |")
        print("| ---- | ---- |")
        for a, b in d.extras:
            if a == " ": a = "Space"
            print("| <kbd>{}</kbd>  | {} |".format(a, b))
        print()
else:
    print("Choose a format ('md' or 'klc') for printing the list of dead keys")