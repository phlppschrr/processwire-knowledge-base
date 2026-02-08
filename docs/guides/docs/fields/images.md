# Unknown

Source: https://processwire.com/docs/fields/images/

This page outlines using and manipulating image fields — one of the most commonly used in ProcessWire.

To interact with the images field. Create a new field (under Setup > Fields) and call it whatever you want, like "images" for example. Set the field type as "image". Save. On the details tab, you may set the maximum quantity of images the field may contain. Please note that if you set it to one (1), the field will usually behave as a single image rather than an array of images, and this affects how you access it from the API. Add this new images field to a template (under Setup > Templates). Then edit a page using that template and upload some images.

### How to access the images field from your templates

In your template files, you can loop through the images field and output each image:

```
foreach($page->images as $image) {
  echo "<img src='$image->url'>";
}
```

If you set your images field to contain just 1 image, then the above wouldn't work because $page->images (which you would probably name $page->image, singular, instead) refers to just a *single* image.* Instead, you would do something like this:

```
if($page->image) echo "<img src='{$page->image->url}'>";
```

**Note for advanced users: the single image behavior described above is only applicable when output formatting is ON, as it is by default in template files. When output formatting is OFF, image fields always behave as arrays. *

When your image field is set to contain more than one image, $page->images is a [WireArray](/api/arrays/). You may use any of the functions provided by WireArray. For example:

```
// grab and output first image
$image = $page->images->first();
if($image) echo "<img src='$image->url'>";

// grab and output a random image
$image = $page->images->getRandom();
if($image) echo "<img src='$image->url'>";
```

### How to tell if a page has images present

It is a good idea to check if an image(s) field has something in it before attempting to output it. When set to contain multiple images, you can tell if a page contains one or more images by using the count() function:

```
if(count($page->images)) {
  // the page has one or more images
}
```

When set to contain a max of one (1) image, then you can just check if your image field has a value:

```
if($page->image) {
  // an image is present
}
```

## Resizing images

### ProcessWire will create your images at any size on the fly and then keep a cache of them.

For instance, lets say we want to cycle through all the images, create a large image at 500 pixel width with proportional height, and a thumbnail at 100x100, and then have the thumbnail link to the large:

```
foreach($page->images as $image) {
 $large = $image->width(500);
 $thumb = $image->size(100, 100);
 echo "<a href='$large->url'><img src='$thumb->url'></a>";
}
```

Note that when sizing an image, a new copy is created and cached, so that it doesn't have to be re-created every time. The table below shows all available image resize functions:

### Image resize functions

### ```

``````

```## ### ```

```## []()### ```

``````

```- [/docs/fields/](/docs/fields/)- [/docs/start/structure/fields/](/docs/start/structure/fields/)- [/docs/fields/dependencies/](/docs/fields/dependencies/)- [/docs/fields/repeaters/](/docs/fields/repeaters/)- [/docs/fields/textarea-fieldtype/](/docs/fields/textarea-fieldtype/)- [/docs/fields/select-options-fieldtype/](/docs/fields/select-options-fieldtype/)- [/docs/fields/images/](/docs/fields/images/)- [/docs/multi-language-support/multi-language-fields/](/docs/multi-language-support/multi-language-fields/)- [/docs/fields/ckeditor/](/docs/fields/ckeditor/)- [/docs/](/docs/)- [/api/ref/](/api/ref/)- [/docs/start/](/docs/start/)- [/docs/front-end/](/docs/front-end/)- [/docs/tutorials/](/docs/tutorials/)- [/docs/selectors/](/docs/selectors/)- [/docs/modules/](/docs/modules/)- [/docs/fields/](/docs/fields/)- [/docs/user-access/](/docs/user-access/)- [/docs/security/](/docs/security/)- [/docs/multi-language-support/](/docs/multi-language-support/)- [/docs/more/](/docs/more/)
