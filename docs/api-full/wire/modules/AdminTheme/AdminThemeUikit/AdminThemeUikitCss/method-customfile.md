# $adminThemeUikitCss->customFile($file, $requireExtension = ''): string

Source: `wire/modules/AdminTheme/AdminThemeUikit/AdminThemeUikitCss.php`

Apply custom file/path replacements

## Usage

~~~~~
// basic usage
$string = $adminThemeUikitCss->customFile($file);

// usage with all arguments
$string = $adminThemeUikitCss->customFile($file, $requireExtension = '');
~~~~~

## Arguments

- `$file` `string`
- `$requireExtension` (optional) `string` Extension to require on given file

## Return value

- `string`
