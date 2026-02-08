# Fieldgroup

Source: `wire/core/Fieldgroup.php`

ProcessWire Fieldgroup

A group of fields that is ultimately attached to a Template.

Fieldgroup is a type of WireArray that holds a group of Field objects for template(s).
For full details on all methods available in a Fieldgroup, be sure to also see the `WireArray` class.

The existance of Fieldgroups is hidden at the ProcessWire web admin level
as it appears that fields are attached directly to Templates. However, they
are separated in the API in case want want to have fieldgroups used by
multiple templates in the future (like ProcessWire 1.x).

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

## other

@property array $fields_id Array of all field IDs in this Fieldgroup

@property null|FieldsArray $removedFields Null when there are no removed fields, or FieldsArray when there are.

## retrieval

@property int $id Fieldgroup database ID

@property string $name Fieldgroup name

## contextNamespacePrefix

Prefix for namespaced field contexts

## add()

Add a field to this Fieldgroup

~~~~~
$field = $fields->get('body');
$fieldgroup->add($field);
~~~~~


@param Field|string $item Field object, field name or id.

@return $this

@throws WireException

## remove()

Remove a field from this fieldgroup

Note that this must be followed up with a `$fieldgroup->save()` before it does anything destructive.
This method does nothing more than queue the removal.

_Technical Details_
Performs a deletion by finding all templates using this fieldgroup, then finding all pages using the template, then
calling upon the Fieldtype to delete them one at a time. This is a potentially expensive/time consuming method, and
may need further consideration.


@param Field|string $key Field object or field name, or id.

@return bool True on success, false on failure.

## softRemove()

Remove a field without queueing it to be removed from database

Removes a field from the fieldgroup without deleting any associated field data when fieldgroup
is saved to the database. This is useful in the API when you want to move a field around within
a fieldgroup, like when moving a field to a Fieldset within the Fieldgroup.


@param Field|string|int $field Field object, name or id.

@return bool|Fieldgroup|WireArray

## getField()

Get a field that is part of this fieldgroup

Same as `Fieldgroup::get()` except that it only checks fields, not other properties of a fieldgroup.
Meaning, this is the preferred way to retrieve a Field from a Fieldgroup.


@param string|int|Field $key Field object, name or id.

@param bool|string $useFieldgroupContext Optionally specify one of the following (default=false):
  - `true` (boolean) Returned Field will be a clone of the original with context data set.
  - Specify a namespace (string) to retrieve context within that namespace.

@return Field|null Field object when present in this Fieldgroup, or null if not.

## hasFieldContext()

Does the given Field have context data available in this fieldgroup?

A Field with context data is one that overrides one or more settings present with the Field
when it is outside the context of this Fieldgroup. For example, perhaps a Field has a
columnWidth setting of 100% in its global settings, but only 50% when used in this Fieldgroup.


@param int|string|Field $field Field object, name or id

@param string $namespace Optional namespace string for context

@return bool True if additional context information is available, false if not.

## getFieldContext()

Get a Field that is part of this Fieldgroup, in the context of this Fieldgroup.

Returned Field will be a clone of the original with additional context data
already populated to it.


@param string|int|Field $key Field object, name or id.

@param string $namespace Optional namespace string for context

@return Field|null

## hasField()

Does this fieldgroup have the given field?


@param string|int|Field $key Field object, name or id.

@return bool True if this Fieldgroup has the field, false if not.

## get()

Get a Fieldgroup property or a Field.

It is preferable to use `Fieldgroup::getField()` to retrieve fields from the Fieldgroup because
the scope of this `get()` method means it can return more than just Field object.


@param string|int $key Property name to retrieve, or Field name

@return Field|string|int|null|array

## set()

Set a fieldgroup property


@param string $key Name of property to set

@param string|int|object $value Value of property

@return Fieldgroup|WireArray $this

@throws WireException if passed invalid data

## save()

Save this Fieldgroup to the database

To hook into this, hook to `Fieldgroups::save()` instead.


@return $this

## __toString()

Fieldgroups always return their name when dereferenced as a string

## getPageInputfields()

Get all of the Inputfields for this Fieldgroup associated with the provided Page and populate them.


@param Page $page Page that the Inputfields will be for.

@param string|array $contextStr Optional context string to append to all the Inputfield names, OR array of options.
 - Optional context string is helpful for things like repeaters.
 - Or associative array with any of these options:
 - `contextStr` (string): Context string to append to all Inputfield names.
 - `fieldName` (string|array): Limit to particular fieldName(s) or field ID(s). See $fieldName argument for details.
 - `namespace` (string): Additional namespace for Inputfield context.
 - `flat` (bool): Return all Inputfields in a flattened InputfieldWrapper?
 - `populate` (bool): Populate page values to Inputfields? (default=true) since 3.0.208
 - `container` (InputfieldWrapper): The InputfieldWrapper element to add fields into, or omit for new. since 3.0.239

@param string|array $fieldName Limit to a particular fieldName(s) or field IDs (optional).
 - If specifying a single field (name or ID) and it refers to a fieldset, then all fields in that fieldset will be included.
 - If specifying an array of field names/IDs the returned InputfieldWrapper will maintain the requested order.

@param string $namespace Additional namespace for the Inputfield context (optional).

@param bool $flat Returns all Inputfields in a flattened InputfieldWrapper (default=true).

@return InputfieldWrapper Returns an InputfieldWrapper that acts as a container for multiple Inputfields.

## getTemplates()

Get a list of all templates using this Fieldgroup


@return TemplatesArray

## getNumTemplates()

Get the number of templates using this Fieldgroup


@return int

## saveContext()

Save field contexts for this fieldgroup


@return int Number of contexts saved
