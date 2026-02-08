# $pagefile->install($filename)

Source: `wire/core/Pagefile.php`

Install this Pagefile

Implies copying the file to the correct location (if not already there), and populating its name.
The given $filename may be local (path) or external (URL).

## Usage

~~~~~
// basic usage
$result = $pagefile->install($filename);
~~~~~

## Hookable

- Hookable method name: `install`
- Implementation: `___install`
- Hook with: `$pagefile->install()`

## Arguments

- `$filename` `string` Full path and filename of file to install, or http/https URL to pull file from.

## Exceptions

- `WireException`
