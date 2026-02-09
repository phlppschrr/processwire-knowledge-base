# ProcessWire 3.0.6 brings $pages upgrades, link abstraction and more

Source: https://processwire.com/blog/posts/processwire-3.0.6-brings-pages-upgrades-and-link-abstraction/

## Sections


## ProcessWire 3.0.6 brings $pages upgrades, link abstraction and more

29 January 2016 by Ryan Cramer [ 9 Comments](/blog/posts/processwire-3.0.6-brings-pages-upgrades-and-link-abstraction/#comments)


## ProcessWire 3.0.6

This week we've got some great new optimized methods added to the $pages API variable, plus full link abstraction now built-in, new sub-selector upgrades, and more!


## Improvements to sub-selectors


### Speed improvements

The speed at which sub-selectors operate has now been greatly improved. Basically, they are now hundreds of times faster than before. Though you might not have noticed it unless you were sub-selecting thousands of pages, but if you were, you'll find a major performance difference now.


### Support for nested sub-selectors

We've also added support nested sub-selectors. When using selectors to find pages, like with $pages->find(), $pages->children(), etc., support is now built-in for nesting of these sub-selectors (or sub-selectors within sub-selectors if you prefer). Meaning, you can use selectors like this:

```
template=member, invoice=[status=paid, invoice_row!=[product.color=Red]]
```

*Thanks to Avoine and Antti Peisa for suggesting these improvements. *


## Pages class refactoring ($pages API var)

The Pages class has now been split out into several more specific classes, leaving the current Pages class as the central hub that delegates to them, rather than providing the implementation itself. This particular change does not have any effect on our API or hooks, etc., other than making it more efficient. Not too exciting, but it's one of those things that's been on my todo list for quite some time, and actually quite a big change in terms of the core code–another 3.0 box checked!


## New optimized $pages API methods

In addition to the refactoring above, we've also added some new methods to the $pages class. If you were looking at the cheatsheet, these will all likely fall under the "advanced" category. Always looking for opportunities to optimize, they've been introduced primarily to optimize internal workings in the core. But these methods may be genuinely useful to many of you in our public API, so here they are…


### $pages->getPath()

This method enables you to retrieve the path (or URL) to a page, without loading the page. It accepts a page ID (integer) as the first argument, and an optional options array as the second.

If all you need is the path to a page, the benefit of this method is that it's substantially faster than loading the page and then displaying the path. For instance:

```php
A: echo $pages->get(123)->path;
B: echo $pages->getPath(123);
```

The A option above is already quite fast. But multiply that by thousand or so different pages, and the difference between A and B becomes quite measurable. For instance, here's the result I got after executing the above two lines separately, on 1200 different pages:

```
A: 2.28 seconds
B: 0.85 seconds
```

The getPath() method can also return multi-language paths. Just specify the Language object, id or name as the second argument to $pages->getPath(), i.e.

```php
$path = $pages->getPath(123, 'de');
```

*Side note: how are path and URL different?* You may already know this, but just in case, it's worth noting that path is the ProcessWire path to a page. That's going to be exactly the same as the URL if your site happens to run off the root of the domain. But if it runs off of a subdirectory, then the URL includes that subdirectory, while the path doesn't. Meaning, if you want to use the getPath() method to produce a URL on a site running off a subdirectory, you would just prepend the the root URL to it:

```
$url = $config->urls->root . ltrim($path, '/');
```


### ​$pages->getByPath()

This method is kind of the opposite of the getPath() method, and provides a more optimized way to load a Page, if you happen to know the path to it:

```php
// 4.26 seconds (x1200 calls to unique paths)
$a = $pages->get('/path/to/page');

// 1.98 seconds (x1200 calls to unique paths)
$b = $pages->getByPath('/path/to/page');
```

As you can see, if I load 1200 unique pages this way, the getByPath() method is a little more than twice as fast as $pages->get(). So you might be wondering why not just make a $pages->get('/path/'); call delegate to $pages->getByPath() instead? Well that's exactly what we're going to do, after we spend a little more time in testing. Meaning, you may not even need to remember this getByPath() method. But before you decide, note that getByPath() has a few more tricks up it's sleeve...

The getByPath() method accepts a second argument $options array. It can contain any of the following:

**getID (bool): **If you specify true for this option, it will return the page ID rather than the Page object. If you only need to get an ID for a path, this is the way to go, here's why:

```php
// 0.15 seconds! (x1200 calls to unique paths)
$c = $pages->getByPath('/path/to/page', array('getID' => true));
```

So rather than seconds, we're now talking milliseconds. Basically, if all you need is the ID, this becomes an incredibly fast operation.

**useLanguages (bool):** If you specify true for this option, the getByPath() method will accept a path in any language, and still be able to resolve it to a page.

**useHistory (bool):** If you specify true for this option, the getByPath() method will be able to return a page from a past URL that it may have lived at. This option requires that the PagePathHistory core module is installed, which it now is by default.


### $pages->touch()

This method works very much like the unix "touch" command. Given a $page, it quickly updates that page's modification time (in the database) to now. Or you can specify a second argument with the time that you want it to update it to. That argument may be a unique timestamp or any strtotime() compatible date/time string.

```php
$pages->touch($page); // update mod time to now
$pages->touch($page, '-1 HOUR'); // update mod time to 1 hour ago
```

This is different from $pages->save($page) in that if you only need to update the modification time, it's a lot quicker. In addition, it will always update the modification time, whereas $pages->save() won't if it couldn't identify any changes to the page. This touch() method may also be useful in situations where you are performing large imports or exports and need a simple way to isolate which pages are pending and which are not.


### How to benchmark pages

I've listed some benchmark timers above, and just wanted to explain how we do that. ProcessWire is good about caching pages, so if you don't uncache all the pages in memory before running a benchmark, suddenly everything will load immediately and not even be measurable. That's why it's important to call $pages->uncacheAll(); before running any benchmark that loads pages. Here's a simple example:

```php
$pages->uncacheAll();
$timer = Debug::timer();
$items = $pages->find('id>0'); // 1200 pages
echo "Loaded " . count($items) . " in " . Debug::timer($timer) . " seconds";
```


## New link abstraction features


### Some history

Some of you may remember the old PageLinkAbstractor module that I made back in the earlier days of PW. It would abstract internal links in your HTML/rich-text fields <a href> tags to use the page IDs rather than the page URLs. That ensured that if you migrated a site from a subdirectory to a domain root, the links would still work. It also ensured that if you moved a page or renamed it, the link would continue working.

But there were two problems with PageLinkAbstractor that led me to question it. Abstracting links has significant overhead, loading all linked pages every time a the rich text field is loaded, edited, saved, or output. It also meant that since the <a href> was now pointing to IDs rather than URLs, that markup was pretty much dependent on the PageLinkAbstractor module, making it far less portable.


### Partial solution

PageLinkAbstractor hasn't really been needed for the last couple of years (or so I thought) because the core keeps non-page subdirectories out of URLs in stored markup. And the built in PagePathHistory module takes care of remembering previous URLs that a page may have lived at, ensuring folks always get to the right place (albeit with a 301 redirect).

The benefit of the 301 redirect is that it provides a solution that works whether the page is linked to on-site or off-site. But many would prefer that we had a way of handling this without the involvement of a 301 redirect. Now we do.


### Full solution

Full page link abstraction is now built into the core Textarea field, and it's something you can enable in the HTML options of the field settings. In addition, it's quite an improvement on the PageLinkAbstractor module in that it does it's job with a lot less overhead, and it keeps the markup completely portable. Meaning, if you ever export your field data directly from PhpMyAdmin or ListerPro's CSV export or anything like that, the links in the markup remain in their original form (the linked page ID's are stored in HTML5 valid `data-pwid` attributes).

The new link abstraction feature goes even further in that it supports the option to abstract all URLs for all existing pages. Meaning, it's not one of those things that will only work on "pages saved from this point forward" as it was in PageLinkAbstractor.

There's actually a lot of code behind this link abstraction (I thought it would take a day, and it took a week to code). So consider it very much "beta", like the rest of ProcessWire 3.x, and please let me know if you run into any issues with it.

Hope you all have a great weekend and week ahead and remember to read the [ProcessWire Weekly](http://weekly.pw) this weekend.
