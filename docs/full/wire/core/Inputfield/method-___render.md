# $inputfield->render(): string

Source: `wire/core/Inputfield.php`

Render the HTML input element(s) markup, ready for insertion in an HTML form.

This is an abstract method that descending Inputfield module classes are required to implement.

## Usage

~~~~~
// basic usage
$string = $inputfield->render();
~~~~~

## Hookable

- Hookable method name: `render`
- Implementation: `___render`
- Hook with: `$inputfield->render()`

## Return value

- `string`
