# ProcessWire core updates (2.5.28)

Source: https://processwire.com/blog/posts/processwire-core-updates-2.5.28/

## Sections


## ProcessWire core updates (2.5.28)

24 April 2015 by Ryan Cramer [ 5 Comments](/blog/posts/processwire-core-updates-2.5.28/#comments)


### ProcessWire 2.6 coming as soon as next week

The dev branch has been very stable for quite some time now, and no signs of any deal breaking issues have shown up. As a result, I think we are ready to release ProcessWire 2.6, as soon as next week.

We've intentionally tried not to get into any major core changes this week so as to avoid introducing anything new that would require more days of testing. Outside of those items added this week, consider ProcessWire dev now in a feature freeze, with the plan being to convert the dev branch to the new master branch (and tag it as ProcessWire 2.6) as soon as next week. Your help testing is greatly appreciated. I think the changelog is going to take a good week just to put together, there is so much in this release. Thanks to all of you this will be our best ProcessWire release yet!


### WireCache upgrades

The `$cache` API variable (WireCache) is still a relative newcomer to ProcessWire's core, but it continues to get more and more capable. If you have used MarkupCache in the past, you will likely want to consider using WireCache instead, as it can do quite a lot more. Further, it's always available to you (accessible via `$cache`). Getting and saving caches is quite a simple matter:

```
$content = $cache->get("hello-world");
if(!$content) {
  $content = "<p>Hello World</p>";
  $cache->save('hello-world', $content);
}
echo $content;
```

That's just a really basic example. There would be little point in caching a short "hello world" string like that, other than for demonstration purposes. You'd instead use `$cache` for caching things like the markup behind a large block navigation with dropdowns, a sitemap, or other things that might take significant time to generate. Be sure to see the [WireCache class](https://github.com/ryancramerdesign/ProcessWire/blob/dev/wire/core/WireCache.php) for detailed documentation (inline phpdoc) on all that you can do with it.

This week we expanded the capabilities of it quite a bit further…


### Combined get and save of cache

Now you can specify a function to generate your cache, and the function will only be used when the cache needs to be re-generated. Here's the same example as above, but with the function included:

```
echo $cache->get("hello-world", function() {
  return "<p>Hello World</p>";
});
```

Notice how the function simply returned the value. If you prefer it, the function can instead just echo the value as if it were output. It will still get cached in the same manner:

```
echo $cache->get("hello-world", function() {
  echo "<p>Hello World</p>";
});
```

Whether you return or echo the content to cache matters little, as the result is the same.

Lets say that you wanted your function to have access to the `$pages` API variable (and/or some other API variables). You simply specify them with your function definition and ProcessWire will make sure your function has them locally scoped. It does not matter what API variables you use or what order, or even if they are in scope outside of the function. Of course, you could also just use `wire('pages')` instead in your function, but we like to give you choices. Here's a simple example below.

```php
echo $cache->get("top-navigation", function($pages) {
  foreach($pages->get('/')->children) as $item) {
    echo "<li><a href='$item->url'>$item->title</a>";
  }
});
```

To reiterate, the block of code in that function() above only gets executed if the cache has expired or otherwise needs to be re-generated.

By default a cache lasts for one day. If you want to specify an expiration lifetime (in seconds) or an expiration date, relative date string, page template, or one of the [expire constants](https://github.com/ryancramerdesign/ProcessWire/blob/dev/wire/core/WireCache.php#L19) , you can do so like this:

```
echo $cache->get("hello-world", 3600, function() {
  echo "<p>Hello World</p>";
});
```

Note the 3600 above– We are saying "allow this cache to live for 3600 seconds", which amounts of exactly one hour.

Not specific to ProcessWire per se, but in PHP if you want to pass variables from outside the function scope into a function like this, then you pass with them with `use($var)` directive with the function definition:

```
$hello = "Hello World";
echo $cache->get("hello-world", function() use($hello) {
  echo "<p>$hello</p>";
});
```


### Now you can cache PageArray objects too

WireCache has always let you cache any text, markup or array that you want to. (The ProcessWire core uses `$cache` to cache arrays of module information quite extensively.) Now you can also cache PageArray objects.

Lets say that you have a rather complex` $pages->find()` query that takes 300ms to complete and you'd like it to only have to perform that find() not more than once every 10 minutes. Simply cache the results:

```php
$products = $cache->get("new-products", "+10 minutes", function($pages) {
  return $pages->find("template=product, sort=-created, limit=100");
});
```

Not that the above find() is a good example of something you'd need to cache, but you get the point. Something to note is that it's the PageArray that gets cached, which in turn means it's the find() query in the example above that gets cached. The individual pages that are part of the $products are still loaded as usual. Even if you'd changed one of those pages 5 minutes ago, your change would still be reflected in the pages that are returned. But if you'd created the page 5 minutes ago, then it would not be included, because it didn't exist at the time the cache was generated. So let's say that you wanted it included? You can specify a template as for the $expires argument:

```php
$template = $templates->get("product"); 
$products = $cache->get("new-products", $template, function($pages) {
  return $pages->find("template=product, sort=-created, limit=100");
});
```

The above tells `$cache` to expire the the "new-products" cache every time a page that uses the template "product" is saved. If you don't save a product page for several days, it'll continue using the same cache.


### Load all caches that match a wildcard

The last new addition to mention for `$cache` is that you can now specify wildcards in the cache name that you retrieve. If you wanted to retrieve all caches that began with the word "navigation" then you would do the following:

```
$all_nav = $cache->get("navigation*");
```

Following the above call, the `$all_nav` variable is an array that contains all caches that start with "navigation", and it indexes them by the cache name, i.e.

```
array(
  'navigation-top' => '<ul id="topnav"> ... </ul>',
  'navigation-foot' => '<ul id="footnav"> ... </ul>',
  'navigation-side' => '<div id="sidenav"> ... </div>'
)
```


### System Notifications Updates

ProcessWire's core SystemNotifications module was updated this week to support notifications that alert you when editing a page that is already open by another user, or when editing a page that you already have open in another window or tab. The aim here is to prevent accidental edit conflicts of one person or window overwriting another.

When a conflict is detected, it notifies both users (or windows) immediately, even if they may be in the middle of an edit. However, it does not interfere with the users ability to complete their edit; rather it is there to make them aware of the conflict. This feature can be enabled or disabled on the SystemNotifications module settings (Modules > Core > System > Notifications).

*Get ready for ProcessWire 2.6!*
