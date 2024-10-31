
# https://en-word.net/static/english-wordnet-2023.zip


download-wordnet2023:
	wget https://en-word.net/static/english-wordnet-2023.zip
	rm -rf tmp/
	rm -rf wordnet-2023/
	unzip english-wordnet-2023.zip -d tmp
	rm -rf english-wordnet-2023.zip
	cp -r tmp/oewn2023/  wordnet-2023/
	rm -rf tmp/
