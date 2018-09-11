#! python3

# hint: use set PYTHONIOENCODING=UTF-8 to control encoding of stdout

# Warning about dead keys:
# A deadkey should not have a combination with itself. Eg. we may
# define ` + a -> à, but we must not define ` + ` -> ?. You should
# verify that pressing the deak key twice produces the assigned
# character twice.
# This is why we have γ and ¯ on our main layout, this makes sure
# we don't define g + g -> γ

# and yes, you sometimes have to reboot after rebuilding the layout.

# Final note: carefully match the file name and all the version strings.

import unicodedata

def emit(a, b):
    print("{:04x}\t{:04x}\t// {} -> {}".format(ord(a), ord(b), a, b))

greek = "ΑΒΧΔΕΦΓΗΙϑΚΛΜΝΟΠΘΡΣΤΥςΩΞΨΖαβχδεφγηιϕκλμνοπθρστυϖωξψζ"
latin = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

print("// γ")
print("DEADKEY\t{:04x}".format(ord('γ')))
print()
for a, b in zip(latin, greek):
    emit(a, b)
emit(" ", "γ")
print()

# Note that not all characters work as dead keys. En-dash doesn't work.
# luckily all our combining diacritics work.
diacritics = "\u0300\u0301\u0302\u0303\u0304\u0308\u0327\u0307\u030a\u030c"
keys = diacritics

for d, k in zip(diacritics, keys):
    print("// " + k)
    print("DEADKEY\t{:04x} ".format(ord(k)))
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

    if (k == "¯"):
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

print("// ×")
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
