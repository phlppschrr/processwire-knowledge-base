# $process->browserTitle($title): $this

Source: `wire/core/Process.php`

Set the current browser title tag

## Example

~~~~~
$this->browserTitle("Hello World");
~~~~~

## Usage

~~~~~
// basic usage
$result = $process->browserTitle($title);
~~~~~

## Hookable

- Hookable method name: `browserTitle`
- Implementation: `___browserTitle`
- Hook with: `$process->browserTitle()`

## Arguments

- `$title` `string`

## Return value

- `$this`
