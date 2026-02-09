# PageArrayIterator

Source: `wire/core/PageArrayIterator.php`

Inherits: `Wire`
Implements: `Iterator`

PageArrayIterator for iteration of Page objects in a lazy-loaded fashion

The custom Iterator that finds real Pages in chunks (in advance, and on demand), enabling memory
safety while maintaining reasonable speeds when iterating over a large set of Pages.

Thanks to Avoine and @sforsman for this.

Methods:
Method: [__construct()](method-__construct.md)
Method: [loadChunk()](method-loadchunk.md)
Method: [rewind()](method-rewind.md)
Method: [current()](method-current.md)
Method: [key()](method-key.md)
Method: [next()](method-next.md)
Method: [valid()](method-valid.md)
