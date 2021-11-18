# author: Tiffany Timbers
# date: 2020-01-15

"""This script prints out docopt args.
Usage: demo.py <arg1> --arg2=<arg2> [--arg3=<arg3>] [<arg4>]
Options:
<arg>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
[<arg4>]          Takes any value (this is an optional positional argument)
""" 

from docopt import docopt
opt = docopt(__doc__)

def main(var):
    """
    Print out docopt objects

    This function simply wraps the print statments
    for print argument value and types from docopt object.

    Parameters
    ----------
    var : docopt object
        Input docopt object

    Returns
    -------
    Print statements
    """
    print(var)
    print(type(var))
    print(f"arg4 = {var['<arg4>']}")
    
if __name__ == "__main__":
    main(opt)