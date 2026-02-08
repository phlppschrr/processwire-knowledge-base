# $process->breadcrumb($href, $label): $this

Source: `wire/core/Process.php`

Add a breadcrumb

## Example

~~~~~
$this->breadcrumb("../", "Widgets");
~~~~~

## Usage

~~~~~
// basic usage
$result = $process->breadcrumb($href, $label);
~~~~~

## Hookable

- Hookable method name: `breadcrumb`
- Implementation: `___breadcrumb`
- Hook with: `$process->breadcrumb()`

## Arguments

- `$href` `string` URL of breadcrumb
- `$label` `string` Label for breadcrumb

## Return value

- `$this`
