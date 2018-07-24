#! python3

# hint: use PYTHONIOENCODING to control encoding of stdout

import unicodedata

def emit(a, b):
    print("{:04x}\t{:04x}\t// {} => {}".format(ord(a), ord(b), a, b))

greek = "ΑΒΧΔΕΦΓΗΙϑΚΛΜΝΟΠΘΡΣΤΥςΩΞΨΖαβχδεφγηιϕκλμνοπθρστυϖωξψζ"
latin = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

print("DEADKEY\t0067")
print()
for a, b in zip(latin, greek):
    emit(a, b)
emit(" ", "g")

diacritics = "\u0300\u0301\u0302\u0302\u0303\u0304\u0308\u0327\u0307"
keys = "`'^¼~-\",."

for d, k in zip(diacritics, keys):
    print("DEADKEY\t{:04x}".format(ord(k)))
    print()
    for l in latin:
        a = l+d
        b = unicodedata.normalize("NFC", a)
        if len(b) == 1:
            emit(l, b)

    if (k == "'"):
        emit(",", "‚")   # ← that's a low quotation mark
    if (k == "\""):
        emit(",", "„")

    if (k == "-"):
        emit(">", "→")
        emit("<", "←")
        emit("v", "↓")
        emit("^", "↑")
        emit("-", "–")
        emit("_", "—")
        emit(":", "÷")
        emit("+", "±")

    if (k == "."):
        emit(".", "…")
        emit("-", "·")
        emit("=", "•")
    
    emit(" ", k)
    print()

print("DEADKEY\t{:04x}".format(ord("×")))
emit("<", "≤")
emit(">", "≥")
emit("/", "≠")
emit("~", "≈")
emit("v", "√")
emit("o", "°")
emit("'", "′")
emit("\"", "″")
emit("8", "∞")
emit("D", "∆")
emit("d", "∂")
emit("s", "∫")
emit(" ", "×")

print()
