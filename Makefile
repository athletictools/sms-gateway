
lint:
	diff-quality --compare-branch=origin/master --violations flake8 --html-report diff-quality.html

test: lint
	py.test --cov=. --cov-report=xml --cov-report=html $(arg)
	diff-cover --compare-branch=origin/master coverage.xml --html-report diff-cover.html

