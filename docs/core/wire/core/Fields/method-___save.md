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

## Arguments

- `$item` `Field` The field to save

## Return value

- `bool` True on success, false on failure

## Hooking

- Hookable method name: `save`
- Implementation: `___save`
- Hook with: `Fields::save`

### Hooking Before

~~~~~
$this->addHookBefore('Fields::save', function(HookEvent $event) {
  $fields = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $item);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Fields::save', function(HookEvent $event) {
  $fields = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException`
