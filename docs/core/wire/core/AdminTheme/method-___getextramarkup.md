# $adminTheme->getExtraMarkup(): array

Source: `wire/core/AdminTheme.php`

Enables hooks to append extra markup to various sections of the admin page

## Usage

~~~~~
// basic usage
$array = $adminTheme->getExtraMarkup();
~~~~~

## Hookable

- Hookable method name: `getExtraMarkup`
- Implementation: `___getExtraMarkup`
- Hook with: `$adminTheme->getExtraMarkup()`

## Return value

- `array` Associative array containing the following properties, any of which may be populated or empty: - head - body - masthead - content - footer - sidebar
