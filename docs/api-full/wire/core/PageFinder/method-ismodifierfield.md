# $pageFinder->isModifierField($name): string

Source: `wire/core/PageFinder.php`

Is given field name a modifier that does not directly refer to a field or column name?

## Usage

~~~~~
// basic usage
$string = $pageFinder->isModifierField($name);
~~~~~

## Arguments

- `$name` `string`

## Return value

- `string` Returns normalized modifier name if a modifier or boolean false if not
