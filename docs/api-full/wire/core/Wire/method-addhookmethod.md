# $wire->addHookMethod($method, $toObject, $toMethod = null, $options = array()): string

Source: `wire/core/Wire.php`

Add a hook accessible as a new public method in a class (or object)

- This enables you to add a new accessible public method to an existing object, which will execute
  your hook implementation method when called upon.

- Hook method can accept arguments and/or populate return values, just like any other regular method
  in the class. However, methods such as this do not have access to private or protected
  properties/methods in the class.

- Methods added like this themselves become hookable as well.

## Example

~~~~~
// Adds a myHasParent($parent) method to all Page objects
$wire->addHookMethod('Page::myHasParent', function($event) {
  $page = $event->object;
  $parent = $event->arguments(0);
  if(!$parent instanceof Page) {
    throw new WireException("Page::myHasParent() requires a Page argument");
  }
  if($page->parents()->has($parent)) {
    // this page has the given parent
    $event->return = true;
  } else {
    // does not have the given parent
    $event->return = false;
  }
});

// Calling the new method (from any instance)
$parent = $pages->get('/products/');
if($page->myHasParent($parent)) {
  // $page has the given $parent
}
~~~~~

## Usage

~~~~~
// basic usage
$string = $wire->addHookMethod($method, $toObject);

// usage with all arguments
$string = $wire->addHookMethod($method, $toObject, $toMethod = null, $options = array());
~~~~~

## Arguments

- `$method` `string` Name of method you want to add, must not collide with existing property or method names: - `Class::method` to add the method to all instances of Class. - `method` to just add to a single object instance. - Since 3.0.137 it may also be multiple methods to hook in CSV string or array.
- `$toObject` `object|null|callable` Specify one of the following: - Object instance to call `$toMethod` from (like `$this`). - Inline function (closure) if providing implemention inline. - Procedural function name, if hook is implemented by a procedural function. - Null if you want to use the 3rd argument and don't need this argument.
- `$toMethod` (optional) `string|array` Method from $toObject, or function name to call on a hook event. This argument can be sustituted as the 2nd argument when the 2nd argument isn’t needed, or it can be the $options argument.
- `$options` (optional) `array` Options typically aren't used in this context, but see Wire::addHookBefore() $options if you'd like.

## Return value

- `string` A special Hook ID (or CSV string of hook IDs) that should be retained if you need to remove the hook later.

## See Also

- [https://processwire.com/docs/modules/hooks/](https://processwire.com/docs/modules/hooks/)

## Since

3.0.16 Added as an alias to addHook() for syntactic clarity, previous versions can use addHook() method with same arguments.
