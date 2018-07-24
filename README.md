# QUERTY-AltGr-compose

This keyboard layout adds accented letters and more to the standard QUERTY layout.

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
  
  - A few other mathemtical characters and symbols, like ×, √, ©, etc.
  
  - Greek letters: Use <kbd>AltGr + G</kbd>, followed by a letter. The mapping follows the Symbol font.
  
  - The <kbd>-</kbd> and <kbd>.</kbd> dead keys also include a few punctuation characters (en-dash, ellipsis, arrows, …).

For a full list, the `DEADKEY` sections in the KLC file are reasonably easy to read.

`print-deadkeys.py` generates those lists of dead key combinations.
