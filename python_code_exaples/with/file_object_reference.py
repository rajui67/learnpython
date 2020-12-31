'''

Question
The variable f still references the file object after the file is closed.  Are there any gotchas associated with this? 
E.g.; could Python assign the same reference id to another file object once the files are closed? 
Any consequences that more accomplished persons than I foresee? (This topic applies to all objects, not just file objects)

Response
Each file object reference gets it’s own id() and Python doesn’t overwrite a memory location ID as long as any reference to it still exists anywhere in your program.
 Once the reference count drops to 0, which means that the object isn’t accessible anymore, then Python automatically gets rid of it. This is part of Python’s automatic garbage collection.

Now, why does the TextIOWrapper object reference stay around at all after closing the file object? I don’t know and haven’t yet found a good explanation for it online. 
For all I’ve seen and played around with, there’s nothing practical to do with the TextIOWrapper once the file object has been closed.
There might be a good reason for keeping it around, and maybe @yurigorokhov knows more?

However, if you want to get rid of that reference for good, you could explicitly delete it after the context manager block, like so:

del f

This will remove the reference and allow the memory location to be reassigned to something else. Running your id() checks after this statement will result in an error.
Another thing you might be able to do, if you’d want this to be the default behavior, 
is to overwrite the __del__() method so that it doesn’t just flush the bytestream of your file object and close it, but also deletes any reference to it right away. Not sure this will work, 
but if you’re interested, give it a try and report back here : )

'''


full_path_file_name = "/home/riyer/python_code_exaples/file_operations/random.txt"
with open(full_path_file_name, "r") as f:
    try:
        if not f.closed:
            print(f"OPEN: {f=}", id(f))
        content = f.read()
        print(f"CONTENT: {content[:10]}")
        raise IndexError  # Simulating an exception that is not related to file operations
    except IndexError as err:
        pass  # Stand in for exception handling

if f.closed:
    print(f"CLOSED: {f=}", id(f))
else:
    print(f"STILL OPEN: {f=}", id(f))