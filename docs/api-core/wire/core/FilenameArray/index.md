# FilenameArray

Source: `wire/core/FilenameArray.php`

Inherits: `Wire`
Implements: `IteratorAggregate`, `Countable`

ProcessWire FilenameArray

Manages array of filenames or file URLs, like for $config->scripts and $config->styles.

Methods:
- [`add(string $filename): $this`](method-add.md) Add a file
- [`getKey(string $filename): string`](method-getkey.md) Get key for $filename that excludes query strings
- [`prepend(string $filename): $this`](method-prepend.md) Prepend $filename to the beginning
- [`append(string $filename): FilenameArray`](method-append.md) Append $filename to the end
- [`getIterator(): \ArrayObject`](method-getiterator.md) Make iterable
- [`urls(bool|null|string $useVersion = null): array`](method-urls.md) Get cache-busting URLs for this FilenameArray
- [`unique(): FilenameArray`](method-unique.md) Make FilenameArray unique (deprecated)
- [`remove(string $filename): $this`](method-remove.md) Remove filename
- [`removeAll(): $this`](method-removeall.md) Remove all filenames
- [`replace(string $oldFile, string $newFile): $this`](method-replace.md) Replace one file with another
- [`__toString(): string`](method-__tostring.md) String value containing print_r() dump of all filenames
- [`count(): int`](method-count.md) Return count of items in this FilenameArray
