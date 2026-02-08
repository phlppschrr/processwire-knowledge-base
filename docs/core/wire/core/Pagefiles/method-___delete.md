# $pagefiles->___delete($item): $this

Source: `wire/core/Pagefiles.php`

Delete a pagefile item

Deletes the filename associated with the Pagefile and removes it from this Pagefiles array.
The actual deletion of the file does not take effect until `$page->save()`.

## Arguments

- Pagefile|string $item Pagefile or basename

## Return value

$this
