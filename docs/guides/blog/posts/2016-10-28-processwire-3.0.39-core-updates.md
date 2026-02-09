# ProcessWire 3.0.39 core updates

Source: https://processwire.com/blog/posts/processwire-3.0.39-core-updates/

## Sections


## ProcessWire 3.0.39 core updates

28 October 2016 by Ryan Cramer [ 8 Comments](/blog/posts/processwire-3.0.39-core-updates/#comments)

This week has been busy! We've got updates to our demo site, a new functions API, and other core additions that you may find useful in template files. ProcessWire 3.0.39 is now available on the [dev branch](https://github.com/processwire/processwire/tree/dev).


### Updates to demo site

Our demo site hadn't really changed much in the 5 years since it launched, and while we've kept the ProcessWire version that's running it up-to-date, the front-end really hadn't changed at all. This week I re-developed the front-end using [Uikit](https://getuikit.com) so that now the site hopefully doesn't look like something too old school anymore. The previous iteration wasn't even responsive, consistent with the time it was developed. So it was time for an update…

The end result is completely stock Uikit, which made it quick to develop, but also likely more useful to those that would want to use the site profile as a starting point. Though admittedly, the new site lacks the personality of the old one, as there aren't really any graphical elements or branding details saying anything about skyscrapers. But I think that's okay now, as the site really is about being a demo for ProcessWire rather than any kind of serious directory of buildings. We've also added a few new features and details in this site, and will likely continue to do so.

In terms of the site template files, they have largely been re-developed to simplify a few things. It's using delayed output with the [_init.php](https://github.com/ryancramerdesign/skyscrapers2/blob/master/_init.php) file establishing the output regions, and the [_main.php](https://github.com/ryancramerdesign/skyscrapers2/blob/master/_main.php) file handling the main output. All additional markup is generated from include and view files in [/site/templates/includes/](https://github.com/ryancramerdesign/skyscrapers2/tree/master/includes), which are largely rendered by the [$files->render()](/api/ref/files/render/) API function. I also took the opportunity to use our new functions API updates, and new region() function, both of which are described further in this post.

- [See the new demo site](http://demo.processwire.com)
- [See the template files](https://github.com/ryancramerdesign/skyscrapers2)


### New functions API

The functions API is simply all the core API variables being callable as functions. For instance, rather than `$pages->find()`, you could use `pages()->find()`. What are the benefits of this?

**The function calls are always in scope** Lets say you had a custom function you created where you need to access the [$page](../../../full/wire/core/Page/index.md) API variable. You would either have to pass that `$page` variable as an argument to the function, or you would have to access it from `wire('page')`. Now you can just access `page()` and it doesn't matter if $page is in scope or not.

**More IDE/editor friendly** When working with template files in an IDE like PhpStorm (or others), it probably doesn't recognize what the API variables are. If you type `$pages->find()` it may highlight $pages as an undefined variable (even if it isn't actually). Likewise, your method calls off of API variables won't have known return values or arguments that the IDE can help with. The solution is to use a little phpdoc like `/** @var Pages $pages */` to tell the IDE what $pages is, but that's a hassle. Whereas, IDEs immediately recognize the function call versions of the API variables. So by using `pages()` rather than `$pages`, you can more easily derive the benefits of your IDE knowing everything about the possible method calls (auto-completion), return values and argument types. Basically, it makes life easier and coding faster.

**Shorter API calls** In some cases, using the API functions will result in shorter API calls. This is because an API variable like $pages (and others) are mapped in such a way that `pages()->find("selector")` and `pages("selector")` are equivalent. Here's a few examples, each showing identical API calls. While each section of examples below provide identical results, the first two calls of each section (using the function calls) will likely be recognized by your IDE/editor, while the $variable versions likely won't.

```php
// Use a selector to retrieve multiple pages
$items = pages("template=basic-page");
$items = pages()->find("template=basic-page");
$items = $pages->find("template=basic-page");
$items = wire("pages")->find("template=basic-page");

// Use a path or ID to get a single page
$item = pages("/path/to/page/");
$item = pages()->get("/path/to/page/");
$item = $pages->get("/path/to/page/");
$item = wire("pages")->get("/path/to/page/");

// Get title from page
$title = page('title');
$title = page()->title;
$title = $page->title;
$title = $page->get('title');
$title = wire('page')->get('title');

// Retrieve GET variable
$foo = input('get')->foo;
$foo = input()->get('foo');
$foo = $input->get('foo');
$foo = wire('input')->get('foo');

// Sanitize a variable
$bar = sanitizer('pageName', $foo);
$bar = sanitizer()->pageName($foo);
$bar = $sanitizer->pageName($foo);
$bar = wire('sanitizer')->pageName($foo);
```

For details on possible arguments for all the API variables, see the function declarations and examples in [/wire/core/FunctionsAPI.php](https://github.com/processwire/processwire/blob/dev/wire/core/FunctionsAPI.php). All of this will be in our API reference soon as well.


### Drawbacks of the Functions API

While there are nice benefits to using these alternate function calls for many cases, there are also some drawbacks. None of them are major, but they are good things to consider:

This probably goes without saying, but you can only use this in ProcessWire 3.0.39 or newer.

You won't derive the IDE benefits unless your template file(s) declare "namespace ProcessWire;" at the top. The FileCompiler won't help you here because that takes place at runtime, not while you are coding.

At present, you have to tell ProcessWire you want to use the functions API by setting `$config->useFunctionsAPI = true;` in your /site/config.php file. Though after more testing, we may make it enabled by default in the future. If you don't have that $config property set to true, the functions are still available, but you have to prepend "wire" to them, i.e. the more verbose `wirePages()` rather than `pages()`.

Like using the `wire()` function, using the functions API may add confusion when using multiple instances of ProcessWire at once. That's because all API variables have a ProcessWire instance explicitly connected with them (a nice benefit), whereas the functions API versions are connected with whatever ProcessWire instance the template file is rendered by. Chances are that's what you want, but the reality is the API-variable versions are more explicit and thus preferable in a multi-instance environment.

Consistent with their API variable names, the API function names are pretty generic, i.e. `page()`, `user()`, `input()`, etc. So this increases the potential of collision with your own function names, should you have created a function with the same name (in the ProcessWire namespace). However, since all of these functions are in the ProcessWire namespace, this is less of a concern. But for this reason, using the functions API would be less desirable in the non-namespace ProcessWire 2.8.


### Using the functions API in classes

The functions API is also available to all Wire-derived classes (modules, etc.), and it does *not* require that $config->useFunctionsAPI is set. So for any API variable (i.e. $pages), you can now refer to it within a class as `$this->pages()`. Other than the "$this->" part, these versions work identically to their procedural versions described above. The benefits are the same as the procedural versions, though perhaps not quite as compelling since most Wire-derived classes can already access API variables directly (i.e. $this->pages) and they are always in scope. The following calls are equivalent:

```
$items = $this->pages("template=basic-page");
$items = $this->pages()->find("template=basic-page");
$items = $this->pages->find("template=basic-page");
$items = $this->wire('pages')->find("template=basic-page");
```


### New region function

The new region function provides a nice option for delayed output on the front-end, letting you define regions for output, populate content to it, and retrieve it when ready for output. It's a good alternative to using variables for the same purpose, as editor environments often don't recognize the relationship of variables between files like _init.php (prepend file), template files, and _main.php (append file). It prevents your editor from flagging variables as undefined, and reduces the chance of variable collisions or variables getting accidentally overwritten.

The region function can be accessed as `wireRegion()`, or if you have `$config->useFunctionsAPI` enabled, it can also be accessed as just `region()`. We'll use the short version for our examples below. But first, here's how a typical delayed output site works with variables acting as regions and placeholders for content:

**_init.php**

```
// define default regions
$headline = $page->title;
$content = $page->body;
```

**home.php**

```
// modify regions as needed
$headline = "Welcome";
$content .= "<h2>Latest News</h2> ...";
```

**_main.php**

```php
// output regions in appropriate locations
<h1><?php echo $headline; ?></h1>
<div id='content'>
  <?php echo $content; ?>
</div>
```

And here's how you might do the same thing using the region() or wireRegion() function:

**_init.php**

```
// define default values
region('headline', $page->title);
region('content', $page->body);
```

**home.php**

```
// modify regions as needed
region('headline', 'Welcome');
region('content+', '<h2>Latest News</h2> ...');
```

**_main.php**

```php
// output regions in appropriate locations
<h1><?php echo region('headline'); ?></h1>
<div id='content'>
  <?php echo region('content'); ?>
</div>
```

Benefits of the region() version are that there's little chance of a variable collision. For instance, if you use a variable named `$headline` for some other reason, that would collide with the one you are using for the region. Making use of the region() function to store this prevents that problem. The other benefit is that in both home.php and _main.php, your IDE/editor will likely think that $headline and $content are undefined variables (even if they technically aren't at runtime). Using the region() function solves the false inspection error problem.

One other thing to note: append a "+" to the region name when you want to *append* an existing value that's already present, and prepend a "+" to the region name when you want to *prepend* to an existing value:

```
region('name+', 'value'); 
region('+name', 'value');
```

The region() function and many of the new functions API calls in action can be found in the [new demo site templates](https://github.com/ryancramerdesign/skyscrapers2).


### Recipe: converting thumbnail images for PW3 admin

Lets say that you've recently upgraded to ProcessWire 3.x and noticed that all of your thumbnail images are low-quality in the admin. This is because PW 2.7 used 100-pixel height thumbnails, while PW 3.x uses 260 pixel width thumbnails, quite a size difference. When in the page editor, you'll notice those images look pretty low quality, and that PW gives you a little checkbox you can check to force it to re-create them. But if you've got dozens, hundreds or thousands of pages, you probably aren't going to bother. Here's a way that you can force it to re-create automatically…

In your /site/config.php file, add the following:

```
$config->adminThumbOptions('height', 202);
```

The "202" part actually can be any number, so long as it's not the previous default value of "100", and doesn't overlap with any existing thumbnail sizes (which is why we chose "202" rather than "200", though either would likely work). This "height" property is deprecated and now only used to detect if thumbnails are old or new. So by giving it a value of "202", ProcessWire checks to find no existing thumbnail is present (with height of "202") and it creates a new one using the new default setting of 260px width.

The reason ProcessWire uses the old thumbnails (upscaled in the admin) by default is that creating thumbnails can be an expensive process, especially on pages with lots of large images. One of the sites I work on has thousands of pages with dozens of multi-megabyte villa photos on each. Creating all those thumbnails anew could really slow the editors down when they go to edit each page. They don't care about blurry thumbnails, but they would really care about being slowed down when making edits to existing pages. So before you implement this recipe, make sure your context is not one that's going to result in calls from the client about why the server is slow. :)

That's it for this week. Hope that you all have a great weekend and enjoy reading the [ProcessWire Weekly](https://weekly.pw).
