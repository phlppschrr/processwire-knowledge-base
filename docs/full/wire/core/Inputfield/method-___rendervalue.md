# $inputfield->renderValue(): string

Source: `wire/core/Inputfield.php`

Render just the value (not input) in text/markup for presentation purposes.

## Usage

~~~~~
// basic usage
$string = $inputfield->renderValue();
~~~~~

## Hookable

- Hookable method name: `renderValue`
- Implementation: `___renderValue`
- Hook with: `$inputfield->renderValue()`

## Return value

- `string` Text or markup where applicable
