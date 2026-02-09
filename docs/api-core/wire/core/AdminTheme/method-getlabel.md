# $adminTheme->getLabel($key, $val = ''): string

Source: `wire/core/AdminTheme.php`

Get predefined translated label by key for labels shared among admin themes

## Usage

~~~~~
// basic usage
$string = $adminTheme->getLabel($key);

// usage with all arguments
$string = $adminTheme->getLabel($key, $val = '');
~~~~~

## Arguments

- `$key` `string`
- `$val` (optional) `string` Value to return if label not available

## Return value

- `string`

## Since

3.0.162
