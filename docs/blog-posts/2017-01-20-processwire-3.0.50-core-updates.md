# ProcessWire 3.0.50 core updates

Source: https://processwire.com/blog/posts/processwire-3.0.50-core-updates/

## Sections


## ProcessWire 3.0.50 core updates

20 January 2017 by Ryan Cramer [ 8 Comments](/blog/posts/processwire-3.0.50-core-updates/#comments)


## ProcessWire 3.0.50

This week's version of ProcessWire expands upon our markup regions support introduced last week, and also contains various minor fixes and tweaks. In addition, it adds a `$urls` API variable which is simply a shortcut to `$config->urls`. But since this is so commonly called upon, the shortcut can be useful in reducing verbosity in some template files. Meaning, if you want the URL to /site/templates/, you can now use the shorter `$urls->templates` rather than `$config->urls->templates`, if you'd like. This also adds consistency with our recently introduced `urls()` function that's part of the optional Functions API.


### More on markup regions

Last week we introduced markup regions, and had lots of good feedback. One of the most common requests was the ability to use attributes beyond "id" and "class". We thought that "id" and "class" were good ways to introduce markup regions, because it's so familiar to everyone. But we don't want to limit it to that either. Markup regions are designed to work with the existing markup that you already write, reducing verbosity. So the intention is not to make you write new markup or change how you write markup, but just to work on top of what you already write. This week we expanded that to include custom attributes as an alternative to what was introduced last week, and we found this can work quite nicely.

To start off with, you can use "pw-id" (or "data-pw-id") as an alternative to "id" attributes if you'd prefer. Markup regions don't care which of the id attributes you use, as they all refer to the same thing.

```
html<div id="content"><p>Hello</p></div
<div pw-id="content"><p>Hello</p></div>
<div data-pw-id="content"><p>Hello</p></div>
```

Next, you can now use attributes rather than classes for the "placement" component of a markup region, if you'd like. And we think this actually is a little nicer than using classes.

```
html<p pw-append="content">This paragraph would append to #content</p>
```

A placement attribute can be specified as "pw-append" or "data-pw-append" if you prefer a data attribute. The supported placement attributes are:

- pw-append
- pw-prepend
- pw-before
- pw-after
- pw-replace
- pw-remove

The value portion of a placement attribute would be the "id" (or "pw-id") of the element you want it to work with.

```
html<figure pw-prepend="sidebar">
  <img src="file.jpg">
  <caption>This figure would prepend to sidebar</caption>
</figure>
```

The following would add a ul.breadcrumbs before #content:

```
html<ul class="breadcrumbs" pw-before="content">
  <?=$page->parents->each("<li><a href='{url}'>{title}</a></li>")?>
</ul>
```

As you can see, these new placement attributes can be quite handy and I think are more clear than the placement classes (introduced last week) in many cases. But in the end, use what you prefer.


### Should you use markup regions?

If you already have an output strategy that works well for you, there's no reason to switch to markup regions for an existing project. But for a new project, if you like what you see so far, they are definitely worth considering. They open up some new capabilities that you couldn't previously accomplish without updating code in multiple files.

If used correctly, markup regions can also add more clarity to your template files, making it simpler for others to understand, while reducing the amount of code necessary to accomplish something. This is why we'll be using markup regions in our next new site profile. This increased clarity and reduced verbosity provided by markup regions will help us to better communicate development in ProcessWire template files to others.

We imagine markup regions will appeal more to those that had been using direct output in the past, than those that had already been using delayed output. If your workflow already involves concatenating variables or making `region()` calls combined with delayed output, and you are happy doing that, then there's no reason not to stick with it. That's a tried and true output strategy that works great. Though you might enjoy exploring markup regions on a future personal project just to see what's possible.

On the other hand, if you are currently using direct output, we think you might find markup regions immediately very compelling. They give you the benefits of delayed output while letting you continue to code in much the same way you would with direct output.

It's also worth noting that when you consider what's possible with placement attributes or classes, markup regions are likely to deliver the most result for the least code, over other output strategies in many cases. In the end, only you as the web developer can decide what output strategy what works best for your case. And what strategy is best may change depending on the project. ProcessWire does not require you to use any one output strategy and never will, but we will continue to bring the best tools available to you, and we are happy to add markup regions to the ProcessWire toolbox.

If you are in any way feeling that there's anything complex or unclear about markup regions, then we'd urge you to go ahead and start using them to experiment (at least once they are on the master branch). What you'll find after trying it out is that it's about the simplest thing you've ever used. Sometimes words cannot communicate the simplicity of something, and only in putting it to use does it become clear. There's really nothing to it other than what you already know. Here's a few more examples below that include some of the usages introduced this week:


### Quick recap: how to use markup regions

1. In your /site/config.php file:

```
$config->useMarkupRegions = true;
$config->appendTemplateFile = '_main.php';
```

2. Create a /site/templates/_main.php file:

```
html<!DOCTYPE html>
<html>
  <head>
    <title><?=$page->title?></title>
  </head>
</html>
<body>
  <div id=content>
    <h1 id=headline><?=$page->title?></h1>
    <?=$page->body?>
  </div>
  <aside id=sidebar>
    <?=$page->sidebar?>
  </aside>
</body>
</html>
```

3. Edit a template file, like home.php for your homepage. Or any other template file that you'd like. Anything that you output can replace, prepend, append, insert before or insert after anything that's outlined with an "id" (or "pw-id") attribute in your _main.php file.

Satisfied with the default presentation in _main.php? *Then just leave the template file blank.*

Want to change something, like prepending a big photo to the top of the #content div? Try this:

```
html<img src=photo.jpg pw-prepend=content>  
```

Want to replace the h1#headline to use your headline field rather than title?

```
html<h1 pw-replace=headline><?=$page->headline?></h1>
```

Want to append a p.copyright paragraph under #content?

```
html<p class=copyright pw-append=content>Copyright 2017</p>
```

Want to add a footer element after the sidebar?

```
html<footer pw-after=sidebar>
  Powered by ProcessWire
</footer>
```

That's all for this week. Hope you all have a great weekend and enjoy reading the [ProcessWire Weekly](http://weekly.pw)!
