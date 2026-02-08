# $pagefiles->___delete($item): $this

Source: `wire/core/Pagefiles.php`

Delete a pagefile item

Deletes the filename associated with the Pagefile and removes it from this Pagefiles array.
The actual deletion of the file does not take effect until `$page->save()`.

## Usage

~~~~~
// basic usage
$result = $pagefiles->___delete($item);
~~~~~

## Arguments

- `$item` `Pagefile|string` Pagefile or basename

## Return value

- `$this`
