# $commentStars->render($stars = 0, $allowInput = false): string

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentStars.php`

Render stars

If given a float for $stars, it will render partial stars.
If given an int for $stars, it will only render whole stars.

## Usage

~~~~~
// basic usage
$string = $commentStars->render();

// usage with all arguments
$string = $commentStars->render($stars = 0, $allowInput = false);
~~~~~

## Arguments

- `$stars` (optional) `int|float|null` Number of stars that are in active state
- `$allowInput` (optional) `bool` Whether to allow input of stars

## Return value

- `string`
