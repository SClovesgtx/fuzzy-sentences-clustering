# The present file, 'Makefile' has been modified from the original at
# https://github.com/NeowayLabs/data-science-template
# under the folllowing license:
#
# MIT License
#
# Copyright (c) 2019 Neoway Business Solution
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# BUILD = docker-compose build
# RUN = docker-compose run
# UP = docker-compose up
# DOWN = docker-compose down
# VERSION = $(shell awk -F ' = ' '$$1 ~ /version/ { gsub(/[\"]/, "", $$2); printf("%s",$$2) }' version.toml)

help:
	@echo "USAGE"
	@echo
	@echo "    make <command>"
	@echo "    Include 'sudo' when necessary."
	@echo "    To avoid using sudo, follow the steps in"
	@echo "    https://docs.docker.com/engine/install/linux-postinstall/"
	@echo
	@echo
	@echo "COMMANDS"
	@echo
	@echo "    cyclomatic-complexity        metric for the complexity of our code."
	@echo "    profiler-report              look up for slow code."
	@echo "    test                         run all unit tests."
	@echo "    vulnerability-check          look for security issues in the code."

#################
# User Commands #
#################


cyclomatic-complexity:
	$ radon cc src/phrases_fuzzy_clusters/phrases_fuzzy_clusters.py -a

profiler-report:
	$ pyinstrument --show-all src/phrases_fuzzy_clusters/phrases_fuzzy_clusters.py

test:
	$ pytest src/tests/test_phrases_fuzzy_clusters.py --rootdir src/phrases_fuzzy_clusters/

vulnerability-check:
	$ bandit --recursive src/ --skip "B101"