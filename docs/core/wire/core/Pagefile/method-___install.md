# $pagefile->___install($filename)

Source: `wire/core/Pagefile.php`

Install this Pagefile

Implies copying the file to the correct location (if not already there), and populating its name.
The given $filename may be local (path) or external (URL).

## Arguments

- `$filename` `string` Full path and filename of file to install, or http/https URL to pull file from.

## Throws

- WireException
