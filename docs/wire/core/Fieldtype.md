# Fieldtype

Source: `wire/core/Fieldtype.php`

ProcessWire Fieldtype Base

Abstract base class from which all Fieldtype modules are descended from.

Fieldtype is a module type used to represent a type of field. All Fieldtype modules descend from this.
Almost all methods in a Fieldtype are primarily of concern to module developers, as Fieldtype modules do not
have a public API (most of the time). Instead, they provide methods used by `Page` and `Field` objects (and related)
to work with the field data. Most Fieldtype modules only need to implement a few methods like
`Fieldtype::sanitizeValue()` (which is required) and `Fieldtype::getDatabaseSchema()`, as the default implementation
of most other methods provided in this Fieldtype class accounts for most situations already.

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com


Hookable methods
================

@method InputfieldWrapper getConfigInputfields(Field $field)

@method InputfieldWrapper getConfigAdvancedInputfields(Field $field)

@method array getConfigArray(Field $field)

@method array getConfigAllowContext(Field $field)

@method array exportConfigData(Field $field, array $data)

@method array importConfigData(Field $field, array $data)

@method Fieldtypes|null getCompatibleFieldtypes(Field $field)

@method mixed formatValue(Page $page, Field $field, $value)

@method string|MarkupFieldtype markupValue(Page $page, Field $field, $value = null, $property = '')

@method mixed wakeupValue(Page $page, Field $field, $value)

@method string|int|array sleepValue(Page $page, Field $field, $value)

@method string|float|int|array exportValue(Page $page, Field $field, $value, array $options = array())

@method string|float|int|array|object importValue(Page $page, Field $field, $value, array $options = array())

@method bool createField(Field $field)

@method array getSelectorInfo(Field $field, array $data = array())

@method mixed|null loadPageField(Page $page, Field $field)

@method mixed|null loadPageFieldFilter(Page $page, Field $field, $selector)

@method bool savePageField(Page $page, Field $field)

@method bool deleteField(Field $field)

@method bool deletePageField(Page $page, Field $field)

@method bool emptyPageField(Page $page, Field $field)

@method bool replacePageField(Page $src, Page $dst, Field $field)

@method bool deleteTemplateField(Template $template, Field $field)

@method Field cloneField(Field $field)

@method void renamedField(Field $field, $prevName)

@method void savedField(Field $field)

@method void saveFieldReady(Field $field)

@method void install()

@method void uninstall()

@method array getFieldSetups()

@property string $name Name of Fieldtype module.

@property string $shortName Short name of Fieldtype, which excludes the "Fieldtype" prefix.

@property string $longName Long name of Fieldtype, which is typically the module title.

## getInputfield()

Return new instance of the Inputfield module associated with this Fieldtype.


@param Page $page Page that the Inputfield will be for

@param Field $field Field that the Inputfield will be for

@return Inputfield|null Returns Inputfield or null if not applicable/available.

## ___getConfigInputfields()

Get any Inputfields used for configuration of this Fieldtype.

This is in addition to any configuration fields supplied by the Inputfield.

Classes implementing this method should call upon this parent method to obtain the InputfieldWrapper, and then
append their own Inputfields to that.

NOTE: Inputfields with a name that starts with an underscore, i.e. "_myname" are assumed to be for runtime
use and are NOT stored in the database.


@param Field $field

@return InputfieldWrapper

## ___getConfigArray()

Same as getConfigInputfields but with definition as an array instead

If both getConfigInputfields and getConfigInputfieldsArray are implemented then
definitions from both will be used. It's probably simplest just to implement one
or the other.


@param Field $field

@return array

## ___getConfigAllowContext()

Return an array of configuration field names from that are allowed in fieldgroup/template context

These field names are those that would be used for Inputfields like those returned from getConfigInputfields()
or getConfigArray().

Inputfield field names returned from here are allowed to have unique values per Fieldgroup assignment, rather
than sharing the same setting globally.


@param Field $field

@return array of Inputfield names

## ___getConfigAdvancedInputfields()

Get Inputfields for advanced settings of the Field and Fieldtype

Inputfields returned from this appear under the "Advanced" tab rather than the "Details" tab,
in the Field editor.

In most cases, you will want to implement the getConfigInputfields() or getConfigArray() rather than this method.

NOTE: Inputfields with a name that starts with an underscore, i.e. "_myname" are assumed to be for runtime
use and are NOT stored in the database.


@param Field $field

@return InputfieldWrapper

## ___exportConfigData()

Export configuration values for external consumption

Use this method to externalize any config values when necessary.
For example, internal IDs should be converted to GUIDs where possible.
Most Fieldtype modules can use the default implementation already provided here.


@param Field $field

@param array $data

@return array

## ___importConfigData()

Convert an array of exported data to a format that will be understood internally

This is the opposite of the exportConfigData() method.
Most modules can use the default implementation provided here.


@param Field $field

@param array $data

@return array Data as given and modified as needed. Also included is $data[errors], an associative array
	indexed by property name containing errors that occurred during import of config data.

## ___getCompatibleFieldtypes()

Get an array of Fieldtypes that are compatible with this one

This represents the list of Fieldtype modules that the user is allowed to change to from this one.


@param Field $field

@return Fieldtypes|null

## sanitizeValue()

Sanitize the value for runtime storage and return it.

- Implementation is required by Fieldtype modules, as this method is abstract.
- This method should remove anything that's invalid from the given value. If it can't be sanitized, it should be made blank.
- This method filters every value set to a Page instance, so it should do it's thing as quickly as possible.


@param Page $page

@param Field $field

@param string|int|WireArray|object $value

@return string|int|WireArray|object

## ___formatValue()

Format the given value for output and return a string of the formatted value

Page instances call upon this method to do any necessary formatting of a value in preparation for output,
but only if output formatting `$page->of()` is enabled. The most common use of this method is for text-only fields that
need to have some text formatting applied to them, like Markdown, SmartyPants, Textile, etc. As a result,
Fieldtype modules don't need to implement this unless it's applicable.


@param Page $page Page that the value lives on

@param Field $field Field that represents the value

@param string|int|object $value The value to format

@return mixed

## ___markupValue()

Render a markup string of the value.

Non-markup components should also be entity encoded where appropriate.

Most Fieldtypes don't need to implement this since the default covers most scenarios.

This is different from `Fieldtype::formatValue()` in that it always returns a string (or object that can be
typecast to a string) that is output ready with markup. Further, this method may be used to render
specific properties in compound Fieldtypes. The intention here is primarily for admin output purposes,
but can be used front-end where applicable.

This is different from `Inputfield::renderValue()` in that the context may be outside that of an Inputfield,
as Inputfields can have external CSS or JS dependencies.


@param Page $page Page that $value comes from

@param Field $field Field that $value comes from

@param mixed $value Optionally specify the value returned by `$page->getFormatted('field')`.
 When specified, value must be a formatted value.
	If null or not specified (recommended), it will be retrieved automatically.

@param string $property Optionally specify the property or index to render. If omitted, entire value is rendered.

@return string|MarkupFieldtype Returns a string or object that can be output as a string, ready for output.
	Return a MarkupFieldtype value when suitable so that the caller has potential specify additional
	config options before typecasting it to a string.

## getBlankValue()

Return the blank value for this fieldtype, whether that is a blank string, zero value, blank object or array

Default/non-implemented behavior is to return a blanks string.


@param Page|NullPage $page

@param Field $field

@return string|int|object|null

## isDeleteValue()

Is given value one that should cause the DB row(s) to be deleted rather than saved?

Not applicable to Fieldtypes that override the savePageField() method with their own
implementation, unless they also use this method.

@param Page $page

@param Field $field

@param mixed $value

@return bool

@since 3.0.150

## isEmptyValue()

Return whether the given value is considered empty or not.

This can be anything that might be present in a selector value and thus is
typically a string. However, it may be used outside of that purpose so you
shouldn't count on it being a string.

Example: an integer or text Fieldtype might not consider a "0" to be empty,
whereas a Page reference would.

This method is primarily used by the PageFinder::whereEmptyValuePossible()
method to determine whether to include non-present (null) rows.

3.0.164+: If given a Selector object for $value, PageFinder is proposing
handling the empty-value match condition internally rather than calling
the Fieldtype’s getMatchQuery() method. Return true if this Fieldtype would
prefer to handle the match, or false if not. Fieldtype modules do not need
to consider this unless they want to override the default empty value match
behavior in PageFinder::whereEmptyValuePossible().


@param Field $field

@param mixed $value

@return bool

## ___wakeupValue()

Given a raw value (value as stored in database), return the value as it would appear in a Page object.

In many cases, no change to the value may be necessary, but if a Page expects this value as an object (for instance)
then this would be the method that converts that value to an object and returns it.

This method is called by the Page class, which takes the value provided by `Fieldtype::loadPageField()` and sends
it to this method before making it a part of the Page.


@param Page $page

@param Field $field

@param string|int|array $value

@return string|int|array|object $value

@see Fieldtype::sleepValue()

## ___sleepValue()

Given an 'awake' value, as set by wakeupValue(), convert the value back to a basic type for storage in database.

In many cases, this may mean no change to the value, which is why the default here just returns the value.
But for values that are stored with pages as objects (for instance) this method would take that object
and convert it to an array, int or string (serialized or otherwise).

Returned value must be either an array, number, or string.


@param Page $page

@param Field $field

@param string|int|float|array|object $value

@return string|int|float|array

@see Fieldtype::wakeupValue()

## ___exportValue()

Given a value, return an portable version of it as either a string, int, float or array

If an array is returned, it should only contain: strings, ints, floats or more arrays of those types.
This is intended for web service exports.

When applicable, this method should map things like internal IDs to named equivalents (name, path, etc.).

If not overridden, this takes on the same behavior as `Fieldtype::sleepValue()`. However, if overridden,
it is intended to be more verbose than wakeupValue, where applicable.


@param Page $page

@param Field $field

@param string|int|float|array|object|null $value

@param array $options Optional settings to shape the exported value, if needed:
 - `system` (boolean): Indicates value is being used for a system export via $pages->export() call (default=false).
 - `human` (boolean): When true, Fieldtype may optionally emphasize human readability over importability (default=false).

@return string|float|int|array

## getMatchQuery()

Get the database query that matches a Fieldtype table’s data with a given value.

Possible template method: If overridden, children do not need to call this method
if they update the $query themselves.

Note the following additional properties are available from the $query argument:

 - `$query->field` (Field): Field instance that being referred to match.
 - `$query->group` (string): Original group of the field in the selector (when applicable).
 - `$query->selector` (Selector): Original Selector object (matching the $field).
 - `$query->selectors` (Selectors): Original Selectors object (matching $field and others).
 - `$query->parentQuery` (DatabaseQuerySelect): Parent database query that $query will be merged into.
 - `$query->pageFinder` (PageFinder): The PageFinder instance that initiated the query, for additional info.


@param PageFinderDatabaseQuerySelect $query

@param string $table The table name to use

@param string $subfield Name of the subfield (typically 'data', unless selector explicitly specified another)

@param string $operator The comparison operator.
 - This base Fieldtype class accepts only database operators (=, !=, >, >=, <, <=, &).
 - Other Fieldtypes may choose to accept more operators according to need of Fieldtype.

@param mixed $value Value to find.
 - If given array, this base Fieldtype class (only) will match via OR condition. (3.0.182+)
 - Other Fieldtypes may choose to interpret array values differently according need of Fieldtype.

@return PageFinderDatabaseQuerySelect|DatabaseQuerySelect $query

@throws WireException

## ___createField()

Create a new field table in the database.

This method should execute the SQL query necessary to create $field->table
It should throw a WireException if failure occurs.
Most Fieldtype modules use this built-in implementation.


@param Field $field

@return bool

@throws WireException

## getDatabaseSchema()

Get the database schema for this field

- Should return an array like in the example below, indexed by field name with type details as the value
  (as it would be in an SQL statement).

- Indexes are passed through with a `keys` array. Note that `pages_id` as a field and primary key may be
  retrieved by starting with the parent schema return from the built-in getDatabaseSchema() method.

- At minimum, each Fieldtype must add a `data` field as well as an index for it.

- If you want a PHP `NULL` value to become a NULL in the database, your column definition must specify:
  `DEFAULT NULL`.

~~~~~~
array(
 'data' => 'mediumtext NOT NULL',
 'keys' => array(
   'primary' => 'PRIMARY KEY (`pages_id`)',
   'FULLTEXT KEY data (data)',
 ),
 'xtra' => array(
   // optional extras, MySQL defaults will be used if omitted
   'append' =>
     'ENGINE={$this->config->dbEngine} ' .
     'DEFAULT CHARSET={$this->config->dbCharset}'

   // true (default) if this schema provides all storage for this fieldtype.
   // false if other storage is involved with this fieldtype, beyond this schema
   // (like repeaters, PageTable, etc.)
   'all' => true,
 )
);
~~~~~~


@param Field $field In case it's needed for the schema, but typically isn't.

@return array

## getFieldClass()

Get class name to use Field objects of this type (must be class that extends Field class)

Return blank if default class (Field) should be used.

@param array $a Field data from DB (if needed)

@return string Return class name or blank to use default Field class

@since 3.0.146

## ___getSelectorInfo()

Return array with information about what properties and operators can be used with this field.


@param Field $field

@param array $data Array of extra data, when/if needed

@return array See `FieldSelectorInfo` class for details.

## ___loadPageField()

Load the given page field from the database table and return the value.

- Return NULL if the value is not available.
- Return the value as it exists in the database, without further processing.
- This is intended only to be called by Page objects on an as-needed basis.
- Typically this is only called for fields that don't have 'autojoin' turned on.
- Any actual conversion of the value should be handled by the `Fieldtype::wakeupValue()` method.


@param Page $page Page object to save.

@param Field $field Field to retrieve from the page.

@return mixed|null

## ___loadPageFieldFilter()

Load the given page field from the database table and return a *filtered* value.

This is the same as `Fieldtype::loadPageField()` but enables a selector to be
provided which can filter the returned value.

As far as core Fieldtypes go, this one is only applicable to FieldtypeMulti derived types.


@param Page $page Page object to save.

@param Field $field Field to retrieve from the page.

@param Selectors|string|array $selector

@return mixed|null

## getLoadQuery()

Return the query used for loading all parts of the data from this field.


@param Field $field

@param DatabaseQuerySelect $query

@return DatabaseQuerySelect

## getLoadQueryAutojoin()

Return the query used for Autojoining this field (if different from getLoadQuery) or NULL if autojoin not allowed.


@param Field $field

@param DatabaseQuerySelect $query

@return DatabaseQuerySelect|NULL

## ___savePageField()

Save the given field from given page to the database.

Possible template method: If overridden, it is likely not necessary to call this parent method.


@param Page $page Page object to save.

@param Field $field Field to retrieve from the page.

@return bool True on success, false on DB save failure.

@throws WireException|\PDOException|WireDatabaseException

## ___deleteField()

Delete the given field, which implies: drop the table used by the field.

This should only be called by the `Fields` class since `fieldgroups_fields` lookup entries must be
deleted before this method is called.


@param Field $field Field object

@return bool True on success, false on DB delete failure.

## ___deletePageField()

Delete the given Field from the given Page.

Must delete entries from field's database table that belong to the Page.


@param Page $page

@param Field $field Field object

@return bool True on success, false on DB delete failure.

@throws WireException

## ___emptyPageField()

Empty out the DB table data for page field, but leave everything else in tact.

In most cases this may be nearly identical to `Fieldtype::deletePageField()`, but would be different
for things like page references where we wouldn't want relational data deleted.


@param Page $page

@param Field $field Field object

@return bool True on success, false on DB delete failure.

@throws WireException

## emptyPageFieldTable()

Empty DB table of page field

@param Page $page

@param Field $field

@return bool

@throws WireException

@since 3.0.189

## ___replacePageField()

Move this field’s data from one page to another.


@param Page $src Source Page

@param Page $dst Destination Page

@param Field $field

@return bool

## ___deleteTemplateField()

Delete the given Field from all pages using the given template, without loading those pages.

ProcessWire will use this method rather than deletePageField in cases where the quantity of items
to delete is high (above 200 at time this was written). However, if your individual Fieldtype
defines it's own ___deletePageField method (separate from the one above) then it'll still get used.

This was added so that mass deletions can happen without loading every page, which may not be feasible
when dealing with thousands of pages.


@param Template $template

@param Field $field

@return bool

## ___cloneField()

Return a cloned copy of $field


@param Field $field

@return Field cloned copy

## get()

Get a property from this Fieldtype’s data


@param string $key

@return mixed

## ___install()

Install this Fieldtype, consistent with optional Module interface

- Called once at time of installation by Modules::install().
- If custom Fieldtype classes need to perform any setup beyond that performed in ___createTable(),
  this method is where they should do it. This is not required, and probably not applicable to most.


@throws WireException Should throw an Exception on failure to install

## ___uninstall()

Uninstall this Fieldtype, consistent with optional Module interface

- Checks to make sure it's safe to uninstall this Fieldtype. If not, throw an Exception indicating such.
- It's safe to uninstall a Fieldtype only if it's not being used by any Fields.
- If a Fieldtype overrides this to perform additional uninstall functions, it would be good to call this
  parent uninstall method first to make sure uninstall is okay.


@throws WireException Should throw an Exception if uninstall can't be completed.

## ___upgrade()

Called when module version changes


@param $fromVersion

@param $toVersion

@throws WireException if upgrade fails

## __toString()

The string value of Fieldtype is always the Fieldtype's name.
