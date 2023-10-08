Back-end oassignment using the PeeWee ORM :
using tags 

1
csv: CSV File Reading and Writing
CSV stands for 'comma separated values'. It's the most common import and export format for spreadsheets and databases, used by (or at least compatible with) every software package you can think of in that space. It is a great skill to be able to read, manipulate and write these files.

2
argparse: Parser for command-line options, arguments, and subcommands.
Command-line tools are tools you've probably used a lot already. Examples that may be familiar to you are ls to show the contents of a directory and cd to change the working directory. Another common tool is echo to parse and output some input you give it (try: echo "hello world").

Another CLI tool you are familiar with is wincpy, which does different things based on the arguments you give it. For example, wincpy start starts assignments, while wincpy check checks assignments.

The argparse module helps you to write your own command-line tool. Once you've learned about command-line arguments, you'll see why it's called argparse.  


3
Datetime: basic date and time types.
Dates are notoriously hard to work with in software. The list of things to consider includes timezones, daylight saving time, leap years, and of course countless different notation styles.

We will standardize on a single source of truth, the date object, and use a string representation following the format: '%Y-%m-%d'.
