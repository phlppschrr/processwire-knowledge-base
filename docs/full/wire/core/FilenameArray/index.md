# FilenameArray

Source: `wire/core/FilenameArray.php`

Inherits: `Wire`
Implements: `IteratorAggregate`, `Countable`

ProcessWire FilenameArray

Manages array of filenames or file URLs, like for $config->scripts and $config->styles.

Methods:
- [`add(string $filename): $this`](method-add.md)
- [`getKey(string $filename): string`](method-getkey.md)
- [`prepend(string $filename): $this`](method-prepend.md)
- [`append(string $filename): FilenameArray`](method-append.md)
- [`getIterator(): \ArrayObject`](method-getiterator.md)
- [`urls(bool|null|string $useVersion = null): array`](method-urls.md)
- [`unique(): FilenameArray`](method-unique.md)
- [`remove(string $filename): $this`](method-remove.md)
- [`removeAll(): $this`](method-removeall.md)
- [`replace(string $oldFile, string $newFile): $this`](method-replace.md)
- [`__toString(): string`](method-__tostring.md)
- [`count(): int`](method-count.md)
