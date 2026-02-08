# $adminThemeUikitCss->getCssFile($getPath = false): string

Source: `wire/modules/AdminTheme/AdminThemeUikit/AdminThemeUikitCss.php`

Get the primary Uikit CSS file URL to use (whether default or custom)

## Usage

~~~~~
// basic usage
$string = $adminThemeUikitCss->getCssFile();

// usage with all arguments
$string = $adminThemeUikitCss->getCssFile($getPath = false);
~~~~~

## Arguments

- `$getPath` (optional) `bool` Get disk path rather than URL?

## Return value

- `string`
