# $page->getInputfields($fieldName = ''): null|InputfieldWrapper

Source: `wire/core/Page.php`

Hookable version of getInputfields() method.

See the getInputfields() method above for documentation details.

## Usage

~~~~~
// basic usage
$page->getInputfields();

// usage with all arguments
$page->getInputfields($fieldName = '');
~~~~~

## Hookable

- Hookable method name: `getInputfields`
- Implementation: `___getInputfields`
- Hook with: `$page->getInputfields()`

## Arguments

- `$fieldName` (optional) `string|array`

## Return value

- `null|InputfieldWrapper` Returns an InputfieldWrapper array of Inputfield objects, or NULL on failure.
