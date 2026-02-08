# $process->headline($headline): $this

Source: `wire/core/Process.php`

Set the current primary headline to appear in the admin interface

## Example

~~~~~
$this->headline("Hello World");
~~~~~

## Usage

~~~~~
// basic usage
$result = $process->headline($headline);
~~~~~

## Hookable

- Hookable method name: `headline`
- Implementation: `___headline`
- Hook with: `$process->headline()`

## Arguments

- `$headline` `string`

## Return value

- `$this`
