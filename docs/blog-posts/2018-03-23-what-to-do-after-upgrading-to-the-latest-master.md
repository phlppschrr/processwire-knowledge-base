# What to do after upgrading to the latest master

Source: https://processwire.com/blog/posts/what-to-do-after-upgrading-to-the-latest-master/

## Sections


## What to do after upgrading to the latest master (3.0.96)

23 March 2018 by Ryan Cramer [ 7 Comments](/blog/posts/what-to-do-after-upgrading-to-the-latest-master/#comments)

With the new master version released last week, I'm happy to report we've had lots of positive reports. I also upgraded several client sites this week, and it's been a very smooth upgrade process. We haven't had any major bug reports in the new version, so I've mostly been tweaking small details here and there on the dev branch, but not enough to warrant a version bump, so we'll save 3.0.97 for next week.

Having upgraded a few sites this week to 3.0.96, I wanted to recommend a few additional steps that will help you take advantage of some of the new features:


### Install AdminThemeUikit

The new Uikit admin theme is automatically installed and set as the default when creating a **new** ProcessWire installation. But for **existing** PW installs that you upgrade, you'll need to install it if you want it. Go to Modules > Install > AdminThemeUikit. Once installed, you may want it to be the admin theme used by your login screen, in which case check the box for that in the module configuration. Next, to make it your admin theme, you'll need to select it from your user profile. Recommended: If you want to make it the default admin theme for new users, as well as other users that haven't chosen a specific one in the past, edit your /site/config.php file and add this:

```
$config->defaultAdminTheme = 'AdminThemeUikit';
```


### Install animated GIF support

ProcessWire now supports resizing, cropping and manipulation of animated GIFs, so long as you have the new core ImageSizerEngineAnimatedGif module installed (developed by Horst). Because it's now in the core, simply go to Modules > Install > ImageSizerEngineAnimatedGif. We will likely set this one to auto-install shortly too.


### Enable focus+zoom for image fields

This new version of ProcessWire has the new focus featured enabled by default. I also like to enable the zoom feature that accompanies it, and that is not enabled by default. To enable it, edit your image fields (Setup > Fields > your_images_field), click the *Input* tab, and you'll see an option to enable **focus+zoom**. Click that radio button and save. Now you should have both focus and zoom support.


### Install ImageMagick support (if available)

While ImageMagick isn't new to 3.0.96, it might be a good time to check if you've got this installed or not. If your server supports it, it offers some nice performance improvements when installed. Many servers don't have it, but it's worth a try—click to Modules > Install > ImageSizerEngineIMagick. If your server doesn't support it, then it'll give you an error message and refuse to install, no problem. But if it's there, it's worthwhile to use it.


## Developing for and with ProcessWire

This week I also shifted gears to focus on some pending client work. I'm developing a site for a non-profit science/research related project with a lot of data, resembling some of the first sites I ever developed in ProcessWire (v1.0), now 10 years ago. It was the experience with those sites that had real influence on ProcessWire's architecture and emphasis on scalability when it came to developing ProcessWire 2.0 in 2010. I don't think about it often, but for whatever reason this new project made me reflect a bit on how far we've come. So it's really fun to come back to this kind of project, ready-to-go with a brand new version of ProcessWire. For me, it puts light on the evolution of ProcessWire as a tool over the last 10 years.

Everything has evolved so much, yet the original intentions are all still there. Just to name a few of them: fun and powerful API, every bit of data easily accessible as if it was already in memory, plugin modules for field types and input, flexible and simple hooks, no-nonsense PHP-based templates, page tree + page reference architecture (where almost everything is a page), fast and fun to develop in and use, speedy execution, and an emphasis on near infinite scalability. Every version of ProcessWire just keeps improving upon all of this, and more.

ProcessWire is a timeless tool and I'm confident that I'll be writing to you 10 years from now saying the same thing. Thanks to all of you for making ProcessWire what it is today. It is your enthusiasm, participation and support of this open source project that has enabled it to thrive and grow. I love developing ProcessWire and developing with ProcessWire, every bit as much as a decade ago, and am glad there are so many of us now—we have an awesome community. I look forward to our next 10 years and beyond. Enjoy reading the [ProcessWire Weekly](http://weekly.pw) tomorrow and have a great weekend!
