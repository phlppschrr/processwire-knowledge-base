# PagesLoader::preloadAllFields()

Source: `wire/core/PagesLoader.php`

Preload all supported fields for given page (experimental)

NOTE: This function is currently experimental, recommended for testing only.


@param Page $page Page to preload fields for

@param array $options
 - `debug` (bool): Specify true to return array of debug info (default=false).
 - `skipFieldNames` (array): Optional names of fields to skip over (default=[]).
 - See the `PagesLoader::preloadFields()` method for additional options.

@return array Array of details

@since 3.0.243
