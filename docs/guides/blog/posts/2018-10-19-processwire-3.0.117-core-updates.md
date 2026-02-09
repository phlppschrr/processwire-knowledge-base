# ProcessWire 3.0.117 core updates

Source: https://processwire.com/blog/posts/processwire-3.0.117-core-updates/

## Sections


## ProcessWire 3.0.117 core updates

19 October 2018 by Ryan Cramer [ 6 Comments](/blog/posts/processwire-3.0.117-core-updates/#comments)


## ProcessWire 3.0.117

Work continued this week on development of the new ProcessWire.com website and that's where much of my time went. I've got all the posts in this blog section converted over, as well as the entire ProcessWire 3.x API site running in the new templates. Next week I'll be working on the rest of the documentation section, where quite a few things are moving around. Some of the core updates this week are related to needs that came up during site development, and this post covers a few of them below.


### New “pw-optional” attribute for markup regions

When defining markup regions, you can now specify a "pw-optional" or "data-pw-optional" attribute with your region. When present, the region will be removed if it is not populated by the time the page is rendered. Here's an example from the new processwire.com site templates. We've got this code somewhere in our _main.php file:

```
html<div uk-grid>
  <div id='content' class='uk-width-expand'>
    <?=$page->body?>
  </div>
  <div id='sidebar' class='uk-width-1-3' pw-optional>
  </div>
</div>
```

Note that empty #sidebar div with the pw-optional boolean attribute. If no template files populate that particular markup region, then the entire `<div id='sidebar'></div>` gets removed from the markup, and the #content div fills out the entire width. On the other hand, if the #sidebar is populated, then the sidebar appears in the output. For example, let's say that we have a /blog/ index page lists links to all the blog categories in the sidebar. Here's what's in our blog.php template file:

```php
html<div id='sidebar'>
  <h3>Categories</h3>
  <ul class='uk-nav'>
    <?php
    $categories = $pages->get('/blog/categories/');
    echo $categories->each("<li><a href='{url}'>{title}</a>");
    ?>
  </ul>
</div>
```

In the example above, the sidebar is populated and thus appears in the output, with the #content column consuming 2/3 columns, and the sidebar consuming 1/3 columns.

*Without* the `pw-optional` attribute in our _main.php #sidebar region definition, that #sidebar div would always be consuming 1/3 columns, even if it hadn't been populated with anything. The pw-optional attribute can be quite useful in a lot of cases, and encourages keeping the primary markup structure in your _main.php (or files included from it). I've already found it quite useful in development of the new site. Next time you are working with markup regions, consider trying it out.


### WireArray is now more useful

You might have heard of the [WireArray](../../../full/wire/core/WireArray/index.md) class, which is the foundation for all of ProcessWire's various collections of items (such as [PageArray](../../../full/wire/core/PageArray/index.md), and numerous others). The actual WireArray class isn't used very often on its own, and instead mostly serves as a common base for derived classes.

Part of the reason for that is that the WireArray class can only store objects derived from the Wire class. So if you wanted to use WireArray for some other kind of data type (like strings or numbers) you would have had to extend the WireArray class and implement various methods to create your own derivative of it.

Now WireArray can be used on its own with just about any data type. No longer is this base class limited to working with just Wire-derived objects. That's a good thing, because WireArray has a lot of useful methods already built-in, and thus can often be more handy than using a regular PHP array.

As a really simple example, lets use WireArray to hold some strings, such as CSS filenames. And then lets use the built-in each() method to output them:

```
$styles = new WireArray();
$styles->add('mystyles.css');
$styles->add('yourstyles.css');
$styles->prepend('firststyles.css');

echo $styles->each(function($file) {
  return "<link rel='stylesheet' href='$file'>";
});
```

Another update to WireArray (and all WireArray derived types) is that you can now create a new WireArray and add items to it in the same call, using the static new() method:

```
$styles = WireArray::new([ 'a.css', 'b.css', 'c.css' ]);
```

In the above example, we provided it with 3 items to add, via a regular PHP array. However, you can make it even simpler and provide them as arguments (as many or as few as you want):

```
$styles = WireArray::new('a.css', 'b.css', 'c.css');
```

And just to complete our example, we'll output them. The following renders a <link> tag for each of the css files:

```
echo $styles->each("<link rel='stylesheet' href='{value}'>");
```

The examples above are all really basic, so also wanted to mention that WireArray works as an associative array too (though it has always been the case):

```
$contact = WireArray::new([
  'address' => '123 Peachtree Rd.',
  'city' => 'Atlanta',
  'state' => 'GA',
  'zip' => '30307'
]);

$contact->set('zip', '30307');
$contact['country'] = 'US';

echo $contact->each("<li>{key}: {value}");
```


### Other updates

In addition to the above updates, version 3.0.117 also improves upon the *PagesExportImport* class and related *Process* module for exporting/importing pages. I ran into a small issue with some image and href links breaking in my textarea fields in the blog, when exporting and then importing into the new site. That's because the new development site runs off a subdirectory, while the current live site does not. So the export/import functions now keep track of domain/host they are running at, as well as the root URL, and make adjustments as needed to textarea fields containing HTML, ensuring that local links are never broken by the export/import process.

The blog here (and actually the entire site) contains a lot of user comments powered by ProcessWire's *FieldtypeComments*. Of course these have to be exported and imported along with the rest of the page data. All of that went perfectly, without any hiccups, using the built-in page export/import functions. But I wanted to make a lot of upgrades to the output of the comments markup, so several updates were made to the core *FieldtypeComments* classes in order to support further customization and configuration.

That's all for this week. As mentioned earlier, next week I'm going to be working on the documentation section of the new site, along with likely another core version on the dev branch, as usual. Thanks for reading. Enjoy reading the [ProcessWire Weekly](http://weekly.pw), and have a great weekend!
