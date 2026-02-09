# ProcessWire 3.0.49 introduces a new template file strategy

Source: https://processwire.com/blog/posts/processwire-3.0.49-introduces-a-new-template-file-strategy/

## Sections


## ProcessWire 3.0.49 introduces a new template file strategy

13 January 2017 by Ryan Cramer [ 22 Comments](/blog/posts/processwire-3.0.49-introduces-a-new-template-file-strategy/#comments)


## ProcessWire 3.0.49

Part of our [2017 roadmap](/blog/posts/roadmap-2017/) is to introduce new site profile(s) to our core distribution. One of the challenges in building site profiles for this purpose is finding the right balance between keeping things simple, and showing off the flexibility and power of the system. Currently we accomplish this by having separate "beginner" (direct output) and "intermediate" (delayed output) profiles, plus a multi-language version of the intermediate profile.

What if we had an approach that was as simple (or simpler) than our "beginner" approach, but as powerful as our intermediate approach? And what if someone new to PW didn't have to learn what direct or delayed output was in order to understand how the template files work?

This week, we've got something added to the core that I think builds on the simplicity of direct output, and has the power of delayed output. It doesn't intend to replace either of those strategies (or whatever other strategy you may be using) but provides an alternative that may be very attractive to many, especially those coming from the front-end development side.

This new template file/output strategy is similar to delayed output in that you don't have to split up your main HTML template into separate header/footer sections, or the like. And you can use a `$config->appendTemplateFile` (i.e. _main.php file) with it. Or you could `include()` your document markup on your own.

The new strategy is similar to direct output in that you directly output (or echo) your markup from your template files. No concatenating of variables that will be output somewhere else. You can treat your template files as plain HTML, PHP, or any combination of either.

This strategy does *not* need an _init.php file (`$config->prependTemplateFile`), since it's not necessary to define or concatenate any variables like you might do with delayed output.


### Settings things up

Since this is a new and experimental feature in PW 3.0.49, it's not enabled by default. To enable it, set `$config->useMarkupRegions = true;` in your /site/config.php file. Don't worry, this is safe and shouldn't interfere with anything on an existing installation. For this reason, we may have it enabled by default in the future. But since I don't know all the things you might be using template files for, I figured we'd play it safe for now, just in case. So if you try out this new template strategy, just remember to add the config setting mentioned here.

While not required for this template strategy, if you want to follow along with our examples here, you'll also want to add `$config->appendTemplateFile = '_main.php';` to your /site/config.php file as well.

Let's say that I'm using a _main.php file that serves as my primary document markup, like used in our current default site profile. It contains the main document markup, like this:

```
html
<!DOCTYPE html>
<html>
  <head>
    <title><?=$page->title?></title>
  </head>
  <body>
    <div id='content'>
      <h1 id='headline'><?=$page->title?></h1>
      <div id='bodycopy'>
        <?=$page->body?>
      </div>
    </div>
    <aside id='sidebar'>
      <p>Welcome!</p>
    </aside>
    <footer id='footer'>
      <p>Copyright 2017</p>
    </footer>
  </body>
</html>
```

Note the various regions above identified by HTML `id` attributes:

- content
- headline
- bodycopy
- sidebar
- footer

Our _main.php file outputs default values for these, which we might pull from the current `$page`, or leave some static default value in there (like `<p>Welcome!</p>` in our sidebar), or we could just leave anything blank.

Now lets consider the output for our homepage (file: /site/templates/home.php). If we simply left the file blank, we'd get the default output that we see in the _main.php file above. But lets say that on our homepage, we want to display a `$page->intro` field in our #headline `<h1>` tag, and we want to display a photo in the #sidebar. Here's what our home.php file would look like:

```
html
<h1 id='headline'><?=$page->intro?></h1>
<aside id='sidebar'>
  <img src='<?=$page->image->url?>'>
</aside>
```

**That's the entirety of our home.php file.** It simply outputs whatever regions (identified by `id` attributes) that it wants to modify. Those regions automatically replace the ones from our _main.php file at output time. In this manner, anything output in your HTML that has an "id" attribute becomes a region that you can modify from your template files (or views, or any other file you are rendering/including from them). The strategy is entirely markup based, not unlike what you might use with a CSS framework.

What's already been mentioned above may be all you need. But you can do a lot more by using `pw-` prefix classes on elements. We'll cover these in the sections below.


### Going further: prepend and append

Lets say that we've changed our mind a bit about that homepage, and now we want to *append* the image in the sidebar, rather than replacing it. Meaning, we want it to show the `<p>Welcome!</p>` from the _main.php file (or whatever happens to be there), and have the image appear underneath it, rather than replace it. Here's how we'd do that:

```
html
<aside id='sidebar' class='pw-append'>
  <img src='<?=$page->image->url?>'>
</aside>
```

Note that class attribute that we added: `pw-append`. That indicates that you want the content to append whatever is in that #sidebar rather than replace it. Another way to do the same thing is to output this instead:

```
html
<img class='pw-append-sidebar' src='<=$page->image->url?>'>
```

When just appending one element like this, the shorter syntax above may be preferable. If we were appending a group of elements, or wanting to add new attributes or classes to the `<aside>`, then the earlier syntax would be preferable.

In the same manner, lets say that we want to prepend some big hero image to the #bodycopy div:

```
html
<img class='pw-prepend-bodycopy' src='/img/hero.png'>
```

When viewing the page, now you'd have a big hero image appearing directly within the #bodycopy div, before the `$page->body` text.


### Modifying <head>

Now lets say that we want to append two new `<link>` elements to add new stylesheets to our document head. But these stylesheets are only needed on the homepage, so we don't have them in our _main.php file. We can add them from our home.php template file, but as a prerequisite, we need our `<head>` tag in our main document markup to have a unique `id` attribute, since that is how ProcessWire identifies manipulatable markup regions. So we'd update our head tag in _main.php to be `<head id='html-head'>`, or choose your own id. Then we'd add this HTML below to our home.php file, to add our new stylesheets:

```
html
<head id="html-head" class="pw-append">
  <link rel="stylesheet" type="text/css" href="/path/to/file.css">
  <link rel="stylesheet" type="text/css" href="/another/file.css">
</head>
```


### Inserting new elements before/after other elements

We've covered prepend and append, but what about inserting new elements before or after existing elements? Lets say we want to insert a subhead after the #headline:

```
html
<h2 class='pw-after-headline'><?=$page->subhead?></h2>
```

Or lets say we want to insert a Twitter feed above our #footer:

```
html
<div class='twitter pw-before-footer'>
  <?=$modules->get('MarkupTwitterFeed')->render();?>
</div>
```


### Removing elements

We've continued to re-think our homepage and realized we don't need a sidebar at all, and instead want a full-width #bodycopy with the hero image in it. We also want to add the class "no-sidebar" to our wrapping #content div. Here's how we might do that:

```
html
<aside id='sidebar' class='pw-remove'></aside>
<div id='content' class='pw-append no-sidebar'></div>
```

The above removes the #sidebar `<aside>` completely from the document markup, and adds a "no-sidebar" class to the wrapping #content div.


### Working with attributes

When you use a tag that references an `id` attribute, like `<aside id='sidebar'>`, any attributes you add to that tag get merged with any other appearances of it. Meaning if the sidebar appears as-is in the _main.php file, and like below in my home.php template file…

```
html
<aside id='sidebar' title='Hello world' class='uk-card pw-append'>
```

…then the resulting #sidebar would have the new title and class attributes. *Note that the "pw-" prefix classes do not appear in the markup that gets output to the user.*

If that #sidebar already had a populated class attribute in the _main.php file, then the classes present there would remain, and that "uk-card" class above would be added to the existing class attribute.


### Does any of this depend on using a _main.php file?

No it doesn't. I'm just using that as an example here because it's something that I think readers may be familiar with. You could just as easily `include("./markup.inc")` from your home.php template file, and everything would work the same.

By that token, the elements that you manipulate don't even have to be part of the main document markup. This template strategy can be nested and go recursive. Meaning you can manipulate something you added from a template file or some other include(), which could be useful in certain cases where you might want it.


### How does it work technically?

It's actually really simple. When ProcessWire renders a page, it now asks the question: does any markup appear before the `doctype` or `<html>` element? And if it does, does any of it reference "id" attributes or have "pw-" prefix classes? If so, it processes them as markup regions, letting you do all that's mentioned in this post.

So really it's a combination of direct output and delayed output. Anything that appears in the direct output is considered markup that will be populated somewhere within the delayed output, dynamically.


### Quick reference

Below are some examples to serve as a quick reference. Note that “yo” is used as an example “id” attribute of an element that appears in the main document markup, and the examples below focus on manipulating it. The examples assume there is a `<div id=yo>` in the _main.php file (or wherever the final markup comes from), and the lines in the examples would be output from a template file, which manipulates what would ultimately be output when the page is rendered.

**Replacing and removing elements**

```
html
<div id=yo>Replaces #yo and merges attributes</div>
<div id=yo class=pw-replace>Same as above</div>
<div id=yo class=pw-remove>Removes #yo</div>
```

**Prepending and appending elements**

```
html
<div id=yo class=pw-prepend><p>Prepends #yo with this</p></div>
<div id=yo class='pw-prepend bar'>Prepends #yo, adds bar class</div>
<div id=yo class=pw-append><p>Appends #yo with this p tag</p></div>
<div id=yo class='pw-append foo'>Appends #yo, adds foo class</div>
<div id=yo class=pw-append title=hello>Appends #yo, adds title attr</div>
<div id=yo class='pw-append -baz'>Appends #yo, removes baz class</div>
```

**Inserting new elements**

```
html
<h2 class=pw-before-yo>Adds H2 headline with this text before #yo</h2>
<footer class=pw-after-yo>Adds this footer after #yo</p></footer>
<div class='pw-append-yo foo'>Appends this div.foo to #yo</div>
<div class='pw-prepend-yo bar'>Prepends this div.bar to #yo</div>
```

**Summary of class attributes**

- `pw-replace` replaces element (default assumption)
- `pw-prepend` prepends markup to element
- `pw-append` appends markup to element
- `pw-before` places markup before element
- `pw-after` places markup after element
- `pw-before-id` places this tag and markup before element with "id"
- `pw-after-id` places this tag and markup after element with "id"
- `pw-remove` removes element from document completely
- `foo` adds class "foo" to element (can be any class name)
- `-bar` removes class "bar" from element (can be any class name)

Note: after being processed, the “pw-” classes above are removed from the HTML tags automatically by ProcessWire.


### Benefits and drawbacks

While you can perform some fairly powerful manipulations with this approach, the reality is that it's also unusually simple. Just use your template files to directly output the elements you want to replace or update in the document markup.

Any markup element with an "id" attribute becomes a region that you can modify, insert before, insert after, or remove, dynamically.

No concatenation of string variables is necessary, and there's no need to have an _init.php file predefining variables for that purpose. Just start outputting markup and let ProcessWire match up where it goes in the document via it's “id” attribute.

This strategy is based entirely on HTML markup, and doesn't rely on PHP as our other strategies do. For this reason, I think it will be useful in attracting more front-end developers, and even beginners, to ProcessWire. But unlike other simple template strategies (like direct output) there are no sacrifices that I can think of.

Like I said at the beginning of this post, I was really thinking about what I want both beginners and seasoned professionals [new to ProcessWire] to see in those new site profiles we develop. I think this template strategy will make ProcessWire accessible to a broader audience, since it's based almost entirely around front-end terminology that's already “home” to most, like a really simple CSS framework.

It may be obvious but just want to be clear this is not a template system or something like twig. It is a strategy for communicating markup between template files, not unlike the recently introduced `region()` function. So if you need to do any kind of logic or API calls, that's PHP – nothing changes there when you use this strategy. What this strategy saves you from is having to shuffle variables containing markup, or include() calls across multiple files.

This template file strategy does not replace other strategies, it's just an alternative. For instance, my preferred strategy of using delayed output and region() calls is likely something I'll keep doing. But it's nice to have alternatives.

If your current strategy already involves using template files (or separate views) to generate HTML (as most do), there really aren't may drawbacks that I can think of so far. While there is some overhead in having ProcessWire perform these markup manipulations, the code around it has really been written to be quite fast. For instance, many things I'd usually use regular expressions for have been hand-coded the more verbose and harder way, to optimize them for speed.

I'm not necessarily sure if this is a drawback, but this strategy won't work correctly if there's something wrong with your HTML. While a browser might forgive a missing closing tag for some markup element, it's bound to confuse ProcessWire when populating your regions.

Perhaps there are other drawbacks that will surface as we explore this further. But for now it seems like a good experiment, and this is all very preliminary. I welcome your feedback and am interested to hear what the benefits and drawbacks are in your experience after using it. I'd also like to hear your thoughts on what additions or changes would be helpful to you. For instance, one thought is having an alternative to the “id” attribute for region identification, like a “pwid” attribute that gets stripped from the final markup.

Thanks for reading and I hope that you have a great weekend and week ahead. Be sure to enjoy reading the fantastic [ProcessWire Weekly](http://weekly.pw) tomorrow too.
