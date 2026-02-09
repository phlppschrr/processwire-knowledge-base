# $fields->saveFieldgroupContext(Field $field, Fieldgroup $fieldgroup, $namespace = ''): bool

Source: `wire/core/Fields.php`

Save the context of the given field for the given fieldgroup

## Usage

~~~~~
// basic usage
$bool = $fields->saveFieldgroupContext($field, $fieldgroup);

// usage with all arguments
$bool = $fields->saveFieldgroupContext(Field $field, Fieldgroup $fieldgroup, $namespace = '');
~~~~~

## Hookable

- Hookable method name: `saveFieldgroupContext`
- Implementation: `___saveFieldgroupContext`
- Hook with: `$fields->saveFieldgroupContext()`

## Hooking Before

~~~~~
$this->addHookBefore('Fields::saveFieldgroupContext', function(HookEvent $event) {
  $fields = $event->object;

  // Get arguments
  $field = $event->arguments(0);
  $fieldgroup = $event->arguments(1);
  $namespace = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $field);
  $event->arguments(1, $fieldgroup);
  $event->arguments(2, $namespace);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Fields::saveFieldgroupContext', function(HookEvent $event) {
  $fields = $event->object;

  // Get arguments
  $field = $event->arguments(0);
  $fieldgroup = $event->arguments(1);
  $namespace = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$field` `Field` Field to save context for
- `$fieldgroup` `Fieldgroup` Context for when field is in this fieldgroup
- `$namespace` (optional) `string` An optional namespace for additional context

## Return value

- `bool` True on success

## Exceptions

- `WireException`
