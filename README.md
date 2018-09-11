# QUERTY-AltGr-compose

This keyboard layout adds accented letters (àêï), punctuation (—“”) and more to the standard QUERTY layout.
Useful for those who want to shake their [typewriter habits](https://practicaltypography.com/typewriter-habits.html).

Unlike the standard international QUERTY layout, it does not do this by binding dead
keys to characters like <kbd>'</kbd> and <kbd>^</kbd>. It’s almost impossible to program
on such layout. Instead the <kbd>AltGr</kbd> modifier is used.

To use, you can build a setup package using [Microsoft Keyboard Layout Creator 1.4](https://www.microsoft.com/en-nz/download/details.aspx?id=22339)
(aka MKLC). Although not updated anymore, and it still works on Windows 10. The generated installers
sometimes crash after finishing installation but for now this doesn’t seem to have bad consequences.

## Characters:

  - Accented letters, typed with the <kbd>AltGr</kbd> modifier. This generates
    precomposed characters.
   
    | key           | Accent |
    | ------------- | ------------- |
    | <kbd>`</kbd>  | Grave accent: è |
    | <kbd>Shift + `</kbd>  | Tilde: ñ |
    | <kbd>^</kbd>  | Circumflex: ê |
    | <kbd>Shift + ^</kbd>  | Caron: ě |
    | <kbd>-</kbd>  | Macron: ō |
    | <kbd>o</kbd>  | Ring above: å |
    | <kbd>'</kbd>  | Acute accent: é |
    | <kbd>Shift + '</kbd>  | Diaresis: ë |
    | <kbd>,</kbd>  | Cedilla: ç |
    | <kbd>.</kbd>  | Dot above: ȧ |
    
    One of these dead keys followed by <kbd>Space</kbd> will produce a combining mark. Unfortunately those 
    marks have     to come after the letter, which creates the awkward situation that <kbd>AltGr + 
    a</kbd>, <kbd>A</kbd> produces ā as     expected, but <kbd>AltGr + -</kbd>, <kbd>X</kbd> produces the 
    characters in the wrong order. Too bad, but I don’t know how     to produce a full-blown IME.

  - Non-ASCII quotes (“, ”, «, ») are mapped to the 3d and 4th positions on the various kinds of brackets.
  
  - Proper long dashes: use <kbd>AltGr + -</kbd>, <kbd>-</kbd> and <kbd>AltGr + -</kbd>, <kbd>Shift + -</kbd>
  
  - A few other mathematical characters and symbols, like ×, √, ©, etc.
  
  - Greek letters: Use <kbd>AltGr + G</kbd>, followed by a letter. The mapping follows the Symbol font.
  
  - The <kbd>-</kbd> and <kbd>.</kbd> dead keys also include a few punctuation characters (en-dash, ellipsis, arrows, …).

`print-deadkeys.py` generates those lists of dead key combinations.

## Caveat

This layout uses a few combinations of <kbd>AltGr</kbd> + _Letter_, which may interfere with applications
which use keyboard shortcuts of the form <kbd>Ctrl + Alt</kbd> + _Letter_, because of the quirky
way AltGr is implemented in Windows.

## Implementation notes

There are a few things to watch out for when modifying layouts:

 - A dead key plus <kbd>Space</kbd> should produce that dead key itself.
   Eg. <kbd>AltGr + G</kbd> is assigned to `γ`, and `γ`, _Space_ produces `γ`.
 
 - A dead key plus that same character should not be assigned. Pressing the
   dead key twice will normally produce that character twice. Or maybe I should
   just avoid assigning the same character as both normal key and dead key.
   
   For this reason <kbd>AltGr + G</kbd> is not assigned to `g`: then we would have
   `g`, `g` → `γ`.
   
   The layout will not work properly with GTK+ applications if such combinations
   are there.

 - Some characters just don’t seem to work as dead keys. Noted so far: `–`. This
   is why <kbd>AltGr + -</kbd> is mapped to `¯`.

 - MKLC will not load your layout if a dead key is defined, but the DEADKEY section is
   missing.
   
 - MKLC will refuse to generate a setup package if your layout (with the same name) is
   currently in use. So go to settings and remove it first. And carefully keep the version
   string and description strings in sync, otherwise things will get very confusing in the
   control panel.

 - In general developing this thing is a PITA because Windows doesn’t handle updates
   to layouts well (in their defence it is a very unusual thing to do). Reboot in case
   of doubt.
   
