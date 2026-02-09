# ProcessWire 3.0.7 Expands Field Rendering, Page Path History and More

Source: https://processwire.com/blog/posts/processwire-3.0.7-expands-field-rendering-page-path-history-and-more/

## Sections


## ProcessWire 3.0.7 Expands Field Rendering, Page Path History and More

5 February 2016 by Ryan Cramer [ 6 Comments](/blog/posts/processwire-3.0.7-expands-field-rendering-page-path-history-and-more/#comments)


## ProcessWire 3.0.7

This week we have another new ProcessWire 3.x version for you that includes several updates and optimizations. We've also expanded upon the field rendering with template files, with lots of info below. Hope you enjoy!


### What's new in 3.0.7?


### Page Path History now Multi-Language

The core Page Path History module is a really useful one to have because it keeps track of previous URLs that each page has lived at, and automatically 301 redirects to the new URL. It ensures that links are never broken from moving or renaming pages. Further, other parts of the core (including the new page link abstraction) utilize the Page Path History module.

The only problem was that it didn't support multi-language page URLs, so it was really only useful with the default language. This week we made several updates to the Page Page History module so that it now fully supports multi-language sites.

*Many thanks to GitHub user @bnfcs for originally proposing this update via a [pull request](https://github.com/ryancramerdesign/ProcessWire/pull/1033/files). While we ended up taking a little different approach with regard to the implementation (much has changed in the core since that time), Page Path History now supports multi-language certainly in good part due to @bnfcs submitting that PR.*


## Field rendering with template files

A few weeks ago we introduced [core support for field rendering with template files](/blog/posts/more-repeaters-repeater-matrix-and-new-field-rendering/) located in /site/templates/fields/. I wasn't really sure how much interest there would be in it at first, so kept things simple. There actually has been quite a lot of interest in it, so we've expanded it to do more.

The most requested feature was to have more control over what file renders the field, so we've gone ahead and added a lot more options here in ProcessWire 3.0.7. First off, here's the simplest example:

```
echo $page->render('body');
```

Previously, if you were rendering a field named "body", it would just look for the file /site/templates/fields/body.php and use it to render the field. That's nice and easy. But lets say you don't always render your "body" field the same way, and want more options?

ProcessWire 3.0.7 expands that simple render() call above, by first checking to see if more specific files exist, using the default body.php as the fallback/default. Here is what it checks, in this order (assuming field "body" and template "basic-page"), using the first file that it finds:

- /site/templates/fields/body/basic-page.php
- /site/templates/fields/basic-page/body.php
- /site/templates/fields/body.php (default/fallback)


### Specifying custom views

Now lets say that we wanted bypass that default logic and specify a different template/view file to render our body field. We can now supply a second argument to the render() method that specifies what file we want to use. The .php extension is always assumed on the file argument, so you can choose to omit it if you'd like, as we've done in our examples here.

```
echo $page->render('body', 'custom');
```

The word "custom" above can be any name that you make up, any template name, or any other field name. The above would make it look for the first matching file to perform the render, in this order:

- /site/templates/fields/body/custom.php
- /site/templates/fields/custom/body.php
- /site/templates/fields/custom.php
- /site/templates/fields/body.php (fallback)

If you want to specify exactly what file it should use rather than having it check among potential matches, prepend a slash:

```
echo $page->render('body', '/custom'); // use only custom.php
echo $page->render('body', '/custom/body'); // use only custom/body.php
```


### Render groups

From the above, you may have gathered that there can be more than one file for rendering a specific field. We can set up entire groups of field render files off subdirectories in site/templates/fields/ for specific contextual purposes.

For example, lets say that you have a common need for shortened versions of fields, like you might use in rendering a list of child pages, search results, or the like. For your "body" field, perhaps you only want to render the first paragraph. And perhaps for your "images" field, you only want it to render a thumbnail of the first image in the field. You could create these files:

/site/templates/fields/short/body.php

```php
<?php
// render the first found paragraph only
if(preg_match('!(<p>.+?</p>)!', $value, $matches)) {
  echo $matches[1];
}
```

/site/templates/fields/short/images.php

```php
<?php
// render a thumbnail of the first image
if(count($value)) {
  $image = $value->first()->width(200);
  echo "<img src='$image->url' alt='$image->description'>";
}
```

While we're at it, lets make one for the title field too that automatically links its title in a headline. We'll use a custom name "title-link" for this one, to clarify what it does:

/site/templates/fields/short/title-link.php

```php
<?php
// render a linked title
echo "<a href='$page->url'><h2>$page->title</h2></a>";
```

From your main template file, you might render a list of summarized child pages like this:

```php
<?php
foreach($page->children as $child) {
  echo $child->render('title', 'short/title-link');
  echo $child->render('images', 'short/');
  echo $child->render('body', 'short/');
}
```


### Taking it further

We might want to reuse that block of code above in multiple templates. You could just setup a children.php render file:

/site/templates/fields/children.php

```php
<?php
foreach($value as $child) {
  echo $child->render('title', 'short/title-link');
  echo $child->render('images', 'short/');
  echo $child->render('body', 'short/');
}
```

Now anytime you need to render a list of child pages anywhere in your site, you can just do this:

```
echo $page->render('children');
```


### There’s also $page->renderValue()

Before we wrap up this section of the post, I also wanted to mention the `$page->renderValue()` method, which lets you render a value that you supply, using whatever field template you want. For example, lets say that I want to render search results on in my /site/templates/search.php template file. I want to use the same output that we have for that children.php block above. Here's how you can do that:

```php
$results = $pages->find("body%=some text"); 
echo $page->renderValue($results, 'children');
```

The renderValue() works much the same way as the render() method except that it operates on a value that you give it, rather than pulling a value from the page. Because it doesn't know what field it corresponds to, you always have to specify what field template you want it to use.

In summary, field render templates do a good job of separating field-specific output and markup from other application logic. Of course, there are many ways to do this in ProcessWire, so consider field render templates just one more tool available for when the need suits it. Hope that you all have a great weekend and week ahead. For more, be sure to read the [ProcessWire weekly](http://weekly.pw).
