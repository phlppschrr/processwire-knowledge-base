# ProcessWire Hooks

Source: https://processwire.com/docs/modules/hooks/

## Summary

ProcessWire contains many methods that you may easily hook in order to modify the behavior of the method. Hooks can also be used to add new methods to existing classes.

## Key Points

- Before hooks: A hook that runs before the hooked method. These hooks typically analyze and/or modify the arguments passed to the hooked method.
- After hooks: A hook that runs after the hooked method. These hooks typically analyze and/or modify the return value of the method.
- Replace hooks: A hook that entirely replaces the hooked method. This is a type of Before hook that signals to ProcessWire that it wants to replace the hooked method.
- Method hooks: A hook that adds a new method to a class. The new method becomes accessible via $object->method().
- Property hooks: A hook that adds a new property/variable to a class. The new property becomes accessible via $object->property. Not all ProcessWire classes support property hooks.

## Sections


## Using hooks in ProcessWire

ProcessWire contains many methods that you may easily hook in order to modify the behavior of the method. Hooks can also be used to add new methods to existing classes.


## About hooks


### What are the different types of hooks in ProcessWire?

- Before hooks: A hook that runs before the hooked method. These hooks typically analyze and/or modify the arguments passed to the hooked method.
- After hooks: A hook that runs after the hooked method. These hooks typically analyze and/or modify the return value of the method.
- Replace hooks: A hook that entirely replaces the hooked method. This is a type of Before hook that signals to ProcessWire that it wants to replace the hooked method.
- Method hooks: A hook that adds a new method to a class. The new method becomes accessible via $object->method().
- Property hooks: A hook that adds a new property/variable to a class. The new property becomes accessible via $object->property. Not all ProcessWire classes support property hooks.
- URL/path hooks: A special type of hook that enables the ability to hook into ProcessWire's request URL routing to add your own custom handlers.


### What methods in ProcessWire are hookable?

Any method that begins with 3 underscores, i.e. ___method(), is hookable in ProcessWire.* There are hundreds of them. The ProcessWire API reference outlines the hookable methods for every class and API variable in ProcessWire. Note the icon in the right column of each method list table which identifies hookable methods (example). If you click on the details of any hookable method (example), it also provides introduction of how to hook both before and after that method (example).

New methods added to a class via a hook are themselves hookable too. For example, Page::render(), Page::viewable() and Page::editable() are all methods added to the Page class via method hooks. If you view the /wire/core/Page.php class, you'll see that none of these methods actually exist in the class. However, you can hook before or after any of them just as easily as if they were defined in the class.

If you can't find a hook that you need (or just aren't sure) post a question in the forum. If we don't already have a hook for what you need, we can usually add one.

*Note that the 3 leading underscores for hookable methods only appears in ProcessWire's source code—hookable methods are not identified this way in the online API reference. That's because you should not call a hookable method with the 3 underscores directly, unless you want to intentionally bypass any hooks attached to it.


## Defining Hooks


### Do I want my hook to run before or after the method I am hooking? (Or, does it matter?)

Before hooks You would want your hook to run before the hooked method if you want to analyze or modify the arguments supplied to the hooked method. Another use case for a before hook is if you wanted to entirely replace the implementation of the hooked method. Before hooks are defined with $this->addHookBefore(…); within a class, or wire()->addHookBefore(…); outside of a class.

After hooks You would want your hook to run after the hooked method if you wanted to analyze or modify the return value of the hooked method. An After hook can also analyze the arguments supplied to the hooked method, but not modify them (at least, it wouldn't be particularly useful to). After hooks are defined with $this->addHookAfter(…); within a class, or wire()->addHookAfter(…); outside of a class.

Hooks where it doesn't matter When you are defining a new method or property for a class via a hook, there is no question of before or after, so you can simply define such a hook with $this->addHook(…) or wire()->addHook(…).

Some hookable methods in ProcessWire have no implementation and exist purely for you to hook. Because hooks like this exist purely "to be hooked", it doesn't matter if you hook before or after them. Examples include Pages::saveReady which is called after it's been determined the page will definitely be saved, but right before it is done. Another is Pages::saved, which is called after a page has successfully been saved. These hooks provide more certainty and less need for error checking than hooking before or after Pages::save. You may see several other specific-purpose hooks like this in ProcessWire.

Hooking both before and after If you want your hook method to run both before and after a particular event occurs, you can specify that in an $options array to the addHook() call, like this:

```
$wire->addHook('Class::method', function(HookEvent $e) {
  // ...
}, [ 'before' => true, 'after' => true ]);
```

In the example above, we've specified that we want this hook to run both before and after the method we are hooking. If you want to know what state you are in (before or after) from within the hook function, you can examine the HookEvent "when" property, which will have a value of either "before" or "after":

```
$wire->addHook('Class::method', function(HookEvent $e) { 
  if($e->when == 'before') {
    // this is the 'before' state
  } else if($e->when == 'after') {
    // this is the 'after' state'
  }
}, [ 'before' => true, 'after' => true ]);
```


### Do I want my hook to apply to all instances of a class, or just one?

Most of the time you want a hook to apply to all instances of a class. For instance, when you hook Page::viewable, you likely want your hook to be called regardless of what Page it is. Such hooks are defined by specifying the class and method (i.e. Class::method) in the addHook() call. For example:

```
// inside a class
$this->addHookAfter('Class::method', function($event) {
  // function implementation
});

// inside a class (if 'myHookMethodName' is a public method of class)
$this->addHookAfter('Class::method', $this, 'myHookMethodName');
```

```
// outside a class  
wire()->addHookAfter('Class::method', function($event) {
  // function implementation
});

// outside a class (if 'myHookFunctionName' defined separately)
wire()->addHookAfter('Class::method', null, 'myHookFunctionName');
```

For the times when you want your hook to apply only to a single instance of a class, you can attach the hook directly to the object instance of that class:

```
// inside a class
$page = $this->wire('page'); // may be any Page object instance
$page->addHookAfter('render', function($event) { ... });

// outside a class ($page may be any Page object instance)
$page->addHookAfter('render', function($event) { ... });
```

The primary distinction is that we are calling the addHookAfter() method directly on the $page instance we want to attach it to (rather than attaching it using $this or wire()).

Some of ProcessWire's API variables (like $pages) only ever contain one instance. As a result, you may find it more efficient to attach such hooks directly to $pages (though it really doesn't matter much). For example, these two calls (below) do exactly the same thing. But the second one that attaches directly to $pages may be slightly more efficient:

```php
$this->addHookAfter('Pages::saveReady', function($event) { ... }); 
$pages->addHookAfter('saveReady', function($event) { ... }); // equivalent
```


### Where should I define my hook?

Hooks are most often defined in ProcessWire plugin modules or initialization template files. However, this is not a requirement, and you may technically define hooks anywhere you want. But you need to make sure that your hook really does get called when you want it to, so your hook must be defined and attached sometime before the method you are hooking gets called.


### Attaching hooks from a plugin module

Attach hooks with a plugin module set to "autoload" on every request. Such modules are called "autoload modules." These autoload modules have an init() method that gets called before ProcessWire handles a web request. This is the best place to attach hooks. However, this init() method is called before ProcessWire even knows what $page it will be rendering. So if your module needs to determine whether it should hook or not based on what $page is being viewed, you should attach your hook in a ready() method rather than an init() method. The ready() method is always called for all autoload modules right after ProcessWire determines what $page is going to be viewed.

To summarize: when defining hooks through modules, you will most likely want to attach those hooks through either the init() or ready() method of the module.


### Attaching hooks from /site/ready.php or /site/init.php

A common and excellent place for attaching site-specific hooks is from the /site/ready.php file or sometimes the /site/init.php file. The ready.php file is called when the API is ready, but before page rendering has begun. While the init.php file is called during ProcessWire initialization (before the API is fully ready).


### Attaching hooks from a template file

If you are defining hooks via your template file(s), you will most likely want to place such definitions near the top of the file, or in a common header include file used by all of your template files. An easy way to do this is to define $config->prependTemplateFile in your /site/config.php file. Whatever file you define there will be automatically included before all of your site template files (except for the one used by the admin). Many of ProcessWire's site profile already have this defined as _init.php. Regardless of what it is named, this is the file where you would want to place your hooks.

The $config->prependTemplateFile is not used by the ProcessWire admin, so if you are defining hooks specific to the ProcessWire admin, you should define them at the very top of the /site/templates/admin.php. If your hooks are applicable to both your site (front-end) and the ProcessWire admin, then you should manually include your site's initialization fie, i.e. include("./_init.php"); from your /site/templates/admin.php file.


### How can my hook read (or modify) the arguments sent to the hooked method?

Every hook is passed an object called $event (of type HookEvent). This object contains an arguments() method that you can access to retrieve the arguments of the method either by index or name. This is best demonstrated in code. Lets say that you wanted to hook Pages::saved. In looking at the function definition in Captain Hook or directly in the file at /wire/core/Pages.php, you'll note that this function has one argument called $page. With this knowledge in hand, you have everything you need to retrieve that in your hook function:

```
public function myHookFunction($event) {
  // retrieve first argument by index (0 based)
  $page = $event->arguments(0);
  // OR: retrieve argument by name 'page'
  $page = $event->arguments('page');
  $this->message("You saved page: $page->path");
}
```

A Before hook has the opportunity to modify the arguments sent to the hooked function. In order to modify the argument, the hook must assign the argument back to $event->arguments by index or name, like this:

```
// assign by index (0=first argument)
$event->arguments(0, $myValue);

// assign by name
$event->arguments('argument_name', $myValue);
```


### How can my hook read (or modify) the return value of the hooked method?

The return value of a hooked function may be read or modified in a similar manner to the arguments. However, the return value is only available to After hooks. This is best demonstrated by a code example. Lets say that we want to add the text "Hello World" before the closing </body> tag of each rendered page. We would hook after Page::render with a hook method implementation like this:

```
public function hookAfterPageRender($event) {
  // $value contains the full rendered markup of a $page
  $value  = $event->return;
  $value = str_replace("</body>", "<p>Hello World!</p></body>", $value);
  // set the modified value back to the return value
  $event->return = $value;
}
```


### How can my hook know what object/instance the hook was called on?

Every hook function receives an $event object and this $event contains a property called $event->object. That property ($event->object) contains the instance of the object that the hook was executed on. For example:

```
public function hookAfterPageRender($event) {
  $page = $event->object;
  if($page->id == 1) {
    $event->return = str_replace("</body>", "<p>Homepage!</p></body>", $event->return);
  }
}
```


### How can my hook replace another method entirely?

This is a rare need, and one to be careful with, but it is possible to accomplish in ProcessWire. A hookable method can only be replaced with a Before hook. The hook sets the value of $event->replace = true; and this tells ProcessWire not to call the originally hooked method. Assuming the originally hooked method was going to return some value, the hook should populate $event->return with an expected value since the original method won't be able to do so.

```
public function hookBeforePageRender($event) {
  $page = $event->object;
  // we'll only apply this to the front-end of our site
  if($page->template == 'admin') return;
  // tell ProcessWire we are replacing the method we've hooked
  $event->replace = true;
  $event->return = "Sorry the site is undergoing maintenance";
}
```


### How can I define my own hookable methods?

Hookable methods can be defined in any class derived from ProcessWire's Wire class. Nearly all of ProcessWire's core classes and modules are derivative of the Wire class, and thus capable of having hookable methods. To make a class capable of having hookable methods, simply extend one of ProcessWire's classes such as Wire or WireData as your base. Most ProcessWire modules typically extend the WireData class. Assuming your class or module extends one of ProcessWire's classes, you can make any method hookable simply by prepending 3 underscores to the beginning of the methods you want to be hookable.

```
public function ___hookableMethod($arg1, $arg2) {
  // this method is hookable
}

public function regularMethod($arg1, $arg2) {
  // this method is not hookable
}
```

Calls to a hookable method should always be without the 3 underscores, i.e.

```
$this->hookableMethod('a', 'b');
```

If for some reason you need to bypass ProcessWire's hook system for a given method, you can include the 3 underscores in the method call and no hooks will be executed.


### How can I add a new method via a hook?

You can add new methods to any ProcessWire class in the same way that you would hook an existing method. The only difference is that the method doesn't already exist, so you are adding it. Also, because there is no distinction of "before" or "after" for something that doesn't already exist, you can attach the method using addHook(); rather than addHookBefore(); or addHookAfter() … though technically it doesn't really matter what you use here. Lets say that you wanted to add a new method to all Page instances that outputs a relative time string of when the page was last modified (for example, "45 minutes ago" or "3 days ago", etc.):

```
public function init() {
  $this->addHook('Page::lastModified', $this, 'lastModified');
}

public function lastModified($event) {
  $page = $event->object;
  $event->return = wireRelativeTimeStr($page->modified);
}
```

Now all Page instances have a $page->lastModified(); method:

```
echo $page->lastModified(); // outputs "10 minutes ago"
```

New methods that you add can also use arguments. Lets say that we wanted to change our lastModified() function to accept a single boolean argument that indicates whether it should return a defined date/time like "2013-05-15 10:15:12" or a relative date/time like "10 minutes ago":

```
public function lastModified($event) {
  $page = $event->object;
  if($event->arguments(0) === true) {
    // return relative time
    $event->return = wireRelativeTimeStr($page->modified);
  } else {
    $event->return = date('Y-m-d H:i:s', $page->modified);
  }
}
```

Here are example calls:

```
echo $page->lastModified(true); // returns "10 minutes ago"
echo $page->lastModified(false); // returns "2013-05-15 10:15:12"
echo $page->lastModified(); // returns "2013-05-15 10:15:12"
```


### How can I add a new property via a hook?

You can add new properties to some ProcessWire classes (like the Page class) by attaching it with addHookProperty(). For example, lets say that we wanted to add a "hello" property to all User objects that contains a custom greeting to the user like "Hello [username]":

```
public function init() {
  $this->addHookProperty("User::hello", $this, "hookUserHello");
}

public function hookUserHello($event) {
  $user = $event->object;
  $event->return = "Hello $user->name";
}
```

Now all User instances contain a "hello" property that when accessed, says "Hello [username]":

```
echo $user->hello; // outputs "Hello Karena"
```

As another example, lets say that we want to add a new property called "intro" that returns a short version of the body copy limited to 255 characters. For the sake of diversity, we'll use the "outside of a class" approach that you might use from your template files. In such a case, you would want to define this at the top of your template file (or in a common header include).

```
wire()->addHookProperty('Page::intro', function($event) {
  $page = $event->object;
  $intro = substr(strip_tags($page->body), 0, 255);
  $lastPeriodPos = strrpos($intro, '.');
  if($lastPeriod !== false) $intro = substr($intro, 0, $lastPeriodPos);
  $event->return = $intro;
});
```

Now every Page object has an "intro" property that is a short version of the body copy that can be accessed via $page->intro:

```
foreach($page->children as $child) {
  echo "<p><a href='$child->url'>$child->title</a><br />$child->intro</p>";
}
```


### Shorter hook syntax

While optional, we recommend taking advantage of anonymous functions for shorter syntax. This enables you to attach and define a hook within 1 function call:

```
$this->addHookAfter('Class::method', function($event) { // inside a class
  // hook method implementation
});

wire()->addHookAfter('Class::method', function($event) { // outside a class
  // hook method implementation
});
```

Note: since the anonymous function usage is now common, we use examples of both throughout this documentation page. If for some reason you are using a really old very of ProcessWire (prior to 2.4) you'll want to stick with the non-anonymous function version.


## URL/path hooks

URL/path hooks are quite powerful as they enable you to hook into ProcessWire's request URL routing to add your own custom handlers for any URL. This puts you in full control over ProcessWire’s matching of URLs-to-pages, or URLs-to-anything that you want. For example, the following hook returns the text “Hello World” when you load the URL /hello/world in your browser:

```
$wire->addHook('/hello/world', function($event) {
  return 'Hello World';
});
```

…while the this hook renders the /about/contact/ page when you load the URL /contact/ in your browser:

```
$wire->addHook('/contact/', function($event) {
  return $event->pages->get('/about/contact/');
});
```

The above examples only scratch the surface of what’s possible with URL/path hooks. You can handle multiple URLs in one hook, match URLs dynamically with patterns, convert URL segments to variables, and much more. Because there is so much possible we have a page just for URL/path hooks.

Please see the dedicated URL/path hooks page for full details, documentation and examples.


## Conditional hooks

Conditional hooks imply the ability to specify conditions along with the hook definition. These conditions determine at runtime whether or not your hook function will execute.


### Defining conditional hooks

Conditional hooks are best explained by example. Let's say we've got the following hook function in our /site/ready.php file. The Page::changed hook is called every time a value is modified on a page. It receives 3 arguments: the name of field that changed, the old value, and the new value. Here's what a function that hooks to Page::changed looks like, without use of conditional hooks:

```
$wire->addHookAfter('Page::changed', function(HookEvent $event) {
  $page = $event->object;
  $change = $event->arguments(0);
  if($page->template == 'order' && $change == 'order_status') {
    // execute some code when "order_status" changes on "order" pages.
  }
});
```

The conditional format lets you accomplish the same thing as the above, like this:

```
$wire->addHookAfter('Page(template=order)::changed(order_status)', 
  function($event) {
    // execute some code when "order_status" changes on "order" pages.
  });
```

The expressions in parenthesis that you see in the conditional format (template=order) and (order_status) are where conditions are specified. This can be any selector string or the value you want to match. In our example above, the first argument to Page::changed() is a string (specifically, the name of the field that changed) so we just specify the value we require to be present in order to execute our hook function. Were the argument an object, then we'd specify a selector string to match some property in it.

Here's the same example, but taken a little further on the implementation side:

```
$wire->addHookAfter("Page(template=order)::changed(order_status)", 
  function(HookEvent $event) {
    $page = $event->object;
    $old = $event->arguments(1); // old value
    $new = $event->arguments(2); // new value
    $event->addHookAfter("Pages::saved($page)",
      function($event) use($page, $old, $new) {
        $event->message("Status change: $old->title to $new->title");
        $event->removeHook(null);
      });
  });
```

In the above example, you can see that we are attaching yet another conditional hook Pages::saved($page) within the hook, and that hook executes when the $page that had the order_status change is saved. When that page is saved, we report a message, and then remove the hook (since we only want it to run once).

Stepping back for a minute, lets take a closer look at the ::changed(order_status) part. In most cases, when using conditional hooks you are likely to want to match something from the first argument to the hook method. However, if you want to match a value from something other than the first argument to the hooked method (or maybe multiple arguments at once), you can still do so. Just specify the zero-based index of the argument in this format "0:conditions".

For example, lets say that we wanted our hook to execute when the order_status changes from "pending" to "delivered". Since the Page::changed() method has 3 arguments (property, old value, new value) we can access those as arguments 0, 1, 2. Our hook definition can access them like this below. Note that order_status is a Page field in our case, so will compare against its "name" property.

```
$wire->addHookAfter("Page(template=order)::changed(0:order_status, 1:name=pending, 2:name=delivered)", 
  function(HookEvent $event) {
    // ...
  });
```

With the above, our hook function will only be called when a page using template "order" has an order_status field that changes from "pending" to "delivered". Now that may be getting a little much, and you certainly don't have to place all your conditions in your hook definition of you don't want to. The example is just there to show you that you can, if you want to. You could just as easily do this, using a conditional hook, but checking the order_status values within your hook function instead:

```
$wire->addHookAfter("Page(template=order)::changed(order_status)", 
  function(HookEvent $event) {
    $old = $event->arguments(1);
    $new = $event->arguments(2);
    if($old->name == 'pending' && $new->name == 'delivered') {
      // ...
    }
  });
```

The selectors that you see above like Page(template=order) are just examples. The Page part could be any ProcessWire class name—our example here is just matching instances of Page objects. The template=order can be any selector and use any operator supported by our in-memory selectors. For instance, if we wanted to instead match all Page objects using a template having a name that started with the word "order" then we would use Page(template^=order) since the ^= operator is the "starts with" operator. Such a selector would match Page objects having templates with names like "orderinfo", "order_product", "order-details", etc. For more about about selectors and operators see ProcessWire selectors.


### Conditional hooks matching argument type

In ProcessWire 3.0.222 or newer, you can also match by argument type. To do this, use the type name as the argument value and wrap it with less/greater than signs, i.e. <type>. The type can be an object class or interface, or any one of these predefined type names: <array>, <bool>, <float>, <int>, <null>, <object>, <string>. If you specify a type that does not match one of those listed, it is assumed to be a class or interface name. In the example below, we add a hook to Pages::saveReady that only matches if the first argument ($page) is an object of type User (or one that extends User):

```
$wire->addHook('Pages::saveReady(<User>)', function(HookEvent $event) {
  $user = $event->arguments(0);
  $event->message("Saving user: $user->name");
});
```

To specify an OR condition for the type, separate each type name with a pipe

```
$wire->addHook('Pages::saveReady(<User|Role|Permission>)', function($event) {
  $page = $event->arguments(0);
  $event->message("Saving user, role or permission: $page->name");
});
```

When using <Name> where Name is a class or interface name (i.e. <Page>) please note that it is checking that the argument value is an instance of the given class name. Meaning that <Page> will also match objects of type User since the User class extends the Page class. The same would be true of Role, Permission, and Language objects, since they all extend Page. The point here is that it is performing an instanceof comparison, not a class name comparison.


### Conditional hooks matching return value or type

Matching by return value or type is supported by ProcessWire 3.0.247 and newer.

For methods that return a value, you can use after hooks to conditionally execute your hook code if the return value matches a value, selector or type that you specify. This works very much like argument matching, except that it is instead matching the return value of the hooked function. Here is an example of a hook matching a return value with a selector:

```
$wire->addHookAfter('Field::getInputfield:(label*=Currency)', function($event) {
  $inputfield = $event->return;
  $e->message("Matched '$inputfield->name' with label: $inputfield->label");
});
```

The above says to match any Field::getInputfield() call that returns an object that contains "Currency" somewhere in its "label" property. Note the single colon : in the definition, which tells ProcessWire that what follows is matching the return value of the hooked method. Also note the (label*=currency) selector surrounded in parenthesis. The parenthesis are required when specifying selectors, but can optionally be used in all return value matches.

You can match more than one property at a time, just by separating each key=value selector with a comma, i.e. (label*=Foo, name!=bar).

For methods that return some other type, such as a string or integer, you can match those values directly. If a method returned a string that either contained the word "foo", "bar" or "baz", then you could match only those that returned the word "bar" like this:

```
$wire->addHookAfter('SomeClass::someMethod:(bar)', function($e) { …
```

But since there is no selector in "bar", the parenthesis are optional, so this would do the same as the above:

```
$wire->addHookAfter('SomeClass::someMethod:bar', function($e) { …
```

If we want to match any one of a set of values, we'll want to use a selector. But since we're matching a string value (rather than a property of an object) we'll skip the "key" part of "key=value" in the selector. For example, the following would match if the method returned either "foo" or "bar", but would not match if it returned "baz", or some other value:

```
$wire->addHookAfter('SomeClass::someMethod:(=foo|bar)', function($e) { …
```


### Conditionally hook based on returned array values

For hooked methods that return standard or associative PHP arrays, you may specify any value that might appear in the array and the hook will execute if the array contains the value you specified somewhere within it. The hook definitions are essentially identical to those that deal with direct string or number return values.

```
$wire->addHookAfter('SomeClass::someMethod:someValue', function($e) { …
```

In the above example, if someMethod() returns an array that contains "someValue", somewhere within it, then the hook will execute.

If you want the hook to execute if the returned array includes either "thisValue" or "thatValue" within it then you could do this:

```
$wire->addHookAfter('SomeClass::someMethod:(=thisValue|thatValue)', function($e) { …
```

When it comes to associative arrays, you can match values in the same way that you can with objects by specifying any selector to match the array key and value, using whatever operator is appropriate. The hook example below executes if the returned array includes a "color" index with the value "blue":

```
$wire->addHookAfter('SomeClass::someMethod:(color=blue)', function($e) { …
```


### Conditionally hook by matching return value <type>

In addition to matching by value or selector, you can also match by return type in the same way that you do matching by argument type. When you surround a type name in brackets like <type> it will match that type. When specifying object types, it becomes an "instance of" comparison. So specifying <InputfieldText> will also match InputfieldTextarea and any other Inputfields that extend InputfieldText:

```
$wire->addHookAfter('Field::getInputfield:<InputfieldText>', function($e) { …
```

Since there is no selector present in a selector comparision, the use of parenthesis around the type is optional, so you could specify <InputfieldText> or (<InputfieldText>) in the example above, and the result would be the same. If you want to match multiple types, separate them with a pipe, i.e.

```
$wire->addHookAfter('Field::getInputfield:<InputfieldRadios|InputfieldCheckboxes>', function($e) { …
```

Note that because an "instance of" comparison is used with object return values, you may specify class names or interfaces.

The non-object types that you can match include <array>, <bool>, <float>, <int>, <null>, <object>, <string>

```
$wire->addHookAfter('SomeClass::someMethod:<int|float>', function($e) { …
```

The above hook executes if the hooked method returns an integer or float value.

To conclude our section on conditionally hooking with return types, let's combine this type of conditional hook with the other types of conditionals we've covered so far. This particular example might go in our /site/templates/admin.php file. Note that this is a contrived example and it's unlikely you would actually combine all these types of conditionals in one hook definition like this. Just know that you can if you want to.

```php
<?php namespace ProcessWire;

$wire->addHookAfter('Field(name!=title)::getInputfield(template=product):(label*=description)',
  function(HookEvent $event) {
    $field = $event->object; // Field object not named 'title'
    $page = $event->arguments(0); // Page object using template 'product'
    $inputfield = $event->return; // Inputfield for product page with 'description' in label
    $event->message(
      "We hooked getInputfield for field '$field' that does not have the name 'title' and " .
      "for page '$page' that is using the template 'product', so long as the returned " .
      "Inputfield 'label' ($inputfield->label) contains 'description' somewhere in it. "
    );
  });
```


## More hook features


### Hook priority to dictate execution order

It's likely rare that you will need this, but good to know about when and if the need arises. When adding a hook, you can optionally specify the priority relative to other hooks that may also be attached to the same method. In this manner, you can insure that your hook runs either before or after other hooks. The lower the priority number, the earlier the hook executes. The default priority is 100, so this is the priority number used by the vast majority of hooks. All hooks having the same priority number simply execute in the order they are added. If you wanted to hook before other hooks (that are using the default priority of 100), then you might specify a priority of 99 or some other number lower than 100. If you wanted your hook to run after other default priority hooks, then you might specify a number of 101 or 200 or some other number higher than 100. Here's how to add a hook while specifying the priority number:

```
// hook after any other default priority hooks to Page::render()
$this->addHookAfter('Page::render', $this, 'myHookFunc', [ 'priority' => 200 ]);

// hook before other default priority hooks to Pages::saveReady()
$this->addHookBefore('Pages::saveReady', function($event) {
  // in this case using an anonymous function for hook implementation
}, [ 'priority' => 99 ]);
```


### Hooking multiple methods at once

In ProcessWire 3.0.137 and newer, you can hook multiple methods to the same handling function at once. Just separate the methods you want to hook with a comma:

```php
// hooking to viewable and editable methods from all Page instances
$wire->addHookAfter('Page::viewable, Page::editable', function($e) {
  $event->message("Called the $e->method hook");
});

// hooking to saveReady and saved from $pages API var
$pages->addHookBefore('saveReady, saved', function($event) {
  $event->message("Called the $event->method hook");
});
```

This works with any of the addHook methods, whether it’s addHookBefore, addHookAfter, addHookProperty, addHookMethod, or just the regular addHook method. Here is a real life example of using this capability.


### Removing hooks

When you add a hook, a hook ID is returned. This hook ID can be used to later remove the hook:

```
// add the hook
$hookID = $wire->addHook('Inputfield(name^=repeater_item)::render', function($e) {
  // ...
});

// remove the hook at some later time
$wire->removeHook($hookID);
```

A hook can also remove itself by calling removeHook(null) on the HookEvent object that it receives:

```
$wire->addHook('Inputfield::render', function(HookEvent $e) {
  // do something, then remove hook so that it only runs this once:
  $e->removeHook(null);
});
```


### Additional reading

- Load the Helloworld module in your code/text editor for a good example of various hooks attached via an autoload module.
- HookEvent class
- URL/path hooks
