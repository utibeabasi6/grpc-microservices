build:
	@python3 scripts/bootstrap.py
	@chmod +x scripts/gen.sh && ./scripts/gen.sh
