# Page::preload()

Source: `wire/core/Page.php`

Preload multiple fields together as a group (experimental)

This is an optimization that enables you to load the values for multiple fields into
a page at once, and often in a single query. For fields where it is supported, and
for cases where you have a lot of fields to load at once, it can be up to 50% faster
than the default of lazy-loading fields.

To use, call `$page->preload([ 'field1', 'field2', 'etc.' ])` before accessing
`$page->field1`, `$page->field2`, etc.

The more fields you give this method, the more performance improvement it can offer.
As a result, don't bother if with only a few fields, as it's less likely to make
a difference at small scale. You will also see a more measurable benefit if preloading
fields for lots of pages at once.

Preload works with some Fieldtypes and not others. For details on what it is doing,
specify `true` for the `debug` option which will make it return array of what it
loaded and what it didn't. Have a look at this array with TracyDebugger or output
a print_r() call on it, and the result is self explanatory.

NOTE: This function is currently experimental, recommended for testing only.

~~~~~
// Example usage
$page->preload([ 'headline', 'body', 'sidebar', 'intro', 'summary' ]);
echo "
  <h1 id='headline'>$page->headline</h1>";
  <div id='intro'>$page->intro</div>
  <div id='body'>$page->body</div>
  <aside id='sidebar' pw-append>$page->sidebar</aside>
  <meta id='meta-description'>$page->summary</meta>
";
~~~~~

@param array $fieldNames Names of fields to preload or omit (or blank array)
  to preload all supported fields.

@param array $options Options to modify default behavior:
- `debug` (bool): Specify true to return additional info in returned array (default=false).
- See the `PagesLoader::preloadFields()` method for additional options.

@return array Array of details

@since 3.0.243
