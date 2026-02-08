# $templateFile->___render(): string|array

Source: `wire/core/TemplateFile.php`

Render the template: execute it and return its output

## Usage

~~~~~
// basic usage
$string = $templateFile->___render();
~~~~~

## Return value

- `string|array` The output of the Template File

## Exceptions

- `WireException|\Exception` Throws WireException if file not exist + any exceptions thrown by included file(s)
