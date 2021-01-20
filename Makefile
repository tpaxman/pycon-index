
.PHONY : output

output: output/pycon-links.html
	cmd.exe /C start $^

output/pycon-links.html : output/pycon-links.md
	pandoc $^ -o $@ 

output/pycon-links.md : src/format_pycon_talks.py output/pycon-links.csv
	python $^ $@ 

output/pycon-links.csv : src/list_pycon_talks.py
	python $^ html-data $@

