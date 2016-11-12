clean:
	rm *.hlt *.log
zip:
	zip -r zipped.zip MyBot.py
run:
	./runGame.sh && make zip
