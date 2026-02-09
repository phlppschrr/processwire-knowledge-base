# $pagefile->filemtime($reset = false): int

Source: `wire/core/Pagefile.php`

Get last modified time of file

## Usage

~~~~~
// basic usage
$int = $pagefile->filemtime();

// usage with all arguments
$int = $pagefile->filemtime($reset = false);
~~~~~

## Arguments

- `$reset` (optional) `bool`

## Return value

- `int` Unix timestamp

## Since

3.0.154
