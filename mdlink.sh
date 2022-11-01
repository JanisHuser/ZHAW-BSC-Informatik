# /usr/bin/bash

echo "====================="
echo "searching for markdwon files in $1"

OUTPUT=$(find $1 -name "*.md")

echo "found the following files:"
echo $1
echo "====================="

dt=${OUTPUT//$'\n'/' '} # Remove all newlines.

pdf_file_loc="$1output.pdf"

echo "writing pdf to $pdf_file_loc"

exec $(pandoc $dt -o $pdf_file_loc)