#!/bin/bash
export PYTHONPATH=$(pwd)
pytest -n auto -vv -s --alluredir=/tests/reports