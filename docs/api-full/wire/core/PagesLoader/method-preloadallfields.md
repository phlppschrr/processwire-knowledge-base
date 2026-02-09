# $pagesLoader->preloadAllFields(Page $page, $options = array()): array

Source: `wire/core/PagesLoader.php`

Preload all supported fields for given page (experimental)

NOTE: This function is currently experimental, recommended for testing only.

## Usage

~~~~~
// basic usage
$array = $pagesLoader->preloadAllFields($page);

// usage with all arguments
$array = $pagesLoader->preloadAllFields(Page $page, $options = array());
~~~~~

## Arguments

- `$page` `Page` Page to preload fields for
- `$options` (optional) `array` - `debug` (bool): Specify true to return array of debug info (default=false). - `skipFieldNames` (array): Optional names of fields to skip over (default=[]). - See the `PagesLoader::preloadFields()` method for additional options.

## Return value

- `array` Array of details

## Since

3.0.243
