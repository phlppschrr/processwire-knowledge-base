# Field::flagAccessEditor

Source: `wire/core/Field.php`

If field is access controlled and user has no edit access, they can still view in the editor (if they have view permission)

Without this flag, non-editable values are simply not shown in the editor at all.
