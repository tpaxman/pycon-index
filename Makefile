pycon-links.md : list_pycon_talks.py
	python $^ html-data $@

pycon-links.html : pycon-links.md
	pandoc $^ -o $@ 
