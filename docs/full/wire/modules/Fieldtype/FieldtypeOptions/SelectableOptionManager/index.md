# SelectableOptionManager

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Inherits: `Wire`

ProcessWire Selectable Option Manager, for FieldtypeOptions

Handles management of the fieldtype_options table and related field_[name] table
to assist FieldtypeOptions module.

Methods:
- [`getRemovedOptionIDs(): array`](method-getremovedoptionids.md)
- [`useLanguages(): bool`](method-uselanguages.md)
- [`getOptionsByID(Field $field, array $ids): SelectableOptionArray|SelectableOption[]`](method-getoptionsbyid.md)
- [`getOptions(Field $field, array $filters = array()): SelectableOptionArray|SelectableOption[]`](method-getoptions.md)
- [`findOptionsByProperty(Field $field, string $property, string $operator, string $value): SelectableOptionArray`](method-findoptionsbyproperty.md)
- [`arrayToOption(array $a): SelectableOption`](method-arraytooption.md)
- [`optionsStringToArray($value): array`](method-optionsstringtoarray.md)
- [`optionsArrayToObjects(array $value): SelectableOptionArray`](method-optionsarraytoobjects.md)
- [`getOptionsString(SelectableOptionArray $options, int|string|Language $language = ''): string`](method-getoptionsstring.md)
- [`setOptionsString(Field $field, string $value, bool $allowDelete = true): array`](method-setoptionsstring.md)
- [`setOptionsStringLanguages(Field $field, array $values, bool $allowDelete = true)`](method-setoptionsstringlanguages.md)
- [`setOptions(Field $field, array|SelectableOptionArray $options, bool $allowDelete = true): array`](method-setoptions.md)
- [`updateOptions(Field $field, array|SelectableOptionArray $options): int`](method-updateoptions.md)
- [`deleteOptions(Field $field, array|SelectableOptionArray $options): int`](method-deleteoptions.md)
- [`deleteOptionsByID(Field $field, array $ids): int`](method-deleteoptionsbyid.md)
- [`deleteAllOptionsForField(Field $field): int`](method-deletealloptionsforfield.md)
- [`addOptions(Field $field, array|SelectableOptionArray $options): int`](method-addoptions.md)
- [`updateLanguages(?HookEvent $event = null)`](method-updatelanguages.md)
- [`checkLanguagesAdded(Language|null $languageAdded = null): array`](method-checklanguagesadded.md)
- [`checkLanguagesDeleted(Language|null $languageDeleted = null): array`](method-checklanguagesdeleted.md)
- [`upgrade(string $fromVersion, string $toVersion)`](method-upgrade.md)
- [`install()`](method-install.md)
- [`uninstall()`](method-uninstall.md)

Constants:
- [`optionsTable`](const-optionstable.md)
