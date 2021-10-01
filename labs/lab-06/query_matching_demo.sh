#!/bin/bash

gunicorn query_matching_demo:app \
  --workers 1 \
  --worker-class virtex.VirtexWorker \
  --bind 0.0.0.0:580 \
  --worker-connections 10000 \
  --timeout 60 \
  --log-level INFO
