# Fields::___applySetupName()

Source: `wire/core/Fields.php`

Setup a new field using predefined setup name(s) from the Field’s fieldtype

If no setupName is provided then this method doesn’t do anything, but hooks to it might.

@param Field $field Newly created field

@param string $setupName Setup name to apply

@return bool True if setup was appled, false if not

@since 3.0.213
