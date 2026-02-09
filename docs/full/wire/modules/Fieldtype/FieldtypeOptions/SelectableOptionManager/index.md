# SelectableOptionManager

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Inherits: `Wire`

ProcessWire Selectable Option Manager, for FieldtypeOptions

Handles management of the fieldtype_options table and related field_[name] table
to assist FieldtypeOptions module.

Methods:
- [`getRemovedOptionIDs(): array`](method-getremovedoptionids.md) Return the option IDs found to have been removed from the last setOptions() call.
- [`useLanguages(): bool`](method-uselanguages.md) Whether or not multi-language support is in use
- [`getOptionsByID(Field $field, array $ids): SelectableOptionArray|SelectableOption[]`](method-getoptionsbyid.md) Shortcut to get options by ID number
- [`getOptions(Field $field, array $filters = array()): SelectableOptionArray|SelectableOption[]`](method-getoptions.md) Return array of current options for $field
- [`findOptionsByProperty(Field $field, string $property, string $operator, string $value): SelectableOptionArray`](method-findoptionsbyproperty.md) Perform a partial match on title of options
- [`arrayToOption(array $a): SelectableOption`](method-arraytooption.md) Given an array of option data, populate an Option object and return it
- [`optionsStringToArray($value): array`](method-optionsstringtoarray.md) Given a newline separated options string, convert it to an array
- [`optionsArrayToObjects(array $value): SelectableOptionArray`](method-optionsarraytoobjects.md) Convert an array of option arrays, to a SelectableOptionArray of SelectableOption objects
- [`getOptionsString(SelectableOptionArray $options, int|string|Language $language = ''): string`](method-getoptionsstring.md) Get the options input string used for
- [`setOptionsString(Field $field, string $value, bool $allowDelete = true): array`](method-setoptionsstring.md) Set an options string
- [`setOptionsStringLanguages(Field $field, array $values, bool $allowDelete = true)`](method-setoptionsstringlanguages.md) Set options string, but for each language
- [`setOptions(Field $field, array|SelectableOptionArray $options, bool $allowDelete = true): array`](method-setoptions.md) Set current options for $field, identify and acting on added, deleted, updated options
- [`updateOptions(Field $field, array|SelectableOptionArray $options): int`](method-updateoptions.md) Update options for field
- [`deleteOptions(Field $field, array|SelectableOptionArray $options): int`](method-deleteoptions.md) Delete the given options for $field
- [`deleteOptionsByID(Field $field, array $ids): int`](method-deleteoptionsbyid.md) Delete the given option IDs
- [`deleteAllOptionsForField(Field $field): int`](method-deletealloptionsforfield.md) Delete all options for given field
- [`addOptions(Field $field, array|SelectableOptionArray $options): int`](method-addoptions.md) Add the given option titles for $field
- [`updateLanguages(?HookEvent $event = null)`](method-updatelanguages.md) Hook method called when a language is added or deleted
- [`checkLanguagesAdded(Language|null $languageAdded = null): array`](method-checklanguagesadded.md) Check for added languages
- [`checkLanguagesDeleted(Language|null $languageDeleted = null): array`](method-checklanguagesdeleted.md) Check for deleted languages
- [`upgrade(string $fromVersion, string $toVersion)`](method-upgrade.md) Upgrade fieldtype_options table
- [`install()`](method-install.md) Install
- [`uninstall()`](method-uninstall.md) Uninstall

Constants:
- [`optionsTable = 'fieldtype_options'`](const-optionstable.md)
