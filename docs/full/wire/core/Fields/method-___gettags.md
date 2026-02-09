# $fields->getTags($getFieldNames = false): array

Source: `wire/core/Fields.php`

Get list of all tags used by fields

- By default it returns an array of tag names where both keys and values are the tag names.
- If you specify true for the `$getFields` argument, it returns an array where the keys are
  tag names and the values are arrays of field names in the tag.
- If you specify "reset" for the `$getFields` argument it returns a blank array and resets
  internal tags cache.

## Usage

~~~~~
// basic usage
$array = $fields->getTags();

// usage with all arguments
$array = $fields->getTags($getFieldNames = false);
~~~~~

## Arguments

- `$getFieldNames` (optional) `bool|string` Specify true to return associative array where keys are tags and values are field names …or specify the string "reset" to force getTags() to reset its cache, forcing it to reload on the next call.

## Return value

- `array` Both keys and values are tags in return value

## Hooking

- Hookable method name: `getTags`
- Implementation: `___getTags`
- Hook with: `Fields::getTags`

### Hooking Before

~~~~~
$this->addHookBefore('Fields::getTags', function(HookEvent $event) {
  $fields = $event->object;

  // Get arguments
  $getFieldNames = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $getFieldNames);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Fields::getTags', function(HookEvent $event) {
  $fields = $event->object;

  // Get arguments
  $getFieldNames = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.106 + made hookable in 3.0.179
