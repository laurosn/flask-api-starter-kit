.DEFAULT_GOAL := help


### QUICK
# ¯¯¯¯¯¯¯

install: server.install database.all## Install

daemon: server.daemon ## Start

stop: server.stop ## Stop

start: server.start

all: install start

include makefiles/server.mk
include makefiles/test.mk
include makefiles/database.mk
include makefiles/format.mk
include makefiles/help.mk
