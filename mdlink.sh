# /usr/bin/bash


OUTPUT=$(find $1 -name "*.md")

dt=${OUTPUT//$'\n'/' '} # Remove all newlines.

echo $dt

exec $(pandoc $dt -o $1output.pdf)