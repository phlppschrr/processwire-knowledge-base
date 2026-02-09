# $pageimage->removeVariations(array $options = array()): PageImageVariations|array

Source: `wire/core/Pageimage.php`

Delete all the alternate sizes associated with this Pageimage

## Usage

~~~~~
// basic usage
$pageImageVariations = $pageimage->removeVariations();

// usage with all arguments
$pageImageVariations = $pageimage->removeVariations(array $options = array());
~~~~~

## Arguments

- `$options` (optional) `array` See options for getVariations() method to limit what variations are removed, plus these: - `dryRun` (bool): Do not remove now and instead only return the filenames of variations that would be deleted (default=false). - `getFiles` (bool): Return deleted filenames? Also assumed if the test option is used (default=false).

## Return value

- `PageImageVariations|array` Returns $this by default, or array of deleted filenames if the `getFiles` option is specified
