Names: "spam", "eggs", "bacon" and "ham" 
are coming from https://en.wikipedia.org/wiki/Spam_(Monty_Python_sketch)

names: "foo" and "bar"
are coming from FUBAR = https://en.wiktionary.org/wiki/FUBAR  changed beyond all recognition


snake_case - for names of methods, functions variables
UPPER_SNAKE_CASE - for global constants 

camelCases - ... (can be used for names of methods, functions variables)

PascalCase - for names of classes

Some empirical "Rules":
- larger the name's scope -> the more descriptive it should be (use more longer name), 
- DN’T DRP LTTRS FRM YR SRC CD, 
- don't make attribute *"catWeight"* in class **"Cat"**, but use *kg* or *lbs* if it is unclear,
- don't use sequential numeric suffixes in your names,
- don't use gooseDownload() (even if you know "goose" meaning), use increaseDownloadSpeed(),
- never use Python’s built-in names for your own variables.

Some commonly overwritten Python names are *all*, *any*, *date*, *email*, *file*,
*format*, *hash*, *id*, *input*, *list*, *min*, *max*, *object*, *open*, *random*, *set*, *str*, *sum*, *test*, and *type*. Don’t use these names for your identifiers.

- be careful  with your .py files names they must not to be the same names as third-party modules.
- The name `data` is a terrible, generic variable name, because literally all
variables contain data. The same problems with `var`, `temp`