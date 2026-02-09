# PageimageVariations

Source: `wire/core/PageimageVariations.php`

Inherits: `Wire`
Implements: `IteratorAggregate`, `Countable`

ProcessWire PageimageVariations

Helper class for Pageimage that handles variation collection methods


@since 3.0.137

Methods:
- [`__construct(Pageimage $pageimage)`](method-__construct.md) Construct
- [`count(array $options = array()): int`](method-count.md) Return a total or filtered count of variations
- [`getInfo(string $basename, array|bool $options = array()): bool|string|array`](method-getinfo.md) Given a file name (basename), return array of info if this is a variation for this instance’s file, or false if not.
- [`find(array $options = array()): Pageimages|array|int`](method-find.md) Get all size variations of this image
- [`rebuild(int $mode = 0, array $suffix = array(), array $options = array()): array`](method-rebuild.md) Rebuilds variations of this image
- [`remove(array $options = array()): $this|array`](method-remove.md) Delete all the alternate sizes associated with this Pageimage
- [`removeExtras(Pageimage $pageimage, array &$deletedFiles, array $options)`](method-removeextras.md) Remove extras
