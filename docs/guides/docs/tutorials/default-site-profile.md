# ProcessWire tutorial: intro to default site profile

Source: https://processwire.com/docs/tutorials/default-site-profile/

# Introduction to the default site profile 

Just getting started with ProcessWire and aren't totally clear on what template files are? The good news is that template files aren't anything other than regular HTML or PHP files, and you can use them however you want!

If you know enough to create an HTML or PHP document, then you already know how to use ProcessWire template files. The only difference is that ProcessWire provides your template files with certain variables that you may choose to use, or not use. Most notable is the `$page` variable, which contains all the fields of text or other information contained by the page being viewed.

For instance, `$page->title` contains the text contained in the Title field of the current page, and `$page->body` contains the text for the Body field of the current page. You can choose to output those wherever you want. A really simple template file might look like a regular HTML document except for where you want to output the dynamic portions (like title and body). Here's an example:

```
<html>
  <head>
    <title>
```

That's all that a template file is. But when we're building something for real, we like to save ourselves as much work as possible and avoid writing the same HTML markup in multiple places. In order to do that we'll usually isolate the repetitive markup into separate files or functions so that we don't have to write it more than once. That's not required of course, but it's a good idea to save you time and make it easier to maintain your site further down the road.
- [Beginner / direct output version](#beginner-direct-output-version)
- [Intermediate / delayed output version](#intermediate-delayed-output-version)
- [Multi-language version](#multi-language-version)

### Template file strategies

The default site profile uses a strategy called Delayed Output, but you should use whatever strategy you prefer (or make up your own). The two most popular strategies for template files are:
1. 

[Direct Output](http://processwire.com/to/direct-output/) is the simplest strategy and the one used by the Beginner Default Site Profile (described on the next page). While it doesn't scale as well as other strategies, it is a very good point to start from (and it may be all you ever need). If you've ever worked with WordPress templates, chances are you already know how Direct Output works. If you'd like to get started with this strategy, be sure to install the Beginner Default Site Profile (or the Classic Site Profile also uses this strategy).
2. 

[Delayed Output](http://processwire.com/to/delayed-output/) is the strategy used by the Intermediate Default Site Profile. It is also quite simple but involves populating content to placeholder variables rather than outputting directly. As a result it may take a few more seconds to understand than direct output, but the result can be more scalable and maintainable. By the time you finish reading this tutorial, we think you'll have a good sense of how delayed output works.
3. 

[Markup Regions](/docs/front-end/output/markup-regions/) is the newest supported strategy and for many may also be the easiest to use. It's good to understand the difference between direct and delayed output first, as Markup Regions are kind of a combination of those two. Currently no versions of the “Default” site profile use Markup Regions, but the “Regular” site profile does.

---
[](#)

## Beginner / direct output version

### Why we have different versions of the same site profile

The default site profile comes in 3 different versions: beginner, intermediate, and multi-language. The truth is, they are all equally simple (and all for beginners), but we are anxious to get you working with ProcessWire as quickly and easily as possible, so wanted to show you a couple different ways of doing things. We've found that people just getting started with ProcessWire are more likely to catch on quickly with the beginner version of the default site profile. Not because it's necessarily simpler, but because it uses a strategy similar to what you may have seen elsewhere (like in WordPress).

### How the beginner version of the default site profile works

This beginner version of the default site profile uses the [Direct Output](http://processwire.com/to/direct-output/) strategy. When a page is viewed on your site, here's what happens:
1. 

**The initialization file is loaded:** [_init.php](https://github.com/processwire/site-beginner/blob/main/templates/_init.php)
Here we use it just to define a shared function for navigation.
2. 

**The template file is loaded:** i.e. [basic-page.php](https://github.com/processwire/site-beginner/blob/main/templates/basic-page.php) or another
It outputs the content for the page.

Below are more details on exactly what takes place and in these two steps outlined above:

### 1. The initialization file is loaded (_init.php)

This step is completely optional with direct output, but we find it handy to use this file to define our shared functions (if any). In the case of this profile, we define a single `renderNavTree()` function. It is useful to have this as a re-usable function since we use it to generate markup for more than one place (specifically, for sidebar navigation and for the sitemap). However, **if you have any confusion about this, ignore it for now** and focus on #2 below, as an initialization file is completely optional.

### 2. The template file is loaded (i.e. basic-page.php or another)

Next, ProcessWire loads the template file used by the page being viewed. For example, most pages here use [basic-page.php](https://github.com/processwire/site-beginner/blob/main/templates/basic-page.php).

The first thing that our template file does is include the HTML header markup, which we've put in a file called [_head.php](https://github.com/processwire/site-beginner/blob/main/templates/_head.php):

```
include("./_head.php");
```

The above is simply a PHP function that says "include this file". The leading "./" just means "from the current directory". We also have an underscore "_" prepended to our filename here as a way to identify this as an include file rather than a regular template file. While completely optional, the underscore does also make ProcessWire ignore it when looking for new template files. As a result, you may find it handy to use this convention in your own include files. An alternate would be to use .inc as an extension rather than .php.

Have a look in the [_head.php](https://github.com/processwire/site-beginner/blob/main/templates/_head.php) file now so you can see what's there. It is basically half of an HTML file. Now have a look in [_foot.php](https://github.com/processwire/site-beginner/blob/main/templates/_foot.php), that's the other half. Notice that all the template files that include _head.php at the beginning also include _foot.php at the ending. This is to ensure there is a complete HTML document being output.

This all means that our template files (using direct output) are focused on outputting what goes in-between the [_head.php](https://github.com/processwire/site-beginner/blob/main/templates/_head.php) and [_foot.php](https://github.com/processwire/site-beginner/blob/main/templates/_foot.php). In our case, this is a `<div id='content'>...</div>` and optionally a `<div id='sidebar'>...</div>`. But for your own template files you might choose to output something completely different.

### Files in the beginner default profile

Here is a summary of what is in each of the files in the /site/templates/ directory of the beginner default site profile. We also recommend reviewing them in this order:
- [_head.php](https://github.com/processwire/site-beginner/blob/main/templates/_head.php) - HTML header (top half of HTML document)
- [_foot.php](https://github.com/processwire/site-beginner/blob/main/templates/_foot.php) - HTML footer (bottom half of HTML document)
- [basic-page.php](https://github.com/processwire/site-beginner/blob/main/templates/basic-page.php) - Template file outputting #content and #sidebar columns. This template file is used by most pages in this small site.
- [home.php](https://github.com/processwire/site-beginner/blob/main/templates/home.php) - Template file used by homepage. Note that since the homepage uses nearly the same layout as the other pages in the site, this template file simply includes basic-page.php. No need two have more than one template file with the same contents.
- [sitemap.php](https://github.com/processwire/site-beginner/blob/main/templates/sitemap.php) - Outputs a sitemap of the entire site.
- [search.php](https://github.com/processwire/site-beginner/blob/main/templates/search.php) - Outputs results of site search queries.
- [_init.php](https://github.com/processwire/site-beginner/blob/main/templates/_init.php) - Initialization file that we use to define a shared function for generating navigation markup.

---
[](#)

## Intermediate / delayed output version

### How this differs from the beginner version

The intermediate version of the default site profile is identical in function to the beginner version, except that it uses a different output strategy. Rather than splitting the markup into [_head.php](https://github.com/processwire/site-beginner/blob/main/templates/_head.php) and [_foot.php](https://github.com/processwire/site-beginner/blob/main/templates/_foot.php) files, all the markup is instead contained in a [_main.php](https://github.com/processwire/site-default/blob/main/templates/_main.php) file, which represents an entire HTML document.

In the beginner version, the template files focused on outputting what went in between [_head.php](https://github.com/processwire/site-beginner/blob/main/templates/_head.php) and [_foot.php](https://github.com/processwire/site-beginner/blob/main/templates/_foot.php). In the intermediate version, the template files instead focus on populating placeholders that will be output by the [_main.php](https://github.com/processwire/site-default/blob/main/templates/_main.php) file.

### How the intermediate version of the default site profile works

The intermediate default site profile uses the Delayed Output strategy mentioned on the first page. Here's how it works:
1. 

**The initialization file is loaded: **[_init.php](https://github.com/processwire/site-default/blob/main/templates/_init.php)
We use it to define placeholder variables for content regions.
2. 

**The template file is loaded**: i.e. [home.php](https://github.com/processwire/site-default/blob/main/templates/home.php) or another
We use it to populate values into the placeholder variables.
3. 

**The main output file is loaded: **[_main.php](https://github.com/processwire/site-default/blob/main/templates/_main.php)
It is an HTML document that outputs the placeholder variables.

Below are more details on exactly what takes place and in the three steps outlined above:

### 1. The initialization file is loaded (_init.php)

We define placeholder variables for the regions in our page in the _init.php file. These placeholders can be anything that you like (and in any quantity) and usually depends entirely on the needs of your site design and content.

In this default site, our needs are simple so we've defined placeholders for just 3 regions on the page. We usually name these regions something consistent with the HTML tag, id or class attribute just for ease of readability, but that's not required. These are the three placeholder variables we've defined in this site:
- **$title **- The headline or title (we use for `<title>` and `<h1>`)
- **$content** - The main page content (we use for `<div id='content'>`)
- **$sidebar **- Sidebar content (we use for `<div id='sidebar'>`)

The leading "**$**" is what designates them as placeholder variables. We do this in a file called _init.php. ProcessWire knows to load this _init.php file first, before our actual template file. We define these placeholder variables simply giving each a default value, or by just making them blank. Go ahead and take a look at the [_init.php](https://github.com/processwire/site-default/blob/main/templates/_init.php) file now if you can. But to summarize, here's how you define a blank placeholder variable:

```
$content = '';
```

And here's how you define a placeholder variable with an initial/default value:

```
$content = "<p>Hello World</p>"; // assign static value…
$content = $page->body; // …or assign dynamic value from $page
```

The last thing we want to mention about _init.php is that we might also use it to load any shared functions. You'll see a line in this site's _init.php the includes a file called _func.php. That file simply contains a shared function (used by multiple template files) for generating navigation markup. This part is not so important for now, so come back to it once you understand how everything else works. But the point to understand now is that the _init.php file initializes everything that may be used by the site's template files.

### 2. The template file is loaded (i.e. home.php or another)

Next, ProcessWire loads the template file used by the page being viewed. For example, the homepage uses home.php. We use our template file to populate those placeholder variables we defined in _init.php with the values we want.

For instance, most often we populate our `$content` variable with the body copy from the current page:

```
$content = $page->body;
```

But we might also do something more like append some navigation under the body copy or prepend a photo... the sky is the limit.

```
$content = "<img src='/photo.jpg'>" . $page->body;
```

Our [search.php](https://github.com/processwire/site-default/blob/main/templates/search.php) template file for example, populates `$content` with a list of search results.

Because our placeholder variables were already defined in the _init.php file with default values, our template file (like home.php or basic-page.php) need only focus on populating the placeholder variables that you want to modify. It does not even need to mention those placeholder variables that it doesn't need or doesn't need to change.

### 3. Everything gets output by _main.php

After ProcessWire has loaded our template file (i.e. home.php) it then knows to load the [_main.php](https://github.com/processwire/site-default/blob/main/templates/_main.php) file last. In the case of this site, our _main.php file is an entire HTML document that outputs our placeholder variables in the regions where they should appear. For example, the `$content` variable gets output in #content `<div>` like this:

```
<div id='content'>
```

Please go ahead and take a look at the [_main.php](https://github.com/processwire/site-default/blob/main/templates/_main.php) file for context.

Note that our _main.php uses `<?php echo $content; ?>` style PHP syntax, rather than `<?= $content ?>` syntax (as shown above), just in case you happen to be running an older version of PHP. But more than likely you can use the shorter syntax when preferred, as the two are functionally equivalent. We find the shorter syntax preferable unless there's a chance the site will have to run on an older PHP version.

### Benefits of this delayed output strategy

An obvious benefit to this approach is that our template files can more easily populate output for any regions on a page, rather than just what goes in between _head.php and _foot.php (as in the beginner edition). Furthermore, there are no limits to the number of regions you can choose to setup, and your template files can focus only on the regions that you want them to affect.

Delayed output also tends to lend itself better to scale and change. That's because the individual template files don't need to know where everything goes… that's the job of just one file: [_main.php](https://github.com/processwire/site-default/blob/main/templates/_main.php). In fact, those template files don't need to mention anything other than the regions they want to modify. Like mentioned in the previous point, adding a new region to your layout doesn't mean you have to go change all your template files… just the ones that need to affect that new region differently.

Another benefit of delaying output in this manner means that we can make changes to our placeholders along the way. Nothing is set in stone till our main output file (_main.php) takes over.

For example, lets say that one of the things we need to populate is the `<title>` tag in the document header. In the beginner edition, this lives in the _head.php file and it outputs the page title before we've output our main content. That's fine, but lets say that something about our main content affects the page title. Maybe we're using pagination (like this page you are reading now) or maybe it generates some kind of search results, and we want that to be reflected in the <title> tag… We might like it to say "Products 1-10 of 70" somewhere in the <title> tag. If we were using direct output–as in the beginner profile–it would be too late, because our <title> had already been output by the time we got around to retrieving search results and outputting them in the body copy region. To put it simply, delaying output gives you more control over what the final output will be since nothing is final till the end.

---
[](#)

## Multi-language version

The multi-language version of the default site profile is in fact identical to the intermediate default site profile except for a few minor things:

In any given site, there is going to be some static text for things like buttons, auto-generated headlines and such. We can make these translatable by surrounding that text in a `__('your text here')` function. Once you've done that, you can translate that text per-language in ProcessWire's admin (Setup > Languages), and output values will be automatically changed depending on the language. There are also a couple of other variations on this function, used for certain situations. Here's an example of them all:

```
php// This makes 'text' translatable  
__('text');

// Same as above, but with a specific context
// useful if the same term appears in multiple places
_x('text', 'context');

// For when we need singular and plural translation
_n('singular', 'plural', $count);
```

For more about making your static text translatable see our documentation on [code internationalization](/docs/multi-language-support/code-i18n/).

The only other thing different about the multi-language default site profile is that it contains some additional code in the _main.php file for navigation that lets you view the page in each language. You'll see this near the top of the _main.php file.
- [Tutorials](/docs/tutorials/)
- [A Beginner’s Guide To ProcessWire](https://www.smashingmagazine.com/2016/07/the-aesthetic-of-non-opinionated-content-management-a-beginners-guide-to-processwire/)
- [How to install and setup ProcessWire CMS](https://webdesign.tutsplus.com/tutorials/how-to-install-and-setup-processwire-cms--cms-25509)
- [Hello Worlds](/docs/tutorials/hello-worlds/)
- [How to Create an AJAX Driven Theme for ProcessWire](https://webdesign.tutsplus.com/tutorials/how-to-create-an-ajax-driven-theme-for-processwire--cms-26579)
- [A Beginner’s Introduction to Writing Modules in ProcessWire](https://webdesign.tutsplus.com/tutorials/a-beginners-introduction-to-writing-modules-in-processwire--cms-26862)
- [Extending the ProcessWire Admin Using Custom Modules](https://webdesign.tutsplus.com/tutorials/extending-the-processwire-admin-using-custom-modules--cms-26863)
- [How to Develop a Processwire Theme](https://webdesign.tutsplus.com/tutorials/how-to-develop-a-processwire-theme--cms-25692)
- [Default site profile](/docs/tutorials/default-site-profile/)
- [How to structure your template files](/docs/tutorials/how-to-structure-your-template-files/)
- [Using custom page types in ProcessWire](/docs/tutorials/using-custom-page-types-in-processwire/)
- [More tutorials](https://www.pwtuts.com)

- [Docs](/docs/)
- [API reference](/api/ref/)
- [Getting started](/docs/start/)
- [Front-end](/docs/front-end/)
- [Tutorials](/docs/tutorials/)
- [Selectors](/docs/selectors/)
- [Modules & hooks](/docs/modules/)
- [Fields, types, input](/docs/fields/)
- [Access control](/docs/user-access/)
- [Security](/docs/security/)
- [Multi-language](/docs/multi-language-support/)
- [More topics](/docs/more/)
