# $process->executed($method)

Source: `wire/core/Process.php`

Hookable method automatically called after execute() method has finished.

## Usage

~~~~~
// basic usage
$result = $process->executed($method);
~~~~~

## Hookable

- Hookable method name: `executed`
- Implementation: `___executed`
- Hook with: `$process->executed()`

## Arguments

- `$method` `string` Name of method that was executed
