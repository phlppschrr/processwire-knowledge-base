# CommentStars

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentStars.php`

Inherits: `WireData`

## Summary

Class CommentStars

Common methods:
- [`setDefault()`](method-setdefault.md)
- [`render()`](method-render.md)
- [`renderCount()`](method-rendercount.md)

Groups:
Group: [other](group-other.md)

Handles rendering of star ratings for comments.
Additional code in comments.js and comments.css accompanies this.

## Methods
- [`__construct()`](method-__construct.md) Construct comment stars
- [`setDefault($key, $value)`](method-setdefault.md) Change one of the defaults (see `$defaults`)
- [`render(int|float|null $stars = 0, bool $allowInput = false): string`](method-render.md) Render stars
- [`renderCount(int $count, float|int $stars = 0.0, string $schema = ''): string`](method-rendercount.md) Render a count of ratings
