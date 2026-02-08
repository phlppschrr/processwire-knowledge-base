# $selectableOptionManager->getRemovedOptionIDs(): array

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Return the option IDs found to have been removed from the last setOptions() call.

These are for options not yet deleted, and that should be deleted after confirmation.
They can be deleted with this $this->deleteOptionIDs() method.

## Return value

array
