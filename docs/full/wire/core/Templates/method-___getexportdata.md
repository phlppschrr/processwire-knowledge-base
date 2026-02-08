# $templates->getExportData(Template $template): array

Source: `wire/core/Templates.php`

Export Template data for external use

## Usage

~~~~~
// basic usage
$array = $templates->getExportData($template);

// usage with all arguments
$array = $templates->getExportData(Template $template);
~~~~~

## Hookable

- Hookable method name: `getExportData`
- Implementation: `___getExportData`
- Hook with: `$templates->getExportData()`

## Arguments

- `$template` `Template` Template you want to export

## Return value

- `array` Associative array of export data
