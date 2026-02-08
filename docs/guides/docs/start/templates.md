# ProcessWire CMS template files (PHP)

Source: https://processwire.com/docs/start/templates/

## Summary

Every time a page is loaded on your site, ProcessWire looks at what template is assigned to the page, loads it, gives it several API variables, and then runs it as a PHP script.

## Key Points

- Show 3 pages at the most
- Only show press releases
- Show a date
- Show a summary
- Sort them newest to oldest

## Sections


## Using template files in ProcessWire

Every time a page is loaded on your site, ProcessWire looks at what template is assigned to the page, loads it, gives it several API variables, and then runs it as a PHP script.

This section covers the use of template files and serves as an introduction to using ProcessWire’s API with examples.


## How do template files work?

Every time a page is loaded on your site, ProcessWire looks at what template is assigned to the page, loads it, gives it several API variables, and then runs it as a PHP script. These template files are located in this directory: /site/templates/.

These template files can be as simple as a plain HTML file, or they can be as complex as as an entire PHP application. But like most CMS platforms, the most common instance if for templates to contain markup (HTML) with PHP tags inserted where necessary to output content from ProcessWire.

Adding a template is as simple as placing a new file (with .php extension) in the directory above, going into ProcessWire admin, and clicking on Templates > New. It will find your template and ask you to select which fields should be added to it. This article describes how you would work with the ProcessWire API in a template file.


## Basic Usage

Lets assume we are editing a template file that is just an HTML document. Taking a value from your page in ProcessWire and outputting it from your template file is very simple. Here is an example of a line in a template file that outputs the current page's title:

```
<h1><?=$page->title?></h1>
```

Assuming the page's title field contains the value "Hello World", the resulting output of the template would be:

```
<h1>Hello World</h1>
```

The syntax that you saw above uses something called PHP short tags. Most PHP installations support this. However, if your PHP installation does not, then you would have to do this instead:

```php
<h1><?php echo $page->title; ?></h1>
```

The $page variable seen in the examples above is one of a few API variables that ProcessWire provides to every template file. But $page is the one that you are likely to use most often. It contains all the fields present on the page being viewed. Every one of those fields can be referenced like the 'title' field above.

For example, lets say that you had a field called 'bodycopy' that contained the body copy for your page. You might output it like this in your template:

```
<div id='bodycopy'>
    <?=$page->bodycopy?>
</div>
```

The fields that you can reference from $page depend on what fields you have added to the template in the ProcessWire Admin, under Setup > Templates. The values output depend on what you've typed or pasted into them when editing the page in ProcessWire Admin.


## Using other types of fields

Most fields contain simple values like text or numbers, but some fields can contain other types that you should output in a different way. For instance, lets say that you created a field with the 'Page' field type (FieldtypePage). That type of field is designed to hold one or more other pages. This is different from the title and bodycopy fields mentioned above, which just contained text.

A similar (but more common) field would be $page->children, which is a built-in variable present on every $page. It holds any child pages (aka subpages).

Here is an example of how this type of field works. Lets say that we wanted to output a list of all pages that are children (aka subpages) of the current page, and make them clickable links. First lets see what happens if we use the same strategy as above with the title and bodycopy fields, by putting this in our template:

```
<?=$page->children?>
```

The resulting output might look like this:

```
5723,4958,5937
```

That's not what we wanted. But ProcessWire doesn't want to make any assumptions about what you want, so you have to be more specific. What we will do is loop through these child pages and output them in a list:

```php
<ul><?php
foreach($page->children as $child)
   echo "<li><a href='$child->url'>$child->title</a></li>";
?></ul>
```

The resulting output might look like this:

```
<ul>
<li><a href='/about/contact/'>Contact Us</a></li>
<li><a href='/about/press/'>Press Releases</a></li>
<li><a href='/about/staff/'>Our Staff</a></li>
</ul>
```

For even shorter syntax, below is an alternative way to do the same thing, all on one line:

```
<ul><?=$page->children->each("<li><a href='{url}'>{title}</a></li>")?></ul>
```

In this article, most of the time we'll use the longer syntax since it is more standard PHP and thus may be a little easier to follow. However we wanted to let you know that the shorter syntax is available, when or if you find it helpful.


## Creating markup is your job (most of the time)

ProcessWire is designed to be completely document type agnostic, meaning it makes no assumptions about whether you are using it to output HTML, XHTML, HTML5, XML, JSON, any kind of web service, etc. As a result, ProcessWire's core framework never outputs markup, and that's why we generate the HTML markup in the manner shown in the examples above. However, plugin modules are provided with ProcessWire that do output Markup, should you want to use them (or create your own).

A relevant example in this case is the MarkupPageArray plugin module, which is installed by default and adds a render() function to all fields that return a PageArray (as many functions in ProcessWire do). So a shortcut to the above example could be:

```php
<?php echo $page->children->render(); ?>
```

In most cases, I recommend that you generate the markup yourself rather than using plugins to do it for you... especially when getting started. That way you will get a better understanding of the API and more control over your markup.


## Finding and loading other pages from your template file

The API is not limited to just the $page variable and the variables reference will cover all of them for you. But lets look at another common one, which is the $pages variable. The $pages variable is your connection to all the other pages in your site. It provides get() and find() functions that enable you to find and load other pages with ease.

For example, lets say that we have an 'address' field on our 'Contact Us' page, and it contains the text of our company's mailing address. We want to display it in the footer throughout our site. Here is what the code to do that might look like:

```php
<p>Visit us at: <?php 
$contact = $pages->get("/about/contact/");
echo $contact->address;
?></p>
```

The above example is intentionally verbose for explanation purposes. A shorter way of doing the same thing could be:

```php
<p>Visit us at: <?=$pages->get("/about/contact/")->address?></p>
```

That $pages->get() function will accept a path to a page (like above), a page ID number, or a selector. Assuming it can find a page matching your request, it will return just a single page. If there are more pages that match, it's still just going to return only the first one that it found.

The $pages->find() function works like the get() function except that it returns multiple pages. We'll demonstrate it's use in the examples below.


### Example: finding all featured pages

As an example, lets say that we wanted to display a list of all pages in the site that have a field called 'featured' with a value of 1 (in ProcessWire, a checkbox field has a value of 1 when checked). We want to display this list of featured pages in the sidebar of our homepage. Here is how we could do that in our homepage template file:

```php
<ul><?php
$features = $pages->find("featured=1");
foreach($features as $feature)
   echo "<li><a href='$feature->url'>$feature->title</a></li>";
?></ul>
```


### Beyond the basics

So now we've got a list of featured pages that we're displaying in the sidebar of our homepage. But what if we wanted it to do all of these too:

- Show 3 pages at the most
- Only show press releases
- Show a date
- Show a summary
- Sort them newest to oldest

To achieve the above, we'll assume that press release pages have a 'date' and 'summary' field already. Here are a few ways we might find those pages. If they all have the same parent, then either of these statements achieves the same result:

```php
$pages->find("parent=/about/press/, featured=1, limit=3, sort=-date");
```

...or...

```php
$pages->get("/about/press/")->children("featured=1, limit=3, sort=-date");
```

Looking at the above, we are using a selector to tell the find() or children() functions what to return. Selectors tend to be self explanatory at a glance. This selector literally says "find the 3 most recent featured press releases."

Note that the "sort=-date" essentially says "sort by date descending", whereas "sort=date" (without the minus sign) would mean "sort by date ascending". Since we want newest to oldest, we would need them sorted descending. To achieve that, we just precede the field name with a minus sign.


### Taking it further

Lets say that down the road the press releases section grows and now contains multiple categories of press releases, where the press releases are subpages of categories like:

```
/about/press/marketing/ ...
/about/press/investing/ ...
```

We can no longer assume that all press releases have the same parent, so we'd have to approach our find a little bit differently:

```php
$pages->get("/about/press/")->find("featured=1, limit=3, sort=-date");
```

This is exactly like one of the previous examples, except that the children() has been replaced by a find(). Using the find() function on any given page will traverse all levels of pages within it (children, grandchildren, great grandchildren, and so on), making it suitable for these press releases. Whereas the children() function always just refers to one level – direct children of the page being referenced.


### And further...

But now the client is putting press releases not just in /about/press/, but also in the /products/ section of the site (and who knows where else!). We have to change our strategy to find press releases no matter where they are in the site. To do that, we're going to find our pages by their template rather than their location:

```php
$pages->find("template=press_release, featured=1, limit=3, sort=-date");
```


### Full example in context

To complete our example, here it is in context, including display of the date and summary:

```php
<ul><?php
$features = $pages->find("template=press_release, featured=1, limit=3, sort=-date");
foreach($features as $feature) {
   echo "<li>" .
        "<h3><a href='$feature->url'>$feature->title</a></h3>" .
        "<span class='date'>$feature->date</span>" .
        "<p>$feature->summary</p>" .
        "</li>";
}
?></ul>
```


## Next steps

Look at the different output strategies that you can use with your template files.

Take a look at the template files included with your ProcessWire installation in /site/templates/. They are live examples commented to help get you going.
