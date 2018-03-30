NAME := senior
SRC  := ${NAME}.cob
COBC := cobc
OPTS := 

build: ${NAME}.cob
	${COBC} -x ${OPTS} $<

%.o: %.cob
	${COBC} -c ${OPTS} $<

run: build
	./${NAME}

clean:
	rm -f ${NAME} ${NAME}.so ${NAME}.o
