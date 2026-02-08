# Page::meta()

Source: `wire/core/Page.php`

Get or set page’s persistent meta data

This meta data is managed in the DB. Setting a value immediately saves it in the DB, while
getting a value immediately loads it from the DB. As a result, this data is independent of the
usual Page load and save operations. This is primarily for internal core use, but may be
useful for other specific non-core purposes as well.

Note that this data is tied to the page where you call it. Meta data is completely free-form
and has no connection to ProcessWire fields.

Values for meta data must be basic PHP types, whether arrays, strings, numbers, etc. Please do
not use objects for meta values at this time.

~~~~~
// set and save a meta value
$page->meta()->set('colors', [ 'red', 'green', 'blue' ]);

// get a meta value
$colors = $page->meta()->get('colors');

// alternate shorter syntax for either of the above
$page->meta('colors', [ 'red', 'green', 'blue' ]); // set
$colors = $page->meta('colors'); // get

// delete a meta value
$page->meta()->remove('colors');

// get the WireDataDB instance that stores the meta values,
// it has all the same methods as WireData objects...
$meta = $page->meta();

// ...such as, get all values in an array:
$values = $meta->getArray();
~~~~~


@param string|bool $key Omit to get the WireData instance or specify property name to get or set.

@param null|mixed $value Value to set for given $key or omit if getting a value.

@return WireDataDB|string|array|int|float

@since 3.0.133
