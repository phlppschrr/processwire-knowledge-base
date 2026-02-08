# SelectableOptionManager

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

ProcessWire Selectable Option Manager, for FieldtypeOptions

Handles management of the fieldtype_options table and related field_[name] table
to assist FieldtypeOptions module.

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

## optionsTable

DB table name managed by this class

## getRemovedOptionIDs()

Return the option IDs found to have been removed from the last setOptions() call.

These are for options not yet deleted, and that should be deleted after confirmation.
They can be deleted with this $this->deleteOptionIDs() method.

@return array

## useLanguages()

Whether or not multi-language support is in use

@return bool

## getOptionsByID()

Shortcut to get options by ID number

@param Field $field

@param array $ids

@return SelectableOptionArray|SelectableOption[]

## getOptions()

Return array of current options for $field

Returned array is indexed by "id$option_id" associative, which is used
as a way to identify existing options vs. new options

@param Field $field

@param array $filters Any of array(property => array) where property is 'id', 'title' or 'value'.

@return SelectableOptionArray|SelectableOption[]

@throws WireException

## findOptionsByProperty()

Perform a partial match on title of options

@param Field $field

@param string $property Either 'title' or 'value'. May also be blank (to imply 'either') if operator is '=' or
    '!='

@param string $operator

@param string $value Value to find

@return SelectableOptionArray

## arrayToOption()

Given an array of option data, populate an Option object and return it

@param array $a

@return SelectableOption

## optionsStringToArray()

Given a newline separated options string, convert it to an array

@param $value

@return array

@throws WireException

## optionsArrayToObjects()

Convert an array of option arrays, to a SelectableOptionArray of SelectableOption objects

@param array $value

@return SelectableOptionArray

@throws WireException

## getOptionsString()

Get the options input string used for

@param SelectableOptionArray $options

@param int|string|Language $language Language id, object, or name, if applicable

@return string

@throws WireException if given invalid language

## setOptionsString()

Set an options string

Should adhere to the format

One option per line in the format: 123=title or 123=value|title
where 123 is the option ID, 'value' is an optional value,
and 'title' is a required title.

For new options, specify just the option title
(or value|title) on its own line. Options should
be in the desired sort order.

@param Field $field

@param string $value

@param bool $allowDelete Allow removed lines in the string to result in deleted options?
	If false, no options will be affected but you can call the getRemovedOptionIDs() method
	to retrieve them for confirmation.

@return array containing ('added' => cnt, 'updated' => cnt, 'deleted' => cnt, 'marked' => cnt)
	note: 'marked' means marked for deletion

## setOptionsStringLanguages()

Set options string, but for each language

@param Field $field

@param array $values Array of ($languageID => string), one for each language

@param bool $allowDelete Allow removed lines in the string to result in deleted options?
	If false, no options will be affected but you can call the getRemovedOptionIDs() method
	to retrieve them for confirmation.

@throws WireException

## setOptions()

Set current options for $field, identify and acting on added, deleted, updated options

@param Field $field

@param array|SelectableOptionArray $options Array of SelectableOption objects
	For new options specify 0 for the 'id' property.

@param bool $allowDelete Allow options to be deleted? If false, the options marked for
	deletion can be retrieved via $this->getRemovedOptions($field);

@return array containing ('added' => cnt, 'updated' => cnt, 'deleted' => cnt, 'marked' => cnt)
	note: 'marked' means marked for deletion

@throws WireException

## updateOptions()

Update options for field

@param Field $field

@param array|SelectableOptionArray $options

@return int Number of options updated

## deleteOptions()

Delete the given options for $field

@param Field $field

@param array|SelectableOptionArray $options

@return int Number of options deleted

## deleteOptionsByID()

Delete the given option IDs

@param Field $field

@param array $ids

@return int Number of options deleted

## deleteAllOptionsForField()

Delete all options for given field

@param Field $field

@return int

@throws WireException

## addOptions()

Add the given option titles for $field

@param Field $field

@param array|SelectableOptionArray $options

@return int Number of options added

## updateLanguages()

Hook method called when a language is added or deleted

Also called when module is installed

@param HookEvent|null $event

## checkLanguagesAdded()

Check for added languages

@param Language|null $languageAdded

@return array SQL statements to add language when appropriate

## checkLanguagesDeleted()

Check for deleted languages

@param Language|null $languageDeleted

@return array SQL statements to delete language when appropriate

## upgrade()

Upgrade fieldtype_options table

@param string $fromVersion

@param string $toVersion

@throws WireException

## install()

Install

## uninstall()

Uninstall
