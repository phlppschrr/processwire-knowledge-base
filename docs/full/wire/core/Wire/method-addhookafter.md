# Wire::addHookAfter()

Source: `wire/core/Wire.php`

Add a hook to be executed after the hooked method

- Use an "after" hook when you have code that should execute after a hookable method executes.
- One benefit of using an "after" hook is that you can have it modify the return value.

~~~~~
// Attach hook to a method in current object
$this->addHookAfter('Page::path', $this, 'yourHookMethodName');

// Attach hook to an inline function
$this->addHookAfter('Page::path', function($event) { ... });

// Attach hook to a procedural function
$this->addHookAfter('Page::path', 'your_function_name');

// Attach hook from single object instance ($page) to inline function
$page->addHookAfter('path', function($event) { ... });
~~~~~


@param string|array $method Method to hook in one of the following formats (please omit 3 leading underscores):
 - `Class::method` - If hooking to *all* object instances of the class.
 - `method` - If hooking to a single object instance.
 - Since 3.0.137 it may also be multiple methods to hook in CSV string or array.

@param object|null|callable $toObject Specify one of the following:
 - Object instance to call `$toMethod` from (like `$this`).
 - Inline function (closure) if providing implemention inline.
 - Procedural function name, if hook is implemented by a procedural function.
 - Null if you want to use the 3rd argument and don't need this argument.

@param string|array $toMethod Method from $toObject, or function name to call on a hook event.
  This argument can be sustituted as the 2nd argument when the 2nd argument isn't needed,
  or it can be the $options argument.

@param array $options Array of options that can modify behavior:
 - `type` (string): May be either 'method' or 'property'. If property, then it will respond to $obj->property
    rather than $obj->method(). The default type is 'method'.
 - `priority` (int): A number determining the priority of a hook, where lower numbers are executed before
    higher numbers. The default priority is 100.

@return string A special Hook ID (or CSV string of hook IDs) that should be retained if you need to remove the hook later.

@see https://processwire.com/docs/modules/hooks/
