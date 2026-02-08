# $templateFile->render(): string|array

Source: `wire/core/TemplateFile.php`

Render the template: execute it and return its output

## Usage

~~~~~
// basic usage
$string = $templateFile->render();
~~~~~

## Hookable

- Hookable method name: `render`
- Implementation: `___render`
- Hook with: `$templateFile->render()`

## Return value

- `string|array` The output of the Template File

## Exceptions

- `WireException|\Exception` Throws WireException if file not exist + any exceptions thrown by included file(s)
