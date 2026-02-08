# $pageimageVariations->remove(array $options = array()): $this|array

Source: `wire/core/PageimageVariations.php`

Delete all the alternate sizes associated with this Pageimage

## Arguments

- `$options` (optional) `array` See options for getVariations() method to limit what variations are removed, plus these: - `dryRun` (bool): Do not remove now and instead only return the filenames of variations that would be deleted (default=false). - `getFiles` (bool): Return deleted filenames? Also assumed if the test option is used (default=false).

## Return value

$this|array Returns $this by default, or array of deleted filenames if the `getFiles` option is specified
