clean:
	@rm *.hlt *.log
zip:
	@zip -r zipped.zip MyBot.py hlt.py networking.py helper.py
run:
	@./runGame.sh
all: run zip
