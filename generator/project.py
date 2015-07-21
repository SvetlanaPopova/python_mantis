__author__ = 'User'


from model.project import Project
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
        opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of project", "file"])
except getopt.GetoptError as err:
        getopt.usage()
        sys.exit(2)

n = 2
f = "data/projects.json"

for o, a in opts:
        if o == "-n":
            n = int(a)
        elif o == "-f":
            f = a


def random_string (prefix, maxlen):
    symbols = string.ascii_letters*3 + string.digits + " "*10 #+ string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Project(name=random_string("Project", 20), status=random.choice(["stable", "development", "release", "obsolete"]),
            view_status=random.choice(["public", "private"]), description=random_string("Description", 60)
            , enabled="X") #inherit_gl_categories=random.choice([True, False])
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
