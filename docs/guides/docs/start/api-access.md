# API access

Source: https://processwire.com/docs/start/api-access/

## Sections


## Various ways of accessing the ProcessWire API

In ProcessWire there are several ways that you can access the API and we take a look at the most common ones here. Regardless of what method you use, you are technically accessing what are called API variables.

Each API variable has a unique name to distinguish it from others. For instance, the “pages” (plural) API variable provides access to loading and saving pages, the “page” (singular) API variable provides access to the page being viewed, the “input” API variable provides access to user input, and so on. See the [API reference](../../../full/index.md) for a full list of ProcessWire’s core API variables.

There are several different ways to access these API variables. For instance, all of the following accesses to the $page API variable are synonyms of each other, though with different benefits depending on the context:

- `$page` when $page in scope
- `page()` when using functions API
- `wire('page')` works anywhere
- `$wire->page` when $wire in scope
- `$this->page` when in Wire-derived classes
- `$this->wire('page')` when in Wire-derived classes (preferred method)

You might even come across more but the above are those you are most likely to see at some point.


### You are always accessing the same exact thing

Whichever way you access an API variable, there’s no need for confusion, simply remember that you are always accessing exactly the same thing. The return value from all of the above access methods would be identical.

In the same manner, you might have several different shoes that you wear, but it does not matter what shoes you wear because you are always the same person. Changing shoes does not cause you to become confused, thinking you are now a different person. You naturally choose different shoes depending on the context, like wearing boots in the snow, or sandals at the pool. Regardless of what shoes you wear, those shoes are still walking the same person. Likewise, you can choose different ways of accessing the ProcessWire API depending on the context. Though you don’t have to unless you want to—if you are comfortable with one particular access method, it's generally fine to stick with it. But, since you are reading this, I'm guessing you are interested in learning more…

However you access the API variables, each has several methods/functions and/or properties that enable you to communicate with the API variable. This part is always the same, regardless of how you’ve accessed a particular API variable. For instance, with the “pages” API variable you might ask it to find pages using the [find()](../../../full/wire/core/Pages/method-___find.md) method, i.e. `$pages->find('selector')` or `pages()->find('selector')`. Or on the “page” API variable, you might ask it for the “title” of the current page from the page title property, i.e. `$page->title` or `page()->title`.

So now you know—there are several different ways that you can access these API variables, and it doesn’t really matter how you do so. But over time you may find one method preferable over another, depending on the context. The most common context is from your site’s template files. Other contexts include the code of modules and/or PHP classes, or even other applications or scripts that you’ve booted ProcessWire from. We’ll cover all of these contexts here, though most users will likely be focused on the context of template files since that is where most site-specific development occurs.


## API variables in template files (the most common context)

Most users will be accessing API variables exclusively from the context of their site’s template files. The two most common ways to access API variables from template files are directly, like `$pages` or as a function, like `pages()`. Sometimes you might also see `wire('pages')`. They are all the same thing, but we’ll cover them all here and look at the benefits and drawbacks of each.

If you’ve seen other API access methods like `$this->pages` or `$this->wire('pages');` those are access methods that you would use from within a PHP class. Meaning, if you see `$this` as part of the access method, you can ignore it for now because template files are not PHP classes. Only when you get into module development are you likely to use access methods that start with `$this`.


### The API as PHP $variables

The most common way to access the API is from PHP variables like $pages, $user, $input, etc. This has been available all the way since ProcessWire version 1.0. Every template file that ProcessWire renders is provided with all of the defined API variables, ready to access. If new API variables are added by some module, they likewise become available as $variables in your template files.


### The API as PHP functions()

In ProcessWire 3.x you also have the option of accessing the API as PHP functions, i.e. pages(), user(), input(), etc. They access exactly the same thing as their variable counterparts, but are just typed slightly differently in that they are accessed as `var()` rather than `$var`, which is a very minor difference. Accessing a property or method from them is identical, i.e. `$var->method()` and `var()->method()` are equivalent. However, the function version adds some additional convenience that we’ll take a closer look at here.


### Enabling the functions API

First things first, if you want to use the functions API, you might have to enable it, if it isn’t already. For most new installations, it will already be enabled by default. But for existing installations you may have to add the following to your /site/config.php file:

```
$config->useFunctionsAPI = true;
```

Or if you just want to experiment with it before enabling it for your site, you can include the file below from your template file (or _init.php file) and the Functions API will become immediately available:

```
include_once($paths->core . 'FunctionsAPI.php');
```

Finally, there’s also another option. You can access any functions from the functions API even when it’s not enabled just by prepending the word “wire” to the function name. For instance, rather than calling `pages()` you would call `wirePages()`. However, if you are going the route of using functions rather than variables, I suggest just enabling the functions API as the wire[Name] versions are a bit verbose.

The reason the functions API might not be enabled by default on your existing installation is because it was not originally available in ProcessWire. If you happened to create your own PHP functions having the same name, it would collide with the functions API. For this reason, it may not be enabled for existing installations unless you specify that it should be in your /site/config.php file. If it’s not already enabled, we recommend that you enable it so that you can take advantage of its conveniences.


## Benefits of the functions API


### Functions are always in scope (variables are not)

When ProcessWire renders your template file, it provides all of the API variables to it. But a best practice when coding anything is: do not repeat yourself. Meaning, don’t write the same blocks of code more than once. Most commonly you do this by bundling that block of code into a function, and then calling that function whenever you need the logic that it provides. The problem is that such functions will not see any of the API $variables (unless you pass them in as arguments)—but they can see the API functions, because they are always in scope.

Unlike Javascript, in PHP, variables existing outside the function block are not visible within the function block. Chances are you need one or more API variables in your functions, so you must pass them in as arguments or in `use()` statements. This is no problem if you know what you are doing (other than more typing) but for people learning PHP, it can be a point of confusion. And for people that know what they are doing, it’s more work. We don’t like more work.

By contrast, with the functions API, it does not matter whether your code is in a function or not because the API functions are always accessible (aka in scope), and always accessed the same way. That means fewer variables for you to keep track of (always a good thing), less code for you to type, code that’s potentially easier to read, and almost certainly less confusion, especially for those new to PHP.


### Functions cannot be accidentally overwritten (variables can be)

When using API variables, it’s possible to accidentally overwrite any API variable, and thus break your site. Sometimes it’s not immediately obvious. Take the following as an examples:

```php
// oops, we just overwrote the $page API variable
foreach($pages->find("template=basic-page") as $page) { … }

// oops, we just overwrote the $user API variable
foreach($users->find("role.name=editor") as $user) { … }

// oops, we just overwrote the $files API var
$files = new \DirectoryIterator("/path/");
```

Given that there are so many API variables, you need to be familiar with all of them ahead of time in order to avoid overwriting them. If you aren’t careful, you can run into trouble since many of the API variables use common names. And when you accidentally overwrite an API variable, it may be difficult to discover you have done so. After all, overwriting a variable in PHP is not considered an error (they are designed to be written to, which is kind of the purpose). Yet in the case of API variables, we never want them to be overwritten. If you later need to access one that’s been overwritten, the side effects of doing so would be an error indeed, and potentially a catastrophic one.

By contrast, you cannot overwrite a function once it has been defined. We could not accidentally overwrite the `pages()` function, for instance. So by standardizing on using API functions like `pages()` rather than variables like `$pages`, it’s not a problem if you overwrite an API variable, because you aren’t using them.


### Functions are self-documenting (variables are not)

Most web developers use a software for editing their template files that recognizes PHP and HTML, provides syntax highlighting, auto-completion, various hints and other features. Depending on the case, it might be what’s called an IDE. PhpStorm is one widely used and common example with ProcessWire. Because such software is smart enough to know the ins-and-outs of PHP syntax, it’s also smart enough to highlight common errors like undefined variables, unknown types and more. That’s very useful, but also problematic when it comes to API variables.

The problem is that whenever you access an API $variable, the editor will flag it as an error since it can see that the variable has not previously been defined. Of course, the variable actually is defined (at runtime, rather than explicitly), but there’s not really a way for the editor to know that.

Ignoring these “undefined” and “unknown” errors is a minor annoyance, but there’s another factor. Even if we turn off those “undefined” and “unknown” inspections, the editor still doesn’t know what the variable is. As far as it knows, `$pages` (or any other API variable) could be null, a string, an integer, or an instance of anything. It has no idea it is actually an instance of the [Pages](../../../full/wire/core/Pages/index.md) class. And as a result, it cannot provide us with code hinting, auto completion or argument details when we access anything from that API variable. We are essentially flying blind, using our IDE as if it were just a plain text editor. However, we can overcome that limitation by specifically telling our IDE what each variable is, like this:

```
/** @var Pages $pages */
/** @var WireFileTools $files */
/** @var WireMailTools $mail */
/** @var Sanitizer $sanitizer */
/** @var Page $page */
/** @var User $user */
/** and on and on… */
```

This is fine, but it’s also a pain. Maybe there are other ways to inform our IDE, but the fact is that it’s a lot of extra work, and likely not going to even be apparent to someone new to—or learning—ProcessWire, where it’s even more important.

None of these concerns applies when accessing the API as functions. That’s because functions, by nature, are self documenting. Your editor/IDE will know exactly what you are doing as soon as you type pages(), files(), mail(), sanitizer(), page(), etc. You don’t have to do anything other than start typing the function name, and it’ll even know how to finish typing it for you. And once the function is there, it knows all of the methods, arguments, properties and everything there is to know, without you having to tell it anything. It can fill in the blanks for you and identify when you make an error. So accessing the API as functions makes life a lot nicer if you are using a quality code editor or IDE. And if you aren’t yet using such a software, then look into it, you will be in for a real treat.


### Many API functions have time-and-code saving shortcuts

The most common way to access API functions is by calling them without any arguments between the parenthesis, i.e. `pages()`. All of the API variables can be accessed as functions in this manner, and they simply return the API variable. This is what we recommend for most cases. But many of the API variables also support optional arguments as well, enabling you to use time-saving shortcuts when/if the desire arrives.

For instance, the two most common calls to the `$pages` API variable are to `get()` or `find()` pages, so the `pages()` function provides these built-in shortcuts: if you give it an argument of a single page ID, path or name, it will behave the same as a `$pages->get(…);` call, returning that single page with less code, i.e. `pages(…);` Or, if you give it a selector string (something that can match multiple pages) then it will behave as a `$pages->find(…)` call, returning those multiple pages, giving you the same result with less typing. Shortcuts can be quite handy at times.


### Functions provide greater contrast with your own variables

When working on any reasonably complex project, you are going to be working with PHP variables quite a bit. Beyond what we mentioned earlier about the dangers of accidentally overwriting API variables, there’s also the factor that accessing the API from functions provides a more obvious and distinct contrast between what are ProcessWire API calls and what are your own variables, ultimately making your code easier to read and maintain.

API variables are distinctly different types from your own runtime variables. Yet as far as PHP is concerned—and far as your syntax-highlighting editor is concerned—they are no different from any other variables (other than that it might think they are undefined). But when accessing the API from functions, there is much more obvious distinction between API access calls and your own variables. I personally find this helps a lot with adding clarity to my own template files.


### The functions API also has adds extra helper functions

This is a fairly minor point, but beyond just providing access to ProcessWire’s core API variables, enabling the functions API also enables some additional functions that are convenient for website development, such as [region()](../../../full/wire/core/FunctionsAPI/method-region.md), [setting()](../../../full/wire/core/FunctionsAPI/method-setting.md), and perhaps more down the road. The region() function stores runtime markup, while the setting() function enables you to maintain site-specific settings.


### Potential drawbacks of the functions API

The functions API provides a nice convenience for accessing API variables, but there are also a few considerations to be aware of when using the functions API:

- The functions API is specifically built as a convenience for front-end website or application development. While it can be used anywhere, it is not intended for modules and back-end processes/hooks.
- For API variables with properties (like $page and $user) It’s simpler to dereference variables in double quoted strings than it is functions.
- If booting multiple independent ProcessWire instances on the front-end, you have to pay attention what instance is the current instance.
- The functions API is not enabled by default on existing installations, requiring you to enable it in your `$config` or use “wire” prefixed versions of the functions.
- Not all API variables are available as functions. Only those that are likely to be needed on the front-end of a website or application are available as functions. As a result, it’s a very specific list of functions that does not change based on what modules are installed, etc. (this might also be seen as a benefit in clarity for some)
- API variables provided by 3rd party modules are not available as functions (other than through the `wire()` function) unless the module developer has opted to create one.


## Other API access methods


### Using the API with multiple ProcessWire instances

Technically you can boot multiple different instances of ProcessWire. In a multi-instance environment there may be some ambiguity about what instance API functions and variables are referring to. So when booting multiple instances of ProcessWire, you will want to access your API variables directly from the ProcessWire instance. This will either be `$wire` (the variable the represents the default instance) or it will be the ProcessWire object returned by your own `$pw = new ProcessWire(…);` call. In such a case, you would access the `$pages` API variable or function via `$wire->pages` or `$pw->pages`, depending on the names you chose and the instance you intended (we’re using `$pw` here as an example, but that could be anything that you choose).While somewhat rare to do this from template files, it is technically possible. In such a case, the instance that was present when your template file started rendering should be the same instance that is present on all of your API variables that are currently in scope. In this case, you might prefer to stick with using API variables accessed as literal $variables, as there may be ambiguity about what instance API functions are referring to. However, this can be overcome by calling `ProcessWire::setCurrentInstance($wire);` where `$wire` is the object that represents the instance you want it to use. Though for the ideal multi-instance support, your best bet is to access your API variables directly from the `$wire` variable that represents each ProcessWire instance, i.e. `$wire->pages`.


### Using the wire('var') function

All versions of ProcessWire come with a handy `wire()` function that provides easy access to the entire API. The `wire()` function is always in scope, meaning it’ll work anywhere, and is always enabled. Calling this function with no arguments returns the current ProcessWire instance. Or calling it with the name of an API variable, i.e. `wire(‘pages’);` returns that API variable, ready to use.

```
$items = wire('pages')->find('template=product'); 
$headline = wire('page')->get('headline|title');
```

While this `wire()` function can be very handy, it’s one that is best used just on the front-end in template files (and related). Like the other API functions, it’s bound to whatever is the current instance of ProcessWire, so if you are booting multiple instances, a naked wire() call might be somewhat ambiguous. The wire() function also isn’t as self-describing as the other API variable functions, though it is an improvement over the naked API variables in that respect. But I suggest using wire() for occasional needs on the front-end, like when a variable is out of scope. Or better yet, use the functions API. A lot of wire() calls tends to create confusing redundancy (with “wire” everywhere), which is not present when using more specifically named API variables or functions.


### Accessing API variables from within modules or classes

You cannot access API variables directly in a class (i.e. $pages), because they are out of scope. You can use the API functions like `pages()` or `wire(‘pages’)`, as they are in scope, but we recommend a different strategy…

When you are in a Wire-derived class (such as a ProcessWire module), you should preferably access API variables from `$this->var` (like `$this->pages`). That’s because ProcessWire injects dependencies into every Wire-derived object, which ties it to the current instance. Modules are more likely to be shared and thus more likely to end up in a multi-instance environment. Accessing your API variables from `$this->var` ensures no ambiguity about what instance they getting pulled from.

While `$this->var` works, in most cases we recommend going a step further and instead using `$this->wire(‘var’);` because it’s slightly more efficient, and sightly safer. That’s because it prevents the possibility of name collisions between API variables and your own class variables. Though if you are being reasonably careful, it doesn’t really matter whether you use `$this->var` or `$this->wire(‘var’);` But I like using `$this->wire(‘var’)` because it’s a little more efficient.


### Accessing API variables from hooks

Hooks have the same considerations as classes. You won’t be able to directly access variables like `$pages` because they are out of scope. However, if your hook function happens to be in a class, then you can access API variables the way that was described in the section before this one. Though there’s also another way. Very often hooks are defined as a function directly on the `addHook()` statement. Every hook receives a [HookEvent](../../../full/wire/core/HookEvent/index.md) object. You can access all of the API variables from the `wire()` method of the HookEvent. In the example below we are accessing the [$log](../../../full/wire/core/WireLog/index.md) API variable from the HookEvent’s wire() method:

```php
$pages->addHookAfter("saved", function(HookEvent $e) {
  $e->wire("log")->save("saved-log", "Page {$e->object->path} was saved");
});
```

This is the recommended way to access API variables from hooks. If your hook function is instead part of a module/class, then it doesn’t matter really whether you access it from the HookEvent or from $this. If your hook is a front-end hook for your own purposes (rather than a shared module) then it’s also just fine to access API variables from the functions API or from the wire() function as well. But for more portable hook code, it's preferable to access API variables directly from the HookEvent ($e) object.


### Accessing the API from another application

When you are bootstrapping ProcessWire from another application, chances are that application is going to be in a different PHP namespace. So the functions API and even the wire() function might not be available without referencing ProcessWire’s namespace. Though whether other namespaces are involved or not, I recommend accessing the API directly from the ProcessWire instance that you booted. When you bootstrap ProcessWire, it returns the ProcessWire instance to you, and you can access the API variables directly from the instance. In the example below, we’ve named our instance $wire, and thus can access API variables from it:

```
$wire = new ProcessWire(); 
$items = $wire->pages->get('/products/')->children();
```
