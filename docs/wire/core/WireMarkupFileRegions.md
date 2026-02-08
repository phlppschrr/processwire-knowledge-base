# WireMarkupFileRegions

Source: `wire/core/WireMarkupFileRegions.php`

ProcessWire Markup File Regions

Markup File Regions
Enables you to use the Markup Regions system to populate CSS and JS files.
File regions are an experimental part of ProcessWire’s [Markup Regions](https://processwire.com/docs/front-end/output/markup-regions/)
output strategy. File regions enable you to define CSS, JS, SCSS or LESS in your markup alongside the markup that is styled
or manipulated by it, keeping everything together as a single component, in cases where it's worthwhile. Unlike inline styles
or scripts, ProcessWire takes care of moving these assets to one or more external asset files. These external asset files are
automatically updated whenever you make a change to your file regions.

File regions require ProcessWire 3.0.254 or newer. They are not enabled by default.
Markup Regions with File Regions are enabled with `$config->useMarkupRegions = 2;` in your /site/config.php file.
More about: [Markup Regions](https://processwire.com/docs/front-end/output/markup-regions/).

#### How to use file regions for CSS:

Add a `<link>` tag like the following in the HTML `<head>` section:
~~~~~
<link rel="stylesheet" href="main.css">
~~~~~
Now you can populate the file linked above from one or more file regions, anywhere
in your output using a `<style>` tag. In the `<style>` tag, you must specify a "pw-file"
attribute, and either an "id" or "pw-id" attribute containing a unique ID for your file region.
This unique ID is how ProcessWire will keep track of it and know when to update it.
~~~~~
<style id="hello-world" pw-file="main.css">
   .hello-world {
     color: red;
   }
</style>
~~~~~
That's all that is necessary. Any time you make a change to the region above, it will be
automatically updated in the main.css file. Note that the `<style>` tags do not appear
in the final document output, as their contents is moved to the main.css file.

Now let's add another region to the main.css file, from somewhere else in our output:
~~~~~
<style id="foo-bar" pw-file="main.css">
  .foo { color: green }
  .bar { color: blue }
</style>
~~~~~
Following the above, ProcessWire will now be maintaining regions named `hello-world` and `foo-bar`
in a main.css file. The main.css file (or whatever filename you choose)
is located in /site/assets/markup-regions/. You can add as many file regions as you want,
whether they all point to the same file or point to multiple files.

#### How to use file regions for JS

Exactly the same as using it for CSS, but use `<script>` tags instead. Place the
script tag in your head, before the closing body tag, or wherever you want it:
~~~~~
<script src="main.js"></script>
~~~~~
Then you can populate that main.js file anywhere in your output, from any number of
script tags that point to main.js:
~~~~~
<script id="test-js" pw-file="main.js">
  alert('This is a test');
</script>
~~~~~

#### How to use file regions for SCSS/LESS

This would be the same as for CSS except that you'll be responsible for compiling
the SCSS/LESS file, and pointing to the resulting CSS file, just as you would without
file regions. Your <link> tag will be left as-is.
~~~~~
<link rel="stylesheet" href="<?=$config->urls->markupRegions?>test.css">
~~~~~
Now you can define your SCSS/LESS anywhere in the output, and it will populate
a /site/assets/markup-regions/test.scss (or .less) file. But you'll have to use
whatever tool you want to compile it to a CSS file.
~~~~~
<style id="my-test-scss" pw-file="test.scss">
  $alert-background: red;
  $alert-text: white;
  .alert {
     color: $alert-text;
     background-color: $alert-background;
  }
</style>
~~~~~
Let's say that we were using ProCache to compile our SCSS or LESS, we could
compile and link to it like this:
~~~~~
$css = $procache->css([ $config->urls->markupRegions . 'test.scss' ]);
echo "<link rel='stylesheet' href='$css'>";
~~~~~

#### Deleting regions

ProcessWire manages adding and updating regions, but if you need to delete a
region, just delete the entire file from /site/assets/markup-regions/
and ProcessWire will re-create it on the next page load, without your deleted
region. Perhaps a future version will be able to detect deleted regions somehow
or another. But since the same CSS file (for example) might be populated with
multiple different regions over multiple requests for different pages, ProcessWire
can't assume that it knows the full scope of regions in one file from any single request.
For that reason, it can't safely assume that a particular region has been deleted.
But it can easily re-create any files that you delete, and doing so will ensure
they do not contain CSS or JS for old/deleted regions.

#### Other tips

For CSS or JS you can specify `pw-file` as a boolean attribute and it will
assume the file "main.css" or "main.js", i.e. `<style id="test" pw-file>…</style>`

File regions are not meant to replace the traditional way of managing CSS and JS.
Instead, see it as another tool to use when it fits the need.

Defining file regions in this way means that you can use PHP code and variables
as part of your CSS/JS/SCSS/LESS, should that be useful.

When building components for a site or application, and depending on the case,
it can sometimes be helpful to maintain the PHP, markup, CSS and JS together,
like in the example below. Just one file to launch something new, and ProcessWire
takes care of moving them to externally linked assets.
~~~~~
<ul id="items">
  <?php
  foreach($pages->get('/items/')->children as $item) {
    echo "<li class='item'>$item->title</li>";
  }
  ?>
</ul>

<style id="items-css" pw-file>
  #items .item {
    border-bottom: 1px solid black;
    font-size: 1rem;
  }
</style>

<script id="items-js" pw-file>
  $(function() {
     $('.item').on('click', function() {
       alert("You clicked on: " + $(this).text());
     });
  });
</script>
~~~~~


ProcessWire 3.x, Copyright 2025 by Ryan Cramer
https://processwire.com

@since 3.0.254

## getDefaults()

Get default settings

@return array

## apply()

Apply file regions in given HTML document and regions markup

@param string $htmlDocument

@param string $htmlRegions

@param array $options

@return int Number of file regions

## findRegions()

Find and return file regions in given HTML

@param string $html

@param array $options
 - `action` (string): The "pw-[action]" or "data-pw-[action]" attribute to look for (default='file')
 - `tags` (array): Array of tag names to allow for action, and default action value (when non specified)
 - `exts` (array): File extensions to allow in action value (default=['css','less', 'scss','sass','js'])
 - `allowPaths` (bool): Allow paths in action value? (default=false)

@return array

@since 3.0.254

## populateRegions()

Populate file regions

@param array $fileRegions Regions found by findRegions()

@param string $html HTML to populate them into

@param array $options

@return string Returned value only useful if autoInsert=true

@since 3.0.254

## applyRegionNamespace()

Apply namespace to region content

@param array $region

## applyRegionLinks()

Apply region links (optional)

For example: Converts the `main.css` in `<link rel="stylesheet" href="main.css">`
to `/site/assets/markup-regions/main.css`.

If the autoInsert option is enabled and there is no existing `main.css` to update then it will return
a string with the `<link>` tag to main.css in it.

@param string $html

@param string $basename

@param string $url

@param string $ext

@param array $options

@return string

@since 3.0.254

## addNote()

Add a debug note

@param string $note

## getNotes()

Get debug note

@return array

## addError()

Add an error

@param string $key Error context

@param string $error Error message

## getErrors()

Get errors

@param string $key Optional context

@return array
