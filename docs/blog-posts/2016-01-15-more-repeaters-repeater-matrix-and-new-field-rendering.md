# More Repeaters, Repeater Matrix and New Field Rendering

Source: https://processwire.com/blog/posts/more-repeaters-repeater-matrix-and-new-field-rendering/

## Sections


## More Repeaters, Repeater Matrix and New Field Rendering

15 January 2016 by Ryan Cramer [ 18 Comments](/blog/posts/more-repeaters-repeater-matrix-and-new-field-rendering/#comments)


## ProcessWire 3.0.5

This week we've released ProcessWire version 3.0.5 which actually contains quite a lot of changes. Now you can nest repeater fields (repeaters in repeaters) and use dynamic/AJAX loading for all items. Plus we've got the first test version of Repeater Matrix released, and new support for field templates…


### Repeater upgrades continued in PW 3.0.5

Last week we introduced several upgrades to Repeater fields in ProcessWire 3.0. It ended up being one of the most popular posts in awhile, so I took that as a hint and continued work on both Repeaters and Repeater Matrix. In addition what was added last week, here's what's been added to the core Repeater type this week:


### All repeater items now support dynamic loading (AJAX)

Last week we introduced the option to dynamically load new items to a Repeater field, eliminating the need for the previous "ready pages" that we used. This week we continued that upgrade so that now all repeater items can be dynamically loaded. Meaning, ProcessWire doesn't render the inputs for a given repeater item until you click on the repeater item.

This results in a potential huge performance improvement to the editor, especially on pages where you might have lots of repeater items. It also enables repeater fields to scale much further from an editing standpoint. PageTable and Repeater should now be equals when it comes to editor performance.

In order to utilize dynamic/AJAX loading with repeater items, you must configure your Repeater field appropriately so that existing items are collapsed. Then you should choose the option to to enable dynamic/AJAX loading. See screenshot below, which is what you see on the "Details" tab when configuring your Repeater field.


### New support for nested repeaters

A request that's come in a few times since we originally introduced repeaters was the option to have nested repeaters (or repeaters-in-repeaters). On the surface, it might sound like overkill. But the more you use repeaters, the more the need comes up, and the more useful it can be. It's actually not overkill at all.

For example, lets say I've got an "Events" repeater, where each item represents a multi-day event for an organization. Since each event can span multiple days, you might use another repeater within the Events repeater to represent the itinerary for each day of the event.

This week we added support for these types of nested repeaters. Not only can you have repeaters in repeaters, but you can have repeaters in repeaters in repeaters, if that suits your need! We haven't yet tried to stack them more than 3 levels deep, and not sure we'd recommend that, but the support is there if you need it. Also worth noting is that you can nest regular Repeaters in Repeater Matrix fields, or Repeater Matrix fields in regular Repeaters.


### Repeater Matrix is released (alpha)

In last week's post we introduced Repeater Matrix, which is an extension of Repeaters that enables you to have repeater items of different types in the same repeater. You define what fields accompany each item type. You can have any number of items of any type that you define. Repeater Matrix fields are very similar to regular ProcessWire repeater fields, except that in regular repeater fields, you can only have one type. Repeater Matrix fields enable flexible content types and open the door to all kinds of great content management possibilities.

This week we've got the Repeater Matrix module ready for ProFields users that are interested in trying it out. Though please note it's an alpha version, and likewise requires the alpha version of ProcessWire (3.0.5). The Repeater Matrix module download has been posted to the ProFields support board along with accompanying documentation.


### ProcessWire 3.0.5 introduces field rendering with template files

In addition to the Repeater upgrades introduced this week, ProcessWire 3.0.5 also introduces support for a new kind of template file. You can now have template files for any field in ProcessWire, and those template files can be used to render output for any given field.

These new template files are located in /site/templates/fields/, and are named according to the field name. For instance, if you wanted to have a template file for your "body" field, it would be named body.php. The contents of the template file might look like this:

```
<div class='bodycopy'>
  <?= $value ?>
</div>
```

The `$value` variable is provided to every field template file and it represents the value of the field from the page where it was called. The `$page` variable is present as well, so you could also just use `$page->body` if you preferred it. But we thought we should provide a common variable name for all field template files, for those that wanted that consistency.

To render the contents of a field with its associated template file, you just call the `$page->render()` method:

```
echo $page->render('body');
```

Either of these alternate syntaxes are also supported:

```
echo $page->render->body;
echo $page->_body_;
```

One of the alternate syntaxes above may be useful especially if embedding variables in strings like this:

```
echo "<h1>$page->title</h1>$page->_body_";
```

Think of the leading and trailing underscore as a way of saying *"get the body field, but with surrounding markup"*, where the leading and trailing "_" communicate *"surrounding markup."*

Lets say that you want your body field to only output the first paragraph if a user isn't logged in:

```php
<?php
if(!$user->hasRole('subscriber')) {
  // only show the first paragraph
  $value = substr($value, 0, strpos($value, '</p>') + 4);
  $value .= "<p>Please login to view the rest.</p>";
}
echo "<div class='bodycopy'>$value</div>";
```

Now our "bodycopy" example probably only hints at the usefulness of field template files, but we wanted to start with a simple example. Where they really start to show their usefulness is with fields that might have multiple values or properties. For instance, lets say we have an images field named "gallery" and we want to render a grid of thumbnail photos, and clicking on any one of them opens a lightbox. I'll use [Uikit](http://getuikit.com/) markup in this example.

/site/templates/fields/gallery.php

```php
<ul class='uk-thumbnav'>
  <?php
  foreach($value as $photo) {
    $thumb = $photo->size(100, 100);
    echo "
      <li>
        <a href='$photo->url' data-uk-lightbox>
          <img src='$thumb->url' alt='$photo->description'>
        </a>
      </li>
    ";
  }
  ?>
</ul>
```

Now, any time you want to output that gallery of photos, you can just place this in any template file:

```
echo $page->render('gallery');
```

Or if you prefer HTML context, and perhaps the _underscore_ style:

```
<?= $page->_gallery_ ?>
```

The benefit here is a built-in standard for promoting re-use of code needed to render markup for fields. However, the utility of these field template files goes beyond just rendering of markup. Field template files can also return things like objects and arrays rather than just rendering them. This is done simply by having a `return $something;` statement in your template file, where $something is the value you want to return. I'll leave the possibilities there to your imagination. The point I want to get across is that you can use the value returned however you like. Though I think most will find these field template files primarily useful when it comes to rendering markup.

Something to note is that whether your field template file directly echo's output, or returns it, it is considered delayed output. Meaning, the `$page->render('field_name')` call always returns the value rather than directly outputting it. This ensures you can easily use it both in direct and delayed output scenarios without having to adjust your code.

Also worth mentioning is that each field template file receives all of ProcessWire's API variables. It also receives these in addition to that:

- `$value` - The value that needs to be rendered
- `$page` - The page that $value lives on
- `$field` - The field representing $value (of class Field) if you want it

In order to start using field template files, you have to create them yourself, including the /site/templates/fields/ directory, which doesn't exist by default (though we'll probably update our default site profiles to use and have field template files).

Now some of you might be thinking, "I already have my own way of doing that with [ includes | functions | hooks | etc. ]". That's just fine, and you should keep doing what you are doing. But at some point you may find that field template files open up some useful new possibilities for code re-use, so it's good to have them in your toolbox and good to know about them. One area where field template files are particularly useful is with the new Repeater Matrix field…


### Field template files and Repeater Matrix

Field template files actually originated with a need that we had for the new Repeater Matrix field. While using Repeater Matrix for development, I found myself with giant `if/else` or `switch` statements that would check the type of each Matrix item before rendering it, so that it could render the appropriate fields. Kind of like this, but larger:

```php
<?php
foreach($page->test_matrix as $item) {
  if($item->type == 'content') {
    echo "
      <h3>$item->headline</h3>
      <p>$item->summary</p>
    ";
  } else if($item->type == 'quote') {
    echo "
      <blockquote>
        <p>$item->quote</p>
        <cite>$item->cite</cite>
      </blockquote>
    ";
  } else if( ... ) {
    // and so on
  }
}
```

It just seemed a lot nicer to delegate each of those types to have their own template file. So each Repeater Matrix field has it's main/index file, like those demonstrated above…

/site/templates/fields/test_matrix.php

```php
<?php
foreach($value as $item) {
  echo $item->render();
}
```

…and it also has dedicated template files for each item type:

/site/templates/fields/test_matrix/content.php

```
<h3><?= $page->headline ?></h3>
<p><?= $page->summary ?></p>
```

/site/templates/fields/test_matrix/quote.php

```
<blockquote>
  <p><?= $page->quote ?></p>
  <cite><?= $page->cite ?></cite>
</blockquote>
```

So now we can render our entire Repeater Matrix field with just this:

```
echo $page->render('test_matrix');
```

That's all for this week. Hope that you all have a great weekend and week ahead! Be sure to read more at the [ProcessWire Weekly](http://weekly.pw) tomorrow.
