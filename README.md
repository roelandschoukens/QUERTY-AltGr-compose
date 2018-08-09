# QUERTY-AltGr-compose

This keyboard layout adds accented letters (àêï), punctuation (—“”) and more to the standard QUERTY layout.
Useful for those who want to shake their [typewriter habits](https://practicaltypography.com/typewriter-habits.html).

Unlike the standard international QUERTY layout, it does not do this by binding dead
keys to characters like <kbd>'</kbd> and <kbd>^</kbd>. It’s almost impossible to program
on such layout. Instead the <kbd>AltGr</kbd> modifier is used.

To use, you can build a setup package using [Microsoft Keyboard Layout Creator 1.4](https://www.microsoft.com/en-nz/download/details.aspx?id=22339).
Although not updated anymore I think this still works on recent Windows versions.

## Characters:

  - Accented letters, typed with the <kbd>AltGr</kbd> modifier. This generates
    precomposed characters.
   
    | key           | Accent |
    | ------------- | ------------- |
    | <kbd>`</kbd>  | Grave accent: è |
    | <kbd>'</kbd>  | Acute accent: é |
    | <kbd>^</kbd>  | Circumflex: ê |
    | <kbd>Shift + `</kbd>  | Tilde: ñ |
    | <kbd>-</kbd>  | Macron: ō |
    | <kbd>Shift + '</kbd>  | Diaresis: ë |
    | <kbd>,</kbd>  | Cedilla: ç |
    | <kbd>.</kbd>  | Dot above: ȧ |

  - Non-ASCII quotes (“, ”, «, ») are mapped to the 3d and 4th positions on the various kinds of brackets.
  
  - Proper long dashes: use <kbd>AltGr + -</kbd>, <kbd>-</kbd> and <kbd>AltGr + -</kbd>, <kbd>Shift + -</kbd>
  
  - A few other mathemtical characters and symbols, like ×, √, ©, etc.
  
  - Greek letters: Use <kbd>AltGr + G</kbd>, followed by a letter. The mapping follows the Symbol font.
  
  - The <kbd>-</kbd> and <kbd>.</kbd> dead keys also include a few punctuation characters (en-dash, ellipsis, arrows, …).

For a full list, the `DEADKEY` sections in the KLC file are reasonably easy to read.

`print-deadkeys.py` generates those lists of dead key combinations.

## Caveat

This layout uses a few combinations of <kbd>AltGr</kbd> + _Letter_, which may interfere with applications
which use keyboard shortcuts of the form <kbd>Ctrl + Alt</kbd> + _Letter_, because of the quirky
way AltGr is implemented in Windows.

