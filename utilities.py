
#some important functions to quickly smartly develop a django webapp
import random
import string


def lofformfields(className):
    # className.__dict__['__doc__']#this returns a string like 'ItemInBucket(id, donator, item_id, item_name, image, upvote, downvote, donated, created, location)'
    #                             #1.convert returned string into a list for form field --> then user can simply use it.
    # return
    pass


def uniqueCodeGenerator(size=6, chars = string.digits + string.ascii_letters):
    new_code=''
    for i in range(size):
        new_code+=random.choice(chars)
    return new_code
