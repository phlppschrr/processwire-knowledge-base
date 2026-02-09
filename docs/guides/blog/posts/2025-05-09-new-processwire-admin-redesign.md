# New ProcessWire admin redesign

Source: https://processwire.com/blog/posts/new-processwire-admin-redesign/

## Sections


## New ProcessWire admin redesign

9 May 2025 by Ryan Cramer [ 3 Comments](/blog/posts/new-processwire-admin-redesign/#comments)

When you upgrade to ProcessWire 3.0.248 or newer (currently the dev branch), you’ll immediately notice something new and beautiful. The look of the admin has changed significantly for the better, while still being very familiar.

This is thanks to the fantastic work by Diogo Oliveira and Jan Ploch of [KONKAT Studio](https://konkat.studio) in Hamburg, Germany. KONKAT has also designed the new ProcessWire.com website, currently in development, and coming soon. (We also have some Q&A with KONKAT further below.)

The first time I saw this new design, it immediately felt like home. A newer and nicer home that represents a compelling and refreshing look for ProcessWire. I suspect most will feel the same. After 15 years as an open source project, ProcessWire now has a professionally designed admin, one that I think will be a welcome change for existing users, while helping us to attract new users.


### Getting started

After upgrading, depending on your OS (or browser) settings, you’ll be presented with a dark or light version of the new design. By default it is set for “auto” which inherits from your OS or browser dark mode setting. Here is the dark theme…

…and the light theme:

You can change between light and dark mode by using the toggle in the user tools menu:

It will change immediately as a preview, and ask you to confirm the change:

The setting is remembered with your user account, so it will still be there the next time you login.

When "Auto" is selected, ProcessWire will use whatever setting is defined with your OS or browser. I'm on a Mac, and if I go to System Preferences > General > Appearance, selecting Light or Dark mode immediately changes the ProcessWire interface, without a page reload. Should you choose "Auto" both in your OS and in ProcessWire, then you'll get Light mode during the daytime and Dark mode at night time.


### A new design for AdminThemeUikit

This is not technically a new admin theme in the "module" sense. This is still the AdminThemeUikit theme that’s been built in to ProcessWire for quite some time. But AdminThemeUikit now supports a new custom theming ability, introduced for this redesign. We'll likely cover that in more detail in a future post.

AdminThemeUikit also continues to support customization by admin.less, but note that you’ll want to switch it to the “Original” theme in the AdminThemeUikit module settings, in order to use admin.less customization.


### What’s new and different?

Relative to the “Original” AdminThemeUikit appearance (which is also included), and beyond the obvious "look and feel" differences, you’ll notice several other improvements in our new AdminThemeUikit default theme:

The masthead, primary navigation and search are now always available, fixed to the top of the window.

Dropdown navigation lists with lots of items now scroll within the dropdown rather than the window.

An improved search function and command hotkeys.

As mentioned previously, independent "Light" and "Dark" modes are available, along with an "Auto" mode.

TinyMCE has been custom styled for this new default theme.

Higher quality typography and color usage throughout.

The ability to change the “main” color for the theme from the AdminThemeUikit module settings. There are predefined colors available, or you may specify your own with a color picker.

The entire appearance is controlled by CSS variables and there are [more than 35 of them](https://github.com/processwire/processwire/blob/dev/wire/modules/AdminTheme/AdminThemeUikit/themes/default/admin-custom.css#L34). Though most inherit from other CSS variables by default, so there are only a few independent colors used in an unmodified theme.

You can specify a custom CSS file to modify the appearance. Most modifications can be made with CSS variables, and a few [examples](https://github.com/processwire/processwire/tree/dev/wire/modules/AdminTheme/AdminThemeUikit/themes/default/examples) are included.

When ProcessWire is in advanced mode (`$config->advanced=true`) you can also specify custom CSS directly on the module configuration screen. Since some bad CSS might hide the entire admin interface, we figured it was best to keep it in advanced mode (the mode intended for such settings).


### Configuration

There are several configuration options available in the AdminThemeUikit module settings specific to this new “default” theme.

If you want to standardize on either dark mode or light mode (rather than “auto”) you’ll want to select that in the module configuration. Users can still change to dark or light mode on their own (from the user tools menu) but if you want to prevent them from doing so, there is a checkbox to disable that option.

This new theme is built around a “main” color that is used to style elements throughout the interface. If you want to change this main color, there are 3 predefined options available, or you can select your own from a color picker:

Should you want to customize the admin beyond the main color, you can specify a custom CSS file or if using advanced mode, you can also paste in custom CSS. For instance, check out the included examples: [Borderless](https://github.com/processwire/processwire/blob/dev/wire/modules/AdminTheme/AdminThemeUikit/themes/default/examples/borderless.css), [Custom masthead colors](https://github.com/processwire/processwire/blob/dev/wire/modules/AdminTheme/AdminThemeUikit/themes/default/examples/masthead.css), and [Minimal blue](https://github.com/processwire/processwire/blob/dev/wire/modules/AdminTheme/AdminThemeUikit/themes/default/examples/minimal.css), or see the [admin-custom.css](https://github.com/processwire/processwire/blob/dev/wire/modules/AdminTheme/AdminThemeUikit/themes/default/admin-custom.css#L34) file for a list of all CSS variables you can customize.

If you have a client that struggles with change, you can also switch it back to use the original AdminThemeUikit design:


## Q&A with the KONKAT Studio


### What motivated or inspired you to redesign the ProcessWire admin?

We have been using ProcessWire for a long time and felt it was time to give something back to the community. There is something timeless about ProcessWire because it has remained true to its concept over the years. For us, PW is a very successful combination of simplicity and flexibility. Our aim was to create a design that reflects this. The theme should be simple and intuitive without sacrificing flexibility. It was important to us to design a good default theme that would remain modern and functional for years to come, but still feel like ProcessWire. Especially for new users it is important to have good defaults, as the user interface is a decisive criterion for many users when choosing a CMS. At the same time, we wanted to make it as easy as possible for existing users to customize the theme.


### What are your favorite features, details, or any highlights you'd like to mention about the new design?

The fixed nav-bar, which allows faster navigation of the backend and feels more like an app. We also worked on many small details to increase contrast and improve readability. For example, the new theme uses the Inter font, which was designed specifically for screens and user interfaces.

We also like how easy it is to create completely different looks only with a couple of clicks, or even go further and create your own theme by defining just a few CSS variables.

Making the search input accessible through the Cmd/Crtl+K shortcut makes it feel more like a command palette. We think most people don’t realize how powerful the PW search is and we hope this simple change make it even more useful.


### How would you like others to be able to customize or expand upon this design?

When @teppo expressed the idea of using CSS variables for the new theme in the forum and this was met with great approval, we were motivated to at least try out how this could be integrated into Uikit. The result is that we now have a completely customizable theme without having to resort to CSS preprocessors. We are big fans of using native web technologies as CSS now supports most of the features of LESS natively without the overheat.

With the new variables, sharing a new theme will be as easy as pasting a small snippet. We are excited to see what the community will do with these new possibilities.


### Who is KONKAT Studio? Where are you located and what types of projects do you work on?

We founded KONKAT in 2024 as a collaborative design studio. We met through the PW forum and when Diogo moved to Hamburg (Germany) we decided to join forces. Both of us studied graphic design and became web developers later. But at the time we met, Diogo was mostly doing web development and Jan was mainly doing design. As KONKAT we create brand identities, websites, animations and illustrations for a varied client base.


### What is your experience and history with ProcessWire?

Diogo has been using ProcessWire since it was open-sourced in 2010, and Jan joined in 2015. Over the years we've created PW websites for all sorts of clients, like [a music agency](https://oha-music.com/), [a university](https://bedrohte-ordnungen.de/), [a town](https://www.eitorf.de/), [a magazine](https://www.the-weekender.com/), [an animation studio](https://aimcreativestudios.com/), and [a logistics company](https://gw-atlas.com/), to name a few.


### What other related work have you and/or KONKAT Studio done?

Jan built [PAGEGRID](/modules/fieldtype-page-grid/), a site builder module for PW and [AdminThemeCanvas](/modules/admin-theme-canvas/), a minimal admin theme. In the early days of PW, Diogo created the Portuguese language pack and the [ImageFieldMarkup](/modules/textformatter-image-field-markup/) text formatter, and later the [AdminCustomPages](/modules/process-admin-custom-pages/) module. Diogo also designed the logo for the popular Padloper ProcessWire e-commerce module.

Editor's note: If you haven't yet seen Jan's [PAGEGRID](https://page-grid.com) you must check it out, it's an amazing piece of software. —Ryan


## How to upgrade

Simply upgrading to ProcessWire 3.0.248 (or newer) will automatically enable this new admin design. As of the time this is written, this is currently ProcessWire's dev branch. Please report any issues that you run into in our [issues repo](https://github.com/processwire/processwire-issues/issues). We hope to merge this over to the main/master branch later this summer.


### A huge thanks to KONKAT, Diogo and Jan for this fantastic contribution to ProcessWire and improving the experience of all ProcessWire users!
