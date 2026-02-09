# ProcessWire core updates (2.5.27)

Source: https://processwire.com/blog/posts/processwire-core-updates-2.5.27/

## Sections


## ProcessWire core updates (2.5.27)

17 April 2015 by Ryan Cramer [ 4 Comments](/blog/posts/processwire-core-updates-2.5.27/#comments)


### Getting close to ProcessWire 2.6

You might not be able to tell from the rest of this post (which covers a lot of new stuff), but this week involved resolving a lot of GitHub issue reports in preparation for ProcessWire 2.6.

One particular issue we resolved was the “unknown column” error when adding languages in a multi-language site. It was tough to track down because I wasn't able to reproduce it for quite some time. It took an entire day this week to finally reproduce it, track it down and fix it. But from my perspective it was the last major issue that needed to be resolved before ProcessWire 2.6 could replace the master branch. I'm not aware of any other *major* issues existing in the ProcessWire dev branch at this point, and the dev branch now seems to be significantly more stable than the master branch, in my testing here.

We're not ready to release 2.6 just yet, but I think we are now very close. I think that many (likely most) of you reading this are already using the dev branch, so please let us know how it's working for you.


## Admin Upgrades


### Field cloning upgrade

When creating a new field (in Setup > Fields > Add New) you now have the option of cloning an existing field. When selecting the field “Type” you’ll now see not only all the field types available, but all the existing fields that you can clone from. While you already had the ability to clone fields by editing an existing field, and using the clone option from the “Actions” tab, I think that it’s well hidden enough that a lot of people miss it. Now anytime you create a new field, it’ll be hard to miss the option to clone an existing field.


### Fields now support “notes”

In ProcessWire, you’ve always had the ability to edit a “label” and “description” for each field that you create. Now you also have another text container, called “notes”. This has already been available in ProcessWire since the beginning (and you’ve likely seen it in use on ProcessWire’s own screens quite a bit), but never before has it been available to your custom fields.

As of ProcessWire 2.5.27 you can now make use of this “notes” field on any of your own fields. Notes comprise the text that appears directly under an input. Whereas the “label” and “description” always appear above the input. You’ll see the new “notes” option on the “Basics” tab when editing any field, and it appears right underneath the existing “description” field.


## API Upgrades


### New each() method added to all ProcessWire arrays

Continuing our original goal of having ProcessWire's API gain inspiration from jQuery's, we’re always looking for opportunities to build on that. There are a few things we didn’t initially implement because ProcessWire was originally written to support PHP 5.2, and things like closures simply weren’t an option. Granted, we’ve not supported PHP 5.2 in quite some time, but it recently occurred to me that we could finally support an `each()` method with our arrays (WireArray, PageArray, etc.) just like in jQuery. Of course, PHP is not Javascript and our needs and context are a little different, so we’ve found some opportunities to do more with it too. This is what you will find in ProcessWire 2.5.27 this week.

I think some of the things that you can do with `each()` benefit more from demonstration than verbosity, so I’ll communicate by examples here. I’m going to be demonstrating purely with a PageArray returned from `$pages->find()`, but keep in mind you can use this `each()` method on any PageArray, and in fact any native ProcessWire array type (anything descended from WireArray). Meaning, you can use this pretty much on anything in ProcessWire that contains multiple items.

The following examples all produce exactly the same output, which is this:

```
<li><a href='/path/to/page/a/'>Page A</a></li>
<li><a href='/path/to/page/b/'>Page B</a></li>
<li><a href='/path/to/page/c/'>Page C</a></li>
```

Here we go…

```php
$items = $pages->find("template=basic-page");

// Example 1: direct output of items in PageArray
$items->each(function($item) {
  echo "<li><a href='$item->url'>$item->title</a></li>";
});

// Example 2: all items concatenated and then output
echo $items->each(function($item) {
  return "<li><a href='$item->url'>$item->title</a></li>";
});

// Example 4: item properties can be {tagged}
echo $items->each(function($item) {
  return "<li><a href='{url}'>{title}</a></li>";
});

// Example 5: speaks for itself
echo $items->each("<li><a href='{url}'>{title}</a></li>");

// Example 6: a foreach for comparison, the classic PW way
foreach($items as $item) {
  echo "<li><a href='$item->url'>$item->title</a></li>";
}
```

The examples here just demonstrate using `each()` for generation and output of markup, but of course you can use it with the same utility that you would a regular foreach. Actually, I put that last example there with the `foreach()` just to demonstrate that there isn’t really that much of a difference between what we’ve already had, and using the new `each()` method. However, I think example 5 does start to reveal some definite simplification of syntax that might be handy in many cases.

The `each()` syntax also brings more consistency to our API and that of jQuery, and some may prefer the `each()` syntax to the `foreach()` syntax, even if both are quite powerful and elegant. Because `each()` is implemented by ProcessWire, rather than by PHP, we have the flexibility to do a little more with it. That’s why you have the option to provide either a function or a string, or even use `{tagged}` variables rather than PHP variables. These optimizations aren’t going to replace the power of actual PHP variables and functions, but it’s nice to have the shortcuts when they suit your need.

Another benefit (or drawback, depending on the context) of using the `each()` method is that your code is in its own scope, just like variables within any function exist within their own scope. To put it another way, variables within a `function() { $like_this }` don’t overwrite or persist outside the function. So that presents a significant difference between `foreach()` and `each()`, which might be a good reason to use one or the other in different scenarios.

**More examples**

```
// Need an array index for each item? Just use 2 args rather than 1
echo $items->each(function($index, $item) {
  return "<li>$index <a href='$item->url'>$item->title</a></li>";
});

// Need a quick subnav?
echo $page->children->each("<a href='{url}'>{title}</a>");

// Output a category list
echo $page->cats->each("<li>{parent.title}: {title}</li>");

// Breadcrumb trail, using headline or title
echo $page->parents->each("<a href='{url}'>{headline|title}</a> / ");
```


### More new WireArray syntax fun

For our examples, we’ll say that `$items` is some PageArray:

```php
$items = $pages->find("template=basic-page");
```

Want a PHP array of all "title" values for all those pages?

```
$titles = $items->title();
```

You can take any property that the items in the WireArray have, and access it as a method. Meaning, just add a `()` after the property name. When you do that, it'll return a regular PHP array containing all of them.

But wait, what if you instead want a string of all those titles, each separated by a `<br />` tag? You can do this:

```
$titles = $items->title("<br />");
```

We’re using “title” here as an example, but you can do this with any custom field name or property that exists on the items in the WireArray. This is similar to what you can already do with the` explode()` and `implode()` methods built into WireArray, but may be a nicer syntax in many scenarios.

Speaking of `explode()`, that got an upgrade too. Want to retrieve an associative array of multiple properties for each item in a WireArray? Now the `explode()` method can do that. The following will return a regular PHP array, containing an associative array for each item, populated with url, title and summary indexes:

```
$data = $items->explode(array('url', 'title', 'summary'));
```


### Config arrays now available for Fieldtypes and Inputfields

Several weeks back we introduced the ability for module authors to define their module configuration via a configuration array, rather than programmatically with Inputfields. We now support this with Fieldtype and Inputfield configurations as well. Specifically, I'm talking about the Inputfields that appear when you are editing a field. The Fieldtype config appears on the "Details" tab, and the Inputfield config appears on the "Input" tab.

To use it in your own Fieldtype or Inputfield modules, simply specify a public `___getConfigArray()` method, rather than a `___getConfigInputfields()` method. The only difference is that `___getConfigArray()` returns an Inputfield definition array, rather than an InputfieldWrapper. The benefits of using an array are that they tend to be a little simpler and less verbose relative to building Inputfields programatically. However, in the end it doesn’t matter too much what you use… but since we are supporting the arrays with module configuration, we wanted to make sure there was consistency to use the same method with any kind of Inputfield definition in ProcessWire.

**Example for an Inputfield module:**

```
public function ___getConfigArray() {
  return array(
    'test' => array(
      'type' => 'textarea’,
      'label' => 'This is a test'
    )
  );
}
```


### Expanded module configuration options within module file

A goal with ProcessWire is always to grow simpler, not more complex. This is especially true with regards to our public API and in how people extend ProcessWire with modules. Module configuration has always been a bit of an unusual part of our framework in that it relies on a static `getModuleConfigInputfields()` method, though for very good reasons. But if you’ve been reading past blog posts, you know that we’ve been making upgrades here in providing more options.

A couple weeks ago, we added the ability for you to [define module configuration with a simple array](/blog/posts/processwire-core-updates-pull-requests-and-more-2.5.25/#module-configuration-is-now-even-simpler) in an external ModuleName.config.php file. This is my new favorite way to provide module configuration. But what if you prefer the portability of keeping everything in the same file? Well now you can use the simpler array method from within your module file too. Simply define a `getModuleConfigArray()` method in your module (static or non-static), and have it return an array that defines the inputs to configure your module.

One of the benefits of using an array is that the “value” attributes you specify become the default values provided to the module. That means less code and less fuss. No examining a `$data` array or manually populating values is necessary. You just define an array and that’s it. As an example, here is the `getModuleConfigArray()` now returned by the AdminThemeDefault module:

```
public function getModuleConfigArray() {
  return array(
    'colors' => array(
      'type' => 'radios',
      'label' => __('Color Set'),
      'options' => array(
        'classic' => $this->_('Classic'),
        'warm' => $this->_('Warm'),
        'modern' => $this->_('Modern'),
        'futura' => $this->_('Futura')
      ),
      'value' => 'classic', // default
    )
  );
}
```


### Module configuration methods can now choose to be static or non-static

When using a module configuration method within your module–whether the new `getModuleConfigArray()` method, or the existing `getModuleConfigInputfields()` method–you now have a choice as to whether you want the method to be static or non-static. You make this choice simply by whether or not your function definition starts with `static` or not, i.e.

```
// static methods 
static public function getModuleConfigInputfields($data) { … }
static public function getModuleConfigArray() { … }

// non-static methods
public function getModuleConfigInputfields() { … }
public function getModuleConfigArray() { … }
```

In the past, ProcessWire has only supported the static method: `getModuleConfigInputfields()`. The benefit of being static is that it prevents having to instantiate the module, thereby preventing load of any unnecessary assets (like CSS and JS files) and preventing attachment of unintended hooks. But the reality is, in many cases it simply doesn’t matter that much. For example, maybe your module is an autoload module that is already going to be instantiated either way. (Though with a mini-application Process module (for example), there’s definitely a good case to be made for not having other assets load).

A drawback of the static method is that you have to code outside of the context of `$this`. You can’t access the module’s properties (and configuration values) directly, you can’t access PW API variables without using the `wire()` function, nor can you translate labels with `$this->_('text');` like you would everywhere else in your module… instead you use `__('text')`. Maybe this is all relatively minor, but I really do prefer the consistency of interacting with ProcessWire's API without being in a static method. Another motivation is that when it comes to ProcessWire 3.0, static `getModuleConfigInputfields()` will be deprecated since ProcessWire will support multi-instance, and static methods aren’t instance aware. That however won’t matter to the static version of `getModuleConfigArray()`, and that will not be deprecated.

Notice that my non-static version of `getModuleConfigInputfields()` above has no `$data` array argument. In the static version, that `$data` argument provides the module’s known configuration data. Or if the module hasn’t been configured before, it’ll be empty. You inevitably have to code around that, checking for the existence of each property before accessing it… it’s admittedly kind of a hassle. In the non-static version, there is no `$data` argument because there doesn’t need to be. To access a configuration value from the module, you just pull it from `$this->some_property`, just as you would anywhere else in your module.

However, if you still want a `$data` array argument provided to your non-static `getModuleConfigInputfields()` method for some reason, PW will comply. Simply add it to your method definition and PW will provide it. But since you don’t really need it, what I’d recommend doing instead is defining your method with an `$inputfields` argument, i.e.

```
public function getModuleConfigInputfields($inputfields) { 
  $f = $this->modules->get('InputfieldText');
  $f->attr('name', 'fullname');
  $f->label = $this->_('Your Name');
  $f->attr('value', $this->fullname);
  $inputfields->add($f);
}
```

…when you do that, ProcessWire will provide a ready-to-use InputfieldWrapper to your method, preventing you from having to create one yourself (as you’ve always had to in these methods, and still have to in the static version). You can simply start adding your Inputfield objects to the provided `$inputfields`. It’s not even necessary for you to return `$inputfields` at the end of your method.


### PHP 5.6 and __debugInfo()

When PHP 5.6 came out it added a new magic method to PHP, called [__debugInfo()](http://php.net/manual/en/language.oop5.magic.php#object.debuginfo). This method enables you to control what the `print_r()` output of any object is. If you’ve ever tried to `print_r()` one of ProcessWire’s objects, you might have found yourself with a giant glob of unintelligible data, or even a never-ending output stream of stuff. This often useful tool of PHP’s wasn’t particularly useful with ProcessWire objects.

The folks at PHP recognized this is a common problem in many OO systems, and they added the very useful `__debugInfo()` method. As of the latest dev version of PW, when combined with PHP 5.6+, now you can `print_r()` any ProcessWire object and get genuinely useful information, without all the stuff you don’t need. We’ve worked hard this week to implement useful `__debugInfo()` methods throughout ProcessWire’s classes, and will be refining them further moving forward.
