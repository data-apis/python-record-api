#!/bin/bash -e

TOTAL=$(grep -l pandas scripts/*.py | wc -l)
TOTAL_RUN=0
TOTAL_FAILED=0
TOTAL_IGNORED=0
TOTAL_PREVIOUS=0

mkdir output

echo "Trying to run $(grep -l pandas scripts/*.py | wc -l) scripts"

for FNAME in $(grep -l pandas scripts/*.py); do
    echo "Running: $FNAME..."

    SCRIPT_ID=$(basename $FNAME .py)
    OUTPUT_FNAME=output/$SCRIPT_ID.jsonl
    if [[ -e $OUTPUT_FNAME ]]; then
        TOTAL_PREVIOUS=$((TOTAL_PREVIOUS + 1))
        continue
    fi

    TOTAL_RUN=$((TOTAL_RUN + 1))

    cd scripts
    export PYTHON_RECORD_API_TO_MODULES="pandas"
    export PYTHON_RECORD_API_FROM_MODULES=$SCRIPT_ID
    export PYTHON_RECORD_API_OUTPUT_FILE=../$OUTPUT_FNAME
    set +e
    python -m record_api
    FAILED=$?
    FAILED=$((FAILED != 0 ? 1 : 0))
    TOTAL_FAILED=$((TOTAL_FAILED + FAILED))
    set -e

    echo "Number of scripts: $TOTAL"
    echo "Number of scripts previously run: $TOTAL_PREVIOUS"
    echo "Number of scripts run: $TOTAL_RUN"
    echo "Number of scripts failed: $TOTAL_FAILED"
    echo "Number of scripts ignored (missing data source): $TOTAL_IGNORED"
    echo "*********************************************************************"
done

cd ..
mkdir grouped

for FNAME in $(grep -l pandas output/*.jsonl); do
    echo "Running: $FNAME..."

    SCRIPT_ID=$(basename $FNAME .jsonl)
    OUTPUT_FNAME=grouped/$SCRIPT_ID.jsonl

    cd output
    export PYTHON_RECORD_API_OUTPUT=../$OUTPUT_FNAME
    export PYTHON_RECORD_API_INPUT=$SCRIPT_ID
    python -m record_api.line_counts

done

cd ..
mkdir infer_apis

for FNAME in $(grep -l pandas infer_apis/*.jsonl); do
    echo "Running: $FNAME..."

    SCRIPT_ID=$(basename $FNAME .jsonl)
    OUTPUT_FNAME=infer_apis/$SCRIPT_ID.json

    export PYTHON_RECORD_API_OUTPUT=../$OUTPUT_FNAME
    export PYTHON_RECORD_API_INPUT=$SCRIPT_ID
    export PYTHON_RECORD_API_LABEL=$SCRIPT_ID
    export PYTHON_RECORD_API_MODULES=pandas
    python -m record_api.infer_apis
done