# Module development in ProcessWire CMS

Source: https://processwire.com/docs/modules/development/

## Summary

It is easy to develop a module in ProcessWire, though some PHP experience is helpful. This section introduces module development and guides you through a simple example to get you started.

## Key Points

- Take a look at the HelloWorld module that’s included with the core. You can find it in your /site/modules/HelloWorld/ directory.
- Read the documentation for the [Module class](/api/ref/module/).
- Learn about configurable modules with the [ConfigurableModule class](https://processwire.com/api/ref/configurable-module/).
- Learn about the different kinds of [predefined module types](/docs/modules/types/).
- Check out the [Process Hello](https://github.com/ryancramerdesign/ProcessHello) module which demonstrates how to build an admin application.

## Sections


## Developing modules in ProcessWire

It is easy to develop a module in ProcessWire, though some PHP experience is helpful. This section introduces module development and guides you through a simple example to get you started.


### Creating a simple module

To create a module, you simply create PHP class that extends one of ProcessWire’s core classes, and also implements the [Module interface](https://processwire.com/api/ref/module/). This Module interface doesn't actually have any required methods, but it serves as a way for ProcessWire to recognize PHP classes that are intended to be modules, and it provides guidance on how to implement various optional methods. If creating a module that isn't of a predefined type, it should extend the ProcessWire [WireData](https://processwire.com/api/ref/wire-data/) class, and this is a good place to start (we'll get into predefined types later). Here's an example to summarize the above:

```php
<?php namespace ProcessWire;
class Foo extends WireData implements Module {
  // nothing here yet
}
```

Save the class that you create in a file with the same name as the class, but with the extension “.module” or “.module.php” (either works). For example, a module with class *Foo* (like above) would be in a file named Foo.module or Foo.module.php. The file should be placed in /site/modules/. Though we recommend placing it in a directory within that, having the same name as the module class, like /site/modules/Foo/Foo.module.


### Telling ProcessWire about your module

One of the first things that a module should provide is information about itself, so that it can be identified in ProcessWire. This information can be provided via static `getModuleInfo()` method in the class, or a separate ModuleName.info.php or ModuleName.info.json file. We'll use a static method for now, so that we can keep everything in one file. The method returns an array of information about the module. The minimum information that ProcessWire needs is to know the module’s title, a short text summary, and the version number:

```php
<?php namespace ProcessWire;
class Foo extends WireData implements Module {
  public static function getModuleInfo() {
    return [
      'title' => 'Foo test module',
      'summary' => 'An example of creating a module',
      'version' => 1
    ];
  }
}
```

With the above, you've now got the minimum amount of information that ProcessWire needs to install your module. So go ahead and install it. Since you just creating the file, ProcessWire might not be able to see your module yet, so you'll want to login to your admin and then go to Modules > Refresh. ProcessWire should detect your module, and you'll see it on the Site tab of your Modules screen. Click the “Install” button.

Your module may now be installed, but it doesn't actually do anything. That's okay, we'll get to that next.


### Making the module do something

Continuing our examle above, lets make the module do something. In this case, lets add a hi() method to the module that returns the string "Hello name", where "name" would be the current user's name:

```php
<?php namespace ProcessWire;
class Foo extends WireData implements Module {
  public static function getModuleInfo() {
    return [
      'title' => 'Foo test module',
      'summary' => 'An example of creating a module',
      'version' => 1
    ];
  }
  public function hi() {
    return "Hi there " . $this->user->name;
  }
}
```

Now you've got a module that can do something. You can call upon this module from any of your site template files and use it. For example, here's how you might call upon it from our /site/templates/basic-page.php file:

```
$module = $modules->get('Foo'); 
echo "<h1>" . $module->hi() . "</h1>";
```

The output would be `<h1>Hi there guest</h1>` or whatever the current user’s name is.

So now we've got a module that actually does something. If you are building a module to provide a library of reusable functions or the like, then this might be all you need. But what if you want to create a module that performs actions automatically, without having to be loaded manually? Read on…


### Automatically loading modules

ProcessWire supports something called **autoload modules**. These are modules that are loaded automatically when ProcessWire boots. Autoload modules are especially useful when you want to hook into anything within ProcessWire. We'll get into hooks in a bit, but first we'll tell you how to define an autoload module. It's as simple as just adding `'autoload' => true` to the information returned by your `getModuleInfo()` method or file:

```
public static function getModuleInfo() {
  return [
    'title' => 'Hello World',
    'summary' => 'An example of creating a module',
    'version' => 1,
    'autoload' => true
  ];
}
```

After you've added that autoload property, you'll again want to refresh your modules in the admin (Modules > Refresh), so that ProcessWire will reload all the module information. Once you've done that, ProcessWire will see that your module is now an autoload module.

An autoload module isn't particulary useful unless it also does something automatically. So lets update our earlier example to display our “Hi there” message to the user while they are in the admin. To do this, we will add a `ready()` method to our module. This is a method that ProcessWire automatically calls on all autoload modules as soon as the API is ready.

```php
<?php namespace ProcessWire;
class HelloWorld extends WireData implements Module {
  public static function getModuleInfo() { ... }
  public function hi() { ... }
  public function ready() {
    if($this->page->template == 'admin') {
      $this->message($this->hi());
    }
  }
}
```

If you go into your admin, you should now see a "Hi there name" notification at the top of your screen, on every page in the admin.

Note in the above example that we don't display our “Hi there” message unless the user happens to be in the admin (which we determine by checking the current page's template). While it wouldn't hurt anything if we did, messages/notifications aren't displayed to users on the front-end, so there would be no point.

** Pro Tip: **If you only want your module to autoload in the admin, change your **'autoload' => true** in your getModuleInfo() method to instead return **'autoload' => 'template=admin'**, which essentially says "autoload only if the current page template is admin." If you do this, then you can remove if() statement from the ready() method above, since you are now asking ProcessWire to autoload your module only in the admin. Remember to Modules > Refresh, after making this change.


### Adding hooks to autoload modules

Modules may add hooks to methods in ProcessWire's core or to other modules. Nearly every key component and action in ProcessWire is hookable. A hookable method is identified by the presence of three underscores before its definition, i.e. `public function ___someMethod() { ... }`. You can hook any such methods from your autoload modules.

Modules can schedule designated methods to be executed *before* or *after* any hookable method. They can manipulate the values provided to (or returned from) any hookable method. Modules may also add new methods to existing classes or object instances in ProcessWire.

To demonstrate hooking a method, lets take our example above and make it display our “Hi there” message to the user after every page is rendered. This will make a `<p>Hi there user</p>` appear at the bottom of every page rendered in ProcessWire, so… maybe don't do this on a live site.

```
public function ready() {
  // add hook after Page::render() and make it call the "test" method of $this module
  $this->addHookAfter('Page::render', $this, 'test');
}

public function test($event) {
  // modify the return value of Page::render() to include the following:
  $event->return .= '<p>' . $this->hi() . '</p>';
}
```

You can also implement hooks with anonymous functions. The following would produce an identical result to the above:

```
public function ready() {
  $this->addHookAfter('Page::render', function($event) {
    $event->return .= '<p>' . $this->hi() . '</p>';
  });
}
```

The `$event` argument that the hook function receives is a [HookEvent](https://processwire.com/api/ref/hook-event/) object. Since we are hooking *after* an existing method, it provides us the return value in `$event->return`, which we then modify by appending some more markup to it. It also provides all of the arguments the method received in `$event->arguments()`, and each argument can be retrieved by zero-based index, or by name. Were we using a *before* hook, we could also modify those arguments before they are received by the method we have hooked. For more about hooks and events, please see our [Hooks documentation](/docs/modules/hooks/).


### Using an autoload module to add new methods to existing classes

Before we wrap things up, lets show you how to add a new method to an existing class in ProcessWire. In this case we'll add a new summarize() method to the Page class. This method will auto-generate a summary of the “body” text, of a specified length. This is something that might actually be useful, unlike the previous examples.

```
public function ready() {
  $this->addHook('Page::summarize', $this, 'summarize');
}
public function summarize($event) {
  // the $event->object represents the object hooked (Page)
  $page = $event->object;
  // first argument is the optional max length
  $maxlen = $event->arguments(0);
  // if no $maxlen was present, we'll use a default of 200
  if(!$maxlen) $maxlen = 200;
  // use sanitizer truncate method to create a summary
  $summary = $this->sanitizer->truncate($page->body, $maxlen);
  // populate $summary to $event->return, the return value
  $event->return = $summary;
}
```

With the new summarize() method added to all Page instances via this hook, now we can call summarize() on any Page object. For instance, we might use this when rendering a list of pages or search results:

```
foreach($page->children as $item) {
  $summary = $item->summarize(150);
  echo "<li><a href='$item->url'>$item->title</a><br>$summary";
}
```


### Another example

Before we finish, lets take a look at one more module example. In this case, the module displays a message to the user every time they save a page. If most of this example makes sense to you, then you are ready to move forward with module development. There is one thing a little different here though, lets see if you can spot it. I'll tell you more after the example.

```
class Example extends WireData implements Module {
  public static function getModuleInfo() {
    return [
      'title' => 'Example module',
      'version' => 1,
      'summary' => 'Display message when pages are saved',
      'autoload' => true,
    ];
  }
  public function ready() {
    $this->pages->addHookAfter('saved', function($event) {
      $page = $event->arguments(0);
      $this->message("You just saved page: $page->url");
    });
  }
}
```

What's a little different in this example relative to our previous examples is the way that we are adding the hook in our ready() method. We are adding the hook with `$this->pages->addHookAfter()` rather than `$this->addHookAfter()`. Note also the way we specify the method we are hooking, which is just `saved` rather than `Pages::saved`.

What we are doing here is adding this hook to 1 specific object instance `$this->pages` rather than ALL instances of a class. In this case, it does not matter because there is only ever one instance of the Pages class, identified by `$this->pages`. But for classes that can have any number of instances (like Page) it would matter, as `$this->addHook('Page::method', ...)` would hook all instances of a Page and `$page->addHook('method', ...)` would only add the hook to that one $page.

When it comes to module development, it's more likely you'll be hooking all instances of a class rather than just a single instance, so we won't dive deeper into it here. But if you are interested, be sure to read more in our [hooks documentation](/docs/modules/hooks/). This completes our basic introduction to development of a simple module, but there's lots more to learn if you are interested…


### Module name requirements

When deciding on a name for a module (the class name), please use a format where the first character is an uppercase letter (A-Z), the second character is a lowercase letter (a-z), and the remaining characters are upper-or-lowercase letters. If needed, you may also use numbers at the end of a module name, though it is rare.

Examples of good module name formats are `HelloWorld` and `Helloworld`. Examples of undesirable module name formats are `HELLOworld` and `helloWorld`.

Modules that extend [core module types](/docs/modules/types/) should also have the same prefix as the core module type. Examples of these prefixes include: Process, Fieldtype, Inputfield, Textformatter, Tfa, WireMail, etc. ([details](/docs/modules/types/)). These modules have specific purposes and ProcessWire easily recognizes them by the prefix. But unless you are specifically extending a core module type, you should avoid using these prefixes in your module name.

**The module filename** must be the same as the module class name and end with the extension `.module` or `.module.php`, for example `HelloWorld.module` or `HelloWorld.module.php`.


### Next steps

- Take a look at the HelloWorld module that’s included with the core. You can find it in your /site/modules/HelloWorld/ directory.
- Read the documentation for the [Module class](/api/ref/module/).
- Learn about configurable modules with the [ConfigurableModule class](https://processwire.com/api/ref/configurable-module/).
- Learn about the different kinds of [predefined module types](/docs/modules/types/).
- Check out the [Process Hello](https://github.com/ryancramerdesign/ProcessHello) module which demonstrates how to build an admin application.
- The [Fieldtype Map Marker](https://github.com/ryancramerdesign/FieldtypeMapMarker) module was originally put together as an example of how to create your own [Fieldtype](http://modules.processwire.com/categories/fieldtype/) and [Inputfield](http://modules.processwire.com/categories/inputfield/) (a more advanced example).
- Need to build a module that requires or installs other modules? Learn about [module dependencies](/talk/topic/778-module-dependencies/) and how to use them.
- Want help with module development? We are glad to help and have a [forum board](https://processwire.com/talk/forum/19-moduleplugin-development/) dedicated to it.

- [Add multi-language translations to your module](/docs/modules/development/multi-language-translations/)If you are a module developer, you might want to bundle multi-language translations with your module. This page covers all the…
