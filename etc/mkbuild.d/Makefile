# Makefile for project: @PROJECT@
# Creation date: @CREATIONDATE@

BASEDIR=@PROJECT.DIR@
CONFIGDIR=$(BASEDIR)/<your configuration directory>
COMPILE=<your compiler>
COMPILE_OPTION=<your compiler option>

.PHONY: clean

init:
  <your project structure creation>

clean:
  <clean_option>

clean-all: clean
  find . type f -name "*~" -delete
  find . type f -name "*.class" -delete
  find . type f -name "*.o" -delete
  find . type f -name "*.obj" -delete
  find . type f -name "*.tmp" -delete

build: clean
  <your build rules>

doc:
  doxygen Doxyfile

test:
  <your unit tests/integration tests here>

install:
  <your installation structure>

uninstall:
  <your uninstall procedure>

check:
  <control the installation structure>

