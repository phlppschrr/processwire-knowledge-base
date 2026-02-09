# $wireFileTools->includeOnce($filename, array $vars = array(), array $options = array()): bool

Source: `wire/core/WireFileTools.php`

Same as include() method except that file will not be executed if it as previously been included

See the `WireFileTools::include()` method for details, arguments and options.

## Usage

~~~~~
// basic usage
$bool = $wireFileTools->includeOnce($filename);

// usage with all arguments
$bool = $wireFileTools->includeOnce($filename, array $vars = array(), array $options = array());
~~~~~

## Arguments

- `$filename` `string`
- `$vars` (optional) `array`
- `$options` (optional) `array`

## Return value

- `bool`

## See Also

- [WireFileTools::include()](method-___include.md)

## Since

3.0.96
