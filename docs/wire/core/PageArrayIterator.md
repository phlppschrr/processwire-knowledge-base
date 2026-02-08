# PageArrayIterator

Source: `wire/core/PageArrayIterator.php`

PageArrayIterator for iteration of Page objects in a lazy-loaded fashion

The custom Iterator that finds real Pages in chunks (in advance, and on demand), enabling memory
safety while maintaining reasonable speeds when iterating over a large set of Pages.

Thanks to Avoine and @sforsman for this.

## __construct()

Construct

@param array $lazypages

@param array $options Options provided to $pages->find()

## loadChunk()

Retrieves the next chunk of real pages

## rewind()

Rewind to beginning

## current()

Get current Page

@return Page

## key()

Get current key/position

@return int

## next()

Update current position to next

## valid()

Return whether or not there are more items after current position

@return bool
