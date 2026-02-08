# Fields::___save()

Source: `wire/core/Fields.php`

Save a Field to the database

~~~~~
// Modify a field label and save it
$field = $fields->get('title');
$field->label = 'Title or Headline';
$fields->save($field);
~~~~~

@param Field $item The field to save

@return bool True on success, false on failure

@throws WireException
