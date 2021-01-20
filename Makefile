
.PHONY : output

output: output/pycon-links.html
	cmd.exe /C start $^

output/pycon-links.md : src/list_pycon_talks.py
	python $^ html-data $@

output/pycon-links.html : output/pycon-links.md
	pandoc $^ -o $@ 
