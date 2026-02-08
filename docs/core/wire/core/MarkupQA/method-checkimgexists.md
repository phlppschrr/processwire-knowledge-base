# $markupQA->checkImgExists(Pageimage $pagefile, $img, $src, &$value): int

Source: `wire/core/MarkupQA.php`

Attempt to re-create images that don't exist, when possible

## Arguments

- `$pagefile` `Pageimage`
- $img
- $src
- $value

## Return value

int Returns 0 on no change, negative count on broken, positive count on fixed
