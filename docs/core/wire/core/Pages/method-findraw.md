# Pages::findRaw()

Source: `wire/core/Pages.php`

Find pages and return raw data from them in a PHP array

Note that the data returned from this method is raw and unformatted, directly
as it exists in the database. In most cases you should use `$pages->find()` instead,
but this method provides a convenient alternative for some cases.

The `$selector` argument can be any page-finding selector that you would provide
to a regular `$pages->find()` call. The most interesting stuff relates to the
`$field` argument though, which is what the rest of this section looks at:

If you omit the `$field` argument, it will return all data for the found pages in
an array where the keys are the page IDs and the values are associative arrays
containing all of each page raw field and property values indexed by name…
`$a = $pages->findRaw("template=blog");` …but findRaw() is more useful for cases
where you want to retrieve specific things without having to load the entire page
(or its data). Below are a few examples of how you can do this.

~~~~~
// If you provide a string (field name) for `$field`, then it will return an
// array with the values of the `data` column of that field. The `$field` can
// also be the name of a native pages table property like `id` or `name`.
$a = $pages->findRaw("template=blog", "title");

// The above would return an array of blog page titles indexed by page ID. If
// you provide an array for `$field` then it will return an array for each page,
// where each of those arrays is indexed by the field names you requested.
$a = $pages->findRaw("template=blog", [ "title", "date" ]);

// You may specify field name(s) like `field.subfield` to retrieve a specific
// column/subfield. When it comes to Page references or Repeaters, the subfield
// can also be the name of a field that exists on the Page reference or repeater.
$a = $pages->findRaw("template=blog", [ "title", "categories.title" ]);

// You can also use this format below to get multiple subfields from one field:
$a = $pages->findRaw("template=blog", [ "title", "categories" => [ "id", "title" ] ]);

// You can optionally rename fields in the returned value like this below, which
// asks the 'title' field to have the name 'headline' in return value (3.0.176+):
$a = $pages->findRaw("template=blog", [ "title" => "headline" ]);

// You may specify wildcard field name(s) like `field.*` to return all columns
// for `field`. This retrieves all columns from the field’s table. This is
// especially useful with fields like Table or Combo that might have several
// different columns:
$a = $pages->findRaw("template=villa", "rates_table.*" );

// If you prefer, you can specify the field name(s) in the selector (3.0.173+):
$a = $pages->findRaw("template=blog, field=title");
$a = $pages->findRaw("template=blog, field=title|categories.title");

// Specify “objects=1” in selector to use objects rather than associative arrays
// for pages and fields (3.0.174+):
$a = $pages->findRaw("template=blog, field=title|categories.title, objects=1");

// Specify “entities=1” to entity encode all string values:
$a = $pages->findRaw("template=blog, field=title|summary, entities=1");

// Specify “entities=field” or “entities=field1|field2” to entity encode just
// the specific fields that you name (3.0.174+):
$a = $pages->findRaw("template=blog, entities=title|summary");

// If you prefer, options can also be enabled this way (3.0.174+):
$a = $pages->findRaw("template=blog, options=objects|entities");
~~~~~

In 3.0.193 the following additional options were added for the `$field` argument:

 - Specify `parent.field_name` or `parent.parent.field_name`, etc. to return values from parent(s).
 - Specify `references` or `references.field_name`, etc. to also return values from pages referencing found pages.
 - Specify `meta` or `meta.name` to also return values from page meta data.


@param string|array|Selectors|int $selector Page matching selector or page ID

@param string|array|Field $field Name of field/property to get, or array of them, CSV string, or omit to get all (default='')
 - Optionally use associative array to rename fields in returned value, i.e. `['title' => 'label']` returns 'title' as 'label' in return value.
 - Note: this argument may also be specified in the $selector argument as "field=foo" or "field=foo|bar|baz" (3.0.173+).

@param array $options Options to adjust behavior (may also be specified in selector, i.e. “objects=1, entities=foo|bar”)
 - `objects` (bool): Use objects rather than associative arrays? (default=false) 3.0.174+
 - `entities` (bool|array): Entity encode string values? True or 1 to enable, or specify array of field names. (default=false) 3.0.174+
 - `nulls` (bool): Populate nulls for field values that are not present, rather than omitting them? (default=false) 3.0.198+
 - `indexed` (bool): Index by page ID? (default=true)
 - `flat` (bool|string): Flatten return value as `["field.subfield" => "value"]` rather than `["field" => ["subfield" => "value"]]`?
    Optionally specify field delimiter for the value, otherwise a period `.` will be used as the delimiter. (default=false) 3.0.193+
 - Any of these options above can be specified in the $selector argument as a string, i.e. `…, flat=1, entities=1`.
 - Note the `objects` and `flat` options are not meant to be used together.

@return array

@since 3.0.172
