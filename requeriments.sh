echo "Install Stanza NLP.."
pip install stanza -U

echo "Install Model Stanza EN.."
python -m stanza stanza.download('en')
