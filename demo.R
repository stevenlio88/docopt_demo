# author: Tiffany Timbers
# date: 2020-01-15

"This script prints out docopt args.
Usage: demo.R <arg1> --arg2=<arg2> [--arg3=<arg3>] [<arg4>]
Options:
<arg>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
[<arg4>]   		  Takes any value (this is an optional positional argument)
" -> doc

library(docopt)
opt <- docopt(doc)

main <- function(var) {
	print(var)
	print(typeof(var))
	print(paste0("arg4 = ",var[4]))
}

main(opt)