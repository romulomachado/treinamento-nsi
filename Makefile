all: test

test: unit

unit:
	@echo =======================================
	@echo ========= Running unit specs ==========
	@specloud 01 02 03 04 05 06 07 09 12
	@echo
