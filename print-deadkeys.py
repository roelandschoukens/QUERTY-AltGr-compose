#! python3

# hint: use set PYTHONIOENCODING=UTF-8 to control encoding of stdout

version = [1, 8, 3]

import re
import sys
import unicodedata

latin = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# mapping of latin letters in the Symbol font
greek = "ΑΒΧΔΕΦΓΗΙϑΚΛΜΝΟΠΘΡΣΤΥςΩΞΨΖαβχδεφγηιϕκλμνοπθρστυϖωξψζ"

class DeadKey:
    def __init__(self, name, keypress, basekey, deadkey, combining_accent, extras):
        self.name = name
        self.keypress = keypress
        self.basekey = basekey
        self.deadkey = deadkey
        self.combining_accent = combining_accent
        self.extras = extras
        if self.combining_accent and not unicodedata.combining(self.combining_accent):
            raise ValueError("That is not a combining accent: {}".format(self.combining_accent))

    def isaccent(self):
        return self.combining_accent is not None
        
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
dk = [
    DeadKey("Backtick",  "`", "`", "`", "\u0300", []), 
    DeadKey("Quote",      "'", "'", "´", "\u0301", [
        (",", "‚")  # ← that's a low quotation mark
    ]),
    DeadKey("Circumflex", "6", "6", "^", "\u0302", []), 
    DeadKey("Tilde",      "Shift + `", "~", "~", "\u0303", []), 
    DeadKey("Dash",     "-", "-", "¯", "\u0304", [
        (">", "→"),
        ("<", "←"),
        ("v", "↓"),
        ("^", "↑"),
        ("-", "–"),
        ("_", "—"),
        (":", "÷"),
        ("+", "±"),
    ]), 
    DeadKey("Dot",  ".", ".", "˙", "\u0307", [
        (".", "…"),
        ("-", "·"),
        ("=", "•"),
    ]), 
    DeadKey("Double quote",  "Shift + '", '"', "¨", "\u0308", [
        (",", "„")
        ]), 
    DeadKey("Ring above", "o", "o", "˚", "\u030a", []), 
    DeadKey("Caron",      "Shift + 6", "^", "ˇ", "\u030c", []),
    DeadKey("Cedilla",    ",", ",", "¸", "\u0327", []),
    DeadKey("Mathematical characters",          "+", "=", "×", None,      [
        ("-", "−"), # minus sign (subtly different from en dash)
        (".", "⋅"), # dot operator (subtly different from middle dot)
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
    DeadKey("Greek", "g", "g", "γ", None, list(zip(latin, greek))),
]

dklut = dict((x.basekey, x) for x in dk)

# patch our KLC template

def klc_tochar(s):
    if s == '-1':
        return None
    elif len(s) == 1:
        return s
    else:
        return chr(int(s, 16))

def klc_fromchar(ch, deadkey):
    if ch is None:
        return '-1'
    if deadkey:
        return "{0:04x}@".format(ord(ch))
    else:
        return ch if re.match("[a-zA-Z0-9]", ch) else "{0:04x}".format(ord(ch))

def klc_tocomment(ch):
    if ch is None:
        return '<none>'
    else:
        return unicodedata.name(ch, "?")

def substitute_deadkeys(m):
    """Fill in dead keys.
    
    We configure a dead key for a character by adding AltGr to the matching keystroke.
    Meaning that we cannot have dead keys on keys without AltGr
    """
    keys = list(map(klc_tochar, m.groups()[1:]))
    assert(len(keys) == 5) # that is [normal, shift, ctrl, altgr, shift+altgr]
    dk = [None, None, None, dklut.get(keys[0]), dklut.get(keys[1])]
    for i in range(2):
        if dk[i+3]: 
            if keys[i+3] is not None:
                raise ValueError('dead key configured for {} but AltGr combination already assigned to {}'.format(keys[i], keys[i+3]))
            keys[i+3] = dk[i+3].deadkey
    
    s = m.group(1)
    for i in range(5):
        s += klc_fromchar(keys[i], dk[i] is not None) + '\t'
    
    s += '// '
    s += ", ".join(map(klc_tocomment, keys))
    s += "\n"
    return s

def get_deadkeytables():
    t = []
    for d in dk:
        t.append("DEADKEY\t{:04x} \n".format(ord(d.deadkey)))
        t.append("\n")
        for a, b in d.all():
            t.append("{:04x}\t{:04x}\t// {} -> {}\n".format(ord(a), ord(b), a, b))
        t.append("\n")
    return t
    
def get_deadkeynames():
    t = []
    for d in dk:
        ch = d.deadkey
        t.append("{:04x} \"{}\"\n".format(ord(ch), unicodedata.name(ch)))
    return t
    
# loop over lines, patch up the dead keys in the LAYOUT section
lines = []
with (open('qucmp.klc.in', encoding='utf-16')) as f:
    layout = False
    pat = re.compile(r'([0-9a-f]{2}\t+\w+\t+\w+\t+)(\S+)\t+(\S+)\t+(\S+)\t+(\S+)\t+(\S+)\t+//')
    for line in f:
        if line == "{layout}\n":
            layout = True
        elif line == "{endlayout}\n":
            layout = False
        elif line == "{deadkeys}\n":
            lines += get_deadkeytables()
        elif line == "{deadkeynames}\n":
            lines += get_deadkeynames()
        elif layout and line[0] != '5': # the '5' avoids modifying the "decimal separator" key
            m = pat.match(line)
            if m:
                lines.append(substitute_deadkeys(m))
            else:
                raise ValueError("don’t know how to parse input line\n"+line)
        else:
            lines.append(line.format(v=version))

            
with (open('qucmp{}{}{}.klc'.format(*version), 'w', encoding='utf-16')) as f:
    for l in lines:
        f.write(l)
    
# write markdown

with (open('keys.md', 'w', encoding='utf-8')) as f:
    print("""# Keys

## Combinations with dead keys
""", file=f)
    for d in dk:
        if not d.extras: continue
        print("### {}: <kbd>{}</kbd>".format(d.name, d.keypress), file=f)
        print("| base | char | name     |", file=f)
        print("| ---- | ---- | -------- |", file=f)
        for a, b in d.extras:
            if a == " ": a = "Space"
            print("| <kbd>{}</kbd>  | {} | {} |".format(a, b, unicodedata.name(b).lower()), file=f)
        print(file=f)
