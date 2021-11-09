.DEFAULT_GOAL := help


### QUICK
# ¯¯¯¯¯¯¯

install: server.install ## Install

daemon: server.daemon ## Start

stop: server.stop ## Stop

oi: help help

include makefiles/server.mk
include makefiles/test.mk
include makefiles/database.mk
include makefiles/format.mk
include makefiles/help.mk
