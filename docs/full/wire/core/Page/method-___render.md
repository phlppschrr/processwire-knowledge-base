# $page->___render($options = [], $options2 = null): string|mixed

Source: `wire/core/Page.php`

Render output of this Page or a Field

You may optionally specify 1-2 arguments to the method. The first argument may be any of the following:

1. An `$options` array with predefined options or custom variables (see arguments definition).
2. A filename to use for render (in /site/templates/). When used, you can optionally specify an `$options` array as the 2nd argument.
3. A field name to render. An optional 2nd argument can be a filename (in /site/templates/fields/) to use to render the field,
   though we'd recommend just using the `renderField()` method instead.

If using the `$options` array argument (whether 1st or 2nd argument), you may use it to specify your own variables to pass along to the
template file, and those values will be available in a variable named `$options` within the scope of the template file
(see examples below).

~~~~~
// regular page render call
$out = $page->render();

// render using given file (in /site/templates/)
$out = $page->render('basic-page.php');

// render while passing in custom variables
$out = $page->render([
  'firstName' => 'Ryan',
  'lastName' => 'Cramer'
]);

// in your template file, you can access the passed-in variables like this:
echo "<p>Full name: $options[firstName] $options[lastName]</p>";
~~~~~

Note: If the page’s template has caching enabled, then this method will return a cached page render (when available)
or save a new cache. Caches are only saved on guest users.

For simpler and more specific methods, we recommend using, hooking or overriding `renderPage()` or `renderField()` instead.

## Arguments

- `$options` (optional) `array|string` String of filename to use for render, field name to render, or array of options: - `foo_bar` (mixed): Specify any of your own variable names and values to send to the template file (foo_bar is just an example, use your own). - `filename` (string): Filename to render, typically relative to /site/templates/. But absolute paths must resolve somewhere in PW’s install. (default='') - `prependFile` (string): Filename to prepend to output, must be in /site/templates/ (default=$config->prependTemplateFile) - `prependFiles` (array): Array of additional filenames to prepend to output, must be relative to /site/templates/. - `appendFile` (string): Filename to append to output, must be in /site/templates/. - `appendFiles` (array): Array of additional filenames to append to output, must be relative to /site/templates/. - `pageStack` (array): An array of pages, when recursively rendering. Used internally. You can examine it but not change it. - `allowCache` (bool): Allow cache to be used when template settings ask for it? (default=true) - `forceBuildCache` (bool): If true, the cache will be re-created for this page, regardless of whether it’s expired or not. (default=false) -  Note that the prepend and append options above have default values in `$config` or with the Template.
- `$options2` (optional) `array` If a filename or field name was used for $options then you may optionally specify options array here instead.

## Return value

string|mixed

## Throws

- WireException

## See also

- [Page::renderPage()](method-___renderpage.md)
- [Page::renderField()](method-___renderfield.md)
- [Page::renderValue()](method-___rendervalue.md)
