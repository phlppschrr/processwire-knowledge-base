# ProcessWire 3.0.172 – Find faster and more efficiently

Source: https://processwire.com/blog/posts/find-faster-and-more-efficiently/

## Sections


## ProcessWire 3.0.172 – Find faster and more efficiently

5 February 2021 by Ryan Cramer [ 11 Comments](/blog/posts/find-faster-and-more-efficiently/#comments)

This week ProcessWire gained powerful new tools for finding pages and controlling how they are loaded. If you like to maximize performance and efficiency, you’ll like what 3.0.172 brings.


### Boost performance with new programmatic autojoin options

Before we get into what's new, it helps to have some background on ProcessWire's field autojoin option. ProcessWire is largely focused on lazy loading page data on-demand as it is requested from the API. When you ask for `$page->body` (for example), it will load the value from the database at that time, rather than loading it at the time the $page was loaded. This enables ProcessWire to do much more with less, and prevents it from using CPU cycles and memory for loading, processing and storing data unless/until it is actually used. It also enables ProcessWire to store a whole lot more pages in memory than it would be able to otherwise. But like most things, there's another side to this…


### Classic autojoin

If there are fields that we know are going to be used on every request, then the reality is that it's much faster and more efficient to load that data at the time the $page loads (and in the same query), effectively cancelling the lazy-load behavior for a particular field. This is what we call the "autojoin" option in ProcessWire. It means a field is automatically joined into the page, in the same query that loads the page.

In ProcessWire, the "title" field is one that typically has autojoin enabled by default. That's because the title of a page is almost always used with the $page, whether rendering the entire page or rendering it in a list. But if we disable the autojoin option for the title field, then a simple block of code like the following takes twice as long to complete:

```php
foreach($pages->find('id>0') as $item) {
  echo $item->title;
}
```

On my test installation running locally with 5,500 pages and "title" as the only autojoin field, the code above took 2.3 seconds to complete. But as soon as I disabled autojoin for the title field, it took nearly twice as long: 5.3 seconds. As you can see, effective use of autojoin can double our performance in a case like this.


### Another classic autojoin example

I tried another version of the installation that also had 5,500 pages, but had autojoin settings settings tweaked for each field and template, optimized according to how fields are used in the site. For instance, blog posts autojoin the title, date, summary and author; while pages representing rentable properties autojoin fields like location, price, days, subtitle and summary. That's because those fields are used in rendering lists of these different item types, so autojoin options are configured consistently with the specific list output needs.

In this installation with lots of autojoin fields, my simple example above now takes 24 seconds to execute. The reason for that is that I'm only using the title field in my example, but am loading a whole bunch of other fields behind the scenes since they are autojoin—fields I don't need for my current output. Chances are that's just fine, as it's not often we need to load all 5,500 pages in a website and render their titles... so my example is admittedly contrived. But I think it does help to demonstrate the importance and scope of the autojoin option, both on the positive and negative side. These kinds of factors can be especially impactful when building features like site-wide search engines and the like.


### The new programmatic autojoin option

This week the `$pages->find()` method (and any others that delegate to it) has been upgraded with the ability to let you specify what fields you want to autojoin. This enables us to optimize our $pages->find() operations consistent with specific output needs. We can do this by specifying the `field=name` option in the selector:

```php
$items = $pages->find('id>0, field=title');
```

The above says to load all pages in the site and autojoin the "title" field, and not to autojoin any others. The returned pages ($items) all have their titles populated, but accessing any other fields on those pages triggers the usually lazy loading behavior. My example above that was taking 24 seconds is now back to taking 2.3 seconds.

Let's say that we are finding and rendering search results output for a site-wide search engine. Our search results can include pages of all different kinds of types, with all different kids of fields, some of which have autojoin enabled. But when it comes to search results, we want to render all of our pages consistently, regardless of what type they are. There are two fields which are common to all of our page types, and we want to use in the search results: "title" and "summary". So we specify them in our selector:

```php
$q = 'search query';
$items = $pages->find("title|body*=$q, field=title|summary");
```

You can also specify each field separately, and the result is the same (use whichever format you prefer):

```php
$items = $pages->find("title|body*=$q, field=title, field=summary");
```

When rendering blog posts, we use not just the title and summary, but also the date, author and category in our output, so it's good for us to autojoin those fields:

```php
$pages->find('template=blog-post, field=title|summary|author|category');
```

If you take this approach, then perhaps it is rare that you would need to use the autojoin option configured for fields in the admin. This programmatic autojoin option does give you finer and more context specific control over when and where it is used. In fact, the option is compelling enough that I thought it also needed its own method call, at least for documentation purposes…

Side note: if you have a field in your site literally named “field” (or if you don't like using the keyword “field” in your selector), you can also use the keyword “join” instead. Either works, they are synonyms.


### Using the $pages->findJoin() method

The [$pages->findJoin()](../../../full/wire/core/Pages/method-findjoin.md) method does the same thing as examples above, but the autojoin fields are instead specified in the $fields argument rather than in the selector:

```php
$items = $pages->findJoin($selector, $fields);
```

The $fields argument can be an array or CSV string of field names to autojoin. Want to tell ProcessWire not to autojoin any fields? Here's how you can do it:

```php
$pages->findJoin($selector, false); // this
$pages->find("$selector, field=none"); // or this
```


### Behind the scenes

Whether using the new programmatic autojoin option with $pages->find(), $page->children(), $pages->findJoin() or any other method that delegates to $pages->find(), there's a lot of new stuff going on behind the scenes. ProcessWire now uses a new and different page finding method when autojoin fields are specified programatically. Rather than splitting the page finding and page loading into 2 big separate queries, it does it all in 1 query. This is possible because ProcessWire doesn't need to determine which templates (and thus fields) are in matching pages, and then determine which autojoin fields to use. Instead, when you manually specify the autojoin fields, it doesn't have to do that work, so it can load them all together at once.


### Finding faster with raw data

The new [$pages->findRaw()](../../../full/wire/core/Pages/method-findraw.md) method works just like the $pages->find() method except that it returns the raw data from the matching pages in a PHP array, and lets you specify which fields you want to get from them. Because it has to do a lot less work than $pages->find(), it enables you to retrieve information from pages a whole lot faster, and using a lot less memory, than you could before.

```php
$array = $pages->findRaw($selector, $field)
```

As the method name suggests, the data returned from this method is raw and unformatted, directly as it exists in the database. So this isn't going to be a direct replacement for a $pages->find() in most cases, but in other cases it may be just what you need.

Adrian posted [this comparison](https://processwire.com/talk/topic/25042-weekly-update-%E2%80%93-29-january-2021/?do=findComment&comment=210625) using TracyDebugger in the forum. It appears his test was matching 2600 pages, and I think it does a good job of demonstrating that there is a significant difference in overhead when using findRaw():

```php
d($pages->find('hasParent=1')); // 2297ms, 7.5 MB
d($pages->findRaw('hasParent=1', 'title')); // 279ms, 858 KB
```

The first $pages->find(); performance is going to be affected by installation-specific factors, especially configured autojoin fields. So everyone may experience very different results here, but it is a good example nonetheless.


### Using the $pages->findRaw() method

The `$selector` argument can be any page-finding selector that you would provide to a regular $pages->find() call. The most interesting stuff relates to the $field argument though. If you omit the $field argument, like this…

```php
$a = $pages->findRaw("template=blog-post");
```

…it will return all data for the found pages in an array where the keys are the page IDs and the values are associative arrays containing all of each page’s raw field and property values indexed by name. But retrieving all the data from each page probably isn't the most efficient route to take unless you are trying to do a full export of pages.

Where findRaw() is more useful is for cases where you want to retrieve specific things without having to load the entire page (or its data). To do this, we'll need to use the $field argument. Below are a few examples of how you can do this. If you provide a string (field name) for $field, then it will return an array with the values of the primary (data) column of that field. The following would return an array of blog-post page titles indexed by page ID:

```php
$a = $pages->findRaw("template=blog-post", "title");
```

The $field can also be the name of a native pages table property like "id" or "name".

If you provide an array for $field then it will return an array for each page, where each of those arrays is indexed by the field names you requested:

```php
$a = $pages->findRaw("template=blog-post", [ "title", "date" ]);
```

You may specify field name(s) like `field.subfield` to retrieve a specific column/subfield. When it comes to Page references or Repeaters, the subfield can also be the name of a field that exists on the Page reference or repeater.

```php
$a = $pages->findRaw("template=blog", [ "title", "categories.title" ]);
```

You can also use this format below to get multiple subfields from one field.

```php
$a = $pages->findRaw("template=blog", [ "title", "categories" => [ "id", "title" ] ]);
```

In the example above, we are asking for the "title" from each page, as well as the "id" and "title" from each of the pages in the "categories" page reference field.

You may also specify wildcard field name(s) like `field.*` to return all columns for $field. This retrieves all columns from the field’s table. This is especially useful with fields like FieldtypeTable or FieldtypeCombo that might have several different columns:

```php
$a = $pages->findRaw("template=villa", "rates_table.*" );
```

*There is also the [$pages->getRaw()](../../../full/wire/core/Pages/method-getraw.md) method which works the same way but focuses on getting just 1 page.*


### Get fresh pages when you want them

The last new method we will cover here actually has nothing to do with performance, but it is useful for a completely different reason. The [$pages->getFresh()](../../../full/wire/core/Pages/method-getfresh.md) gets a fresh, non-cached copy of a Page from the database. This method is the same as $pages->get() except that it skips over all memory caches when loading a Page. Meaning, if the Page is already in memory, it doesn’t use the one in memory and instead reloads from the DB. Nor does it place the Page it loads in any memory cache.

```php
$freshPage = $pages->getFresh($selectorOrPage);
```

Use this method to load a fresh copy of a page that you might need to compare to an existing loaded copy, or to load a copy that won’t be seen or touched by anything in ProcessWire other than your own code.

```php
$p1 = $pages->get(1234);
$p2 = $pages->get($p1->path);
$p1 === $p2; // true: same Page instance

$p3 = $pages->getFresh($p1);
$p1 === $p3; // false: same Page but different instance
```

Have any questions about these new options? Feel free to comment below. Be sure to read the [ProcessWire Weekly](https://weekly.pw) as well. Thanks for reading and have a great weekend!
