# Field: properties

Source: `wire/core/Field.php`

@property int $id Numeric ID of field in the database

@property string $name Name of field

@property string $table Database table used by the field

@property string $prevTable Previously database table (if field was renamed)

@property string $prevName Previously used name (if field was renamed), 3.0.164+

@property Fieldtype|null $type Fieldtype module that represents the type of this field

@property Fieldtype|null $prevFieldtype Previous Fieldtype, if type was changed

@property int $flags Bitmask of flags used by this field

@property-read string $flagsStr Names of flags used by this field (readonly)

@property string $label Text string representing the label of the field

@property string $description Longer description text for the field

@property string $notes Additional notes text about the field

@property string $icon Icon name used by the field, if applicable

@property string $tags Tags that represent this field, if applicable (space separated string).

@property-read array $tagList Same as $tags property, but as an array.

@property array $allowContexts Names of settings that are custom configured to be allowed for context.
