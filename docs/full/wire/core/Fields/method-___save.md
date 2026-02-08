# $fields->save(Saveable $item): bool

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
$bool = $fields->save($item);

// usage with all arguments
$bool = $fields->save(Saveable $item);
~~~~~

## Hookable

- Hookable method name: `save`
- Implementation: `___save`
- Hook with: `$fields->save()`

## Arguments

- `$item` `Field` The field to save

## Return value

- `bool` True on success, false on failure

## Exceptions

- `WireException`
