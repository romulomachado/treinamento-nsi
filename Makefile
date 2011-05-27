all: test

test: unit

unit:
	@echo =======================================
	@echo ========= Running unit specs ==========
	@specloud 01 02 03 04 05
	@echo
