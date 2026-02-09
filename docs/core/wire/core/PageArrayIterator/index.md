# PageArrayIterator

Source: `wire/core/PageArrayIterator.php`

Inherits: `Wire`
Implements: `Iterator`

PageArrayIterator for iteration of Page objects in a lazy-loaded fashion

The custom Iterator that finds real Pages in chunks (in advance, and on demand), enabling memory
safety while maintaining reasonable speeds when iterating over a large set of Pages.

Thanks to Avoine and @sforsman for this.

Methods:
- [`__construct(array $lazypages, array $options = [])`](method-__construct.md) Construct
- [`loadChunk()`](method-loadchunk.md) Retrieves the next chunk of real pages
- [`rewind()`](method-rewind.md) Rewind to beginning
- [`current(): Page`](method-current.md) Get current Page
- [`key(): int`](method-key.md) Get current key/position
- [`next()`](method-next.md) Update current position to next
- [`valid(): bool`](method-valid.md) Return whether or not there are more items after current position
