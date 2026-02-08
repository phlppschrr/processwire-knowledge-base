# Fields

Source: `wire/core/Fields.php`

ProcessWire Fields

Manages collection of ALL Field instances, not specific to any particular Fieldgroup

ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

Manages all custom fields in ProcessWire, independently of any Fieldgroup.
$fields
Each field returned is an object of type `Field`. The $fields API variable is iterable:
~~~~~
foreach($fields as $field) {
  echo "<p>Name: $field->name, Type: $field->type, Label: $field->label</p>";
}
~~~~~

## other

@method Field|null get($key) Get a field by name or id

@method bool changeFieldtype(Field $field1, $keepSettings = false)

@method bool saveFieldgroupContext(Field $field, Fieldgroup $fieldgroup, $namespace = '')

@method bool deleteFieldDataByTemplate(Field $field, Template $template)

@method void changedType(Saveable $item, Fieldtype $fromType, Fieldtype $toType)

@method void changeTypeReady(Saveable $item, Fieldtype $fromType, Fieldtype $toType)

@method bool|Field clone(Field $item, $name = '') Clone a field and return it or return false on fail.

@method array getTags($getFieldNames = false) Get tags for all fields (3.0.179+)

@method bool applySetupName(Field $field, $setupName = '')

## __construct()

Construct

## loadRowsReady()

Called after rows loaded from DB but before populated to this instance

@param array $rows

## makeItem()

Make an item and populate with given data

@param array $a Associative array of data to populate

@return Saveable|Wire

@throws WireException

@since 3.0.146

## initItem()

Create a new Saveable item from a raw array ($row) and add it to $items

@param array $row

@param WireArray|null $items

@return Saveable|WireData|Wire

@since 3.0.194

## getWireArray()

Get WireArray container that items are stored in

@return WireArray

@since 3.0.194

## ___save()

Save a Field to the database

~~~~~
// Modify a field label and save it
$field = $fields->get('title');
$field->label = 'Title or Headline';
$fields->save($field);
~~~~~

@param Field $item The field to save

@return bool True on success, false on failure

@throws WireException

## checkFieldTable()

Check that the given Field's table exists and create it if it doesn't

@param Field $field

## ___delete()

Delete a Field from the database

This method will throw a WireException if you attempt to delete a field that is currently in use (i.e. assigned to one or more fieldgroups).

@param Field $item Field to delete

@return bool True on success, false on failure

@throws WireException

## ___clone()

Create and return a cloned copy of the given Field

@param Field $item Field to clone

@param string $name Optionally specify name for new cloned item

@return Field $item Returns the new clone on success, or false on failure

## ___saveFieldgroupContext()

Save the context of the given field for the given fieldgroup


@param Field $field Field to save context for

@param Fieldgroup $fieldgroup Context for when field is in this fieldgroup

@param string $namespace An optional namespace for additional context

@return bool True on success

@throws WireException

## ___changeFieldtype()

Change a field's type


@param Field $field1 Field with the new type already assigned

@param bool $keepSettings Whether or not to keep custom $data settings (default=false)

@throws WireException

@return bool

## ___deleteFieldDataByTemplate()

Physically delete all field data (from the database) used by pages of a given template

This is for internal API use only. This method is intended only to be called by
Fieldtype::deleteTemplateField

If you need to remove a field from a Fieldgroup, use Fieldgroup::remove(), and this
method will be call automatically at the appropriate time when save the fieldgroup.


@param Field $field

@param Template $template

@return bool Whether or not it was successful

@throws WireException when given a situation where deletion is not allowed

## getNumPages()

Return a count of pages containing populated values for the given field

@param Field $field

@param array $options Optionally specify one of the following options:
 - `template` (template|int|string): Specify a Template object, ID or name to isolate returned rows specific to pages using that template.
 - `page` (Page|int|string): Specify a Page object, ID or path to isolate returned rows specific to that page.
 - `getPageIDs` (bool): Specify boolean true to make it return an array of matching Page IDs rather than a count.

@return int|array Returns array only if getPageIDs option set, otherwise returns count of pages.

@throws WireException If given option for page or template doesn't resolve to actual page/template.

## getNumRows()

Return a count of database rows populated the given field

@param Field $field

@param array $options Optionally specify any of the following options:
 - `template` (Template|int|string): Specify a Template object, ID or name to isolate returned rows specific to pages using that template.
 - `page` (Page|int|string): Specify a Page object, ID or path to isolate returned rows specific to that page.
 - `countPages` (bool): Specify boolean true to make it return a page count rather than a row count (default=false).
	  There will only be potential difference between rows and pages counts with multi-value fields.
 - `getPageIDs` (bool): Specify boolean true to make it return an array of matching Page IDs rather than a count (overrides countPages).

@return int|array Returns array only if getPageIDs option set, otherwise returns a count of rows.

@throws WireException If given option for page or template doesn't resolve to actual page/template.

## isNative()

Is the given field name native/permanent to the database?

Such fields are disallowed from being used for custom field names.

@param string $name Field name you want to check

@return bool True if field is native (and thus should not be used) or false if it's okay to use

## ___getTags()

Get list of all tags used by fields

- By default it returns an array of tag names where both keys and values are the tag names.
- If you specify true for the `$getFields` argument, it returns an array where the keys are
  tag names and the values are arrays of field names in the tag.
- If you specify "reset" for the `$getFields` argument it returns a blank array and resets
  internal tags cache.


@param bool|string $getFieldNames Specify true to return associative array where keys are tags and values are field names
  …or specify the string "reset" to force getTags() to reset its cache, forcing it to reload on the next call.

@return array Both keys and values are tags in return value

@since 3.0.106 + made hookable in 3.0.179

## findByTag()

Return all fields that have the given $tag

Returns an associative array of `['field_name' => 'field_name']` if `$getFieldNames` argument is true,
or `['field_name => Field instance]` if not (which is the default).

@param string $tag Tag to find fields for

@param bool $getFieldNames If true, returns array of field names rather than Field objects (default=false).

@return array Array of Field objects, or array of field names if requested. Array keys are always field names.

@since 3.0.106

## findByType()

Find fields by type

@param string|Fieldtype $type Fieldtype class name or object

@param array $options
 - `inherit` (bool): Also find types that inherit from given type? (default=true)
 - `valueType` (string): Value type to return, one of 'field', 'id', or 'name' (default='field')
 - `indexType` (string): Index type to use, one of 'name', 'id', or '' blank for non-associative array (default='name')

@return array|Field[]

@since 3.0.194

## getAllNames()

Get all field names

@param string $indexType One of 'name', 'id' or blank string for no index (default='')

@return array

@since 3.0.194

## ___changedType()

Hook called when a field has changed type


@param Field $item

@param Fieldtype $fromType

@param Fieldtype $toType

## ___changeTypeReady()

Hook called right before a field is about to change type


@param Field $item

@param Fieldtype $fromType

@param Fieldtype $toType

## ___applySetupName()

Setup a new field using predefined setup name(s) from the Field’s fieldtype

If no setupName is provided then this method doesn’t do anything, but hooks to it might.

@param Field $field Newly created field

@param string $setupName Setup name to apply

@return bool True if setup was appled, false if not

@since 3.0.213
