# PageValues

Source: `wire/core/PageValues.php`

ProcessWire Page Values

Provides implementation for several Page value get() functions.

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

@since 3.0.205

## getDotValue()

Given a 'field.subfield' type string traverse properties and return value

@param Page $page

@param string $key

@return mixed|null

## getBracketValue()

Get value that ends with square brackets to get iterable value, filtered value or property value

~~~~~
$iterableValue = $page->get('field_name[]');
~~~~~
Note: When requesting an iterable value, this method will return an empty array in cases where
the Page::get() method would return null.

@param Page $page

@param string $key

@param mixed $value Value to use rather than pulling from $page

@return array|mixed|Page|PageArray|Wire|WireArray|WireData|string|\Traversable

## getMultiple()

Get multiple Page property/field values in an array

This method works exactly the same as the `get()` method except that it accepts an
array (or CSV string) of properties/fields to get, and likewise returns an array
of those property/field values. By default it returns a regular (non-indexed) PHP
array in the same order given. To instead get an associative array indexed by the
property/field names given, specify `true` for the `$assoc` argument.

~~~~~
// returns regular array i.e. [ 'foo val', 'bar val' ]
$a = $page->getMultiple([ 'foo', 'bar' ]);
list($foo, $bar) = $a;

// returns associative array i.e. [ 'foo' => 'foo val', 'bar' => 'bar val' ]
$a = $page->getMultiple([ 'foo', 'bar' ], true);
$foo = $a['foo'];
$bar = $a['bar'];

// CSV string can also be used instead of array
$a = $page->getMultiple('foo,bar');
~~~~~

@param page $page

@param array|string $keys Array or CSV string of properties to get.

@param bool $assoc Get associative array indexed by given properties? (default=false)

@return array

## getFieldFirstValue()

Given a Multi Key, determine if there are multiple keys requested and return the first non-empty value

A Multi Key is a string with multiple field names split by pipes, i.e. headline|title

Example: browser_title|headline|title - Return the value of the first field that is non-empty

@param page $page

@param string $multiKey

@param bool $getKey Specify true to get the first matching key (name) rather than value

@return null|mixed Returns null if no values match, or if there aren't multiple keys split by "|" chars

## getMarkup()

Return the markup value for a given field name or {tag} string

1. If given a field name (or `name.subname` or `name1|name2|name3`) it will return the
   markup value as defined by the fieldtype.
2. If given a string with field names referenced in `{tags}`, it will populate those
   tags and return the populated string.

@param Page $page

@param string $key Field name or markup string with field {name} tags in it

@return string

@see Page::getText()

## getText()

Same as getMarkup() except returned value is plain text

If no `$entities` argument is provided, returned value is entity encoded when output formatting
is on, and not entity encoded when output formatting is off.

@param Page $page

@param string $key Field name or string with field {name} tags in it.

@param bool $oneLine Specify true if returned value must be on single line.

@param bool|null $entities True to entity encode, false to not. Null for auto, which follows page's outputFormatting state.

@return string

@see Page::getMarkup()

## setStatus()

Set the status setting, with some built-in protections

This method is also used when you set status directly, i.e. `$page->status = $value;`.

~~~~~
// set status to unpublished
$page->setStatus('unpublished');

// set status to hidden and unpublished
$page->setStatus('hidden, unpublished');

// set status to hidden + unpublished using Page constant bitmask
$page->setStatus(Page::statusHidden | Page::statusUnpublished);
~~~~~

@param Page $page

@param int|array|string Status value, array of status names or values, or status name string.

@return Page

@see Page::addStatus(), Page::removeStatus()

## removeStatus()

Remove the specified status from this page

This is the preferred way to remove a status from a page. There is also a corresponding `Page::addStatus()` method.

~~~~~
// Remove hidden status from the page using status name
$page->removeStatus('hidden');

// Remove hidden status from the page using status constant
$page->removeStatus(Page::statusHidden);
~~~~~

@param Page $page

@param int|string $statusFlag Status flag constant or string representation (hidden, locked, unpublished, etc.)

@return Page

@throws WireException If you attempt to remove `Page::statusSystem` or `Page::statusSystemID` statuses without first adding `Page::statusSystemOverride` status.

@see Page::addStatus(), Page::hasStatus()

## setName()

Set the page name, optionally for specific language

~~~~~
// Set page name (default language)
$page->setName('my-page-name');

// This is equivalent to the above
$page->name = 'my-page-name';

// Set page name for Spanish language
$page->setName('la-cerveza', 'es');
~~~~~

@param string $value Page name that you want to set

@param Language|string|int|null $language Set language for name (can also be language name or string in format "name1234")

@return Page

## getInputfields()

Return all Inputfield objects necessary to edit this page

This method returns an InputfieldWrapper object that contains all the custom Inputfield objects
required to edit this page. You may also specify a `$fieldName` argument to limit what is contained
in the returned InputfieldWrapper.

Please note this method deals only with custom fields, not system fields name 'name' or 'status', etc.,
as those are exclusive to the ProcessPageEdit page editor.


@param string|array $fieldName Optional field to limit to, typically the name of a fieldset or tab.
 - Or optionally specify array of $options (See `Fieldgroup::getPageInputfields()` for options).

@return null|InputfieldWrapper Returns an InputfieldWrapper array of Inputfield objects, or NULL on failure.

## getInputfield()

Get a single Inputfield for the given field name

- If requested field name refers to a single field, an Inputfield object is returned.
- If requested field name refers to a fieldset or tab, then an InputfieldWrapper representing will be returned.
- Returned Inputfield already has values populated to it.
- Please note this method deals only with custom fields, not system fields name 'name' or 'status', etc.,
  as those are exclusive to the ProcessPageEdit page editor.


@param string $fieldName

@return Inputfield|InputfieldWrapper|null Returns Inputfield, or null if given field name doesn't match field for this page.

## getField()

Get a Field object in context or NULL if not valid for this page

Field in context is only returned when output formatting is on.


@param Page $page

@param string|int|Field $field

@return Field|null

@todo determine if we can always retrieve in context regardless of output formatting.

## getFields()

Returns a FieldsArray of all Field objects in the context of this Page

Unlike $page->fieldgroup (or its alias $page->fields), the fields returned from
this method are in the context of this page/template. Meaning returned Field
objects may have some properties that are different from the Field outside of
the context of this page.


@param Page $page

@return FieldsArray of Field objects

## hasField()

Returns whether or not given $field name, ID or object is valid for this Page

Note that this only indicates validity, not whether the field is populated.


@param Page $page

@param int|string|Field|array $field Field name, object or ID to check.
 - In 3.0.126+ this may also be an array or pipe "|" separated string of field names to check.

@return bool|string True if valid, false if not.
 - In 3.0.126+ returns first matching field name if given an array of field names or pipe separated string of field names.

## getFieldValue()

Get the value for a non-native page field, and call upon Fieldtype to join it if not autojoined

@param string $key Name of field to get

@param string $selector Optional selector to filter load by...
  ...or, if not in selector format, it becomes an __invoke() argument for object values .

@return null|mixed

## formatFieldValue()

Return a value consistent with the page’s output formatting state

This is primarily for use as a helper to the getFieldValue() method.

@param Page $page

@param Field $field

@param mixed $value

@return mixed
