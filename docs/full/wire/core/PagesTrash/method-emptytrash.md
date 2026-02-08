# $pagesTrash->emptyTrash(array $options = array()): int|array

Source: `wire/core/PagesTrash.php`

Delete all pages in the trash

Populates error notices when there are errors deleting specific pages.

## Usage

~~~~~
// basic usage
$int = $pagesTrash->emptyTrash();

// usage with all arguments
$int = $pagesTrash->emptyTrash(array $options = array());
~~~~~

## Arguments

- `$options` (optional) `array` - `chunkSize` (int): Pages will be deleted in chunks of this many pages per chunk (default=100). - `chunkTimeLimit` (int): Maximum seconds allowed to process deletion of each chunk (default=600). - `chunkLimit' (int): Maximum chunks to process in an emptyTrash() call (default=1000); - `pageLimit` (int): Maximum pages to delete per emptyTrash() call (default=0, no limit). - `timeLimit` (int): Maximum time (in seconds) to allow for trash empty (default=3600). - `pass2` (bool): Perform a secondary pass using alternate method as a backup? (default=true) Note: pass2 is always disabled when a pageLimit is in use or timeLimit has been exceeded. - `verbose` (bool): Return verbose array of information about the trash empty process? For debug/dev purposes (default=false)

## Return value

- `int|array` Returns integer (default) or array in verbose mode. - By default, returns total number of pages deleted from trash. This number is negative or 0 if not all pages could be deleted and error notices may be present. - Returns associative array with verbose information if verbose option is chosen.
