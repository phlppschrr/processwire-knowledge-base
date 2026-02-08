# Unknown

Source: https://processwire.com/docs/tutorials/how-to-structure-your-template-files/

How to use some of the more common strategies used by developers in structuring template files. Includes pros and cons as well as extensive examples.

When ProcessWire loads a template file, it hands it a copy of the current $page, along with all of the other ProcessWire API variables. Beyond that, it is just a regular PHP file. What happens within that file is entirely to the developer.

ProcessWire knows nothing about the type of output you intend to produce with that template file. In fact, you can produce any kind of output with your template file, which is one of the reasons why ProcessWire is so flexible. But with flexibility comes some ambiguity, especially for developers new to ProcessWire. Such developers may be asking themselves "what exactly should I put in this template file?" or "what are the best practices?".

With this tutorial, we hope to outline some of the more common strategies used by developers in structuring template files. So as not to extend the scope too broadly, we'll limit this tutorial to output of HTML documents and the different methodologies one might use.

Note: This tutorial does not yet cover Markup Regions, something new to ProcessWire 3.x, which is a nice mashup between direct and delayed output.

### Remember to enable debug mode

Regardless of what template file strategy you use, you will almost always want debug mode ON when you are working with template files. This ensures that you see error messages and notices as they occur. On a production site you would of course want error messages suppressed so that they do not interfere with the user–or worse–reveal sensitive details that might affect security. But when developing a site and making edits to template files, you most certainly want to see error messages and notices, otherwise it would be very difficult to make progress! Edit your /site/config.php file, locate the line referring to `$config->debug` and change it from `false` to `true`.

file:/site/config.php

```
$config->debug = true;
```

Remember to change it back to `false` *before* your site is live.

---

## Direct Output

The first strategy is the easiest to understand (though also likely the least flexible). But even if you don't intend to use this strategy, read on, as it does help to establish the context that template files operate in. When a template file is used as direct output, the only difference between a template file and an HTML file is that you can use some PHP in there when you want to. Here is an example of a template file using direct output:

file:/site/templates/basic-page.php

```
<html>
  <head>
    <title>Hello World</title>
  </head>
  <body>
    <h1>Hello World</h1>
    <p>How do you like my HTML document?</p>
  </body>
</html>
```

There literally isn't any difference between that and a regular old HTML document. Lets go a little further and throw in some PHP so that the output of the `<title>` tag, `<h1>` tag and body copy are dynamic, coming from the $page being viewed:

file:/site/templates/basic-page.php

```
<html>
  <head>
    <title><?php echo $page->title; ?></title>
  </head>
  <body>
    <h1><?php echo $page->title; ?></h1>
    <?php echo $page->body; ?>
  </body>
</html>
```

Simply by adding `<?php echo $page->title; ?>` where we want to output the page's title, and `<?php echo $page->body; ?>` where we want to output the page's body, are all that is necessary to have a template file that we could use for dynamic output of any page in our site. Note that you may also shorten that to just `<?=$page->title?>` and `<?=$page->body?>` if you prefer (and the same goes for the rest of this tutorial), but we will stick to the longer syntax since there are still a few (rare) web servers out there that may not support these PHP short open/close tags.

Getting back to the real world, it's not likely our site will only need one template (and template file). And chances are our document markup will consist of a lot more than what this simple example shows. That leads us nicely into our next template file strategy…

---

## Direct Output with Includes

When we want to utilize the convenience of direct output, but don't want to repeat the same markup in every template file, we move the code that we want to re-use into separate files. That way we can have multiple template files that pull in the same bits of code without us having to repeat ourselves. The benefit is that if we need to change something, we only need to change it in one place rather than in all of our template files.

To get started, lets figure out the parts of our basic-page.php template file that we want to re-use in other template files. In this case, we know that the markup at the top of all our template files will be the same, so lets move that to a head.inc file (or whatever you want to name it). We'll use the .inc extension for the file just to clarify that it is a file meant to be included in others, rather than a dedicated template file of it's own (though this naming convention is optional).

file:/site/templates/head.inc

```
<html>
  <head>
    <title><?php echo $page->title; ?></title>
  </head>
  <body>
    <h1><?php echo $page->title; ?></h1>
```

We also know that the markup at the end of all our template files will be the same, so we'll move that markup into a foot.inc file.

file:/site/templates/foot.inc

```
</body>
</html>
```

Where the template files will vary is what's in-between head.inc and foot.inc. So we'll use our basic-page.php template file to do the following, in this order:

1. include the head.inc file
2. output content
3. include the foot.inc file

Here's how we might do that:

file:/site/templates/basic-page.php

```
<?php
include("./head.inc");
echo $page->body;
include("./foot.inc");
```

The output is identical to when basic-page.php was an entire HTML document. But our template file has become a lot smaller, and we can re-use our head.inc and foot.inc in any other template files that we want to. For instance, we might have another template called *sidebar-page* (with file sidebar-page.php) that produces output similar to basic-page.php while being able to support separate bodycopy and sidebar columns:

file:/site/templates/sidebar-page.php

```
<?php include("./head.inc"); ?>
  <div id='bodycopy'>
    <?php echo $page->body; ?>
  </div>
  <div id='sidebar'>
    <?php echo $page->sidebar; ?>
  </div>
<?php include("./foot.inc"); ?>
```

Using includes for head.inc and foot.inc is just for starters. You can use includes for literally anything. Many people refer to these types of includes as *partials. *You can extend their use to anything that you might want to repeat or reuse in any template file.

### Direct output with automatic inclusions

It's not actually necessary to manually `include("./head.inc")` and `include("./foot.inc")` in each of your template files. You can make this happen automatically by editing your /site/config.php file and populating these two lines like so:

```
$config->prependTemplateFile = 'head.inc';
$config->appendTemplateFile = 'foot.inc';
```

What the above essentially says is to automatically load the contents of head.inc file before your template file (prepend), and load the contents of foot.inc after your template file (append). The result is that it's no longer necessary to manually include those in each of your template files. These automatic inclusions actually come in handy in other template file strategies too, so keep them in mind!

### Disadvantages of direct output

Where direct output starts to fall apart is when you want to affect the output in multiple regions on a page. In our examples above, our template files only control the output for what comes between head.inc and foot.inc. While we could accommodate more regions with additional includes, it starts to get a little cumbersome. What if any of our template files could populate any region in our markup without us having to know exactly where it will go ahead of time? That leads into our next strategy…

---

## Delayed Output

### Also known as the main.inc strategy

This strategy focuses on generating the output for all the various regions of our final document ahead of time, and temporarily storing them in placeholders (called variables). Rather than including a head.inc and foot.inc file, we instead just include a main.inc file at the end. That main.inc file knows where to output all the placeholders.

The placement of content matters little to our template files, which can focus purely on populating those placeholders. Should the site later be re-designed and have everything get moved around, our template files don't need to change. Only our main.inc file and CSS files are likely to need adjustment to support the new design.

### What does this strategy look like?

When using delayed output with variables, your template files focus on populating variables rather than outputting them. This leads to template files that are quite a bit simpler, and occasionally even blank! Here's an example of what our template file might look like:

file:/site/templates/basic-page.php

```
<?php
$headline = $page->get("headline|title");
$bodycopy = $page->body;
$sidebar = $page->sidebar;
include("./main.inc");
```

As you can see above, our template file is simply populating 3 predefined regions by using placeholder variables: `$headline`, `$bodycopy`, and `$sidebar`. These variables are populated with values that we want to be output in main.inc. Then we end by just including the main.inc file. What does this mysteries main.inc file look like?

file:/site/templates/main.inc

```
<html>
  <head>
    <title><?php echo $headline; ?></title>
  </head>
  <body>
    <div id='bodycopy'>
      <h1><?php echo $headline; ?></h1>
      <?php echo $bodycopy; ?>
    </div>
    <div id='sidebar'>
      <?php echo $sidebar; ?>
    </div>
  </body>
</html>
```

What this example isn't showing is that your `$bodycopy` and `$sidebar` may consist of a lot more than just `$page->body` and `$page->sidebar`. Which leads us to…

### Populating placeholders (variables) with more

Lets say that you want your `$bodycopy` to include a list of comments at the end, and you want your `$sidebar` to include sub-navigation to child pages. Here's how that might look:

file:/site/templates/basic-page.php

```
<?php
$headline = $page->get("headline|title");

// bodycopy is body text plus comments
$bodycopy = $page->body . $page->comments->render();
$sidebar = $page->sidebar;

// check if this page has any children
if(count($page->children)) {
  // render sub-navigation in sidebar
  $sidebar .= "<ul class='nav'>";
  foreach($page->children as $child) {
    $sidebar .= "<li><a href='$child->url'>$child->title</a></li>";
  }
  $sidebar .= "</ul>";
}

include("./main.inc");
```

As you can see, we can put whatever we want into our predefined placeholders/variables very easily. We've got a lot of flexibility here.

### Defining new placeholders to represent new regions

Lets say that we wanted to let our main.inc file decide where the sub-navigation should appear, rather than us appending it to the sidebar. Whether you need that or not depends, but lets look at how we might approach it. We will give our main.inc full control over where that `<ul class='nav'>…</ul> `sub-navigation lives. We could do that by setting up another placeholder variable, which we will name `$subnav`. Rather than populating `$sidebar`, we would populate `$subnav`. Then our main.inc file would determine where that `$subnav` gets displayed.

**Using the placeholder to hold pages rather than markup**
In this particular case, we would have to repeat ourselves with writing the `foreach()` code to generate the `<ul class='nav'>…</ul>` in every template file where we wanted sub-navigation. It would make more sense to let our main.inc file handle that markup generation, and let our template file just pass it the list of pages that should appear in that sub-navigation. So we will use our `$subnav` placeholder variable to hold a group of pages rather than a string of markup. Here's how that might look:

file:/site/templates/basic-page.php

```
<?php
$headline = $page->get("headline|title");
$bodycopy = $page->body . $page->comments->render();
$sidebar = $page->sidebar;
$subnav = $page->children;
include("./main.inc");
```

And here's how the main.inc file might look:

file:/site/templates/main.inc

```
<html>
  <head>
    <title><?php echo $headline; ?></title>
  </head>
  <body>
    <div id='bodycopy'>
      <h1><?php echo $headline; ?></h1>
      <?php echo $bodycopy; ?>
    </div>
    <div id='sidebar'>
      <?php
      echo $sidebar
      if(count($subnav)) {
        echo "<ul class='nav'>";
        foreach($subnav as $child) {
          echo "<li><a href='$child->url'>$child->title</a></li>";
        }
        echo "</ul>";
      }
      ?>
    </div>
  </body>
</html>
```

### Adding an init.inc file to the mix (a best practice)

One of the problems with the above examples is that each template file must populate every single placeholder variable output by the main.inc file. If you decide to add a new placeholder for a new region, you'd have to go back and edit all your template files to account for it. Otherwise you'd end up with "undefined variable" notices. In addition, maybe a lot of our template files simply don't need `$bodycopy` to be anything more than `$page->body` and don't need `$sidebar` to be anything more than `$page->sidebar`. We could think of those as our default values. Wouldn't it be nice if we didn't have to even mention them in our template files when we didn't need them to be different from the default?

This is an easy task to accomplish. Simply include an init.inc file at the top of each template file. Like the name implies, the init.inc file initializes all the placeholder variables that will get output in main.inc by establishing default values to them. Here's how our init.inc file might look:

file:/site/templates/init.inc

```
<?php
$headline = $page->get("headline|title");
$bodycopy = $page->body;
$sidebar = $page->sidebar;
$subnav = $page->children;
```

Now all of our placeholders in main.inc are accounted for with default values. Our template files can focus only on modifying the placeholders that they want to be different from the defaults. Our basic-page.php only needs to append comments to the `$bodycopy`, so it now looks like this:

file:/site/templates/basic-page.php

```
<?php
include("./init.inc");
$bodycopy .= $page->comments->render();
include("./main.inc");
```

### Automatic inclusions

We now have a scalable and sustainable strategy for our template files, but it's a little annoying to have to repeat the `include("./init.inc");` and `include("./main.inc");` in every single one of our template files. Thankfully, there are two `$config` options that can solve this for us:

file:/site/config.php

```
$config->prependTemplateFile = 'init.inc';
$config->appendTemplateFile = 'main.inc';
```

The `$config->prependTemplateFile` specifies the file that you want ProcessWire to load *before* your template file, and the `$config->appendTemplateFile` specifies the file you want ProcessWire to load *after* your template file. These files are assumed to live in /site/templates/. They act as if they had literally been prepended or appended to your template file, sharing the same variable space as your main template file. This is what enables you to share variables between them. Meaning, a variable set in your init.inc file (like `$bodycopy`) will still be present ("in scope") in your template file, and will still be present in the main.inc file as well.

After editing our /site/config.php file to add those two options, our basic-page.php template file may be reduced to just this:

file:/site/templates/basic-page.php

```
<?php
$bodycopy .= $page->comments->render();
```

**When to use automatic inclusions**
Whether or not you should use automatic inclusions kind of depends on the situation. If you are working with a site that has various output needs, some direct and some delayed, then automatic inclusions may get in the way. Likewise, if you have more than one main.inc file (perhaps representing different layouts) then it might be preferable to `include()` whatever output file you desire at the end of each template file. You may find in some cases that you'll use `$config->prependTemplateFile`, but not `$config->appendTemplateFile`. Again, it really just depends on the situation. However, now that you know about automatic inclusions, we think you'll find them very useful in many instances.

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
