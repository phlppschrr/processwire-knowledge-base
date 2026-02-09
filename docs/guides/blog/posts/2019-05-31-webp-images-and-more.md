# WEBP image strategies, Google Client API, FormBuilder and more…

Source: https://processwire.com/blog/posts/webp-images-and-more/

## Sections


## WEBP image strategies, Google Client API, FormBuilder and more…

31 May 2019 by Ryan Cramer [ 2 Comments](/blog/posts/webp-images-and-more/#comments)

This week we’ll take a look at 3 different WEBP image strategies that you can use in ProcessWire 3.0.132+. Then we’ll dive into a major update for the Google Client API module, and finish up by outlining some useful new updates in FormBuilder.


## WEBP image strategies in ProcessWire

Last week we looked at the new [WEBP image support](/blog/posts/webp-images-in-pw/) built into ProcessWire, and if you haven’t read that yet, please do. This is part 2 of that post. This week we’ll dive in a little further and look at how you can take that WEBP support further. Most of this section centers around the new `webpAdd` ImageSizer option, which you can add to your /site/config.php file like this:

```
$config->imageSizerOptions('webpAdd', true);
```

This is an option that came via Horst’s pull request, but we didn’t discuss it in last week's post. What it does is tell ProcessWire to automatically create a WEBP image for every image variation. Meaning, you don’t have to call `$image->webp->url` in order to trigger the creation of a WEBP image, and it’ll instead get created automatically.

Why would you want WEBP images to be created automatically rather than as a result of you asking for one? Well, let’s say that you don’t want to have to think about or code for WEBP images in order to benefit from them. Maybe you just want your website to start serving up WEBP images automatically, without any changes in your code. That’s where this `webpAdd` option comes in handy.


### Strategy 1: Automatically delivering WEBP for JPG/PNG images

Just enabling the `webpAdd` option is what automates the generation WEBP images. But if you are looking for a turn-key solution, then you also want to automate the delivery of them as well. You can do this by adding some new rules to your .htaccess file that make it deliver the WEBP image rather than the JPG/PNG, when a WEBP version is available and supported by the browser. All credit for this solution goes to Horst. You would add the following to your .htaccess file, somewhere after the `RewriteEngine On` line.

```
# Send WEBP images for JPG or PNG when supported and available.
# This means that a request for a JPG or PNG file will instead deliver
# WEBP data, but only when the browser supports and understands it.

RewriteCond %{HTTP_ACCEPT} image/webp
RewriteCond %{REQUEST_FILENAME} -f
RewriteCond %{DOCUMENT_ROOT}/$1$2$3/$4.webp -f
RewriteCond expr "! %{QUERY_STRING} -strmatch 'nc=*'"
RewriteRule ^(.*?)(site/assets/files/)([0-9]+)/(.*)\.(jpe?g|png)(.*)$ /$1$2$3/$4.webp [L]
```

These rewrite rules will need adjustment if you are using `$config->pagefileExtendedPaths` (though I don’t think many are using that option).

If accessed with a “cache busting” URL (like those used in the admin) it will still deliver the original JPG/PNG image rather than the WEBP image. This is due to the second-to-last line containing the `strmatch` for `nc=*`. If you didn’t want that behavior, you could comment out or remove that line.

One drawback (or benefit?) to consider: If the user downloads the image for some purpose other than viewing it on the website, they probably won’t be able to because it’ll result in a WEBP image with a JPG or PNG extension. Plus, WEBP support is pretty limited outside of web browsers. This isn’t a problem for the websites I work on, and actually I think my clients might see it as a benefit (protecting their images). But others have expressed that could be potentially problematic for their case, so that’s something to consider before choosing this solution.


### Strategy 2: Delivering WEBP and automatically falling back to JPG/PNG

In strategy 1 we were still outputting JPG/PNG images in our markup, and the server was automatically converting them to WEBP images when available and supported. Strategy 2 takes the opposite approach and instead delivers URLs to WEBP images in the markup, but uses rules in the .htaccess file to automatically redirect them to their JPG/PNG equivalents when the client browser does not support WEBP. This solution is again thanks to Horst. Like the previous solution, you would place this in your .htaccess file, somewhere after the “RewriteEngine On” line:

```
# Output WEBP image URLs from ProcessWire, but redirect them to the  
# JPEG or PNG when the browser does not support WEBP.

RewriteCond %{HTTP_ACCEPT} !image/webp [OR]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{DOCUMENT_ROOT}/$1$2$3/$4.jpg -f
RewriteRule ^(.*?)(site/assets/files/)([0-9]+)/(.*)\.webp(.*)$ /$1$2$3/$4.jpg [R=307,L]

RewriteCond %{HTTP_ACCEPT} !image/webp [OR]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{DOCUMENT_ROOT}/$1$2$3/$4.png -f
RewriteRule ^(.*?)(site/assets/files/)([0-9]+)/(.*)\.webp(.*)$ /$1$2$3/$4.png [R=307,L]
```

Like with the previous solution, if you are using `$config->pagefileExtendedPaths`, you’ll have to make some adjustments here. With this strategy, you are letting WEBP take the lead on your site, and are falling back for the older browsers. It also doesn’t have the drawbacks of downloading a JPG/PNG image with WEBP content (if it matters to your situation). And we don’t really need to consider “cache busting” here either.

But there is one major drawback here and that is that it depends on us outputting the WEBP image in our markup, and thus means we’d have to update any API calls for `$image->url()` to instead use `$image->webp->url()`. Meaning, it’s not exactly a turn-key solution if we have to update lots of code to make it happen…

Thankfully in ProcessWire, we have [hooks](/docs/modules/hooks/). So if we want to use this WEBP-first strategy, we could instead hook to `Pageimage::url` and make it return the WEBP version rather than the JPG/PNG version, automatically! To do that, we’d add the following to our /site/ready.php file:

```
// output webp version for all $image->url() calls
$wire->addHookAfter('Pageimage::url', function($event) {
  static $n = 0;
  if(++$n === 1) $event->return = $event->object->webp()->url();
  $n--;
});
```

If we wanted to limit this behavior to just the front-end of our site, then we’d check that the current page template is not “admin”, before attaching the hook:

```
if($page->template != 'admin') {
  $wire->addHookAfter('Pageimage::url', function($event) {
    static $n = 0;
    if(++$n === 1) $event->return = $event->object->webp()->url();
    $n--;
  });
}
```

The reason we have to keep that `static $n` variable in there is that the `$image->webp->url()` method actually calls the `$image->url()` method too, so if we didn’t have that static `$n` variable keeping track of recursion depth, then we’d end up with an infinite loop!


### Strategy 3: Handling WEBP with markup instead

This is the strategy we mentioned in [last week’s blog post](/blog/posts/webp-images-in-pw/). Rather than relying on .htaccess rules or hooks, it instead relies upon the HTML5 `<picture>` element, letting the browser handle the use or fallback from the WEBP image. It’s quite a bit more verbose in terms of markup output and it’s definitely not a turn-key solution, at least not for existing sites, since it requires outputting very different markup than you otherwise might. But it is also a very simple and direct solution with no tricks or ambiguity, and might be just right for many.

```
<picture>
  <source srcset="<?= $image->webp->url ?>" type="image/webp">
  <img src="<?= $image->url ?>" alt="<?= $image->description ?>">
</picture>
```


### Troubleshooting WEBP

If you are having trouble getting your browser to recognize WEBP, it’s possible that you may need to add content-types for it to your .htaccess file and to your `$config->contentTypes`. At the top of your .htaccess file, you can add the following:

```
<IfModule mod_mime.c>
  AddType image/webp .webp
</IfModule>
```

And in your /site/config.php file, you can add the following:

```
$config->contentTypes('webp', 'image/webp');
```

The .htaccess update is for Apache and its communication with the browser, while the config.php update is for when ProcessWire is responsible for delivering the image, such as when they might be protected with the `$config->pagefileSecure` option.


## Google Client API module update

This week I released a new major version of the [Google Client API](https://github.com/ryancramerdesign/GoogleClientAPI) module that's been in development for the last couple of months. This module manages and simplifies the authentication and setup between Google service APIs and ProcessWire, and it is handled in the module settings. It handles the OAuth 2.0 configuration, enabling it all to be managed interactively.

The module also currently provides common API calls for Google Sheets and Google Calendar via dedicated classes, enabling a much simpler interface to these services than is available through Google’s client libraries. However, you can use any of Google’s APIs using OAuth 2.0 through this module. Here’s a [list of all the APIs you can use](https://developers.google.com/identity/protocols/googlescopes) via their scopes—there are hundreds of them.


### API usage example (Google Sheets)

```
// Get Google sheets
$google = $modules->get('GoogleClientAPI');
$sheets = $google->sheets();

// URL for the spreadsheet (copied from our browser)
$url = 'https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit#gid=SHEET_ID';

// Print out rows 1-5 from a spreadsheet
$sheets->setSpreadsheetUrl($url);
$rows = $sheets->getRows(1, 5);
print_r($rows);

// Create a new spreadsheet, add a header row and another row
$sheets->addSpreadsheet('Hello World');
$sheets->setRows(1, [ // set rows starting from row 1
  [ 'First name', 'Last name', 'Email', 'Age' ], // row 1: our header row
  [ 'Ryan', 'Cramer', 'ryan@processwire.com', 44 ] // row 2: example data
]);

// Append another row to the spreadsheet
$sheets->appendRow([ 'Karen', 'Cramer', 'karen@processwire.com', 39 ]);
```


## New FormBuilder version

It was only a couple of weeks ago that we had a major new version of FormBuilder. This week, we’ve got another update that builds upon it even more. This version is available for download now in the FormBuilder support board.


### New “save to Google sheets” action

Now you can configure FormBuilder to save submitted form entries into Google Sheets. In order to do it, you must have the new GoogleClientAPI module installed (the one mentioned in the previous section of this post). Saving entries into Google Sheets is really handy because you can assign access to other people to read and/or edit to the entries through Google, without giving them access to anything in ProcessWire. We are already using this to provide info to a shipping company. When someone requests a catalog from the website, their entry goes into Google Sheets and the shipping company automatically gets those updates and ships out catalogs, without us having to do anything. It makes for some great automation! [Screenshot of configuration screen](https://d1juguve2xwkcy.cloudfront.net/assets/files/2594/formbuilder-google-sheets.1200x0-is.png)


### New “remember input values in cookies” option

On the settings tab of any form (in the FormBuilder admin) you can now configure any form to remember input values for every field in the form so that as soon as the user inputs a value, it gets remembered in a cookie. No need for the form to be submitted. The result is that a user can start filling out a form, leave the page, and then come back later and everything they entered will still be there. This is useful for longer forms so that there’s no chance of the user losing their work, but it’s also useful for sites that have forms that a user might submit multiple times, such as information request forms for different products, etc.


### Stripe payments: Saving cards and recurring payments

A new version of the Stripe payments module was released with this latest FormBuilder update as well. Like the previous version, this one enables you to use FormBuilder forms to process card payments with Stripe. But it also now does a lot more…

**Save cards for later charging** This new version goes much further and now enables you to save the payment method in Stripe so that you can charge it later. This creates a “Customer” in Stripe that you can go in and add charges to at any time. This is useful for cases like booking engines where you don’t want to charge their card until you can confirm the availability of the property. It’s also useful for cases like product orders, where you don’t want to charge the card until the order actually ships. It’s also useful for cases where you might need to make multiple independent charges to the same card to represent different stages in an order (deposit, 1st payment, 2nd payment etc.) These are just examples of how this feature can be useful.

**Recurring payments/subscriptions** In addition, this new version of the Stripe payments for FormBuilder module adds support for recurring payments or subscriptions. Now you can use a FormBuilder form to setup a recurring payment that is automatically charged once monthly, or whatever frequency you choose. In Stripe this is referred to as a Subscription. Whenever you create a subscription, you also create a “Customer” that you can independently manage in Stripe.

Thanks for reading, and hope that you have a great weekend! Visit the [ProcessWire Weekly](https://weekly.pw) for the latest news and updates, with new issues posted every week.
