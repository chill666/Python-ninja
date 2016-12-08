import urllib
import re


def ed2k_crawler(url):
    # Get HTML page
    page = urllib.urlopen(url)
    html = page.read()
    # Get match
    # reg = r'img src="(.+?\.jpg)" '
    ed2kre = re.compile(r'<a href="(ed2k://|file|.*\|/)"')
    ed2klist = re.findall(ed2kre, html)

    # Print result to file
    f = open("output.txt", "a")  # Append mode

    for ed2kurl in ed2klist:
        print >> f, ed2kurl
    print >> f, "\n ========================================== \n"
    f.close()
    print url + " Done! ==> Print to output.txt"

if __name__ == "__main__":

    # Clean up output.txt before write
    of = open("output.txt", "w")  # Write mode
    of.close
    # of.seek(0)
    # of.truncate()

    # Read source urls from file
    fi = open("input.txt")

    while 1:
        lines = fi.readlines(100000)
        if not lines:
            break
        for line in lines:
            ed2k_crawler(line)
