# $notice->getName(): string

Source: `wire/core/Notice.php`

Get the name for this type of Notice

This name is used for notice logs when Notice::log or Notice::logOnly flag is used.

## Usage

~~~~~
// basic usage
$string = $notice->getName();
~~~~~

## Return value

- `string` Name of log (basename)
