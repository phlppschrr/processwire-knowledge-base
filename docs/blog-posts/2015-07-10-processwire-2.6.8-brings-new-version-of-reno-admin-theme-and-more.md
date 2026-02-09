# ProcessWire 2.6.8 brings new version of Reno admin theme and more

Source: https://processwire.com/blog/posts/processwire-2.6.8-brings-new-version-of-reno-admin-theme-and-more/

## Sections


## New version of Reno admin theme and more

10 July 2015 by Ryan Cramer [ 13 Comments](/blog/posts/processwire-2.6.8-brings-new-version-of-reno-admin-theme-and-more/#comments)


## ProcessWire 2.6.8

This week we're excited to bring you a new version of the Reno admin theme that offers a lot of nice refinements and new features. Special thanks to Tom Reno for these updates, and for writing about them in this blog post. Also thanks to Pete Burlingham (Pete) for making it possible to specify your own color themes with the Reno admin theme, writing about it here, and sharing the great new color themes that he's created.

In addition to the Reno admin theme updates, we also have several useful new methods added to the core API in 2.6.8 – we think you may find them useful. Hope that you all have a great weekend and week, and remember to check out the [ProcessWire weekly](http://www.flamingruby.com) on Saturday morning. *–Ryan*


### New version of the Reno admin theme

*Author: *[Tom Reno](http://www.tomrenodesign.com)

Hello all, Tom Reno (Renobird) here. This weeks additions to the dev branch include some major updates to AdminThemeReno. If you aren't familiar with AdminThemeReno, it's a core admin theme that ships alongside the ProcessWire default admin. Ryan asked if I would give a guided tour of the more prominent changes/features:


### Sidebar retains open/closed state

Previously if you opened or closed the sidebar it didn't retain that state when you navigated to a new page. The latest version now uses local storage to save the open/close state of the sidebar and retain its state on a per user basis. For device widths less than 690px, the sidebar defaults to closed so you don't have the sidebar taking up potentially the entire screen on each page view.

In addition to using the sidebar toggle icon (now located to the right of the ProcessWire logo), you can also open or close the sidebar with the right/left arrow keys.


### Search input is now a masthead overlay

The admin search is a powerful way to quickly find pages or other resources you need. In the previous version of AdminThemeReno, the search input was a part of the masthead, and contained placeholder text like "Type here to search...". It took up a decent amount of space, and despite its prominence, I found that many users simply overlooked it. The latest version now has the magnifying glass icon in the top navigation, and when clicked/touched the search input slides down to overlay the masthead. This might sound like it takes more clicks to get to the search, but actually it takes the same number as before (one) since the input is automatically focused when visible. The overlay can be closed with the (x) icon, pressing the up arrow key, or by clicking anywhere on the page except the search results.


### User display name is now configurable

The module settings now allow you to specify any text fields associated with user template(s) for use as the user's display name in the masthead. For example, if your user template has the fields `first_name` and `last_name`, you can now use those fields as the display name, instead of the name field. I've found this particularly useful, as our usernames are numeric.


### Support for multiple user templates

User images and display name now support multiple user template(s). If you have [more than one user template defined for creating users](/blog/posts/processwire-core-updates-2.5.14/#multiple-templates-or-parents-for-users), the module configuration will now pick those additional templates and allow you to customize the image field and display name for each of them individually. I don't suspect this will be a commonly used feature, but it's nice to support it, and while implementing I discovered a nice use for it myself.

Thanks to Benjamin Milde (LostKobrakai) for requesting this feature.


### Custom Color Schemes

You can now define your own color schemes in: /site/modules/AdminTheme/AdminThemeReno/styles/.

These files survive PW updates, so you can easily create custom variations on the theme without having to reinstall it after an update. The screenshot below shows the 3 default colors, and some additional color schemes that Pete created, that I also have installed. [See and download Pete's color themes further down in this post]

Thanks to Pete Burlingham (Pete) for contributing this feature.


### Top navigation quicklinks to common ProcessWire resources

This menu item is currently only visible to Superusers, but I plan to make it configurable to specific roles in a future release.


### Top navigation items are now hookable

While its always been possible to add items to the sidebar by creating new admin pages, or by specifying [Process module navigation](/blog/posts/processwire-2.5-updates/#how-to-expose-navigation-from-your-process-module), you can now add/modify/remove items in the top navigation using a [hook](/api/hooks/), like the following in your /site/templates/admin.php file:

```
wire()->addHookBefore("AdminThemeRenoHelpers::topNavItems", function($event) {

  // Get the $items array passed to the topNavItems method
  $items = $event->arguments("items");

  // Setup the new parent item.
  $newItem = array(
    "class" => "test",
    "label" => "<i class='fa fa-file-text-o'></i>",
    "link" => "http://google.com",
    // Setup any children this item will have.
    // Note: children are not required (can omit for single items).
    "children" => array(
      "Google" => "http://google.com",
      "Github" => "http://github.com",
      "ProcessWire" => "http://processwire.com"
    )
  );

  // Add new item at the beginning of the array
  array_unshift($items, $newItem);

  // populate updated items back to hooked method
  $event->arguments("items", $items);
});
```


### Styling for new System Notifications Module

Last but not least, the theme has some updated styles to support the core System Notifications module.


### Admin Theme Reno Roboto Colours

*Author: *[Peter Burlingham](https://www.notanotherdotcom.com)

As per Tom's updates mentioned above, custom colour schemes for the Reno admin theme are possible and survive core upgrades on the latest dev branch release: 2.6.8.

I created some custom colours a while back but was waiting for the right time to release them - i.e. when the code was in place so that you could place them in: /site/modules/AdminTheme/AdminThemeReno/styles/.

Simply update to 2.6.8, [download the attached zip file](/site/assets/files/1141/robot-styles.zip), create the folder path above, install/configure the AdminThemeReno module and you'll see the four additional colour schemes - Red Robot, Green Robot, Blue Robot and Purple Robot. "Why Robot?" you may ask - because it uses Google Fonts' Roboto font so it made sense to me.

I originally created one of these when learning SCSS last year and, since the SCSS files are in the Reno admin theme folder, you too can now create new colour schemes, stick them in the above folder and release them to the community if you like.

[[clear]]


## New core API methods in 2.6.8


### New $pageimage->maxSize($width, $height) method

ProcessWire comes with several methods enabling you to resize images on-the-fly for output. For instance, one of the most used is the `size()` method, which you might use in a context like this:

```
$image = $page->images->first();
$thumb = $image->size($width, $height);
echo "<img src='$thumb->url' alt='$thumb->description' />";
```

The returned `$thumb` is an image that is exactly the `$width` and `$height` dimensions, cropped as needed to reach those dimensions (to ensure no stretching of proportions).

In some cases, you just need an image that you know will fit within a container of a specific width and height, but you don't want any cropping to take place. For example, you wouldn't want any cropping to take place on an image of a company logo. For this particular need, we've added the new `maxSize()` method, which works like this:

```
$thumb = $image->maxSize($width, $height);
```

This will return an image no larger than the given dimensions, *without cropping or anything that would modify the proportions.* Of course, this also means that it's likely one of the dimensions (width or height) will be less than what you asked for, since nothing can be cropped.

This new method accompanies the existing `$pageimage->maxWidth()` and `$pageimage->maxHeight()` methods that have already been in the core. But those methods weren't particularly convenient for images placed within fixed size containers – if the image was particularly wide or tall, you would have to perform two resizes, or check the dimensions ahead of time to determine whether you needed a maxWidth() or a maxHeight() call. This new maxSize() method will save you the time and trouble.


### New $session->forceLogin($user) method to login user without a password

If you've used ProcessWire's `$session->login($username, $password)` method before, you know that it won't let you login any user without also having their password. This is good from a security standpoint, but also a pain in some cases. For instance, when you are needing to perform any kind of automation, such as executing API-side tasks from a user account without them being there, or delegating to an external authentication service, among other things.

There are a lot of API-side use cases for needing to login a user without having them there to type the actual password. For these cases, we've added the new `$session->forceLogin($user);` method, which automatically logs in the given user and keeps them logged in for that session until they logout or you call `$session->logout()`.

The `$user` that you pass to `$session->forceLogin($user)` can either be a User object or a username. On success, it returns the User object, and on failure it returns null.

Worth mentioning is that it was possible to do this before, but not very easily. You had to hook to `Session::authenticate`, and make it return either true or false according to your own logic. The new `$session->forceLogin($user)` provides a more straightforward path to logging in a user without a password. Though there may still be instances where you would want to use the existing Session::authenticate hook, so that of course will be sticking around too.


### New $this->halt() method for use in template files

Sometimes you need to stop a page from delivering further output. An example would be a page that can serve both ajax and regular HTML content. If you detect that you've received an ajax request (`$config->ajax == true`), you might output some JSON rather than the usual HTML output. Following that, you need to prevent any additional output, whether from the current template file, or from `$config->appendTemplateFile` or whatever else might come next.

It used to be that the simplest path to do this (stop execution and thus output) was to use a PHP `exit()` or `die()` function, which isn't terribly elegant, but it gets the job done. The only issue is that PHP stops after that, and ProcessWire's normal shutdown process doesn't get to proceed as planned. Though we've never actually seen any issue with this approach, we wanted something better, especially since last week we introduced a new /site/finished.php file that you could use to tap into the shutdown process. And we want to make sure that it really does get called on every request. So we had to come up with another way to halt all output, without halting execution (the normal shutdown process).

Now you can call `return $this->halt();` from within any template file, and it will prevent further output from that template file (and anything that comes after it, like an appendTemplateFile). This enables output to stop, but PW's normal execution and shutdown process to proceed normally. Please note that `return $this->halt();` must be called from directly within the template file, outside of any function or class scope.


### New $page->createdStr and $page->modifiedStr

You may be familiar with the `$page->created` and `$page->modified` properties, which return the date created and date modified for the given page, in unix timestamp format.

The `$page->createdStr` and `$page->modifiedStr` return the same thing as $page->created and $page->modified, except that they are a formatted string rather than a unix timestamp. The format used is the system date format, specified with `$config->dateFormat`.

Of course, you have always been able to format the created/modified dates however you want just by passing the created/modified value to PHP's `date()` or ProcessWire's `wireDate()` function, but hopefully these new shortcut properties provide a nice convenience for some occasions.
