#!/bin/bash

echo "Install Stanza NLP.."
pip install -U stanza

echo "Install Model Lang En.."
python -c "import stanza; stanza.download('en')"
