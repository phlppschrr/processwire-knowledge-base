# ProcessWire 2.6 RC1 (2.5.29) and more

Source: https://processwire.com/blog/posts/processwire-2.6-rc1-2.5.29-and-more/

## Sections


## ProcessWire 2.6 RC1 (2.5.29) and more

1 May 2015 by Ryan Cramer [ 14 Comments](/blog/posts/processwire-2.6-rc1-2.5.29-and-more/#comments)


### ProcessWire 2.6 RC1

We just pushed ProcessWire 2.5.29 to the dev branch, and this should be considered the first release candidate (RC1) of ProcessWire 2.6. Ideally this will be our only release candidate and it can be merged to the master branch is 2.6 next week. However, we could use your help with a little bit of last minute testing.

If you've got the bandwidth, please grab ProcessWire 2.5.29, test it out, and let us know how it goes by replying to this post. If everything runs perfectly, we'd love to hear that! Likewise, if you run into some issues, we'd love to hear that too.

- New installations and upgrades of existing sites are of equal interest and please indicate which you tested.
- If an existing site upgrade, please indicate which version you upgraded from.
- If testing with a new installation, please indicate which site profile was used.
- If using multi-language support please indicate that too.
- If you run into any issues, please tell us what PHP version and what other 3rd party modules you have installed.

Thanks for your help testing! If we can get an all-clear with no major issues over the next few days, we'll plan to release early next week.


### What's new this week (ProcessWire 2.5.29)

What's new? Not a lot actually, and that's a good thing. When ready to put out a major release, you don't want to have a lot of change, because all new code needs testing. So the ideal situation is to have the code base just sit for a week without the need for any changes. That's not what happened this week, though it was close.

Last week we introduced some new ways that you can use WireCache (the `$cache` API variable), but there was one part of it that I had wanted to finish and didn't get time to. Specifically, it was support for page selectors in cache expiration. To put it another way, I wanted to be able to tell WireCache this:

Cache this content and consider it valid until a page matching my criteria is saved.

Prior to this week, the only "criteria" that you could specify (beyond dates/times) was a single page template. Meaning, you could make a cache automatically expire once a page using a certain template was saved. That's really useful, but not enough.

Now you literally can specify *any* criteria that can be matched by a single in-memory selector string that matches pages. Specify that selector string as your "expires" argument rather than a date, quantity of seconds, or template.

For example, lets say that you want to generate a cache that expires any time a page having the homepage as its parent is saved… perhaps to cache the markup of primary navigation:

```php
echo $cache->get("topnav", "parent=/", function($pages) {
  foreach($pages->get('/')->children as $item) {
    echo "<li><a href='$item->url'>$item->title</a></li>";
  }
});
```

Something to mention is that in-memory selector strings aren't quite as capable as the more commonly used database-driven selector strings. You don't have things like [OR-groups](/blog/categories/selectors/#or-groups) or [sub-selectors](/blog/categories/selectors/#sub-selectors), among others for example. If you need to do something with this selector string that the in-memory selector isn't allowing, you can always map a database selector to a page selector like this…

```php
$items = $pages->find("company=[locations>5, locations.title%=Finland]"); 
echo $cache->get("cache-name", "id=$items", function() {
  // ...
});
```

…however, hopefully the new built-in selector string support in $cache will serve the vast majority of needs one could have for cache expiration.


### ProcessWire and PHP's interactive mode

You may already be familiar with WireShell, which is a great command-line companion to use with ProcessWire. But did you know that you can use the entire ProcessWire API from the command line without anything more than the core? This is admittedly something very different from WireShell, but can be very handy during development if you want to quickly test out API commands without having to edit, save and then run a PHP script. Here's how to use it:

1. **To get things started, you need to be in a Terminal window at a command prompt. **This can either by on a web server through SSH, or directly on your computer.

2. **Change to the directory where you have ProcessWire installed.** For the site I'm working on now, that's: htdocs/tripsite/ so I type:

```
cd htdocs/tripsite/
```

3. **Now run PHP as an interactive shell:**

```
php -a 
```

The command above will put you in PHP's interactive shell, waiting for your command, which looks like this below:

```
Interactive shell
php > 
```

4. **From here you can do anything that you can in PHP.** Since we're wanting to use ProcessWire's API, we'll go ahead and bootstrap ProcessWire, just by including its index.php file:

```
php > include("index.php");
```

Note that the `php >` is not something that you have to type. That is simply PHP's command prompt that appears on every line in the interactive shell automatically. I'll just leave it out of the remaining examples for brevity.

5. **With ProcessWire bootstrapped, now you can run any PW API commands that you wish.** For instance, lets say that we want to list the titles (one per line) of all pages with the "basic-page" template, sorted by title:

```php
echo $pages->find("template=basic-page")->implode("\n", "title");
```

How about the last 10 modified page URLs with user that modified them:

```php
echo $pages->find("limit=10")->each("{url} mod by {modifiedUser}\n");
```

6. **Commands can span more than one line.** Lets say that we want to add a new "basic-page" beneath the homepage:

```php
$p = $pages->add('basic-page', '/', 'new-page-name');
$p->title = 'My New Page';
$p->save();
```

8. Remember the `__debugInfo()` methods we [implemented a couple weeks back](/blog/posts/processwire-core-updates-2.5.27/#php-5.6-and-debuginfo), that enables you to `print_r()` any PW object? They come in particularly handy in command line mode:

```php
print_r($pages->find("template=basic-page"));
```

Here's the output:

```
PageArray Object
(
  [items] => Array
    (
      [0] => /about/
      [1] => /about/background/
      [2] => /about/updates/
      [3] => /about/analysis/
      [4] => /about/disclaimer/
      [5] => /about/hello-there/
      [6] => /new-page-name/
    )
  [count] => 7
  [total] => 7
  [start] => 0
  [limit] => 0
  [selectors] => template=basic-page, status<1024
)
```

Next you might try doing a `print_r()` on one of those individual Page objects to see what's in it.

```php
print_r($pages->find("template=basic-page")->first());
```

I'll leave the output for you to test on your own.

**This interactive shell isn't anything new**, but I've lately found it very handy during development, so figured I would pass it along for those that didn't already know about it.

**What is new is that you can use ProcessWire's API variables directly in the shell.** For example `$pages` rather than `wire('pages')`. This was added to ProcessWire's index.php file a few dev versions back. If you are using an older version of ProcessWire, you'll still need to use the wire() function to access API variables. If you are using the latest ProcessWire, then make sure your index.php file is up-to-date so that you can access PW's API variables directly.


### What if to doesn't work?

My understanding is that PHP's interactive mode may not always work on Windows systems due to some platform limitations (though someone correct me if I'm wrong), so you may have to limit your usage to your web servers, Linux and OS X machines.

In my OS X environment using MAMP, the `php` command was actually pointing to one that comes with OS X (/usr/bin/php) rather than the one that MAMP installed. I managed to get into the interactive shell, but as soon as I typed `include("index.php");` I'd get a MySQL exception, as OS X's PHP doesn't know about MAMP's MySQL. I got around that by aliasing the `php` command to point to MAMP's PHP rather than mine. If you have a similar need, edit the `.bash_profile` in your home directory (i.e. /Users/your-name/.bash_profile), and add the following to it:

```
alias php="/Applications/MAMP/bin/php/php5.6.2/bin/php"
```

Your MAMP PHP version may be different than mine, so you might want to head on over to that directory first to make sure it lines up with yours. Once you've saved your .bash_profile file, close the terminal window or type `source .bash_profile` in the Terminal window to reload it. Now when you type `php` in the terminal, it should map to MAMP's copy and enable you to use PHP's interactive shell with ProcessWire (or whatever else you'd like).

Lastly, when ready to leave the interactive shell:

```
php > quit
```
