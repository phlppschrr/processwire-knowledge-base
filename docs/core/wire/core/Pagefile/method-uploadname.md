# $pagefile->uploadName(): string

Source: `wire/core/Pagefile.php`

Original and unsanitized filename at the time it was uploaded

Returned value is also entity encoded if $page’s output formatting state is ON.
For files uploaded in ProcessWire 3.0.212 or newer. Falls back to current file
basename for files that were uploaded prior to 3.0.212.

## Return value

string

## Since

3.0.212
