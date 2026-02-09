# Field: properties

Source: `wire/core/Field.php`

- $id: int Numeric ID of field in the database

- $name: string Name of field

- $table: string Database table used by the field

- $prevTable: string Previously database table (if field was renamed)

- $prevName: string Previously used name (if field was renamed), 3.0.164+

- $type: Fieldtype|null Fieldtype module that represents the type of this field

- $prevFieldtype: Fieldtype|null Previous Fieldtype, if type was changed

- $flags: int Bitmask of flags used by this field

- $flagsStr: string Names of flags used by this field (readonly)

- $label: string Text string representing the label of the field

- $description: string Longer description text for the field

- $notes: string Additional notes text about the field

- $icon: string Icon name used by the field, if applicable

- $tags: string Tags that represent this field, if applicable (space separated string).

- $tagList: array Same as $tags property, but as an array.

- $allowContexts: array Names of settings that are custom configured to be allowed for context.
