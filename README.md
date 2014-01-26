py-gmail-unread
===============

I wanted to inject the number of unread messages I have into my ZSH prompt and
obviously I needed a way to get the unread count. This script should be set up
in cron to run periodically as it's a bit too slow for inline calls. Depends on
the EMAIL environment variable as well as your password being loaded up into
the OSX keychain under the name "email" using your password as the account. The
script saves the unread count out to /tmp/GMAIL_UNREAD and then you can do
whatever the fuck you want do to with it, as long as it's not illegal.

## This shit sucks

Like many small projects I failed to realize that this is easily accomplished
with shell scripting alone:

	export KEYCHAIN_ITEM='email' && curl -u `security find-generic-password -s ${KEYCHAIN_ITEM} | grep 'acct' | cut -c 19- | tr -d '"' | tr -d '\n'`:`security find-generic-password -w -s ${KEYCHAIN_ITEM}` --silent "https://mail.google.com/mail/feed/atom" | perl -ne 'print "$2\n" if /<(email)>(.*)<\/\1>/;' | wc -l | tr -d ' '

Where `KEYCHAIN_ITEM` is the name of the Keychain Access key that you stored
your email address and password in. This command provides more flexibility as
you can easily run it multiple times against different keys (if you have
multiple emails you want to check) and you can do whatever you want with the
output (pipe it to a file, shove it up your ass, whatever you’re into).

So yeah, I’ll leave this project up since it does provide a nice example of
checking for unread messages in Python but I don’t plan on using it any longer
as the CLI solution has way more sex appeal.

Possibly maintained gist available [here](https://gist.github.com/joshtronic/8640234)
