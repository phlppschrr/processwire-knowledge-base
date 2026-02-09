# $pages->newPage($options = array()): Page

Source: `wire/core/Pages.php`

Return a new Page object without saving it to the database

To create a new Page object and save it the database, use the `$pages->new()` or `$pages->add()` methods,
or call `save()` on the Page object returned from this method.

 - When a template is specified, the `pageClass` can be auto-detected from the template.
 - In 3.0.152+ you may specify the Template object, name or ID instead of an $options array.
 - In 3.0.191+ you may specify a selector string for the $options argument (alternative to array),
   see the `$pages->new()` method `$selector` argument for details.
 - In 3.0.191+ the `pageClass` can also be specified as `class`, assuming that doesn’t collide
   with an existing field name.

## Example

~~~~~
// Create a new blank Page object
$p = $pages->newPage();

// Create a new Page object and specify properties to set with an array
$p = $pages->newPage([
  'template' => 'blog-post',
  'parent' => '/blog/posts/',
  'title' => 'Hello world',
]);

// Same as above but using selector string (3.0.191+)
$p = $pages->newPage('template=blog-post, parent=/blog/posts, title=Hello world');

// Create new Page object using 'blog-post' template
$p = $pages->newPage('blog-post');

// Create new Page object with parent and name implied by given path (3.0.191+)
$p = $pages->newPage('/blog/posts/hello-world');
~~~~~

## Usage

~~~~~
// basic usage
$page = $pages->newPage();

// usage with all arguments
$page = $pages->newPage($options = array());
~~~~~

## Arguments

- `$options` (optional) `array|string|Template` Optionally specify array (or selector string in 3.0.191+) with any of the following: - `template` (Template|id|string): Template to use via object, ID or name. The `pageClass` will be auto-detected. - `parent` (Page|int|string): Parent page object, ID or path. - `name` (string): Name of page. - `path` (string): Specify /path/for/page/, name and parent (and maybe template) can be auto-detected. 3.0.191+ - `pageClass` (string): Class to use for Page. If not specified, default is from template setting, or `Page` if no template. - Specify any other Page properties or fields you want to set (name, title, etc.). Note that most page fields will need to have a `template` set first, so make sure to include it in your options array when providing other fields.

## Return value

- `Page`
