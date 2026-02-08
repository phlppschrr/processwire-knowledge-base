# PagesLoader::preloadFields()

Source: `wire/core/PagesLoader.php`

Preload/Prefetch fields for page together as a group (experimental)

This is an optimization that enables you to load the values for multiple fields into
a page at once, and often in a single query. This is similar to the `joinFields` option
when loading a page, or the `autojoin` option configured with a field, except that it
can be used after a page is already loaded. It provides a performance improvement
relative lazy-loading of fields individually as they are accessed.

Preload works only with Fieldtypes that do not override the core’s loading methods.
Preload also does not work with FieldtypeMulti types at present, except for the Page
Fieldtype when configured to load a single page. Though it can be enabled for testing
purposes using the `useFieldtypeMulti` $options argument.

NOTE: This function is currently experimental, recommended for testing only.


@param Page $page Page to preload fields for

@param array $fieldNames Names of fields to preload

@param array $options
 - `debug` (bool): Specify true to include additional debug info in return value (default=false).
 - `useFieldtypeMulti` (bool): Enable FieldtypeMulti for testing purposes (default=false).
 - `loadPageRefs` (bool): Optimization to early load pages in page reference fields? (default=true)

@return array Array containing what was loaded and skipped

@since 3.0.243
