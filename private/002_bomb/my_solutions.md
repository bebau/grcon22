# ULTIMATE BOMB CHALLENGE

This is sort of "choose your own adventure" in that you can either attempt to extract the .exe and decompile/run `strings` on the .pyc files OR you can exploit a python string format vulnerability. I think the 2nd one is more fun/interesting so that's what I wrote the clues for. There are probably even more solutions that I haven't thought of. 

## Path 1: Decompiling

You can use [pyinstxtractor](https://github.com/extremecoders-re/pyinstxtractor) to extract the login file like...

`python pyinstxtractor.py login`

And you get a whole bunch of files. The one of interest is in the `login_extracted/PYZ-00.pyz_extracted` directory. It is currently named `bomb3_secret.pyc` but I think I will rename it to something a little less obvious.

I haven't tried every decompiler. I tried [decompyle++](https://github.com/zrax/pycdc) which didn't work... which I expected because I swapped the python opcodes. PyREtic seems promising but a bit high effort, so I didn't try that (yet). Uncompyle6 and Decompyle3 don't work with python3.9. 

Once decompiled, it's pretty obvious what the flag is. 

At the moment, it's one of not very many strings in the code. So you can simply run `strings bomb3_secret.pyc` and it is pretty obvious as well. But I will fix that...

Presumably, by this point you've got the flag. 

## Path 2: Mr. Robot Hackerman status 

This involves no decompiling of the source code. Simply exploiting str.format(blah) which the terrorist has very sloppily implemented in python. 

The clue guides you to notice there's a string format vulnerability when you enter "{" and see an "Unhandled Exception" message. This is exactly how you do SQL injection, by entering a single quote ' and see if you get some unknown error message that seems to indicate a vulnerability. 

You can start entering all sorts of stuff, and the error messages along the way will help you figure it out!

Here's what I entered to see the flag: 

`Username: Gort the Evil`
`Password: {pw_obj.check_password.__code__.co_consts}`
