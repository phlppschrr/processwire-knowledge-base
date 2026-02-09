# PageimageVariations

Source: `wire/core/PageimageVariations.php`

Inherits: `Wire`
Implements: `IteratorAggregate`, `Countable`

ProcessWire PageimageVariations

Helper class for Pageimage that handles variation collection methods


@since 3.0.137

Methods:
- [`__construct(Pageimage $pageimage)`](method-__construct.md)
- [`count(array $options = array()): int`](method-count.md)
- [`getInfo(string $basename, array|bool $options = array()): bool|string|array`](method-getinfo.md)
- [`find(array $options = array()): Pageimages|array|int`](method-find.md)
- [`rebuild(int $mode = 0, array $suffix = array(), array $options = array()): array`](method-rebuild.md)
- [`remove(array $options = array()): $this|array`](method-remove.md)
- [`removeExtras(Pageimage $pageimage, array &$deletedFiles, array $options)`](method-removeextras.md)
