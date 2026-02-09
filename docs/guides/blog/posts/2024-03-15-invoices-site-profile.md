# Invoices site for ProcessWire, PHP invoicing application

Source: https://processwire.com/blog/posts/invoices-site-profile/

## Sections


## ProcessWire Invoices Application Site Profile

15 March 2024 by Ryan Cramer [ 0 Comments](/blog/posts/invoices-site-profile/#comments)

The new invoices site profile is a free invoicing application developed in ProcessWire. It enables you to create invoices, record payments to them, email invoices to clients, print invoices, and more.


## About the invoices site profile

The site profile is designed first to be a useful application for those wanting to manage their client invoices. It came about when the invoicing service that I'd used for years decided to raise their rates beyond what was affordable for me. It gave me the motivation I needed to build this site profile. I've been using it for awhile now and have found it provides everything I need for creating and managing my client invoices.

While the site profile is primarily used from ProcessWire's admin, it does also come with front-end templates to list, view, email, and print invoices. Should you want it, each invoice also has URL that can be shared with the client.

The site profile is also designed to be an example of creating a simple application in ProcessWire, using only what's provided with the ProcessWire core (no extra modules). The other site profiles I've built have been very basic website-style site profiles, and I thought we needed something a little different that would better show the diversity of applications that ProcessWire can be used for.


### Development highlights

While this is still a relatively small scale site for ProcessWire, it is built with some of the ideas and approaches sometimes used on larger projects, and it should scale well. Below are a few highlights:


### Installation

See the [installation instructions](https://github.com/processwire/site-invoices/blob/main/README.md) in the site profile's readme file.


## Getting started

After installation, login to the admin and you'll see there are some example clients and invoices. They are just there to demonstrate how you should create your own clients and invoices. You can delete the example data when you no longer need it.


### Populate your settings

The first thing you'll likely want to do is edit the Settings page (Pages > Settings) to populate your own information, logo image, and currency.


### Add a client

After updating the settings, I suggest adding one or more clients (Pages > Clients > New). A client must exist before you can create an invoice for them.


## Creating an invoice

Now you can create a new invoice (Pages > Invoices > New). Use whatever format you prefer for the "Invoice title/ID". For example, my company name is "Ryan Cramer Design", and if I'm invoicing a company named "Some Big Company" then I use a format of "RCD-SBC-20240315" where "RCD" is short for "Ryan Cramer Design", "SBC" is short for "Some Big Company" and 20240315 is year, month, and day. This format works for me, but may not for you. Just identify a a format that you can use consistently across your invoices and stick to it.


### Adding billable line items

Now focus on the meat of the invoice, which is adding one or more billable line items (hours, services or products) that represent the work you've done for the client. Once finished adding line items to your invoice, Save it, and then View it.


## Sending an invoice to a client


### Print invoice (or save to PDF)

If your intention is to mail (print) the invoice, or send (PDF) the invoice to your client, then you can do that while viewing it on the front-end of the site. There is a print action (printer icon) that you can click to print and/or Save to PDF.


### Email invoice

If you want to email the invoice to the client, this profile comes with a built in function to do that. When editing the invoice, see the "Invoice action" field at the bottom. You'll probably want to "Email invoice to another address" and send it to yourself to preview. When ready, you can then use the "Email invoice to client" action.

If you do not have reliable email delivery from your web server, you can always forward the copy you sent yourself to the client. Or if your invoices site is web-accessible then you can view the invoice and copy the URL out of the address bar and email that to the client.

As you can see, there are many options to sending the invoice to the client. Use what works best for you.


## Receiving payments

We don't make any assumptions about how the client pays you, whether sending a check, doing a bank transfer, or paying by card. This part is up to you to arrange with your clients. When you have received a payment, you'll want to edit the invoice, click on the "Received payments" field, add the payment information, and save.

While invoices might usually be paid in one payment, the invoice editor supports multiple payments when needed. If your client has some kind of previous credit, this is also a good place to add that.

After adding received payment, and saving your invoice, the invoice status may update to indicate the invoice has been paid. If not yet paid in full, the invoice status will remain as pending or past due.


### Handling paid invoices

Once the received payments match or exceed the billable line items, the invoice status changes to "Paid". When an invoice is fully paid, it is complete and may not be needed anymore. You can always move the invoice to the trash, but I recommend just un-publishing it so that it remains for archival purposes, but isn't listed on the front-end invoices list. You can un-publish an invoice by editing it, clicking on the Settings tab, and checking the "Status > Unpublished" checkbox.


## Customizing the invoices site

While the invoices site profile might be quite useful as-is, it's also built to be customized and expanded upon. It is intentionally simple so that it's easy to make it your own. Modify the template files and CSS as you see fit. The section below this one outlines many of the files used by this site profile, hopefully making it clear where different components are edited.


### Adding payment solutions

One of the most obvious additions to this site profile might be adding payment links in each invoice. This could be as simple as PayPal or Stripe "pay now" buttons. Or it could be something more advanced, like an inline credit card payment form, perhaps via the [FormBuilder](/store/form-builder/) modules: [Stripe Elements Inputfield](/store/form-builder/stripe/) or [Stripe Checkout Payment Processor](/blog/posts/stripe-payment-processor-form-builder/). Integration into the invoice page should be relatively simple.


### Login required (except when…)

Use of the Invoices site requires that you are logged in. Though actual invoices can be viewed directly by URL whether logged in or not. This enables you to send the URL to a client if you want to. It also enables the email-invoice function to work. If you want to change or customize the logic behind the access control, you can do so from the [_init.php](https://github.com/processwire/site-invoices/blob/main/templates/_init.php) file.


## Overview of files and directories

Below are descriptions of most directories and files included in the site profile, and what they are for:


### /site/classes/

The [/site/classes/](https://github.com/processwire/site-invoices/tree/main/classes) directory contains custom classes for various Page types. The best example is the [InvoicePage.php](https://github.com/processwire/site-invoices/blob/main/classes/InvoicePage.php) file which has an InvoicePage class representing pages using the invoice template. This enables invoice pages to have their own API with various useful methods, outlined further in this post.


### /site/templates/

PHP files in this directory handle the output for the site. Each template file corresponds to a page template that you'll see in the admin. Though there's an exception: you'll notice some files that begin with an underscore, such as the first 3 listed below. These files (with a leading underscore) don't represent individual page template files, but are usually shared or used by them. ProcessWire will ignore these files it comes to adding new templates.

**[_func.php](https://github.com/processwire/site-invoices/blob/main/templates/_func.php)** These are shared functions used throughout the site.

**[_init.php](https://github.com/processwire/site-invoices/blob/main/templates/_init.php)** This file is called before rendering any non-admin page. In this case, we use it to limit access to the front-end of the invoices site so that the user must be logged in before they can list invoices. Invoice pages are still directly accessible by URL (without login), in case you want to send an invoice link to a client.

**[_main.php](https://github.com/processwire/site-invoices/blob/main/templates/_main.php)** This is the main output file that all the other template files populate by using [Markup Regions](/docs/front-end/output/markup-regions/).

**[admin.php](https://github.com/processwire/site-invoices/blob/main/templates/admin.php)** This is the template file used by ProcessWire’s admin. It's a good place for admin-specific hooks. In our case, we use it to include the /site/templates/admin/invoice-edit.php file when we detect that an invoice page is being edited.

**[basic-page.php](https://github.com/processwire/site-invoices/blob/main/templates/basic-page.php)** This is a basic page template that you see on just about every site profile. It can be used for generic content pages. In our case, we only use it for the 404 page. But you might want to use it for adding your own content pages to the site.

**[client.php](https://github.com/processwire/site-invoices/blob/main/templates/client.php)** This provides the output for the pages using the "client" template. It simply lists all invoices for whatever client is being viewed.

**[clients.php](https://github.com/processwire/site-invoices/blob/main/templates/clients.php)** Simply lists and links to all client pages.

**[home.php](https://github.com/processwire/site-invoices/blob/main/templates/home.php)** Renders the homepage. Lists invoices if user is logged in, or directs them to login.

**[invoice.php](https://github.com/processwire/site-invoices/blob/main/templates/invoice.php)** Renders an invoice. This is the most significant template file in the site.

**[invoice-status.php](https://github.com/processwire/site-invoices/blob/main/templates/invoice-status.php)** Used by invoice status pages which list invoices having the given status.


### /site/templates/classes/

Included in this directory are helper classes used by template files, listed below.

**[EmailTemplateHelper.php](https://github.com/processwire/site-invoices/blob/main/templates/classes/EmailTemplateHelper.php)** A class for helping to make invoices email client friendly by converting class attributes to inline styles.

**[Labels.php](https://github.com/processwire/site-invoices/blob/main/templates/classes/Labels.php)** A class that combines all (or most) of the text labels used in the invoices site. So if you are using multi-language support, you can translate everything in one file.


### /site/templates/admin/

This directory contains files for working with the admin side of the site, primarily by way of hooks.

**[invoice-edit.php](https://github.com/processwire/site-invoices/blob/main/templates/admin/invoice-edit.php)** This file is included by /site/templates/admin.php when editing a page using template "invoice". It contains hooks to update the output and behavior of the page editor when editing invoices.

**[invoice-edit.js](https://github.com/processwire/site-invoices/blob/main/templates/admin/invoice-edit.js)** This collaborates with the above invoice-edit.php and contains the Javascript side of things to update the page editor when editing invoices.


### /site/templates/parts/

This directory contains parts of the site that are included by template files. Think of "parts" as a shorter label for "partials".

**[invoice-email.php](https://github.com/processwire/site-invoices/blob/main/templates/parts/invoice-email.php)** This file is included by the invoice.php template file when an email-friendly render has been requested. It uses the EmailTemplateHelper class mentioned earlier.

**[invoice-list.php](https://github.com/processwire/site-invoices/blob/main/templates/parts/invoice-list.php)** This file provides the markup for a table list of invoices. It expects to receive an $items variable that is an array or PageArray of InvoicePage objects. You'll see it used by the home.php and client.php template files.

**[logo.php](https://github.com/processwire/site-invoices/blob/main/templates/parts/logo.php)** This invoice profile uses a custom logo that you can specify in the admin on the settings page. This file renders the markup for the logo, and creates both regular and hidpi versions. If you upload a custom logo and it isn't sized quite right in the output, you'll want to edit this file to update the $logoHeight variable, which by default is set to 120 pixels.

**[status-nav.php](https://github.com/processwire/site-invoices/blob/main/templates/parts/status-nav.php)** This renders the navigation for jumping between different invoices statuses to list matching invoices.

**[topnav.php](https://github.com/processwire/site-invoices/blob/main/templates/parts/topnav.php)** This renders the primary/top navigation, which is a breadcrumb-style navigation that also contains tools (represented by icons) contextual to the page being viewed.


## Invoices API

Should you need it, this site profile comes with its own API for managing invoices. While much of it is the same as managing any other type of pages in ProcessWire from its API, the class (InvoicePage) used by individual invoices contains several helpful API methods. Following are examples of using the functions available on InvoicePage items. These all assume $invoice is an InvoicePage:

```php
// get an invoice 
$invoice = $pages->get('/invoices/some-invoice-abc123/');

// get the total of all invoice line items
$amount = $invoice->getSubtotal();

// Get total amount due (invoice total minus payments received)
$amount = $invoice->getTotalDue();

// Get total amount of all received payments
$amount = $invoice->getPaymentsTotal();

// Is invoice paid in full? Returns true or false
$paid = $invoice->isPaid();

// Is the invoice past due? Returns true or false
$pastDue = $invoice->isPastDue();

// Get due date as unix timestamp
$ts = $invoice->getDueDate();

// Get due date as formatted date string
$date = $invoice->getDueDate(true);

// Get number of days remaining till invoice is due
$days = $invoice->getDaysRemaining();

// Get days invoice was paid in or false if not yet paid
$days = $invoice->getPaidInDays();

// Add billable line item: Type, Description, Units, Rate per unit
$invoice->addLineItem('hours', 'Website development', 3.5, 125.00);
$invoice->save();

// Add a payment
$invoice->addPayment('2024-03-15', 500.00, 'Check #1234');
$invoice->save();

// Add a log entry (true=save now)
$invoice->addLog("Client says payment is on the way", true);

// Get invoice status
$status = $invoice->getInvoiceStatus();
echo "Invoice status: $status->title"; // Pending, Paid, Past Due
```

The above are examples of using functions available on the InvoicePage. Note also that that each InvoicePage has several properties. See the top of the [InvoicePage](https://github.com/processwire/site-invoices/blob/main/classes/InvoicePage.php) class for a description of these properties.


## Download

You can grab the Invoices site profile from the [site-invoices GitHub repository](https://github.com/processwire/site-invoices/). Here's a direct link to download the [ZIP file](https://github.com/processwire/site-invoices/archive/refs/heads/main.zip) for the site profile. Note that ProcessWire 3.0.227 or newer is required. Once downloaded, proceed with [installation](https://github.com/processwire/site-invoices/?tab=readme-ov-file#installation).
