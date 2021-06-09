#!/bin/bash

for i in $(find . -type f -name "*.md");
do
	path=`echo $i | rev | awk '{ print substr( $0, 11 ) }' | rev`
	cat $i | sed 's/\!\[\[Pasted image /\!\[\]\(https\:\/\/github.com\/H0j3n\/EzpzCTF\/blob\/main\/src\/Pasted%20image%20/g' | sed 's/.png\]\]/.png\)/g' > $path/test.md
	mv $path/test.md $i
done
