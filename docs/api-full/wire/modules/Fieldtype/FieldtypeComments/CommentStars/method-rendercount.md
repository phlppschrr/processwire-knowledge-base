# $commentStars->renderCount($count, $stars = 0.0, $schema = ''): string

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentStars.php`

Render a count of ratings

## Usage

~~~~~
// basic usage
$string = $commentStars->renderCount($count);

// usage with all arguments
$string = $commentStars->renderCount($count, $stars = 0.0, $schema = '');
~~~~~

## Arguments

- `$count` `int`
- `$stars` (optional) `float|int`
- `$schema` (optional) `string` May be "rdfa" or "microdata" or blank (default) to omit.

## Return value

- `string`
