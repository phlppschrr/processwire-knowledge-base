# Bootstrapping ProcessWire CMS from external scripts

Source: https://processwire.com/docs/front-end/include/

## Sections


## Including and bootstrapping ProcessWire

Use ProcessWire’s API in other PHP apps and shell scripts… It’s easy!

ProcessWire's API and data can be used from other PHP scripts, including command line PHP scripts. This is a simple matter of just including ProcessWire's ./index.php file from any other PHP script.

```
include("/path/to/processwire/index.php");
```

It doesn't matter if your intended use is HTTP or command line... ProcessWire will auto-detect the state from which it was included.

Once you've included ProcessWire like in the example above, the API is now available to you, just like in template files. For example, here is how you would retrieve a fictional "Contact Us" page from ProcessWire's [$pages](/docs/start/variables/pages/) API variable. Each line below is equivalent, so what syntax best suits your needs:

```php
$mypage = $pages->get("/about/contact/"); 
$mypage = pages()->get("/about/contact/");
$mypage = $wire->pages->get("/about/contact/");
$mypage = wire('pages')->get("/about/contact/");
```

Note that if using `pages()` or `wire('pages')` with ProcessWire 3.x, you'll need to call them from the ProcessWire namespace. You can do this by having a `namespace ProcessWire;` at the top of your PHP file, or by referencing the namespace directly, i.e. `\ProcessWire\wire('pages')->get(…);`

You can access all of the same [API variables](/docs/start/variables/) that you can from a template, except that there is no default `$page` variable accessible from the API since ProcessWire is not handling the web request. Of course, you are welcome to retrieve any page you want from the [$pages API variable](/docs/start/variables/pages/). Likewise you can modify, save, and delete pages as usual.


### Creating a ProcessWire command-line script

Here is an example of a command line shell script called sitemap.sh that outputs all pages in the site in an indented site map. We do this with a very small amount of code by creating a function called listPage that we use recursively:

```php
#!/usr/bin/php
<?php namespace ProcessWire;
include("/home/ryan/www/index.php"); // bootstrap ProcessWire
function listPage($page, $level = 0) {
  echo str_repeat("  ", $level) . $page->title . "\n";
  foreach($page->children as $child) {
    listPage($child, $level+1);
  }
}
listPage($pages->get("/")); // start at homepage
```

Note that you would need to replace the lines containing paths to have the equivalent paths on your machine (lines 1 and 3). You would also make the shell script executable, i.e.

```
chmod +x sitemap.sh
```

Next you would run the shell script:

```
./sitemap.sh
```

And here is what the output looked like when I ran it here:

```
Home
    About
        What's Unique?
        Why ProcessWire?
        Background
        Requirements
        License
    Developer API
        Concept
        What is the API?
        Directories
        Template Files
        Variables
            $page
            $pages
            $input
            $sanitizer
        Selectors
        Syntax
        Plugin Modules
    Download
    Demo
    Videos
    Contact
```


### Including ProcessWire from another PHP script

ProcessWire can be included from any other PHP script in the same manner it was included from the command line script above. Just include ProcessWire's root ./index.php file, and you have full access to it's API.

We'll use the same example as in the shell script above, except that we'll use markup to make an HTML5 page with semantic lists and links to each page. We'll call this file sitemap.php and assume it lives in the web root where ProcessWire's index.php file is:

```php
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <title>Site Map</title>
</head>
<body>
    <h1>Site Map</h1>
    <?php
    include("./index.php"); // bootstrap ProcessWire
    function listPage($page, $level = 0) {
        echo "<li><a href='$page->url'>$page->title</a>";
        if($page->numChildren) {
            echo "<ul>";
            foreach($page->children as $child) listPage($child, $level+1);
            echo "</ul>";
        }
        echo "</li>";
    }
    ?>
    <ul>
      <?php listPage($pages->get("/")); ?>
    </ul>
    </body>
</html>
```

You can do anything with ProcessWire's API that you can do from a template, so everything you can do in template files still applies, as does everything in the [developer API](../../api-full/index.md).
