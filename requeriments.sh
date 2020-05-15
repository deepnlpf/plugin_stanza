echo "Install Stanza NLP.."
pip install stanza -U

echo "Install Model Stanza EN.."
python -c "import stanza; stanza.download('en')"
