# $pagesLoader->preloadAllFields(Page $page, $options = array()): array

Source: `wire/core/PagesLoader.php`

Preload all supported fields for given page (experimental)

NOTE: This function is currently experimental, recommended for testing only.

## Arguments

- Page $page Page to preload fields for
- array $options - `debug` (bool): Specify true to return array of debug info (default=false). - `skipFieldNames` (array): Optional names of fields to skip over (default=[]). - See the `PagesLoader::preloadFields()` method for additional options.

## Return value

array Array of details

## Meta

- @since 3.0.243
