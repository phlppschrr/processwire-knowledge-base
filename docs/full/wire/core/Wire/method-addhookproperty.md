# Wire::addHookProperty()

Source: `wire/core/Wire.php`

Add a hook that will be accessible as a new object property.

This enables you to add a new accessible property to an existing object, which will execute
your hook implementation method when called upon.

Note that adding a hook with this just makes it possible to call the hook as a property.
Any hook property you add can also be called as a method, i.e. `$obj->foo` and `$obj->foo()`
are the same.

~~~~~
// Adding a hook property
$wire->addHookProperty('Page::lastModifiedStr', function($event) {
  $page = $event->object;
  $event->return = wireDate('relative', $page->modified);
});

// Accessing the property (from any instance)
echo $page->lastModifiedStr; // outputs: "10 days ago"
~~~~~


@param string|array $property Name of property you want to add, must not collide with existing property or method names:
 - `Class::property` to add the property to all instances of Class.
 - `property` if just adding to a single object instance.
 - Since 3.0.137 it may also be multiple properties to hook in CSV string or array.

@param object|null|callable $toObject Specify one of the following:
 - Object instance to call `$toMethod` from (like `$this`).
 - Inline function (closure) if providing implemention inline.
 - Procedural function name, if hook is implemented by a procedural function.
 - Null if you want to use the 3rd argument and don't need this argument.

@param string|array $toMethod Method from $toObject, or function name to call on a hook event.
  This argument can be sustituted as the 2nd argument when the 2nd argument isn’t needed,
  or it can be the $options argument.

@param array $options Options typically aren't used in this context, but see Wire::addHookBefore() $options if you'd like.

@return string A special Hook ID (or CSV string of hook IDs) that should be retained if you need to remove the hook later.

@see https://processwire.com/docs/modules/hooks/
