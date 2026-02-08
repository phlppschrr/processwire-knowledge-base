# $adminTheme->___getExtraMarkup(): array

Source: `wire/core/AdminTheme.php`

Enables hooks to append extra markup to various sections of the admin page

## Usage

~~~~~
// basic usage
$array = $adminTheme->___getExtraMarkup();
~~~~~

## Return value

- `array` Associative array containing the following properties, any of which may be populated or empty: - head - body - masthead - content - footer - sidebar
