GV_FILES = $(wildcard *.gv)
PDF_FILES = $(GV_FILES:.gv=.pdf)

all: $(PDF_FILES)

%.pdf: %.gv
	dot -Tpdf $^ > $@

clean:
	rm *.pdf

# all: carStateMachine.pdf carStateMachine_simple.pdf

# carStateMachine.pdf: carStateMachine.gv
# 	dot -Tpdf carStateMachine.gv > carStateMachine.pdf

# carStateMachine_simple.pdf: carStateMachine_simple.gv
# 	dot -Tpdf carStateMachine_simple.gv > carStateMachine_simple.pdf
