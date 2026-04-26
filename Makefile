.PHONY: setup test train-smoke

setup:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

test:
	python version_check.py

train-smoke:
	python -c "from genomics_system import CancerGenomicsDatabase; db=CancerGenomicsDatabase(); print('patients', len(db.patients))"
