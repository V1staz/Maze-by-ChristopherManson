#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"
xdg-open "$DIR/cover.html" 2>/dev/null || open "$DIR/cover.html" 2>/dev/null
