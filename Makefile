output-data/pycon-links.csv : src/list_pycon_talks.py
	python $^ input-data $@

