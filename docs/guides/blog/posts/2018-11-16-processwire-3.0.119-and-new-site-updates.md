# ProcessWire 3.0.119 and new site updates (part 3)

Source: https://processwire.com/blog/posts/processwire-3.0.119-and-new-site-updates/

## Sections


## ProcessWire 3.0.119 and new site updates (part 3)

16 November 2018 by Ryan Cramer [ 17 Comments](/blog/posts/processwire-3.0.119-and-new-site-updates/#comments)


## ProcessWire 3.0.119

This week we take a look at what's new in ProcessWire 3.0.119 and then we finish up by taking a look at a few screenshots from the new ProcessWire development website. If you read my post last week in the forum, you may already be familiar with some of these updates, but we'll cover them in a little more detail here.


### Auto-opening file/image fields

This handy update comes via Robin S. (@Toutouwai). When you drag an file into the ProcessWire page editor and drag it over a field that accepts files (like file, image or CKEditor field) it will automatically open that field if it happens to be collapsed. See this short screencast with Robin S. demonstrating the feature:

I'm personally thrilled with this feature because I usually keep my file/image fields collapsed when not populated. So I often run into the case where I'm dragging an image in, but have to abandon it once I realize the field isn't open. This solves that.


### Chunked ajax file upload

This next update comes to us via @BitPoet, who noted that our ajax upload feature can run out of memory if you try to upload a file that is too large to fit in memory. So BitPoet proposed a specific update for our WireUpload class so that rather than reading the whole file into memory before writing it, it would read 8 megabytes, write it, and then read the next 8 megabytes, write again, and so on. Now it should be able to handle files of any size.


### New WireArray slices() method

A new method has been added to WireArray and all derived types: `slices()`. This method accepts a single argument, which is the number of slices that you want to split the WireArray into. It returns an array of WireArray objects, each containing the number of items you requested. This method is non-destructive, so it leaves the original WireArray in tact.

One example of where this method can be useful is in handling multi-column navigation. For instance, lets say want to have a 3 column layout where a navigation list is equally split among the 3 columns. Here's a look at just such a scenario from the new ProcessWire website sites directory showcase, where we have a "categories" dropdown that appears on hover. Because there's a lot of categories, I want to display it in 3 columns, so that the user doesn't have to scroll:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2458/sites-dir-category-dropdown.png)

Here's how we're using the `slices()` method to handle that:

```php
$categories = $pages->get('/about/sites/categories/')->children();
foreach($categories->slices(3) as $items) {
  echo "<div class='uk-width-1-3'><ul>";
  echo $items->each("<li><a href='{url}'>{title}</a>");
  echo "</ul></div>";
}
```


### New functions API setting() function

This week I added a new function to the ProcessWire functions API, which is always available if you've got `$config->useFunctionsAPI = true;` in your /site/config.php. (This is already the case for most new installations).

This function does something very simple—it sets and gets runtime settings to use in your site templates. It's kind of like using $config except that it's a blank slate intended purely for your own front-end runtime settings. So there's no danger of overwriting anything. Furthermore, it's accessible just as a function, so it is always in scope and you won't get any complaints from your IDE. You also don't have to worry about overwriting it, like you would with passing variables between templates.

Here's how it works:

```
// set a setting named “foo” to value “bar”
setting('foo', 'bar');

// get a setting named “foo”
$value = setting('foo');

// set or replace multiple settings
setting([
  'foo' => 'value',
  'bar' => 123,
  'baz' => [ 'foo', 'bar', 'baz' ]
]);

// get all settings in associative array
$a = setting();

// to unset a setting
setting(false, 'foo');
```

The above aren't exactly real-world examples, so lets take a look at a real-world example. In this case, the new ProcessWire website. I have a /site/templates/_init.php file where I establish all the default settings for the site. Here's how I'm initializing them with the setting function:

```
setting([
  'site-title' => 'ProcessWire',
  'browser-title' => page()->get('browser_title|title'),
  'meta-description' => page()->get('meta_description|summary'),
  'masthead-class' => 'uk-section-primary',
  'headline-class' => 'uk-section-primary',
  'headline-layout' => 'normal',
  'content-class' => '',
  'content-layout' => '2col',
  'content-layout-primary-class' => 'uk-width-expand',
  'content-layout-2col-side-class' => 'uk-width-1-4@m',
  'content-layout-3col-side-class' => 'uk-width-1-4@m',
  'content-layout-3col-meta-class' => 'uk-width-1-5@m',
  'canonical-url' => page()->httpUrl(),
  'search-placeholder' => __('Search…'),
  'html-classes' => WireArray([
    'template-' . page()->template->name,
    'page-' . page()->id,
  ]),
  'css-files' => WireArray([
    'https://fonts.googleapis.com/css?family=Krub:300,400,400i,500,600,600i',
    urls('uikit') . 'css/uikit.min.css',
    urls('templates') . 'styles/main.css',
    urls('templates') . 'scripts/highlight/styles/ir-black.css',
  ]),
  'js-files' => WireArray([
    urls('JqueryCore') . 'JqueryCore.js',
    urls('uikit') . 'js/uikit.min.js',
    urls('uikit') . 'js/uikit-icons.min.js',
    urls('templates') . 'scripts/highlight/highlight.pack.js',
    urls('templates') . 'scripts/main.js',
  ]),
]);
```

As you can see, I'm using the `setting()` function in my /site/templates/_init.php file to define layout settings, various class names that my individual template files might manipulate, default values for common elements that I might sometimes modify per-template, the default set of css/js files, and more.

In some templates I modify the defaults where needed. For instance, in my template file for the sites directory, I modify a few of the settings, since it has a few unique factors relative to other more text-oriented pages in the site:

```
setting('content-layout', '1col');
setting('content-class', 'uk-section-primary');
```

In my case, most of the settings are ultimately used in the /site/templates/_main.php file. For instance, here's an abbreviated look at the file (thoug the <head> section is complete):

```
html<!DOCTYPE html>
<html lang='en' class='<?=setting('html-classes')->implode(' ')?>'>
<head id='html-head'>
  <meta http-equiv='content-type' content='text/html; charset=utf-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1'>
  <title id='html-title'><?=setting('browser-title')?></title>
  <meta name='description' content='<?=setting('meta-description')?>'>
  <link rel='canonical' href='<?=setting('canonical-url')?>'>
  <?=setting('css-files')->each("<link rel='stylesheet' href='{value}'>")?>
  <?=setting('js-files')->each("<script src='{value}'></script>")?>
</head>
<body id='html-body'>
  <header id='masthead' class='<?=setting('masthead-class')?>'>
    ...
  </header>
  <main id='content' class='<?=setting('content-class')?>'>
    ...
  </main>
  ...
</body>
</html>
```

This simple `setting()` function can be quite handy, and a lot less prone to error than using variables shared between template files.


### New ProcessWire.com site update (part 3)

Since much of this post has been using examples from the new ProcessWire.com website, and you've already seen one screenshot above, we might as well take a look at a few more. These are very much preliminary.

While far from final, at present, the new design evolves from the current site rather than completely re-thinking it. It also uses the same exact colors, though with a more flat approach. Maybe this will change once we get more designers involved in the project, but that's where it is at right now.

In terms of concept, I've been happy with what we communicate with the skyscrapers (building and scale), and wanted to continue that, even if subtle. But I also felt like the design should evoke this conceptual definition of ProcessWire a little more:

ProcessWire is like the “wire” that delivers the electricity to your “process”. The term “ProcessWire” refers to bringing everything together simply, easily and securely. Specifically, bringing together all the processes involved in building a website or application and wiring them all together to create something whole and complete. ProcessWire enables you to make all these connections intelligently, efficiently and easily. Metaphorically these connections are the wire, plug, socket and electricity all in one, while you provide the application. It is the tool that works with your existing processes (whatever they may be) and seamlessly wires them together, powering them into something greater than the sum of their parts.

The logo reflects this well, but I felt like the rest of the design needed to push that concept little more. As a result, there are more subtle wire and electrical symbols and motifs in the design. There is no homepage yet, I've been purely focused on the inside content pages of the website. Here's a look at a few of them.

**Viewing screenshots inline like this changes the feel of it quite a bit, so I recommend clicking the screenshots below to view the full-size versions. **

This is a typical index page (page that is more about showing children than content). This also demonstrates the dropdown navigation for the Docs section:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2458/structure.png)

Here's another variation of an index page that we use in other spots where the section navigation isn't as important, so we turn off the sidebars:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2458/output-strategies.png)

Here's a typical content page:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2458/docs-api.png)

Now we get into the ProcessWire API reference:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2458/apiref-modules.png)

Here's an API reference function details page:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2458/apiref-func.png)

The ProcessWire sites directory is below. This one selects featured categories randomly and displays sliders for each of them. You can click any category to view all the sites in the category. Hovering over any site reveals the details of the site. Clicking the site preview opens the actual website.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2458/sites-dir.png)

This screenshot demonstrates the hover state from the sites directory, where you can see details about each site:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2458/sites-dir-hover.png)

Lastly, you saw this one earlier, but I'll repeat it here again since this is the intended location for it. It shows the dropdown where you can select categories to filter sites by:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/2458/sites-dir-category-dropdown.png)

Thanks for reading. I hope you all have a great weekend and enjoy reading the [ProcessWire Weekly](http://weekly.pw)!
