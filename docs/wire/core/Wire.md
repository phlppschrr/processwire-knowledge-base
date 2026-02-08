# Wire

Source: `wire/core/Wire.php`

ProcessWire Base Class "Wire"

Wire is the base class for most ProcessWire classes and modules.
Wire derived classes have a `$this->wire()` method that provides access to ProcessWire’s API variables.
API variables can also be accessed as local properties in most cases. Wire also provides basic methods
for tracking changes and managing runtime notices specific to the instance.

Wire derived classes can specify which methods are “hookable” by precending the method name with
3 underscores like this: `___myMethod()`. Other classes can then hook either before or after that method,
modifying arguments or return values. Several other hook methods are also provided for Wire derived
classes that are hooking into others.
Shortcuts to ProcessWire API variables. Access without any arguments returns the API variable. Some support arguments as shortcuts to methods in the API variable.
Methods to support tracking and retrieval of changes made to the object.
Methods for managing hooks for an object instance or class.

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com



API variables accessible as properties (unless $useFuel has been set to false):


The following map API variables to function names and apply only if another function in the class does not
already have the same name, which would override. All defined API variables can be accessed as functions
that return the API variable, whether documented below or not.


Other standard hookable methods

## api-helpers

@method WireCache|string|array|PageArray|null cache($name = '', $expire = null, $func = null) Access the $cache API variable as a function.

@method Config|mixed config($key = '', $value = null) Access the $config API variable as a function.

@method WireDatabasePDO database() Access the $database API variable as a function.

@method WireDateTime|string|int datetime($format = '', $value = '') Access the $datetime API variable as a function.

@method Field|Fields|null fields($name = '') Access the $fields API variable as a function.

@method WireFileTools files() Access the $files API variable as a function.

@method WireInput|WireInputData|WireInputDataCookie|array|string|int|null input($type = '', $key = '', $sanitizer = '') Access the $input API variable as a function.

@method WireInputDataCookie|string|int|array|null inputCookie($key = '', $sanitizer = '') Access the $input->cookie() API variable as a function.

@method WireInputData|string|int|array|null inputGet($key = '', $sanitizer = '') Access the $input->get() API variable as a function.

@method WireInputData|string|int|array|null inputPost($key = '', $sanitizer = '') Access the $input->post() API variable as a function.

@method Languages|Language|NullPage|null languages($name = '') Access the $languages API variable as a function.

@method Modules|Module|ConfigurableModule|null modules($name = '') Access the $modules API variable as a function.

@method Page|Mixed page($key = '', $value = null) Access the $page API variable as a function.

@method Pages|PageArray|Page|NullPage pages($selector = '') Access the $pages API variable as a function.

@method Permissions|Permission|PageArray|null|NullPage permissions($selector = '') Access the $permissions API variable as a function.

@method Roles|Role|PageArray|null|NullPage roles($selector = '') Access the $roles API variable as a function.

@method Sanitizer|string|int|array|null|mixed sanitizer($name = '', $value = '') Access the $sanitizer API variable as a function.

@method Session|mixed session($key = '', $value = null) Access the $session API variable as a function.

@method Templates|Template|null templates($name = '') Access the $templates API variable as a function.

@method User|mixed user($key = '', $value = null) Access the $user API variable as a function.

@method Users|PageArray|User|mixed users($selector = '') Access the $users API variable as a function.

## other

@method changed(string $what, $old = null, $new = null) See Wire::___changed()

@method log($str = '', array $options = array()) See Wire::___log()

@method callUnknown($method, $arguments) See Wire::___callUnknown()

@method Wire trackException(\Exception $e, $severe = true, $text = null)

## __construct()

Construct

## __clone()

Clone this Wire instance

## getInstanceNum()

Get this Wire object’s instance number

- This is a unique number among all other Wire (or derived) instances in the system.
- If this instance ID has not yet been set, this will set it.
- Note that this is different from the ProcessWire instance ID.


@param bool $getTotal Specify true to get the total quantity of Wire instances rather than this instance number.

@return int Instance number

## className()

****************************************************************************************************
IDENTIFICATION

## className()

Return this object’s class name

By default, this method returns the class name without namespace. To include the namespace, call it
with boolean true as the first argument.

~~~~~
echo $page->className(); // outputs: Page
echo $page->className(true); // outputs: ProcessWire\Page
~~~~~


@param array|bool|null $options Specify boolean `true` to return class name with namespace, or specify an array of
 one or more options:
	- `lowercase` (bool): Specify true to make it return hyphenated lowercase version of class name (default=false).
	- `namespace` (bool): Specify true to include namespace from returned class name (default=false).
	- *Note: The lowercase and namespace options may not both be true at the same time.*

@return string String with class name

## __toString()

Unless overridden, classes descending from Wire return their class name when typecast as a string

@return string

## _wireHooks()

@return WireHooks|null

@since 3.0.171

## __call()

Provides the gateway for calling hooks in ProcessWire

When a non-existant method is called, this checks to see if any hooks have been defined and sends the call to them.

Hooks are defined by preceding the "hookable" method in a descending class with 3 underscores, like __myMethod().
When the API calls $myObject->myMethod(), it gets sent to $myObject->___myMethod() after any 'before' hooks have been called.
Then after the ___myMethod() call, any "after" hooks are then called. "after" hooks have the opportunity to change the return value.

Hooks can also be added for methods that don't actually exist in the class, allowing another class to add methods to this class.

See the Wire::runHooks() method for the full implementation of hook calls.

@param string $method

@param array $arguments

@return mixed

@throws WireException

## _callWireAPI()

Helper to __call() method that maps a call to an API variable when appropriate

@param string $method

@param array $arguments

@return array|bool

@internal

## ___callUnknown()

If method call resulted in no handler, this hookable method is called.

This standard implementation just throws an exception. This is a template method, so the reason it
exists is so that other classes can override and provide their own handler. Classes that provide
their own handler should not do a `parent::__callUnknown()` unless they also fail, as that will
cause an exception to be thrown.

If you want to override this method with a hook, see the example below.
~~~~~
$wire->addHookBefore('Wire::callUnknown', function(HookEvent $event) {
  // Get information about unknown method that was called
  $methodObject = $event->object;
  $methodName = $event->arguments(0); // string
  $methodArgs = $event->arguments(1); // array
  // The replace option replaces the method and blocks the exception
  $event->replace = true;
  // Now do something with the information you have, for example
  // you might want to populate a value to $event->return if
  // you want the unknown method to return a value.
});
~~~~~


@param string $method Requested method name

@param array $arguments Arguments provided

@return null|mixed Return value of method (if applicable)

@throws WireException

## getHooks()

Return all hooks associated with this class instance or method (if specified)


@param string $method Optional method that hooks will be limited to. Or specify '*' to return all hooks everywhere.

@param int $type Type of hooks to return, specify one of the following constants (from the WireHooks class):
	- `WireHooks::getHooksAll` returns all hooks (default).
	- `WireHooks::getHooksLocal` returns local hooks only.
	- `WireHooks::getHooksStatic` returns static hooks only.

@return array

## hasHook()

Returns true if the method or property is hooked, false if it isn’t.

- This method checks for both static hooks and local hooks.
- Accepts a `method()` or `property` name as an argument.
- Class context is assumed to be the current class this method is called on.
- Also considers the class parents for hooks.

~~~~~
if($pages->hasHook('find()')) {
  // the Pages::find() method is hooked
}
~~~~~


@param string $name Method() name or property name:
  - If checking for a hooked method, it should be in the form `method()`.
  - If checking for a hooked property, it should be in the form `property`.

@return bool True if this class instance has the hook, false if not.

@throws WireException When you try to call it with a Class::something() type method, which is not supported.

## addHookBefore()

Add a hook to be executed before the hooked method

- Use a "before" hook when you have code that should execute before a hookable method executes.
- One benefit of using a "before" hook is that you can have it modify the arguments that are sent to the hookable method.
- This type of hook can also completely replace a hookable method if hook populates an `$event->replace` property.
  See the HookEvent class for details.

~~~~~
// Attach hook to a method in current object
$this->addHookBefore('Page::path', $this, 'yourHookMethodName');

// Attach hook to an inline function
$this->addHookBefore('Page::path', function($event) { ... });

// Attach hook to a procedural function
$this->addHookBefore('Page::path', 'your_function_name');

// Attach hook from single object instance ($page) to inline function
$page->addHookBefore('path', function($event) { ... });
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
  This argument can be sustituted as the 2nd argument when the 2nd argument isn’t needed,
  or it can be the $options argument.

@param array $options Array of options that can modify behavior:
 - `type` (string): May be either 'method' or 'property'. If property, then it will respond to $obj->property
    rather than $obj->method(). The default type is 'method'.
 - `priority` (int): A number determining the priority of a hook, where lower numbers are executed before
    higher numbers. The default priority is 100.

@return string A special Hook ID (or CSV string of hook IDs) that should be retained if you need to remove the hook later.

@see https://processwire.com/docs/modules/hooks/

## addHookAfter()

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

## addHookProperty()

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

## addHookMethod()

Add a hook accessible as a new public method in a class (or object)

- This enables you to add a new accessible public method to an existing object, which will execute
  your hook implementation method when called upon.

- Hook method can accept arguments and/or populate return values, just like any other regular method
  in the class. However, methods such as this do not have access to private or protected
  properties/methods in the class.

- Methods added like this themselves become hookable as well.


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

@param string $method Name of method you want to add, must not collide with existing property or method names:
 - `Class::method` to add the method to all instances of Class.
 - `method` to just add to a single object instance.
 - Since 3.0.137 it may also be multiple methods to hook in CSV string or array.

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

@since 3.0.16 Added as an alias to addHook() for syntactic clarity, previous versions can use addHook() method with same arguments.

@see https://processwire.com/docs/modules/hooks/

## removeHook()

Given a Hook ID, remove the hook

Once a hook is removed, it will no longer execute.

~~~~~
// Add a hook
$hookID = $pages->addHookAfter('find', function($event) {
  // do something
});

// Remove the hook
$pages->removeHook($hookID);
~~~~~
~~~~~
// Hook function that removes itself
$hookID = $pages->addHookAfter('find', function($event) {
  // do something
  $event->removeHook(null); // note: calling removeHook on $event
});
~~~~~


@param string|array|null $hookId ID of hook to remove (ID is returned by the addHook() methods)
 Since 3.0.137 it may also be an array or CSV string of hook IDs to remove.

@return $this

## trackChangesOn

****************************************************************************************************
CHANGE TRACKING

## trackChangesOn

For setTrackChanges() method flags: track names only (default).

## trackChangesValues

For setTrackChanges() method flags: track names and values.

## isChanged()

Does the object have changes, or has the given property changed?

Applicable only when object has change tracking enabled.

~~~~~
// Check if page has changed
if($page->isChanged()) {
  // Page has changes
}

// Check if the page title field has changed
if($page->isChanged('title')) {
  // The title has changed
}
~~~~~


@param string $what Name of property, or if left blank, checks if any properties have changed.

@return bool True if property has changed, false if not.

## ___changed()

Hookable method that is called whenever a property has changed while change tracking is enabled.

- Enables hooks to monitor changes to the object.
- Do not call this method directly, as the `Wire::trackChange()` method already does so.
- Descending classes should call `$this->trackChange('name', $oldValue, $newValue);` when a property they are tracking has changed.


@param string $what Name of property that changed

@param mixed $old Previous value before change

@param mixed $new New value

@see Wire::trackChange()

## trackChange()

Track a change to a property in this object

The change will only be recorded if change tracking is enabled for this object instance.


@param string $what Name of property that changed

@param mixed $old Previous value before change

@param mixed $new New value

@return $this

## untrackChange()

Untrack a change to a property in this object


@param string $what Name of property that you want to remove its change being tracked

@return $this

## setTrackChanges()

Turn change tracking ON or OFF

~~~~~
// Enable change tracking
$page->setTrackChanges(true);

// Disable change tracking
$page->setTrackChanges(false);

// Enable change tracking and remember values
$page->setTrackChanges(Wire::trackChangesValues);
$page->setTrackChanges(true);
~~~~~


@param bool|int $trackChanges Specify one of the following:
  - `true` (bool): Enables change tracking.
  - `false` (bool): Disables change tracking
  - `Wire::trackChangesOn` (constant): Enables change tracking (same as specifying boolean true).
  - `Wire::trackChangesValues` (constant): Enables tracking of changed values when change tracking is already on.
    This uses more memory since it keeps previous values, so it is not enabled by default. Once enabled, the
    setting will persist through boolean true|false arguments.

@return $this

## trackChanges()

Returns true or 1 if change tracking is on, or false or 0 if it is not, or mode bitmask (int) if requested.


@param bool $getMode When true, the track changes mode bitmask will be returned

@return int 0/false if off, 1/true if On, or mode bitmask if requested

## resetTrackChanges()

Clears out any tracked changes and turns change tracking ON or OFF

~~~~
// Clear any changes that have been tracked and start fresh
$page->resetTrackChanges();
~~~~


@param bool $trackChanges True to turn change tracking ON, or false to turn OFF. Default of true is assumed.

@return $this

## getChanges()

Return an array of properties that have changed while change tracking was on.

~~~~~
// Get an array of changed field names
$changes = $page->getChanges();
~~~~~


@param bool $getValues Specify one of the following, or omit for default setting.
 - `false` (bool): return array of changed property names (default setting).
 - `true` (bool): return an associative array containing an array of previous values, indexed by
    property name, oldest to newest. Requires Wire::trackChangesValues mode to be enabled.
 - `2` (int): Return array where both keys and values are changed property names.

@return array

## _notice()

Record a Notice, internal use (contains the code for message, warning and error methods)

@param string|array|Wire $text Title of notice

@param int|string $flags Flags bitmask or space separated string of flag names

@param string $name Name of container

@param string $class Name of Notice class

@return $this

## message()

Record an informational or “success” message in the system-wide notices.

This method automatically identifies the message as coming from this class.

~~~~~
$this->message("This is the notice text");
$this->message("This notice is also logged", true);
$this->message("This notice is only shown in debug mode", Notice::debug);
$this->message("This notice allows <em>markup</em>", Notice::allowMarkup);
$this->message("Notice using multiple flags", Notice::debug | Notice::logOnly);
~~~~~


@param string|array|Wire $text Text to include in the notice

@param int|bool|string $flags Optional flags to alter default behavior:
 - `Notice::admin` (constant): Show notice only if user is in the admin.
 - `Notice::allowMarkdown` (constant): Allow basic markdown and bracket markup (see $sanitizer->entitiesMarkdown()).
 - `Notice::allowMarkup` (constant): Indicates notice should allow the use of HTML markup tags.
 - `Notice::debug` (constant): Indicates notice should only be shown when debug mode is active.
 - `Notice::log` (constant): Indicates notice should also be logged.
 - `Notice::logOnly` (constant): Indicates notice should only be logged.
 - `Notice::login` (constant): Show notice only if it will be seen by a logged-in user.
 - `Notice::noGroup` (constant): Indicates notice should not group with others of the same type (where supported).
 - `Notice::prepend` (constant): Indicates notice should prepend rather than append.
 - `Notice::superuser` (constant): Show notice only if current user is a superuser.
 - `true` (boolean): Shortcut for the `Notice::log` constant.
 - In 3.0.149+ you may also specify a space-separated string of flag names, i.e. "admin log noGroup".

@return $this

@see Wire::messages(), Wire::warning(), Wire::error()

## warning()

Record a warning error message in the system-wide notices.

This method automatically identifies the warning as coming from this class.

~~~~~
$this->warning("This is the notice text");
$this->warning("This notice is also logged", true);
$this->warning("This notice is only shown in debug mode", Notice::debug);
$this->warning("This notice allows <em>markup</em>", Notice::allowMarkup);
$this->warning("Notice using multiple flags", Notice::debug | Notice::logOnly);
~~~~~


@param string|array|Wire $text Text to include in the notice

@param int|bool|string $flags Optional flags to alter default behavior:
 - `Notice::admin` (constant): Show notice only if user is in the admin.
 - `Notice::allowMarkdown` (constant): Allow basic markdown and bracket markup (see $sanitizer->entitiesMarkdown()).
 - `Notice::allowMarkup` (constant): Indicates notice should allow the use of HTML markup tags.
 - `Notice::debug` (constant): Indicates notice should only be shown when debug mode is active.
 - `Notice::log` (constant): Indicates notice should also be logged.
 - `Notice::logOnly` (constant): Indicates notice should only be logged.
 - `Notice::login` (constant): Show notice only if it will be seen by a logged-in user.
 - `Notice::noGroup` (constant): Indicates notice should not group with others of the same type (where supported).
 - `Notice::prepend` (constant): Indicates notice should prepend rather than append.
 - `Notice::superuser` (constant): Show notice only if current user is a superuser.
 - `true` (boolean): Shortcut for the `Notice::log` constant.
 - In 3.0.149+ you may also specify a space-separated string of flag names, i.e. "admin log noGroup".

@return $this

@see Wire::warnings(), Wire::message(), Wire::error()

## error()

Record an non-fatal error message in the system-wide notices.

- This method automatically identifies the error as coming from this class.
- You should still make fatal errors throw a `WireException` (or class derived from it).

~~~~~
$this->error("This is the notice text");
$this->error("This notice is also logged", true);
$this->error("This notice is only shown in debug mode", Notice::debug);
$this->error("This notice allows <em>markup</em>", Notice::allowMarkup);
$this->error("Notice using multiple flags", Notice::debug | Notice::logOnly);
~~~~~


@param string|array|Wire $text Text to include in the notice

@param int|bool|string $flags Optional flags to alter default behavior:
 - `Notice::admin` (constant): Show notice only if user is in the admin.
 - `Notice::allowMarkdown` (constant): Allow basic markdown and bracket markup (see $sanitizer->entitiesMarkdown()).
 - `Notice::allowMarkup` (constant): Indicates notice should allow the use of HTML markup tags.
 - `Notice::debug` (constant): Indicates notice should only be shown when debug mode is active.
 - `Notice::log` (constant): Indicates notice should also be logged.
 - `Notice::logOnly` (constant): Indicates notice should only be logged.
 - `Notice::login` (constant): Show notice only if it will be seen by a logged-in user.
 - `Notice::noGroup` (constant): Indicates notice should not group with others of the same type (where supported).
 - `Notice::prepend` (constant): Indicates notice should prepend rather than append.
 - `Notice::superuser` (constant): Show notice only if current user is a superuser.
 - `true` (boolean): Shortcut for the `Notice::log` constant.
 - In 3.0.149+ you may also specify a space-separated string of flag names, i.e. "admin log noGroup".

@return $this

@see Wire::errors(), Wire::message(), Wire::warning()

## ___trackException()

Hookable method called when an Exception (or Error) occurs

- It will log Exception to `exceptions.txt` log if 'exceptions' is in `$config->logs`.
- It will log Error to `errors.txt` log if 'errors' is in `$config->logs`.
- It will re-throw Exception or Error if `$config->allowExceptions` is true.
- If additional `$text` is provided, it will be sent to notice method call.

Please note that if your root /index.php version is less than 302 it will only receive
Exception (and not Error) objects.


@param \Throwable $e Exception or Error object that was thrown.

@param bool|int $severe Whether or not it should be considered severe (default=true).

@param string|array|object|true $text Additional details (optional):
	- When provided, it will be sent to `$this->error($text)` if $severe is true, or `$this->warning($text)` if $severe is false.
	- Specify boolean `true` to just send the `$e->getMessage()` to `$this->error()` or `$this->warning()`.

@return $this

@throws \Exception|\Error If `$severe==true` and `$config->allowExceptions==true`

## errors()

Return or manage errors recorded by just this object or all Wire objects

This method returns and manages errors that were previously set by `Wire::error()`.

~~~~~
// Get errors for one object
$errors = $obj->errors();

// Get first error in object
$error = $obj->errors('first');

// Get errors for all Wire objects
$errors = $obj->errors('all');

// Get and clear all errors for all Wire objects
$errors = $obj->errors('clear all');
~~~~~


@param string|array $options One or more of array elements or space separated string of:
	- `first` - only first item will be returned
	- `last` - only last item will be returned
	- `all` - include all errors, including those beyond the scope of this object
	- `clear` - clear out all items that are returned from this method
	- `array` - return an array of strings rather than series of Notice objects.
	- `string` - return a newline separated string rather than array/Notice objects.

@return Notices|array|string Array of `NoticeError` errors, or string if last, first or str option was specified.

## warnings()

Return or manage warnings recorded by just this object or all Wire objects

This method returns and manages warnings that were previously set by `Wire::warning()`.

~~~~~
// Get warnings for one object
$warnings = $obj->warnings();

// Get first warning in object
$warning = $obj->warnings('first');

// Get warnings for all Wire objects
$warnings = $obj->warnings('all');

// Get and clear all warnings for all Wire objects
$warnings = $obj->warnings('clear all');
~~~~~


@param string|array $options One or more of array elements or space separated string of:
	- `first` - only first item will be returned
	- `last` - only last item will be returned
	- `all` - include all errors, including those beyond the scope of this object
	- `clear` - clear out all items that are returned from this method
	- `array` - return an array of strings rather than series of Notice objects.
	- `string` - return a newline separated string rather than array/Notice objects.

@return Notices|array|string Array of `NoticeWarning` warnings, or string if last, first or str option was specified.

## messages()

Return or manage messages recorded by just this object or all Wire objects

This method returns and manages messages that were previously set by `Wire::message()`.

~~~~~
// Get messages for one object
$messages = $obj->messages();

// Get first message in object
$message = $obj->messages('first');

// Get messages for all Wire objects
$messages = $obj->messages('all');

// Get and clear all messages for all Wire objects
$messages = $obj->messages('clear all');
~~~~~


@param string|array $options One or more of array elements or space separated string of:
	- `first` - only first item will be returned
	- `last` - only last item will be returned
	- `all` - include all messages, including those beyond the scope of this object
	- `clear` - clear out all items that are returned from this method
	- `array` - return an array of strings rather than series of Notice objects.
	- `string` - return a newline separated string rather than array/Notice objects.

@return Notices|array|string Array of `NoticeMessage` messages, or string if last, first or str option was specified.

## ___log()

Log a message for this class

Message is saved to a log file in ProcessWire's logs path to a file with
the same name as the class, converted to hyphenated lowercase. For example,
a class named `MyWidgetData` would have a log named `my-widget-data.txt`.

~~~~~
$this->log("This message will be logged");
~~~~~


@param string $str Text to log, or omit to return the `$log` API variable.

@param array $options Optional extras to include:
 - `url` (string): URL to record the with the log entry (default=auto-detect)
 - `name` (string): Name of log to use (default=auto-detect)
 - `user` (User|string|null): User instance, user name, or null to log for current User. (default=null)

@return WireLog

## _()

****************************************************************************************************
TRANSLATION

## _()

Translate the given text string into the current language if available.

If not available, or if the current language is the native language, then it returns the text as is.


@param string|array $text Text string to translate (or array in 3.0.151 also supported)

@return string

## _x()

Perform a language translation in a specific context

Used when to text strings might be the same in English, but different in other languages.


@param string|array $text Text for translation.

@param string $context Name of context

@return string Translated text or original text if translation not available.

## _n()

Perform a language translation with singular and plural versions


@param string $textSingular Singular version of text (when there is 1 item).

@param string $textPlural Plural version of text (when there are multiple items or 0 items).

@param int $count Quantity used to determine whether singular or plural.

@return string Translated text or original text if translation not available.

## wire()

Get an API variable, create an API variable, or inject dependencies.

This method provides the following:

- Access to API variables:
  `$pages = $this->wire('pages');`

- Access to current ProcessWire instance:
  `$wire = $this->wire();`

- Creating new API variables:
  `$this->wire('widgets', $widgets);`

- Injection of dependencies to Wire derived objects:
  `$this->wire($widgets);`

Most Wire derived objects also support access to API variables directly via `$this->apiVar`.

There is also the `wire()` procedural function, which provides the same access to get API
variables. Note however the procedural version does not support creating API variables or
injection of dependencies.

~~~~~
// Get the 'pages' API variable
$pages = $this->wire('pages');

// Get the 'pages' API variable using alternate syntax
$pages = $this->wire()->pages;

// Get all API variables (returns a Fuel object)
$all = $this->wire('all');

// Get the current ProcessWire instance (no arguments)
$wire = $this->wire();

// Create a new API variable named 'widgets'
$this->wire('widgets', $widgets);

// Create new API variable and lock it so nothing can overwrite
$this->wire('widgets', $widgets, true);

// Alternate syntax for the two above
$this->wire()->set('widgets', $widgets);
$this->wire()->set('widgets', $widgets, true); // lock

// Inject dependencies into Wire derived object
$this->wire($widgets);

// Inject dependencies during construct
$newPage = $this->wire(new Page());
~~~~~

@param string|object $name Name of API variable to retrieve, set, or omit to retrieve the master ProcessWire object.

@param null|mixed $value Value to set if using this as a setter, otherwise omit.

@param bool $lock When using as a setter, specify true if you want to lock the value from future changes (default=false).

@return ProcessWire|Wire|Session|Page|Pages|Modules|User|Users|Roles|Permissions|Templates|Fields|Fieldtypes|Sanitizer|Config|Notices|WireDatabasePDO|WireHooks|WireDateTime|WireFileTools|WireMailTools|WireInput|PagesVersions|string|mixed

@throws WireException

## __get()

Get an object property by direct reference or NULL if it doesn't exist

If not overridden, this is primarily used as a shortcut for the fuel() method.

Descending classes may have their own __get() but must pass control to this one when they can't find something.

@param string $name

@return mixed|null

## __debugInfo()

debugInfo PHP 5.6+ magic method

This is used when you print_r() an object instance.

@return array
