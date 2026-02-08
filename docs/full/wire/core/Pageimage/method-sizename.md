# $pageimage->sizeName($name, array $options = array()): Pageimage

Source: `wire/core/Pageimage.php`

Return image of size indicated by predefined setting

Settings for predefined sizes can be specified in `$config->imageSizes` array.
Each named item in this array must contain at least 'width' and 'height, but can also
contain any other option from the `Pageimage::size()` argument `$options`.

## Arguments

- `$name` `string` Image size name
- `$options` (optional) `array` Optionally add or override options defined for size.

## Return value

Pageimage

## Throws

- WireException If given a $name that is not present in $config->imageSizes

## Since

3.0.151
