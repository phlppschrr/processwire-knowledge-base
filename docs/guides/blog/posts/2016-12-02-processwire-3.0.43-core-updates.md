# ProcessWire 3.0.43 core updates

Source: https://processwire.com/blog/posts/processwire-3.0.43-core-updates/

## Sections


## ProcessWire 3.0.43 core updates

2 December 2016 by Ryan Cramer [ 2 Comments](/blog/posts/processwire-3.0.43-core-updates/#comments)


## ProcessWire 3.0.43


### Core updates

This new core version of ProcessWire focuses on resolving several issue reports and integrating pull requests. It also adds some nice upgrades that we'll cover in more detail below. First, here's a list of all that's new in 3.0.43 dev relative to 3.0.42 master:


### Upgrades to the $page->url() method

The $page->url() method (and property) is probably one of the most used API calls in ProcessWire. Its never done anything other than simply return the URL to the page, so its always been very singular in purpose. In seeing some recent code examples from others (including last weeks ProcessWire Weekly recipe) I realized that this method could really benefit from some more options available… things that could really save developers a lot of time.

ProcessWire 3.0.43 adds a single `$options` argument to the `$page->url()` method that enables you to specify a lot of different add-ons for the returned url, like this:

```
$options = [ ... ]; // Array
echo $page->url($options);
```

Here's a look at all of the possible `$options` as an associative array:

I'm guessing that often you'll only need a single option at once, so the method includes several shortcuts that assume a particular option:

**If you specify an integer** for options it is assumed to be the pageNum option:

```
echo $page->url(3); // output: /example/page3
```

**If you specify “+” or “-”** for options it is assumed to be the “pageNum” next/previous pagination option. Lets assume we are on pageNum 4 for the example below:

```
echo $page->url('+'); // output: /example/page5
echo $page->url('-'); // output: /example/page3
```

**If you specify any other string** for options it is assumed to be the urlSegmentStr option. Note that the url() method is doing more here than just appending URL segments–it's also sanitizing those segments consistent with page name format.

```
echo $page->url('foo/bar'); // output: /example/foo/bar/
```

**If you specify a boolean (true)** for options it is assumed to be the http option. This would be the same as using the $page->httpUrl() method:

```
echo $page->url(true); // output: http://domain.com/example/
```

**You can of course specify multiple options too**, by using an associative array for the options argument. For example:

```
echo $page->url([
  'http' => true,
  'pageNum' => 3,
  'urlSegmentStr' => 'foo',
  'data' => [ 'bar' => 'baz' ]
]);
// output: http://domain.com/example/foo/page3?bar=baz
```


### Why not just add URL segments, page numbers and query strings yourself?

As you can see there is a lot of focus on handling page numbers and URL segments in the url() method options. Prior to today, if you needed to add URL segments or page numbers to URLs, you did it manually by appending them to the URL. The trouble is that there are a lot of configurable options around how exactly those should work, such as:

Those are a lot of factors to consider. That's why I thought we really needed something in the core `$page->url()` method to handle that logic, rather than expecting one to consider all of those things when using URL segments or pagination.

Then there are query strings, like `?process=wire&is=fun`. If these are being appended to a URL, then the query string keys and values should be URL encoded. If the URL is being used in output (like in an `<a href>` tag) then the query string should also be entity encoded. The `$page->url()` method takes care of these details for you. Note that while URL encoding is always active, the query string is only entity encoded if the page's output formatting state is ON (which is the front-end default).

*Note: Our online API reference will show documentation for these updates shortly as well. Users of ProDevTools [API Explorer](/api/modules/api-explorer/) **can also see the documentation when running it with ProcessWire 3.0.43+. *


### New FileCompiler options

These are relatively minor, but may be useful to some of you using ProcessWire 3.x with template compilation enabled. It may also be useful to module developers that are developing modules without using a namespace (to maintain PW 2.x compatibility).

There are some instances where you may want to prevent the *FileCompiler* from compiling something. ProcessWire lets you exclude entire files from compilation by adding a `/*FileCompiler=0*/` comment anywhere in it. However, there have been requests for an additional option to exclude file(s) from compilation before they are even included. Basically, a way to prevent the *FileCompiler* from even looking at the file, or anything else it loads. This is particularly useful for 3rd party library files.

You can now add a `/*NoCompile*/` comment within the `include()` statement, and *FileCompiler* will leave the file alone. For instance, lets say you had this include() statement:

```
include(__DIR__ . '/library/file.php');
```

Just add the `/*NoCompile*/` comment, either at the front or back of it, within the parenthesis:

```
include(/*NoCompile*/ __DIR__ . '/library/file.php'); // do this…
include(__DIR__ . '/library/file.php' /*NoCompile*/ ); // …or this
```

We are using include() as an example here, but this also of course works with `include_once()`, `require()` and `require_once()`.

**What about autoloaded classes?** The *FileCompiler* doesn't get involved with those either way, so *FileCompiler* is really only applicable to files loaded directly by PW, from template files, modules, and any files manually included from them. The new NoCompile comment now gives you control over how those manual include statements are handled.


### How to tell if output from a file is compiled?

Most of you can probably skip this section. But if the headline above reminded you that you've run into this question before, read on…

It's really difficult to tell if output from a file is compiled. That's because part of compilation involves a trick that makes the compiled file think it's in the source location, ensuring that it behaves the same way. You can't simply output something like PHP's [__FILE__](http://php.net/manual/en/language.constants.predefined.php) constant, or the [getcwd()](http://php.net/manual/en/function.getcwd.php) function, because they will both report the file to be in the source location, even if it's actually a compiled copy running elsewhere.

If you have a need to tell if a file is compiled or not, you can now do so by adding `FileCompiler=?` somewhere in the file. For example:

```
echo "FileCompiler=?";
```

If the file is compiled, the output will change to `FileCompiler=Yes`. If the file is not compiled, it will remain untouched as `FileCompiler=?`. Chances are you won't ever need this, but I mention it here in case it's helpful to module developers during development, or anyone else that's ever come across the need, like I have.


### ProcessWire recipe revisited

Last week the [ProcessWire Weekly #133](https://weekly.pw/issue/133/) had a recipe that showed you how to use `<link>` tags for pagination with `rel=next` and `rel=prev` attributes as a technique helpful to search engines. This recipe originated from the great [ProcessWire Recipes](https://processwire-recipes.com/recipes/enhance-paginator-with-rel-attr-for-seo/) site. Seeing the cryptic nature of the URL generation and situations where it would break was part of the motivation behind upgrading the `$page->url()` method as discussed earlier in this post. It wasn't a problem with the recipe, rather the issue was that ProcessWire didn't provide an easy core method for making a pagination URL. With that in mind, let's revisit that recipe to make it a little simpler by using today's updates.

First things first, when doing something like this I prefer using [delayed output](/to/delayed-output/) rather than [direct output](/to/direct-output/). That's because you are needing to insert `<link>` tags in the document `<head>` that contain data generated from a page finding call that produces output somewhere in the `<body>`. Meaning, you need to know what's in the `<body>` before you can generate the `<head>`. Delayed output makes this a little simpler because everything is generated ahead of time, with all the regions output by a _main.php file (or whatever you decide to name it) at the end.

Lets start with our template file that is generating the paginated items, we'll call it products.php. Since we're using delayed output, I'll use our recently added `region()` function to hold output. If you don't have the functions API enabled, you can `wireRegion()` instead.

```php
<?php namespace ProcessWire;

// get items to paginate
$items = $page->children("limit=12");
$paginations = ceil($items->getTotal() / $items->getLimit());

if($input->pageNum > 1) {
  $url = $page->url('-'); // prev pagination URL
  region("head+", "<link rel=prev href=$url>");
}

if($input->pageNum < $paginations) {
  $url = $page->url('+'); // next pagination URL
  region("head+", "<link rel=next href=$url>");
}

// list the items to appear in <body>
foreach($items as $item) {
  region("body+", "<p><a href=$item->url>$item->title</a></p>");
}

// append pagination links
region("body+", $items->renderPager());
```

Next, our _main.php file outputs those regions we generated above. I'm leaving out everything except what's applicable, just to keep it simple:

```php
<?php namespace ProcessWire; ?>
<html>
  <head>
    <?=region('head')?>
  </head>
  <body>
    <?=region('body')?>
  </body>
</html>
```

That's it for today. Hope you all had a great week, and have a great weekend! See you at the [ProcessWire Weekly](http://weekly.pw) tomorrow.
