# $textformatter->format(&$str)

Source: `wire/core/Textformatter.php`

Format the given text string, outside of specific Page or Field context.

## Usage

~~~~~
// basic usage
$result = $textformatter->format($str);

// usage with all arguments
$result = $textformatter->format(&$str);
~~~~~

## Arguments

- `$str` `string` String is provided as a reference, so is modified directly (not returned).
