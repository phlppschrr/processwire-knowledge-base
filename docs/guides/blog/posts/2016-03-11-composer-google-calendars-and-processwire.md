# Composer, Google, Calendars and ProcessWire

Source: https://processwire.com/blog/posts/composer-google-calendars-and-processwire/

## Sections


## Composer, Google, Calendars and ProcessWire

11 March 2016 by Ryan Cramer [ 6 Comments](/blog/posts/composer-google-calendars-and-processwire/#comments)

This week we've been focused on one of the major 3.x roadmap items, which is to have strong Composer support in ProcessWire. In this post, we now have an outlined process and a full proof-of-concept module built to demonstrate it all, plus info on how other module authors can support Composer as an alternative installation method. To add to that, we get into Google's Client API with a new 3.x specific module and how to connect Google's Calendar services with ProcessWire.


## ProcessWire and Composer


### Finding a place for Composer in the PW ecosystem

I personally haven't experienced a lot of the benefits of Composer because the type of sites/apps I build rarely have 3rd party dependencies, and when they do, they are already part of the ProcessWire ecosystem. I suspect this is likely the case for many of us. Though I don't think it's the case in the larger PHP community outside of our ecosystem. ProcessWire already manages its own 3rd party libraries (modules) and dependencies in a manner more targeted to PW, so the case for Composer has always been a bit of a hard sell in our context.

Still, I've always stood on the side admiring what Composer did (and what some of you are doing with it), but never quite able to find a useful place for it in my own workflow. Yet, if ProcessWire is going to have strong Composer support in 3.x, then it's got to become part of my workflow too... otherwise how am I going to support it? So I've been waiting around looking for a good use case to implement Composer further in PW3, and this week one appeared. So I jumped at the chance and enthusiastically moved forward with it.

What I found is that once you do get Composer into your workflow, the case becomes more compelling in ProcessWire, even if you thought it appeared a little redundant from the outside. Composer support is something more than just point to be met on our roadmap. There are some people that will benefit significantly from using it, and some that won't benefit at all, but either way it's something to open yourself up to in ProcessWire. Sooner or later you will find a strong use case for it, especially if bringing other 3rd party libraries into PW. I also think PW recognizing and supporting it has potential to drive a lot more PHP developers to the project.


## Using Composer


### The Google Client API module

Today I'm releasing a new module ([GoogleClientAPI](https://github.com/ryancramerdesign/GoogleClientAPI)) that demonstrates how Composer can be beneficial in ProcessWire. It's a module that would have been a lot trouble to build and maintain without Composer, due to its 3rd party dependencies. So it ends up being that use case I was looking for in order to really dive in to our Composer support.

The purpose of the module is not just to demonstrate Composer in ProcessWire though. The module is something I've needed and something I know others have too. It is a Google Client API module that enables you to connect your site with various Google web services via OAuth2. It picks up where [Google's own PHP client](https://github.com/google/google-api-php-client) leaves off, managing the connection to a Google account, maintaining the access and refresh tokens, and more. Handling this with only Google's API client library has been a pain (as I've used it on a few occasions in the past), and this GoogleClientAPI makes it a whole lot simpler and more bulletproof.

Where might you use this GoogleClientAPI module? Google provides a lot of different web services that you could use it with, but my own primary use case has been with [Google Calendar](https://calendar.google.com). So that's also my primary focus for this module in the tutorial below.


### Live examples

It helps to see what we're talking about. Here's a few examples of of the Google Client API module implemented with with Google's Calendar service:

- [Washington Waldorf School Calendar​](http://www.washingtonwaldorf.org/calendar/)
- [Wye River Upper School Homepage](http://www.wyeriverupperschool.org/) (scroll to School Calendar)
- [Wye River Upper School Calendar](http://www.wyeriverupperschool.org/tools/calendar/2016/2)

There's no eye candy here, but the benefits of pulling from Google's services (like Calendar) aren't so much in the output of examples like this, but instead in the fact that their website is connected to a bigger ecosystem. An ecosystem the client can manage in various places and with various people, various devices and so on. A service like Calendar can also be subscribed to by other users and is generally a lot more broadly "connected" than an individual website would be. Being able to make the website part of that bigger network of activity is a real benefit to clients. And the fact that it's essentially free, while more capable and powerful than almost any paid option is definitely a mountain of icing on the cake.


### Successor to MarkupLoadGCal

While GoogleClientAPI can use more than just Google's calendar services, it was the calendar services that motivated its development. Some of you might remember a previous module of mine called [MarkupLoadGCal](https://github.com/ryancramerdesign/MarkupLoadGCal), which enabled one to pull events from a Google Calendar and display them in a site using your own markup.

The problem with that module was Google's changing strategy. In 2014 they dropped the publicly accessible verbose feeds to Google Calendar, leaving just the basic feed. So MarkupLoadGCal was updated with a reduced feature set to accept that limitation and just use the basic feed. Then just recently, they dropped the basic feed, leaving the MarkupLoadGCal module unable to read from anything, making it useless.

Now the only way to access a Google Calendar is with an OAuth2 authenticated account to Google using their Client API library – a lot more trouble! Though I really can't complain, as these Google services have always been free, so some "having to work with the system" is fine. Though using an authenticated account opens up the possibility of not just reading data, but writing it too. We won't get into that in this post, other than to say that the option is there if you need it.


### Installing the module with Composer

In this section, we'll use the GoogleClientAPI module as an example, but this can be replaced with any ProcessWire module available on Packagist. I'm not sure there are any others at the moment, but hopefully that will change when modules move to exclusive ProcessWire 3.x versions perhaps later this year. The tutorial here requires ProcessWire 3.x, as does the GoogleClientAPI module.

**1. Install Composer and ensure your composer.json file is up-to-date. **

**2. Install the GoogleClientAPI module with Composer. **

Once Composer is installed, open a terminal to the root of your ProcessWire installation (where the index.php file is located), and execute the following command:

```
composer require processwire/google-client-api
```

The above command installs the ProcessWire GoogleClientAPI module and all required dependencies. There's also a little bit of magic going on here that may not be immediately obvious, thanks to the work of Hari KT. We'll cover some more details on that further down in this post.

**3. Enable the GoogleClientAPI module in ProcessWire.**


### Setting up your Google API account and connecting it to your site

**1. Go to [console.developers.google.com](https://console.developers.google.com) and login. **

**2. Once API access is enabled, click to "Create a new project."**

**3. Next, at the "Add credentials to your project" screen…**

**4. Click the "What credentials do I need?" button… **

**5. On the "Set up the OAuth 2.0 consent" screen…**

**6. Now you will be on the "Download credentials" section.**


### Configuring the Google Client API module

**1. Back to your PW admin > Google Client API module settings. **

**2. It will now take you to a Google authentication page.**

**3. If everything was successful… **


### Setting up Google Calendar

**1. While logged into your Google account, open [Google Calendar](https://calendar.google.com). **

**2. Go to the calendar settings**


### Adding the calendar to your website

With everything setup from the Google side, and with your GoogleClientAPI module now installed, you are ready to work with the calendar from the ProcessWire API.

You may already have a place in mind where you'd like you calendar to go, in which case start editing the appropriate template file. Otherwise, open an existing template file to test with, or create a new one. For instance, I have created /site/templates/calendar.php, and likewise created a page called /calendar/ in my site that uses this template.

The following code in your template file will enable you to list events from the calendar. Note the first line with the Calendar ID, which you should copy/paste from Google Calendar. Or if using the primary calendar, you should make your `$calendarID` be 'primary'.

```php
<?php
$calendarID = 'en.usa#holiday@group.v.calendar.google.com';
$google = $modules->get('GoogleClientAPI');
$events = $google->getCalendarEvents($calendarID);
echo "<h3>Upcoming events</h3><ul>";
foreach($events->getItems() as $event) {
  $summary = $sanitizer->entities($event->getSummary());
  $date = $event->start->dateTime; // date AND time
  if(empty($date)) $date = $event->start->date; // just date
  echo "<li>$summary ($date)</li>";
}
echo "</ul>";
```

The above is a really simple example of using Google's Client API to list events in a calendar, but of course much more is possible. After implementing calendars with it on a few sites, I found a lot of things that could be further simplified and abstracted from Google's API, and have included a new module for that purpose called [MarkupGoogleCalendar](https://github.com/ryancramerdesign/GoogleClientAPI/blob/master/MarkupGoogleCalendar.module). It's included with the GoogleClientAPI module as an example of implementation. We'll take a look at using that module next.


### Calendars made easy: the MarkupGoogleCalendar module

The MarkupGoogleCalendar module comes with the GoogleClientAPI module and serves as a demonstration of using the Google Client API. However, if you are implementing a calendar in your site, I think you'll find it much nicer and simpler to use the MarkupGoogleCalendar module rather than the GoogleClientAPI module directly. That's because it handles most of the mundane details like date conversions, entity encoding, and converting events to markup.

Note that the MarkupGoogleCalendar module uses the GoogleClientAPI module, it just abstracts a lot of the usual work away so that implementing a calendar becomes even simpler. Here's how to use the MarkupGoogleCalendar module:

**1. Install the MarkupGoogleCalendar module **

**2. Copy the event template file (optional, recommended):**

**3. Add the Calendar API code to a template file**

Open any template file where you want to place the calendar output, and add the following:

```php
<?php
$cal = $modules->get('MarkupGoogleCalendar');
$cal->calendarID = 'en.usa#holiday@group.v.calendar.google.com';
echo $cal->renderUpcoming(10);
```

The above would render the next 10 upcoming events. Change out the 'calendarID' to be the ID of the calendar you want to display.

**4. Take a look at that /site/templates/_mgc-event.php file**

**5. Want to render all the events for a given month?**

Here's how you'd do that for the month of April 2016:

```
echo $cal->renderMonth(4, 2016);
```

There is a lot more you can do with MarkupGoogleCalendar! The module includes several other convenience methods and properties that you can customize, so be sure to take a look at the [module documentation](https://github.com/ryancramerdesign/GoogleClientAPI#markup-google-calendar-module) if you decide to use it.


## More on ProcessWire and Composer


### Analyzing the benefits

The tutorial above begins by guiding you through installing a ProcessWire module with Composer, something that is new with ProcessWire 3.x. (Though it was possible in previous versions of ProcessWire as well, with a little more setup on your part.)

This installation method made a lot of sense for the GoogleClientAPI module because it has dependencies on Google's official google-api-php-client library, which in turn has several dependencies of it's own. But we didn't have to bundle any of these dependencies with the GoogleClientAPI module, nor did you have to install them yourself. Instead, Composer took care of all of it, and it will likewise take care of keeping them up-to-date. That's where Composer really starts to become compelling.

Admittedly, there aren't a lot of modules that have these kinds of dependencies in ProcessWire. But I've been looking for a good opportunity to explore how such a scenario would be handled in ProcessWire, especially since we are now officially supporting Composer in ProcessWire 3.x. The GoogleClientAPI module turned out to be a very good test and example.

If there are other current and/or future modules that also have dependencies on libraries available through Packagist, then the Composer installation method proves to be a very simple and useful way to maintain them. Though even if a module has no external dependencies, the Composer installation method is still worthwhile. I think it's something we should strive to support in all PW 3.x modules, as an alternative installation method for those that wish to use it. If you are a module developer, I'll cover how you can support it further in this post.


### How is it possible to install and update modules with Composer?

Installation of modules via Composer is thanks to the handiwork of [Hari KT](http://harikt.com/blog/2013/11/16/composer-support-for-processwire-modules/) ([@harikt](https://twitter.com/harikt)). He devised a [clever system](https://github.com/harikt/pwmoduleinstaller) whereby ProcessWire modules could be installed with Composer, while stepping outside Composer's usual boundaries ([related blog post](http://harikt.com/blog/2013/11/16/composer-support-for-processwire-modules/)). Usually when libraries are installed in Composer, it keeps them all under a /vendor/ directory off of your installation root. But when your module lists `hari/pw-module` as one of its dependencies, and `pw-module` as the "type" in the composer.json file, Composer treats the installation differently, completing the installation in ProcessWire's /site/modules/ModuleName/ rather than /vendor/.

This is the bit of magic that is taking place behind the scenes. Huge thanks to Hari KT for coming up with this Composer installation method… something that he did a couple of years ago actually. I think ProcessWire 3.x is the time for us to start putting it to good use for those that want to maintain their modules with Composer. As a result, we'll be officially documenting and supporting this installation method as an alternative from this point forward in ProcessWire 3.x.


### How else might you benefit from Composer in ProcessWire?

If your site/application ever needs any external libraries available through [Packagist](https://packagist.org/), you can have composer maintain them for you in the same way that it did for the GoogleClientAPI module. You would just install it from the command line like you did in the tutorial above, replacing "vendor/package" with the vendor and package name of the library you want to install:

```
composer require vendor/package
```

Once you've done that, you can call upon the library from anywhere in ProcessWire, whether in your template files, modules, hooks, etc. It's basically available for your use from anywhere. And like many ProcessWire modules, it doesn't actually get loaded in memory unless you call upon it.


### When will ProcessWire itself be available through Composer?

When ProcessWire 3.0 is released as the new stable branch, it will likewise become available through Packagist (and thus installable by Composer). Meaning, you'll be able to install ProcessWire like this, when it suits your need:

```
composer require processwire/processwire
```


### Git tags and Packagist

Some have asked about the use of git tags on the ProcessWire core. In the past we haven't given much focus to them because there wasn't any particularly compelling reason to do so. (Other than perhaps for past version download links.) Packagist changes that, as it's the means by which it is best able to identify the version, and thus identify when something needs an update. That's a very strong reason to maintain granular tags with each version, regardless of how major or minor. So you'll see us adopting this strategy as soon as the core is on Packagist and thus installable via Composer.


## Composer for module developers

We encourage all modules designed for ProcessWire 3.x to support Composer as an alternative installation method, and it's really quite simple to add this support. We'll cover the few steps necessary below.


### Three easy steps + one optional step

**1. Add a composer.json file as part of your module's files.**

Using the following as your template/starting point:

```
{
  "name": "your-vendor-name/your-module-name",
  "type": "pw-module",
  "description": "Description of module",
  "keywords": [ "processwire", "module" ],
  "homepage": "http://modules.processwire.com",
  "license": "MPL-2.0",
  "authors": [
    {
      "name": "Your Name",
      "email": "you@domain.com",
      "homepage": "https://domain.com",
      "role": "Developer"
    }
  ],
  "require": {
    "hari/pw-module": "~1.0",
  }
}
```

Properties above that you'll want to update specific to your module are: name, description, homepage, license, and authors. You'll also want to append any other "require" dependencies when applicable.

Note that the "type" of `pw-module` and the "require" line containing `hari/pw-module` are needed in order for the module to be installable via Composer, so make sure you keep those.

**2. Upload and maintain your module at GitHub or BitBucket.**

**3. Put your module on Packagist. **

**4. Connect Packagist with GitHub (or other service). **


### Module version numbers and Git tags

You'll have to maintain your module version number not only in your ProcessWire `getModuleInfo()` array, but also with Git tags. This is because Composer and Packagist don't know about the ProcessWire module conventions, and instead can use Git tags in order to identify version numbers. You'll want to use [Semantic Versioning](http://semver.org/), or something that looks like it, which means versions in the format `1.2.3` or `v1.2.3`. The following is [quoted](https://packagist.org/about#managing-package-versions) from packagist.org:

The easiest way to manage versioning is to just omit the version field from the composer.json file. The version numbers will then be parsed from the tag and branch names. Tag/version names should match 'X.Y.Z', or 'vX.Y.Z', with an optional suffix for RC, beta, alpha or patch versions. Here are a few examples of valid tag names:

```
1.0.0
v1.0.0
1.10.5-RC1
v4.4.4beta2
v2.0.0-alpha
v2.0.4-p1
```

In your module's getModuleInfo() array, if your 'version' property is using the `X.Y.Z` (string) version format, then you can use the same for your Git tag. If you are using an integer for your 'version' property, we suggest translating them to your Git tags as follows:

```
1 = 0.0.1
12 = 0.1.2
123 = 1.2.3
```

This is consistent with how ProcessWire translates integers to 3-part version numbers. If you outgrow the bounds of what is supported by an integer version number, you can always switch to an `X.Y.Z` string.


### How to tag a version number for your module

To tag a version number just open a terminal window to your module source code and make sure you are on the branch/commit that you want to tag. Then type the following:

```
git tag 1.0.0
git push origin --tags 
```

The first line above adds the tag "1.0.0", which you'll want to replace with your actual version. The second line pushes it to the remote repository.


### Modules directory support for Composer

Once ProcessWire 3.x is stable (or sooner if possible), the Modules directory will be updated to automatically identify composer.json files from your module repositories and indicate that as an installation option for modules that support it.
