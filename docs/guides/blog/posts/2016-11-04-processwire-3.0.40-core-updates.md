# ProcessWire 3.0.40 core and more

Source: https://processwire.com/blog/posts/processwire-3.0.40-core-updates/

## Sections


## ProcessWire 3.0.40 core and more

4 November 2016 by Ryan Cramer [ 7 Comments](/blog/posts/processwire-3.0.40-core-updates/#comments)


## Core updates


### New master and dev versions

This week version 3.0.39 (introduced last week) became our new master version, and 3.0.40 became our new dev version. For more on what's new between 3.0.39 and the previous master version (3.0.36) be sure to see the [last 3 weeks of blog posts](/blog/posts/). Version 2.8.39 legacy will be appearing shortly as well.

Version 3.0.40 now on the dev branch focuses primarily on resolving submitted issue reports and integrating pull requests.


### Pull requests

This week we merged the following pull requests:

- A couple of code optimizations submitted by [pine3ree](https://github.com/pine3ree).
- New configuration option for image fields that enables swapping the configured min/max dimensions for portrait image, submitted by [LostKobrakai](https://github.com/LostKobrakai).
- New honeypot option for comments fields submitted by [iamwebrocker](https://github.com/iamwebrocker).
- Fix for an Firefox display issue in our "add page" function, submitted by [gmclelland](https://github.com/gmclelland).

In addition to the above, 3.0.40 contains numerous minor bug fixes, documentation updates, code cleanup, optimizations and more. See the full [dev commit log](https://github.com/processwire/processwire/commits/dev) for October 30–November 4 for full details.


## More on the Functions API

Last week we introduced the new [Functions API](/blog/posts/processwire-3.0.39-core-updates/#new-functions-api) to you and told you about all the API functions that bear the same name as the API variable counterparts. What we didn't tell you last week is that the Functions API also includes some useful shortcuts as well, which some of you may have spotted in the new Skyscrapers templates. We'll cover those in more detail here.

Note that all of these require the `$config->useFunctionsAPI = true;` setting in your /site/config.php file. If not enabled, then they can still be accessed by prepending the word "wire" to the function calls, i.e. `wireUrls()` rather than `urls()`, but we'd recommend you enable the Functions API if planning to use it. For more about why/when you might use the Functions API vs. the API variables, be sure to see last week's [post](/blog/posts/processwire-3.0.38-core-updates/).


### urls() and paths()

These functions are shortcuts for the `$config->urls` and `$config->paths` properties. They can be called with no arguments, or they can be given an argument of the url (or path) you want to retrieve. To demonstrate, all of the following are equivalent:

```
echo $config->urls->templates;
echo config()->urls->templates;
echo config('urls')->templates;
echo urls()->templates; // shortcut version
echo urls('templates'); // shortcut version
```

I find this shortcut handy when outputting things like `<link>` or `<script>` tags:

```
<link rel='stylesheet' href='<?=urls('templates')?>styles/main.css'>
```


### inputGet(), inputPost() and inputCookie()

These shortcut functions are equivalent to `$input->get`, `$input->post` and `$input->cookie`, providing access to GET, POST and COOKIE input variables. To demonstrate, all of the following are equivalent:

```
$foo = $input->get->foo;
$foo = $input->get('foo');
$foo = inputGet('foo'); // shortcut version

$bar = $input->post->bar;
$bar = $input->post('bar');
$bar = inputPost('bar'); // shortcut version
```

If you want the returned value to be already sanitized, specify the name of a [$sanitizer](../../../full/wire/core/Sanitizer/index.md) as the second argument:

```
$username = inputPost('username', 'alphanumeric');
```


## Tips and tricks


### Getting one field or another from a Page

Many of you reading this may already be familiar with this type of syntax in a [$page](../../../full/wire/core/Page/index.md) API call:

```
$title = $page->get('headline|title');
```

In English, it means "get headline if it's populated, otherwise get title". It can be extended further with as many OR conditions as you want. Here's how you might use it:

```
echo "<h1>" . $page->get('headline|title') . "</h1>";
echo "<p>" . $page->get('date|intro|summary') . "</p>";
```

As of ProcessWire 3.0.39 (master) you can also do this:

```
echo "<h1>$page->headline_OR_title</h1>";
echo "<p>$page->date_OR_intro_OR_summary</p>";
```

Basically, you can use `_OR_` splitting your field names, rather than `|`. The _OR_ contains all characters that are allowed in PHP variables, whereas the pipe "|" is not. Being able to express this as a variable has a couple of benefits:

- It can be placed right in a string with no need to break in and out of the string like in the first example.
- The "OR" syntax may be more readable to some.

I just wanted to let you know of this new option, but of course use whatever syntax is simplest for your need.


### Recipe: implementing an “unknown” fallback

Often times when outputting content for a page you'll need to check if a value is populated before outputting it. That can sometimes result in a mess of `if()` statements or difficult to read ternary statements. For example:

```php
<dt>Width</dt>
<dd><?php
  if($page->width) {
    echo $page->width;
  } else {
    echo "Not available";
  }
?></dd>

<dt>Height</dt>
<dd><?php
  if($page->height) {
    echo $page->height;
  } else {
    echo "Not available";
  }
?></dd>
```

Of course, you can get fancier by using the ternary operator, but this sacrifices some code readability, and still results in label duplication. Nevertheless, the following is logically identical to the above:

```
<dt>Width</dt>
<dd><?= $page->width ? $page->width : "Not available"; ?></dd>

<dt>Height</dt>
<dd><?= $page->height ? $page->height : "Not available"; ?></dd>
```

One solution we've found more useful is to define your default fallback value/text once, and then make use of "|" OR calls like mentioned in the previous section. First you define what you want your default/fallback value to be. This could be placed anywhere, perhaps in an _init.php file. We'll use the word "unknown" as the name for our fallback value. Of course, you could use anything here, but you'd just want to make sure it doesn't conflict with an existing field name.

```
$page->set('unknown', 'Not available');
```

Now when you are outputting any text or number value, you have the choice of using that "unknown" fallback, which ProcessWire will automatically pull when your first requested value isn't present:

```
<dt>Width</dt>
<dd><?=$page->get('width|unknown')?></dd>

<dt>Height</dt>
<dd><?=$page->height_OR_unknown?></dd>
```

Note the Height section above also demonstrates the alternate OR syntax introduced earlier in this post.

If the "width" or "height" properties are empty on the page, it will just output "Not available" rather than blank or zero. While this is a somewhat contrived and simple example, it becomes more useful the larger the set of data and need for fallbacks you have. This is the same technique we use in the new Skyscrapers demo site template files ([see here](https://github.com/ryancramerdesign/skyscrapers2/blob/master/_func.php#L196)).

It's worth noting that this would work equally well substituting default fallbacks for any type of field. You aren't just limited to doing this with text or numbers. You could do it with images, pages or any other kind of field type.

That's it for this week! Hope that you all have a great weekend and enjoy reading the [ProcessWire Weekly](https://weekly.pw).
