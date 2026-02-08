# $fields->___save(Saveable $item): bool

Source: `wire/core/Fields.php`

Save a Field to the database

~~~~~
// Modify a field label and save it
$field = $fields->get('title');
$field->label = 'Title or Headline';
$fields->save($field);
~~~~~

## Arguments

- `$item` `Field` The field to save

## Return value

bool True on success, false on failure

## Throws

- WireException
