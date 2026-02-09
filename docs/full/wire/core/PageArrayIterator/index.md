# PageArrayIterator

Source: `wire/core/PageArrayIterator.php`

Inherits: `Wire`
Implements: `Iterator`

PageArrayIterator for iteration of Page objects in a lazy-loaded fashion

The custom Iterator that finds real Pages in chunks (in advance, and on demand), enabling memory
safety while maintaining reasonable speeds when iterating over a large set of Pages.

Thanks to Avoine and @sforsman for this.

Methods:
- [`__construct(array $lazypages, array $options = [])`](method-__construct.md)
- [`loadChunk()`](method-loadchunk.md)
- [`rewind()`](method-rewind.md)
- [`current(): Page`](method-current.md)
- [`key(): int`](method-key.md)
- [`next()`](method-next.md)
- [`valid(): bool`](method-valid.md)
