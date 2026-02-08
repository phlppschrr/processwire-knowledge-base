# $pagefiles->delete($item): $this

Source: `wire/core/Pagefiles.php`

Delete a pagefile item

Deletes the filename associated with the Pagefile and removes it from this Pagefiles array.
The actual deletion of the file does not take effect until `$page->save()`.

## Usage

~~~~~
// basic usage
$result = $pagefiles->delete($item);
~~~~~

## Hookable

- Hookable method name: `delete`
- Implementation: `___delete`
- Hook with: `$pagefiles->delete()`

## Arguments

- `$item` `Pagefile|string` Pagefile or basename

## Return value

- `$this`
