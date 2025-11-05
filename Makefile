.PHONY: all
all:
	@echo "Run make help to see available commands"

.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make run          - Run locally"

.PHONY: run
run:
	./preview_build -port 8081 -input .
