# $wireMarkupFileRegions->applyRegionLinks(&$html, $basename, $url, $ext, array $options): string

Source: `wire/core/WireMarkupFileRegions.php`

Apply region links (optional)

For example: Converts the `main.css` in `<link rel="stylesheet" href="main.css">`
to `/site/assets/markup-regions/main.css`.

If the autoInsert option is enabled and there is no existing `main.css` to update then it will return
a string with the `<link>` tag to main.css in it.

## Arguments

- `$html` `string`
- `$basename` `string`
- `$url` `string`
- `$ext` `string`
- `$options` `array`

## Return value

string

## Since

3.0.254
