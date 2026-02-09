# ProcessWire 3.0.62 and more on markup regions

Source: https://processwire.com/blog/posts/processwire-3.0.62-and-more-on-markup-regions/

## Sections


## ProcessWire 3.0.62 and more on markup regions

5 May 2017 by Ryan Cramer [ 4 Comments](/blog/posts/processwire-3.0.62-and-more-on-markup-regions/#comments)


## ProcessWire 3.0.62 dev

On the dev branch this week we've got ProcessWire version 3.0.62. This version contains some minor bug fixes, with the biggest one being that the “Upload image” option in the CKEditor image selection dialog wasn't working quite right in 3.0.61. For that reason, next week we'll merge this version to the master branch as well. Note that the more commonly used image upload in the page editor is not affected by this issue.

With 3.0.61 being the first master version release that supports markup regions, we thought it was a good time to revisit them. Markup regions have evolved and changed a bit since they were originally introduced, so we wanted to take this opportunity to properly document them, since some information in past posts may now be incomplete or no longer applicable. Below we cover how markup regions work on the current master branch of ProcessWire. This will eventually be migrated to a documentation page for markup regions.


## All about markup regions

In ProcessWire, you typically follow one of two output strategies (or some variation of them):

ProcessWire master version 3.0.61+ enables you to use another output strategy called Markup Regions. These markup regions are perhaps the simplest output strategy, and they are kind of like a cross between the two output strategies mentioned above. Like direct output, your template files can directly output markup in a free-form fashion. And like delayed output, the locations of the markup are determined later (by the _main.php file). Meaning, the output is non-linear and it doesn't matter what order you echo the output in.

Markup regions can help you to decouple your template files from your main document markup in the same way that delayed output does. But unlike delayed output, you don't necessarily have to pre-define where everything goes. The placement of the markup in the document is dictated by the attributes in the HTML tags that you output. When used correctly, this can help to reduce dependencies between template files and main document markup and provides and simple and easy-to-use output strategy.

The benefits of markup regions are best demonstrated rather than verbalized…


### Enabling markup regions

Markup regions are not enabled by default in ProcessWire, unless you installed it with a site profile that is using them. To enable markup regions, you must add the following line to your /site/config.php file:

```
$config->useMarkupRegions = true;
```


### Defining regions

Define markup regions anywhere in your `<html>...</html>` with existing HTML tags (typically in _main.php), and identify them with "id" attributes:

```
html<div id="something">...</div> 
```

If you don't like using "id" attributes, you are also welcome to use "pw-id" or "data-pw-id" attributes instead. They do the same thing, but only ProcessWire can see them – they are removed from the final output and thus not visible to front-end markup, CSS or JS.

```
html<div data-pw-id="something">...</div>
```

Note that we are using <div> tags in many of our examples here, but it can be any HTML tag.

If you want to define a region where only the *inner* HTML will be used, and the wrapping tags won't appear in the final markup, you can define such a placeholder using either the `<region>` tag or `<pw-region>` tag (they are the same thing):

```
html<region id="something">...</region>
<pw-region id="something-else">...</pw-region>
```


### Populating regions

Once there are regions defined within the `<html>...</html>` main document markup, you can populate them. This is typically handled from your site template files, or other files included from them. Here is a simple example of populating a region:

```
html<div id="something">
  This content will be populated to div#something.
</div>
```

The above example simply replaces whatever appears in the originally defined div#something, and replaces it with the content that you specify. The following example is functionally identical to the above example, just using different syntax to introduce "pw-" attributes:

```
html<div pw-replace="something">
  This content will be populated to div#something.
</div>
```

Notice that "pw-replace" attribute above. That's called an action attribute. The default action is to replace, which is why we didn't have to specify it in the example before this one.

**Stop for a second: **There's a good chance that what's been mentioned above is all you will ever need from markup regions. But you can do quite a bit more when/if the need arises. We'll cover that below. But we just wanted to point out that if you understood what we've mentioned so far, then you already understand everything you need to know in order to start using markup regions. All that follows gets into the more advanced usage of markup regions.


### Actions for populating regions

In addition to replacing the markup in a region, you can also append markup, prepend markup, insert markup before or insert markup after any defined region using these "pw-" action attributes (or "data-pw-" attributes if you prefer). These are best demonstrated by examples:

```
html<p pw-append="something">
  This paragraph will append to div#something
</p>

<p pw-prepend="something">
  This paragraph will prepend div#something
</div>

<p pw-before="something">
  This will insert a p tag with this content, before div#something
</p>

<p pw-after="something" class="hello">
  This will insert a p.hello tag with this content, after div#something
</p>
```

*Note: Any of the "pw-action" attributes above can also be specified as "data-pw-action" if you prefer it. Regardless of what format you use, the action attributes are only seen by ProcessWire and they are removed from the final markup. *

Lets look at another example. Say that you've got this region defined in your _main.php file…

```
html<ul pw-id="foo">
  <li>First item</li>
</ul>
```

…and you've got this in one of your other template files:

```
html<li pw-prepend="foo">Hello!</li>
<li pw-append="foo">Second item</li>
<h3 pw-before="foo">Test headline</h3>
```

The final output would be this:

```
html<h3>Test headline</h3>
<ul>
  <li>Hello!</li>
  <li>First item</li>
  <li>Second item</li>
</ul>
```


### Advanced: adding attributes

When replacing a region (pw-replace), any non-pw attributes you add to the tag will be added to the originally defined region tag. Lets say that you've got this region defined in your _main.php file…

```
html<div class="myclass" id="content-body"></div>
```

…and you've got this in one of your other template files:

```
html<div id="content-body" title="hello">
  <p>Hello there</p>
</div>
```

The final output would be this:

```
html<div class="myclass" id="content-body" title="hello">
  <p>Hello there</p>
</div>
```

Essentially, the attributes of the original tag in _main.php are merged with those of your new tag.


### Advanced: using class attributes

When specifying class attributes, the classes from the action tag and the region tag are combined. Meaning, classes you specify in a action tag behave as an "add class":

```
html<!--Region definition-->
<ul pw-id="mylist" class="foo"></ul>
```

```
html<!--Region action-->
<ul pw-id="mylist" class="bar"><li>Item</li></ul>
```

```
html<!--Resulting output-->
<ul class="foo bar"><li>Item</li></ul>
```

If needed, you can specify "remove class" in the region action by prepending the class name you want to remove with a hyphen:

```
html<!--Region action-->
<ul pw-id="mylist" class="-foo bar"><li>Item</li></ul>

<!--Resulting output-->
<ul class="bar"><li>Item</li></ul>
```


### Debugging regions

If you are getting an unexpected result with your markup regions, you may want some more information about what's happening with the markup regions behind the scenes. Included is a special comment you can add somewhere in your `<html>...</html>`, typically in your _main.php file:

```
html<!--PW-REGION-DEBUG-->
```

That comment gets automatically replaced with a pre.pw-region-debug element that contains some basic debugging information about what it did:

```
3. replace => #content-head ... <h1 id='content-head'>
6. replace => #sidebar ... <aside id='sidebar'>
26. replace => #content-body ... <div class='uk-margin-top' id='content-body'>
0.0044 seconds
```

Above we can see there were 3 replace actions in your template file replacing the contents of tags in our _main.php file. The number at the beginning of each line is a number PW uses internally to identify the region. The format is this:

```
number. action => region-id ... tag
```

Below the list of regions is a timer indicating the amount of time that was spent processing the regions.


### How it works (technical detail)

That's it in a nutshell. This blends very well with the delayed output methodology, where your main HTML document markup is in your _main.php file, and the rest of your site template files output just the portions they want to populate or modify.


### Markup regions audience

Markup regions work kind of like magic, connecting everything behind the scenes into the final output. But it takes ProcessWire a little more work to handle this than it does with direct or delayed output – it's an extra step. For most cases, it's a relatively small extra step, and has little or no measurable drawback in terms of site performance. But if you are outputting large amounts of markup, it's possible for there to be overhead associated with markup regions relative to the other output strategies. For this reason, we'd suggest you might prefer direct or delayed output if your site happens to deal with really heavy amounts of output.

Experienced ProcessWire developers may already have an output strategy that works well for them, and when this is the case, we suggest sticking with what you are already doing. The people that will find the most benefit from markup regions are those that like the simplicity, convenience and code style of direct output, but want the benefits of delayed output. We also think dedicated front-end developers and those new to ProcessWire will appreciate markup regions. If you are interested in using markup regions, but not completely sure about it, we encourage you to give it a try in your next project.

Hope that you all have a great weekend. See you at [ProcessWire Weekly](http://weekly.pw)!
