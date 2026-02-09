# New Repeater and Repeater Matrix features

Source: https://processwire.com/blog/posts/new-repeater-and-repeater-matrix-features/

## Sections


## New Repeater and Repeater Matrix features

22 October 2021 by Ryan Cramer [ 1 Comment](/blog/posts/new-repeater-and-repeater-matrix-features/#comments)

This week we have some very useful new additions to both the core Repeater Fieldtype and the ProFields Repeater Matrix Fieldtype. This post covers all the details along with a couple of brief demonstration videos.


### Overview

In [last week's forum post](https://processwire.com/talk/topic/26236-pw-30186-%E2%80%93%C2%A0core-updates-repeaters/) I showed you some updates to the core Repeater Fieldtype in ProcessWire 3.0.186, which now supports the ability to insert new items before or after existing items, briefly demonstrated in the video below:


### Inline cloning

This week (ProcessWire 3.0.187), the core repeater was also updated to support inline cloning. Previously when you cloned a repeater item, it would always go to the end. Now it clones directly below (or above when appropriate) the item being cloned.


### Repeater Matrix updates

These new features are useful in the Repeater Fieldtype, but they are potentially even more so when used with the [Repeater Matrix](/store/pro-fields/repeater-matrix/) Fieldtype. So this week, Repeater Matrix was also updated to support insert before/after as well as inline clone.

But that's just for starters. Repeater Matrix also added support for different "add item" types. Previously it only supported a list of links at the bottom with the different types you could add. Now it supports new Select, Images, and Custom options:

The "Select" option now replaces "Links" as the new default option. If you want to use the "Images" option, then you just need to supply an image file to represent each type. Both the "Select" and "Images" options are demonstrated below, along with insert before/after and inline-clone options.

Note that the image examples in the video I extracted from a screenshot posted by Ivan Gretsky in the Repeater Matrix forum, as they seemed like good examples to test with. His screenshot actually had a lot of other types in it too. But you can create and add any images you want to represent your Repeater Matrix types.


### Matrix type groups

In the "Select" example from the video (the first half of the video), note that I'm also demonstrating another new feature: Matrix Type Groups. When your matrix type labels are in the format “Group > Label” then all matrix types sharing the same “Group” get displayed under the same option group in the select. This can be useful if you have a lot of related matrix types that are helpful to group together. In my example, I'm just using "Text" and "Image" groups, but presumably a real-world case for groups would likely use more.


### Custom icons for repeater types

Another thing you might notice in the video is the use of custom icons for repeater items. When you define your repeater matrix types, you can also specify the icon to use in the header setting. When specified, it gets used instead of the default arrows icon.


### Custom add-new option

What's not demonstrated in the video is a new "Custom" option for how users can add new repeater matrix items. This option lets you use a hook to have complete control over the add-new output, something that's been requested for quite awhile. When you select this option in the matrix field configuration, it provides you with the example hook implementation below, which you place in your /site/templates/admin.php file and then edit to get your desired output:

```
$wire->addHookAfter("InputfieldRepeaterMatrix::renderAddMatrixCustom", 
  function($event) {
    $style = "display:inline-block;background:#ccc;padding:40px;margin:5px"; // example
    $out = "";
    foreach($event->arguments(0) as $type) {
      $out .= "<a href='$type[href]' style='$style'>$type[label]</a>";
    }
    $event->return = [ "Select type to add", $out ]; // headline, output
  }
);
```

The example is intentionally simple and self contained, so it uses a simple style attribute to drive what it does. But for those actually using this, I'm guessing you may use more custom markup or add a custom stylesheet to $config->styles, custom images, or any number of things... there are no limits here. Your custom output will display in the same modal selection window that the "Images" option output appears in.

In addition to the updates mentioned here, both Repeater and Repeater Matrix also have other small improvements both on the code side and on the configuration side.


### Requirements

These updates require the newest dev version of Repeater Matrix which will be posted to the ProFields download section this weekend. Because many of the updates are also inherited from the core Repeater, it will also require ProcessWire 3.0.187 (current dev branch) or newer.


### What’s next?

Still on the to-do list for Repeater Matrix is to add the ability to control what item types are allowed where, kind of like the Family settings on page templates.

In both Repeater and Repeater Matrix, I plan to update the current clone feature to support a "Copy" option, enabling you to copy/paste repeater items from one page to another. This is something that I think may already be possible with a 3rd party module, but seems like it would be useful to support natively with the current clone option. There are more items on the to-do list as well, but those mentioned here are likely the next two.

That's all for this week! As always, keep up to date with [ProcessWire Weekly](https://weekly.pw) for the latest ProcessWire news and updates. Thanks for reading and have a great weekend.
