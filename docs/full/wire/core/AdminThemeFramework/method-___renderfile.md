# $adminThemeFramework->renderFile($file, array $vars = array()): string

Source: `wire/core/AdminThemeFramework.php`

Render a admin theme template file

This method is only used if it is hooked

## Usage

~~~~~
// basic usage
$string = $adminThemeFramework->renderFile($file);

// usage with all arguments
$string = $adminThemeFramework->renderFile($file, array $vars = array());
~~~~~

## Hookable

- Hookable method name: `renderFile`
- Implementation: `___renderFile`
- Hook with: `$adminThemeFramework->renderFile()`

## Arguments

- `$file` `string` Full path and filename
- `$vars` (optional) `array` Associative array of variables to populate in rendered file

## Return value

- `string` Returns blank string when $echo is true

## Since

3.0.196
