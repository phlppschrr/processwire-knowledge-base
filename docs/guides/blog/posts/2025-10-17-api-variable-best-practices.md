# Best practices for using API variables

Source: https://processwire.com/blog/posts/api-variable-best-practices/

## Sections


## Best practices for using ProcessWire API variables

17 October 2025 by Ryan Cramer [ 2 Comments](/blog/posts/api-variable-best-practices/#comments)

ProcessWire’s API is accessible through API variables and it provides multiple ways to access them. There are benefits and drawbacks to each approach and this post aims to cover them all.


### Using the ProcessWire namespace

Many of the suggestions in this post depend upon being in the ProcessWire namespace. So if you aren't already using some other namespace for one reason or another, make sure you have the ProcessWire namespace defined at the top of your PHP files, such as template and module files, custom class files, and any other PHP files referred to by any of them:

```php
<?php namespace ProcessWire;
```

Another reason to use the ProcessWire namespace (or any namespace for that matter) is that ProcessWire will attempt to compile PHP files that are in the root namespace. This was really helpful when upgrading from PW 2.x to 3.x, but that was many years ago, and there's no reason not to use the ProcessWire namespace now.


### More than one way to access API variables

For some, the differences in API syntax may not matter much. But for others, there are significant benefits and drawbacks to the different syntax options, depending on the context.

Below are all the different ways we can access API variables. We'll use the `$page` API variable as an example, but the same would apply to any other core API variable.

| Syntax | Wired | Tired |
| --- | --- | --- |
| `$page` |  | Not always in scope. Can be accidentally overwritten. Phpdoc required to identify to IDE. |
| `wire('page')` | Works anywhere. | Not recognized by IDE. Not multi-instance. |
| `wire()->page` | Works anywhere. IDE support. | Not multi-instance. Type can’t be redeclared. |
| `page()` | Works anywhere. IDE support. | Not enabled in all installations. Not multi-instance. Type can’t be redeclared. |
| `wirePage()` | Works anywhere. Always enabled. IDE support. | Not multi instance. Rarely used or seen. Type can’t be redeclared. |
| `$this->page` | IDE support. Easy and short. Class can declare type. | Can collide with class variables. Relies upon __get() fallback. Not all classes support. |
| `$this->wire()->page` | Works in all classes. IDE support. | Kind of verbose. Type can’t be redeclared. |
| `$this->wire('page')` | Works in all classes. | Not recognized by IDE. Kind of verbose. Type can’t be redeclared. |

The `$this` reference can be replaced with almost any other Wire-derived object instance, as they all are connected to the ProcessWire API in the same way. For instance, a hook receives a `HookEvent` variable typically named `$event` or `$e`, which could be used instead of `$this` to access an API variable from within a hook function. There is an example of this further down in this post.


### What’s better: `wire()->apiVar` or `wire('apiVar')`?

Use `wire()->apiVar` or `apiVar()` rather than `wire('apiVar')` …and when in a class use `$this->wire()->apiVar` rather than `$this->wire('apiVar')`.

Why? IDEs can better identify what type `apiVar` is when accessed as a function or as a property off of a function call. This makes it possible for the IDE to identify what methods can be accessed from it, what arguments are available, what the return values are, let you know when you've made a typo, and more.

```php
// Before:
$items = wire('pages')->find('…');
$items = $this->wire('pages')->find('…'); // in class

// After:
$items = wire()->pages->find('…'); // works anywhere
$items = pages()->find('…'); // if using functions API
$items = $pages->find('…'); // if $pages in scope
$items  $this->wire()->pages->find('…'); // in class method
```


### What about using `$this->apiVar` in a class?

You can use `$this->apiVar` in most Wire derived classes (i.e. `$this->pages`), and this syntax still provides the type-hinting benefits to your IDE. But you can't always count on this local-variable access to be available, so I tend to avoid using this syntax. For instance, what if the class (or any descending class) declares its own variable that happens to conflict with an API variable name? The API variable no longer works. The other downside is that accessing `$this->apiVar` gets sent to the `__get()` method in the class, which may or may not have a lot of comparisons to make. So it's generally more efficient to use `$this->wire()->apiVar`. As a bonus, it also makes it simpler to differentiate uses of API variables from class variables.


### Using API variables in functions or methods

In functions or methods, if you refer to any API variable more than once or twice, or refer to it in a loop, create and use your own local copy of the API variable.

Why? It makes your code easier to read, and reduces the number of function calls taking place.

```
// Before (in class):
public function foo(array $bars) {
  foreach($bars as $bar) {
    echo $this->wire()->sanitizer->text($bar);
  }
}

// After (in class):
public function foo(array $bars) {
  $sanitizer = $this->wire()->sanitizer;
  foreach($bars as $bar) {
    echo $sanitizer->text($bar);
  }
}

// After (procedural function):
function foo(array $bars) {
  $sanitizer = wire()->sanitizer;
  foreach($bars as $bar) {
    echo $sanitizer->text($bar);
  }
}
```

In the examples above, let's say that there are 100 items in the `$bars` array variable. The "before" version of the function would make at least 200 function calls, while the "after" versions would make about half that many function calls (~101). Multiply this over many times and it might add up. This is likely more of a micro-optimization, but it benefits readability either way by not having numerous redundant `$this->wire()->...` calls.


### `wire()` vs `$this->wire()` in classes

Use `$this->wire()->apiVar` rather than `wire()->apiVar` when inside Wire derived classes like modules or custom class files in /site/classes/.

Why? In a multi-instance environment, it can be ambiguous which ProcessWire instance `wire()->apiVar` is referring to.

ProcessWire supports multiple instances of itself running from the same request. So it may not be clear which instance a `wire()->apiVar` call is referring to, especially if inside a class, such as a module. So a best practice for custom class or module authors would be to avoid using `wire()->apiVar` and instead use `$this->wire()->apiVar`. By referring to `$this`, it can only refer to the ProcesssWire instance it was loaded from.

This is unlikely to be an issue in template files. That's because ProcessWire sets the instance that `wire()` refers to before it starts rendering a template file, and then restores it after rendering a template file.


### Using ProcessWire’s functions API

Consider using ProcessWire’s functions API for files in /site/templates/.

Why? It makes code easy to write, easy to read, and easy for your IDE to understand.

You can enable the [functions API](../../../full/wire/core/FunctionsAPI/index.md#pwapi-methods-Functions-API) by setting this in your /site/config.php file, if it isn't already:

```
$config->useFunctionsAPI = true;
```

Most of the code we write for a web site is generally in /site/templates/. ProcessWire’s functions API makes it possible to refer to most API variables as functions. For instance, `$pages` and `pages()` would refer to the same thing. And `$pages->find()` would be the same as `pages()->find()`.

The benefit of using the function version is two-fold:

When using the variable version (i.e. `$pages`) your IDE won't know what type `$pages` is, nor will it even know that it's a defined variable, unless you tell it with phpdoc, like this:

```
/** @var Pages $pages */
```

So by using the `function()` version of API variables, you do not need to tell your IDE that it is defined or what type it is. That's because the functions are already in scope and the IDE can already derive that information from the function API definitions.


### Benefits of using the function version of API variables:

- Access is always in scope whether inside a function or outside of it.
- They are self documenting with your IDE, unlike API $variables.
- They cannot be accidentally overwritten the way variables can be.
- They provider greater contrast between what are API-calls and user defined variables.
- In some cases it makes for shorter API calls, in terms of code.


### Drawbacks of using the functions API

- It's optional so not every installation will have it enabled (not ideal for modules).
- It's not ideal for sites using multi-instance support.
- If using [custom page classes](/blog/posts/pw-3.0.152/#new-ability-to-specify-custom-page-classes), your IDE will only know that `page()` refers to a [Page](../../../full/wire/core/Page/index.md), and not specifically what type of Page.
- It's a function call rather than a variable, so `page()->title` is slightly less efficient than `$page->title`.
- Function calls embedded in double quoted strings are a bit cryptic relative to variables.
- Non-core API variables generally do not have function equivalents, unless added by a module author.


### Avoid `$this->...` in template files

Avoid `$this->wire()->apiVar` when outside of a Wire derived class, such as in code in template files.

Why? `$this->wire()` and `$this->apiVar` may not work, but even when it does (such as in the root scope of a template file) your IDE won't know what object `$this` is referring to.* The same would be true of any `$this->...` reference in a template file, outside of a class. Whereas `wire()->apiVar` is always in scope, whether in a template file, some file rendered from it, or within some function you've defined.

*If you were curious, in the root scope of a template file, $this refers to the instance of [TemplateFile](../../../full/wire/core/TemplateFile/index.md) that is rendering the current PHP template file. That's probably not what you wanted, which is another reason why we say to avoid it.


### Tell your IDE about API variables

When using API variables in template files (like `$page`) use phpdoc to let your IDE know what they are.

Why? Unless I've missed something, IDEs don't know about ProcessWire’s API variables unless called from a function like `wire()` or `pages()`. ProcessWire passes a whole bunch of API variables to every template file that gets rendered, but your IDE doesn't know that, unless and until you tell it with phpdoc.

A best practice is to define all of the API variables you will use at the top of your template file. That way, any references to `$page` (for example) will be understood by your IDE. Here's how we use phpdoc to do that:

```php
<?php namespace ProcessWire;

/** @var Page $page */
/** @var Pages $pages */
/** @var User $user */
/** @var Input $input */
// ...and so on as needed...
```

If you are using [custom page classes](/blog/posts/pw-3.0.152/#new-ability-to-specify-custom-page-classes), then for that first example above, you'd want to clarify what type of Page object it is, i.e.

```
/** @var BlogPostPage $page */
```


### When to use `$page` rather than `wire()->page` or `page()` ?

If referring to properties in an API variable (i.e. `$page->title`) for markup generation, use the $variable version of it for convenience in strings.

Why? You can use variables as-is in double quoted PHP strings, making it easier to work with in generating output. Whereas if a function call is involved in accessing a property, we either have to concatenate it to the string, or end up with some {cryptic} looking brackets that doesn't make things simpler. If I can simply use a variable in a string to make code shorter and easier to read, then I'll always do so.

```
echo "<h1>" . wire()->page->title . "</h1>"; // before
echo "<h1>" . page()->title . "</h1>"; // before (functions API)
echo "<h1>$page->title</h1>"; // after, much better
```

When using [custom page classes](/blog/posts/pw-3.0.152/#new-ability-to-specify-custom-page-classes), you might find using the `$page` variable to be more convenient than its functional equivalents.

Why? Whether accessing `page()` or `wire()->page`, our IDE only knows that it's an object of type [Page](../../../full/wire/core/Page/index.md), and not specifically what kind of Page it is. But with the variable `$page`, we can tell our IDE specifically what kind of Page it is:

```
/** @var BlogPostPage $page */

echo "Written on $page->date by $page->author_name";
```

In the above example, our IDE knows about the "date" and "author_name" properties of this `$page` since we told it that it's a `BlogPostPage`.


### Avoid variable name collisions

Avoid the temptation of defining variables that use the same name as ProcessWire's API variables.

Why? At worst, your variable could overwrite ProcessWire's API variable, breaking any following code that uses the API variable. At best, the variable might be confused with a ProcessWire API variable when looking at the code. Even if I'm outside the scope of ProcessWire’s API variables (such as in a function) I still avoid using API variable names, just to avoid confusion.

ProcessWire has [20+ API variables](../../../full/index.md) that are provided to every template file. Their names are common enough that you might be tempted to use the same names for your own variables (i.e. `$pages`, `$mail`, `$files`, `$config`, etc.). But if you want to avoid bugs and confusing code, then take care to use variable names different from the ones that ProcessWire defines.


### API variables in hooks

Use `$event->wire()->apiVar` to access API variables from within hooks.

Why? While there are other ways to access an API variable, such as `wire()->apiVar` or `apiVar()`, accessing the needed API variable from the given [HookEvent](../../../full/wire/core/HookEvent/index.md) `$event` object will ensure that it's the API variable from the ProcessWire instance that the hook was called from.

```
$wire->addHookAfter('Pages::trashed', function(HookEvent $event) {
  $user = $event->wire()->user;
  $mail = $event->wire()->mail;
  $config = $event->wire()->config;
  $page = $event->arguments(0); /** @var Page $page */
  $mail->new()
    ->to('somebody@company.com')
    ->subject("Trashed page at $config->httpHost")
    ->body("Page $page->path trashed by $user->name")
    ->send();
});
```

If multi-instance is not a factor with your hooks, such as those you might put in /site/init.php or /site/ready.php, then it doesn't really matter how you access the API variables. But if your hooks are part of a module or other type of shared code, then it's good to consider that it may at some point operate in a multi-instance context. Accessing the API variables from the [HookEvent](../../../full/wire/core/HookEvent/index.md) ensures you are accessing the right ones.


### Adding your own API variables

Add your own API variable(s) to make an object instance (like a module) or any other kind of value available to your entire installation.

Should you want to add your own API variables, it's very easy to do. Let's say we wanted to add a variable named `$foo`. To keep it simple, we'll make it a string with the value "bar". In order to ensure the API variable is available to whatever page gets rendered, we'll add this bit of code in our /site/init.php or /site/ready.php file:

```
$wire->wire('foo', 'bar');
```

Once we've done that, we'll have a new API variable named `$foo` that contains the value "bar". So we could do this from any template file:

```
echo $foo;
```

We should probably tell our IDE about it, so that it doesn't get flagged with a red underline:

```
/** @var string $foo */ 
echo $foo;
```

We could also access it from `wire()`:

```
echo wire('foo');
echo wire()->foo; // works, but IDE will flag it
```

But note that this will NOT work:

```
echo foo(); // error: undefined function
```

So if you want that to work, then you'd also have to add the function to your /site/init.php or /site/ready.php file (or some file included from either):

```
function foo() {
  return wire('foo');
}
```

It's rare to use API variables for strings like this, though there's no harm in it either. But it would be more common for an **autoload** module to add a reference to itself as an API variable from its `init()` function:

```
class HelloWorld extends WireData implements Module {
  public function init() {
    $this->wire('hello', $this);
  }
  public function world() {
    return 'Hello World';
  }
}
```

Then from a template file, or really anywhere else:

```
/** @var HelloWorld $hello */
echo $hello->world(); // Hello World
echo wire()->hello->world(); // works but IDE doesn't know about "->hello"
echo wire('hello')->world(); // works but IDE doesn't know about "world()"
```

In this post we've looked at a lot of best practices for using API variables in ProcessWire. All of these options are here to enable flexibility and make everything easy to get to. What works best for me may not necessarily be what works best for you, so it's good to know about the various options available and explore what works best for you. If you have any other best practices or related ideas that you think should also be mentioned, please reply below and share.
