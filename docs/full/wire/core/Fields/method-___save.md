# $fields->___save(Saveable $item): bool

Source: `wire/core/Fields.php`

Save a Field to the database

## Example

~~~~~
// Modify a field label and save it
$field = $fields->get('title');
$field->label = 'Title or Headline';
$fields->save($field);
~~~~~

## Usage

~~~~~
// basic usage
$bool = $fields->___save($item);

// usage with all arguments
$bool = $fields->___save(Saveable $item);
~~~~~

## Arguments

- `$item` `Field` The field to save

## Return value

- `bool` True on success, false on failure

## Exceptions

- `WireException`
