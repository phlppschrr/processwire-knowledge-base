# $functionsAPI->region($key = '', $value = null): string|null|bool|array

Source: `wire/core/FunctionsAPI.php`

Get or set an output region (primarily for front-end output usage)

This function is an convenience for storing markup that ultimately gets output in a _main.php file
(or whatever file `$config->appendTemplateFile` is set to). It is an alternative to passing variables
between included files and provides an interface for setting, appending, prepending and ultimately
getting markup (or other strings) for output. It’s designed for use the the “Delayed Output” strategy,
though does not necessarily require it.

This function can also be accessed as `wireRegion()`, and that function is always available
regardless of whether the Functions API is enabled or not.

*Note: unlike other functions in the Functions API, this function is not related to API variables.*

~~~~~
// define a region
region('content', '<p>this is some content</p>');

// prepend some text to region
region('+content', '<h2>Good morning</h2>');

// append some text to region
region('content+', '<p><small>Good night</small></p>');

// output a region
echo region('content');

// get all regions in an array
$regions = region('*');

// clear the 'content' region
region('content', '');

// clear all regions
region('*', '');
~~~~~

## Arguments

- string $key Name of region to get or set. - Specify "*" to retrieve all defined regions in an array. - Prepend a "+" to the region name to have it prepend your given value to any existing value. - Append a "+" to the region name to have it append your given value to any existing value. - Prepend a "++" to region name to make future calls without "+" automatically prepend. - Append a "++" to region name to make future calls without "+" to automatically append.
- null|string $value If setting a region, the text that you want to set.

## Return value

string|null|bool|array Returns string of text when getting a region, NULL if region not set, or TRUE if setting region.
