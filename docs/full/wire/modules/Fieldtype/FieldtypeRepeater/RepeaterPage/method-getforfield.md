# RepeaterPage::getForField()

Source: `wire/modules/Fieldtype/FieldtypeRepeater/RepeaterPage.php`

Return the field that this repeater item belongs to

Returns null only if $forField has not been set and cannot be determined from any other
properties of this page. Meaning null return value is not likely.

@return Field|null
