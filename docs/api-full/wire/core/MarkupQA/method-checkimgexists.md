# $markupQA->checkImgExists(Pageimage $pagefile, $img, $src, &$value): int

Source: `wire/core/MarkupQA.php`

Attempt to re-create images that don't exist, when possible

## Usage

~~~~~
// basic usage
$int = $markupQA->checkImgExists($pagefile, $img, $src, $value);

// usage with all arguments
$int = $markupQA->checkImgExists(Pageimage $pagefile, $img, $src, &$value);
~~~~~

## Arguments

- `$pagefile` `Pageimage`
- $img
- $src
- $value

## Return value

- `int` Returns 0 on no change, negative count on broken, positive count on fixed
